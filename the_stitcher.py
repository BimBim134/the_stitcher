#!/usr/bin/env python
# This Python file uses the following encoding: utf-8

import sys
import os
from pathlib import Path
from turtle import color

from modules.image_processing import *
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QMessageBox

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from modules.ui_form import Ui_Widget


class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        self.ui.file_line_edit.setPlaceholderText("your image...")

        # open files :
        self.ui.choose_file_button.clicked.connect(self.openFile)
        self.ui.choose_file_button_2.clicked.connect(self.openFile)
        self.ui.choose_palette_button_2.clicked.connect(self.openPalette)

        self.ui.ok_button.clicked.connect(self.launchButton_easy)
        self.ui.ok_button_2.clicked.connect(self.launchButton_pro)

        self.image = None
        self.palette_file = None  # for pro mode only

        self.imageProportion = self.ui.height_selector.value()/self.ui.width_selector.value()

        self.ui.height_selector.valueChanged.connect(
            self.conserveProportion_height)
        self.ui.height_selector_2.valueChanged.connect(
            self.conserveProportion_height)

        self.ui.width_selector.valueChanged.connect(
            self.conserveProportion_width)
        self.ui.width_selector_2.valueChanged.connect(
            self.conserveProportion_width)

        self.ui.conserve_proportion_button.toggled.connect(
            self.setImageProportion)
        self.ui.conserve_proportion_button_2.toggled.connect(
            self.setImageProportion)

    def setImageProportion(self):
        # set proportions :
        if self.ui.conserve_proportion_button.isChecked():
            self.imageProportion = self.ui.height_selector.value()/self.ui.width_selector.value()
        if self.ui.conserve_proportion_button_2.isChecked():
            self.imageProportion = self.ui.height_selector_2.value() / \
                self.ui.width_selector_2.value()

        # connect proportion buttons states together
        if self.ui.tabWidget.currentIndex() == 0:
            self.ui.conserve_proportion_button_2.setChecked(
                self.ui.conserve_proportion_button.isChecked())
        elif self.ui.tabWidget.currentIndex() == 1:
            self.ui.conserve_proportion_button.setChecked(
                self.ui.conserve_proportion_button_2.isChecked())

    def conserveProportion_height(self):
        if self.ui.conserve_proportion_button.isChecked():
            self.ui.width_selector.setValue(
                self.ui.height_selector.value()/self.imageProportion)

        if self.ui.conserve_proportion_button_2.isChecked():
            self.ui.width_selector_2.setValue(
                self.ui.height_selector_2.value()/self.imageProportion)

    def conserveProportion_width(self):
        if self.ui.conserve_proportion_button.isChecked():
            self.ui.height_selector.setValue(
                self.ui.width_selector.value()*self.imageProportion)

        if self.ui.conserve_proportion_button_2.isChecked():
            self.ui.height_selector_2.setValue(
                self.ui.width_selector_2.value()*self.imageProportion)

    def openFile(self):
        self.fileName = QFileDialog.getOpenFileName(self,
                                                    "choose your input file",
                                                    os.getcwd())
        try:
            self.image = io.imread(self.fileName[0]).astype('float64')

            if np.max(self.image) > 1:
                self.image /= 255

            if self.image.shape[2] == 4:
                print(self.image.shape)
                self.image = self.image[:, :, 0:3]
                print(self.image.shape)

            self.ui.file_line_edit.setText(self.fileName[0])
            self.ui.file_line_edit_2.setText(self.fileName[0])

            self.imageProportion = self.image.shape[0]/self.image.shape[1]

            self.ui.width_selector.setValue(self.image.shape[0])
            self.ui.width_selector.setMaximum(self.image.shape[0])
            self.ui.width_selector_2.setValue(self.image.shape[0])
            self.ui.width_selector_2.setMaximum(self.image.shape[0])

            self.ui.height_selector.setValue(self.image.shape[1])
            self.ui.height_selector.setMaximum(self.image.shape[1])
            self.ui.height_selector_2.setValue(self.image.shape[1])
            self.ui.height_selector_2.setMaximum(self.image.shape[1])

        except ValueError:
            msgBox = QMessageBox()
            msgBox.setWindowTitle('error !')
            msgBox.setText("This is not an image file.")
            msgBox.setInformativeText(
                "Please make sure your image have a suitable image format :\n*.jpg or *.png for example.")
            msgBox.exec()

    def openPalette(self):
        self.paletteFileName = QFileDialog.getOpenFileName(self,
                                                           "choose your input file",
                                                           os.getcwd())
        try:
            self.palette_file = io.imread(
                self.paletteFileName[0]).astype('float64')
            self.ui.palette_line_edit_2.setText(self.paletteFileName[0])

            if np.max(self.palette_file) > 1:
                self.palette_file /= 255

        except ValueError:
            msgBox = QMessageBox()
            msgBox.setWindowTitle('error !')
            msgBox.setText("This is not an image file.")
            msgBox.setInformativeText(
                "Please make sure your image have a suitable image format :\n*.jpg or *.png for example." +
                "\nA palette is a image with a height of 1 pixel and as many row as you want ! " +
                "Each pixel is a color the algorithm will be able to use." +
                " You can make one easily with your favorite editing software.")
            msgBox.exec()

    def generatePreview(self, output, outputFilename_preview, mode):
        if mode == 'easy':
            # generate the preview using matplotlib
            fig_pr = plt.figure()
            ax_pr = fig_pr.add_subplot(1, 1, 1)
            ax_pr.imshow(output)
            ax_pr.axis('off')
            fig_pr.tight_layout()
            fig_pr.savefig(outputFilename_preview, dpi=300)
            plt.close()
        else:
            # generate the preview using io.imsave
            io.imsave(outputFilename_preview, output)

    def generatePattern(self, output, outputFilename_withGrid, height, width):
        fig_pt = plt.figure()
        ax_pt = fig_pt.add_subplot(1, 1, 1)
        ax_pt.imshow(output)
        x_major = np.arange(0, output.shape[1], 5) - 0.5
        y_major = np.arange(0, output.shape[0], 5) - 0.5
        x_minor = np.arange(0, output.shape[1]) - 0.5
        y_minor = np.arange(0, output.shape[0]) - 0.5
        ax_pt.set_xticks(x_major, minor=False)
        ax_pt.set_yticks(y_major, minor=False)
        ax_pt.set_xticks(x_minor, minor=True)
        ax_pt.set_yticks(y_minor, minor=True)
        ax_pt.tick_params(colors='w')
        ax_pt.grid(which='major', color='w', linewidth=0.5)
        ax_pt.grid(which='minor', linewidth=0.25)
        fig_pt.tight_layout()
        fig_pt.savefig(outputFilename_withGrid,
                       dpi=max(height, width, 200)*5)
        plt.close()

    def generatePalette(self, outputFilename_palette, palette):
        fig_pl = plt.figure()
        ax_pl = fig_pl.add_subplot(1, 1, 1)
        ax_pl.imshow(palette)
        fig_pl.tight_layout()
        fig_pl.savefig(outputFilename_palette, dpi=300)
        plt.close()

    def launchButton_easy(self):
        # all the magic goes here !
        if self.image is None:
            msgBox = QMessageBox()
            msgBox.setWindowTitle('error !')
            msgBox.setText("No image selected !")
            msgBox.setInformativeText(
                "Please select an image by clicking on the button on the right of the input file section")
            msgBox.exec()
        else:
            self.inputImagePath = Path(self.fileName[0])

            # generate the output
            out, self.palette = processPicture(
                self.image,
                [self.ui.height_selector.value(), self.ui.width_selector.value()],
                int(self.ui.nb_colors_selector.value()))

            # generate all the filepath
            self.outputFilename_preview = "{}/{}_{}x{}_{}_preview.png".format(
                self.inputImagePath.parent, self.inputImagePath.stem, out.shape[0], out.shape[1], self.palette.shape[1])

            self.outputFilename_withGrid = "{}/{}_{}x{}_{}_withGrid.png".format(
                self.inputImagePath.parent, self.inputImagePath.stem, out.shape[0], out.shape[1], self.palette.shape[1])

            self.outputFilename_palette = "{}/{}_{}x{}_{}_palette.png".format(
                self.inputImagePath.parent, self.inputImagePath.stem, out.shape[0], out.shape[1], self.palette.shape[1])

            self.generatePreview(
                out,
                self.outputFilename_preview,
                'easy')

            self.generatePattern(
                out,
                self.outputFilename_withGrid,
                self.ui.height_selector.value(),
                self.ui.width_selector.value())

            self.generatePalette(
                self.outputFilename_palette,
                self.palette)

            msgBox = QMessageBox()
            msgBox.setWindowTitle('operation completed !')
            msgBox.setText("your pattern has been created !")
            msgBox.setInformativeText(
                "you'll find all the files in the same folder as the input" +
                "\n\nIf you're not completely happy with the result, please try using the pro mode !")
            msgBox.exec()

    def launchButton_pro(self):
        # all the magic goes here !
        if self.image is None or self.palette_file is None:
            msgBox = QMessageBox()
            msgBox.setWindowTitle('error !')
            msgBox.setText("No image or/and palette selected !")
            msgBox.setInformativeText(
                "Please select an image or/and a palette by clicking on the button on the right of the input file section")
            msgBox.exec()

        else:
            self.inputImagePath = Path(self.fileName[0])

            out = dithering(self.image, self.palette_file)

            # generate all the filepath
            self.outputFilename_preview = "{}/{}_{}x{}_{}_preview.png".format(
                self.inputImagePath.parent, self.inputImagePath.stem, out.shape[0], out.shape[1], self.palette_file.shape[1])

            self.outputFilename_withGrid = "{}/{}_{}x{}_{}_withGrid.png".format(
                self.inputImagePath.parent, self.inputImagePath.stem, out.shape[0], out.shape[1], self.palette_file.shape[1])

            self.outputFilename_palette = "{}/{}_{}x{}_{}_palette.png".format(
                self.inputImagePath.parent, self.inputImagePath.stem, out.shape[0], out.shape[1], self.palette_file.shape[1])

            self.generatePreview(
                out,
                self.outputFilename_preview,
                'easy')

            self.generatePattern(
                out,
                self.outputFilename_withGrid,
                self.ui.height_selector_2.value(),
                self.ui.width_selector_2.value())

            self.generatePalette(
                self.outputFilename_palette,
                self.palette_file)

            msgBox = QMessageBox()
            msgBox.setWindowTitle('operation completed !')
            msgBox.setText("your pattern has been created !")
            msgBox.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
