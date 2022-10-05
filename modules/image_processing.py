import numpy as np
from numba import jit
from skimage import io
from skimage.transform import resize
from skimage.util import crop


@jit(nopython=True, cache=True)
def squareCropCoordinate(image):
    # return the coordinate of the largest square
    # possible in the image
    height = image.shape[0]
    width = image.shape[1]

    # is the image already square ?
    if height == width:
        return ((0, 0), (0, 0), (0, 0))

    # Is the image in portrait or landscape mode
    is_portrait = height > width

    if is_portrait:
        deltaX = int((height - width) / 2)
        return ((deltaX, deltaX), (0, 0), (0, 0))
    else:
        deltaY = int((width - height) / 2)
        return ((0, 0), (deltaY, deltaY), (0, 0))


def palette2bit():
    # this palette has been carefully chosen
    # so it can reproduce almost every picture
    # with only 4 colors
    return np.array([[[32, 26, 102],
                      [191, 59, 38],
                      [76, 230, 46],
                      [255, 255, 255]]])/255


def remapValue(value, in_min, in_max, out_min, out_max):
    return (value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


# the next two functions replace np.unravel_index()
# because this one don't work with numba

@jit(nopython=True, cache=True)
def tuple_rev(tup):
    out = []
    for i in range(len(tup), 0, -1):
        out.append(tup[i-1])
    return out


@jit(nopython=True, cache=True)
def find_index(index, shape):
    out = []
    for dim in tuple_rev(shape):
        out.append(index % dim)
        index = index // dim
    return tuple_rev(np.array(out))


@jit(nopython=True, cache=True)
def meanCutPaletteExtract(image, nb_color):
    # add another channel to the image to store bucket id
    # like so : [R, G, B, Bucket_id]
    # every pixel is on the bucket 0 at first
    imgToSort = np.concatenate(
        (image, np.zeros(image.shape[0:2] + (1,))), axis=2)

    # initialize the next bucket
    next_bucket = 1

    for i in range(nb_color-1):
        # initialize the disparities array
        # row : channel (R,G,B)
        # column : bucket id
        min_array = np.ones((3, next_bucket))
        max_array = np.zeros(min_array.shape)

        for x in range(imgToSort.shape[0]):
            for y in range(imgToSort.shape[1]):
                for ch in range(3):
                    # search for min
                    if imgToSort[x, y, ch] < min_array[ch, int(imgToSort[x, y, 3])]:
                        min_array[ch, int(imgToSort[x, y, 3])] = \
                            imgToSort[x, y, ch]

                    # search for ax
                    if imgToSort[x, y, ch] > max_array[ch, int(imgToSort[x, y, 3])]:
                        max_array[ch, int(imgToSort[x, y, 3])] = \
                            imgToSort[x, y, ch]

        disparities = max_array - min_array
        whereToCut = find_index(np.argmax(disparities), disparities.shape)

        # determine the channel and bucket on wich to calculate mean
        channelToCut = whereToCut[0]
        bucketToCut = whereToCut[1]

        # calculate mean of selected pixels
        meanValue = np.zeros(image.shape[0]*image.shape[1])
        counter = 0
        for x in range(imgToSort.shape[0]):
            for y in range(imgToSort.shape[1]):
                if imgToSort[x, y, 3] == bucketToCut:
                    meanValue[counter] = imgToSort[x, y, channelToCut]
                    counter += 1
        meanValue = np.mean(meanValue[0:counter-1])

        # sort pixels
        for x in range(imgToSort.shape[0]):
            for y in range(imgToSort.shape[1]):
                if imgToSort[x, y, channelToCut] < meanValue:
                    if imgToSort[x, y, 3] == bucketToCut:
                        imgToSort[x, y, 3] = next_bucket

        next_bucket += 1

    # calculate the mean of each bucket
    palette = np.zeros((1, nb_color, 3))
    for bucket in range(nb_color):
        colors = np.zeros((imgToSort.shape[0]*imgToSort.shape[1], 3))
        pixelCounter = 0
        for x in range(imgToSort.shape[0]):
            for y in range(imgToSort.shape[1]):
                if imgToSort[x, y, 3] == bucket:
                    colors[pixelCounter, :] = imgToSort[x, y, 0:3]
                    pixelCounter += 1
        palette[0, bucket, 0] = np.mean(colors[0:pixelCounter, 0])
        palette[0, bucket, 1] = np.mean(colors[0:pixelCounter, 1])
        palette[0, bucket, 2] = np.mean(colors[0:pixelCounter, 2])

    # clipping
    palette = np.minimum(palette, np.ones(palette.shape))
    palette = np.maximum(palette, np.zeros(palette.shape))

    return palette


@jit(nopython=True, cache=True)
def paletteRefinement(image, dithered_image, palette, iteration):
    new_dithered_image = np.copy(dithered_image)
    new_image = np.copy(image)

    err = np.ones(iteration)

    new_palette = np.copy(palette)
    new_palette *= 1 + (0.9-np.max(new_palette))

    for i in range(iteration):
        difference = image - new_dithered_image
        new_image += difference

        err[i] = np.sqrt(
            (np.sum(new_image[:, :, 0]-image[:, :, 0])/image.size)**2 +
            (np.sum(new_image[:, :, 1]-image[:, :, 1])/image.size)**2 +
            (np.sum(new_image[:, :, 2]-image[:, :, 2])/image.size)**2)

        if abs(err[i]) > 0.02:
            break

        new_palette = meanCutPaletteExtract(new_image, palette.shape[1])
        new_dithered_image = dithering(image, new_palette)

        if np.max(new_palette) == 1.:
            break

    return new_palette


@jit(nopython=True, cache=True)
def findClosest(value, palette):
    x = palette[0, :, 0]
    y = palette[0, :, 1]
    z = palette[0, :, 2]

    dx = x - value[0]
    dy = y - value[1]
    dz = z - value[2]

    dist = np.sqrt(dx**2 + dy**2 + dz**2)

    return palette[0, np.argmin(dist), :]


@jit(nopython=True, cache=True)
def dithering(image, palette, bias=2):
    # this function will constrain image color to palette color
    # using dithering (the atkinson algorithm)
    # . * 1 1
    # 1 1 1 .
    # . 1 . .

    image = np.concatenate(
        (np.zeros((image.shape[0], 1, 3)), image,
         np.zeros((image.shape[0], 2, 3))),
        axis=1
    )
    image = np.concatenate(
        (image, np.zeros((2, image.shape[1], 3))),
        axis=0
    )

    output = np.copy(image)

    for y in np.arange(1, output.shape[1] - 2, 1):
        for x in np.arange(0, output.shape[0] - 2, 1):

            oldPixel = np.copy(output[x, y, :])
            newPixel = findClosest(oldPixel, palette)
            output[x, y, :] = newPixel

            quant_err = (oldPixel - newPixel) / (6 + bias)

            output[x+1, y, :] = output[x+1, y, :] + quant_err
            output[x+2, y, :] = output[x+2, y, :] + quant_err

            output[x-1, y+1, :] = output[x-1, y+1, :] + quant_err
            output[x, y+1, :] = output[x, y+1, :] + quant_err
            output[x+1, y+1, :] = output[x+1, y+1, :] + quant_err

            output[x, y+2, :] = output[x, y+2, :] + quant_err

    # crop the un-converged pixels
    output = output[:-2, 1:-2, :]

    # clipping
    output = np.minimum(output, np.ones(output.shape))
    output = np.maximum(output, np.zeros(output.shape))

    return output


@jit(nopython=True, cache=True)
def blurImg(img):
    work = np.zeros((img.shape[0]+2, img.shape[1]+2, 3))
    out = np.copy(work)
    work[1:-1, 1:-1, :] = img
    work[:, 0] = work[:, 1]
    work[:, -1] = work[:, -2]
    work[0, :] = work[1, :]
    work[-1, :] = work[-2, :]

    for x in range(1, out.shape[0]-1):
        for y in range(1, out.shape[1]-1):
            out[x, y, :] = np.array([
                np.median(work[x-1:x+1, y-1:y+1, 0]),
                np.median(work[x-1:x+1, y-1:y+1, 1]),
                np.median(work[x-1:x+1, y-1:y+1, 2])])

    return out[1:-1, 1:-1, :]


def processPicture(image, size, nb_color, blur=False):
    image = resize(image, (size[0], size[1], 3))
    palette = meanCutPaletteExtract(image, nb_color)
    dithered = dithering(image, palette)
    refined_palette = paletteRefinement(image, dithered, palette, 10)
    out = dithering(image, refined_palette)
    if blur:
        out = blurImg(out)
    return out, refined_palette


if __name__ == "__main__":
    # this code file is only usable as a module
    pass
