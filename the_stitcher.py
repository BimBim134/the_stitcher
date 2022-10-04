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
        self.ui.choose_file_button.clicked.connect(self.openFile)

        self.ui.ok_button.clicked.connect(self.launchButton)

        self.image = None

        self.imageProportion = self.ui.height_selector.value()/self.ui.width_selector.value()
        self.ui.height_selector.valueChanged.connect(
            self.conserveProportion_height)
        self.ui.width_selector.valueChanged.connect(
            self.conserveProportion_width)
        self.ui.conserve_proportion_button.toggled.connect(
            self.setImageProportion)

    def setImageProportion(self):
        if self.ui.conserve_proportion_button.isChecked():
            self.imageProportion = self.ui.height_selector.value()/self.ui.width_selector.value()

    def conserveProportion_height(self):
        if self.ui.conserve_proportion_button.isChecked():
            self.ui.width_selector.setValue(
                self.ui.height_selector.value()/self.imageProportion)

    def conserveProportion_width(self):
        if self.ui.conserve_proportion_button.isChecked():
            self.ui.height_selector.setValue(
                self.ui.width_selector.value()*self.imageProportion)

    def openFile(self):
        self.fileName = QFileDialog.getOpenFileName(self,
                                                    "choose your input file",
                                                    os.getcwd())
        try:
            self.image = io.imread(self.fileName[0])
            self.ui.file_line_edit.setText(self.fileName[0])

            self.imageProportion = self.image.shape[0]/self.image.shape[1]

            self.ui.width_selector.setValue(self.image.shape[0])
            self.ui.width_selector.setMaximum(self.image.shape[0])

            self.ui.height_selector.setValue(self.image.shape[1])
            self.ui.height_selector.setMaximum(self.image.shape[1])

        except ValueError:
            msgBox = QMessageBox()
            msgBox.setWindowTitle('error !')
            msgBox.setText("This is not an image file.")
            msgBox.setInformativeText(
                "Please make sure your image have a suitable image format :\n*.jpg or *.png for example.")
            msgBox.exec()

    def launchButton(self):
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

            # generate all the filepath
            self.outputFilename_preview = "{}/{}_preview.jpg".format(
                self.inputImagePath.parent, self.inputImagePath.stem)

            self.outputFilename_withGrid = "{}/{}_withGrid.jpg".format(
                self.inputImagePath.parent, self.inputImagePath.stem)

            self.outputFilename_palette = "{}/{}_palette.jpg".format(
                self.inputImagePath.parent, self.inputImagePath.stem)

            # generate the output
            self.output, self.palette = processPicture(
                self.image,
                [self.ui.height_selector.value(), self.ui.width_selector.value()],
                int(self.ui.nb_colors_selector.value()))

            # generate the preview

            fig1 = plt.figure()
            ax1 = fig1.add_subplot(1, 1, 1)
            ax1.imshow(self.output)
            ax1.axis('off')
            fig1.tight_layout()
            fig1.savefig(self.outputFilename_preview, dpi=300)
            fig1.clf()

            # generate pattern
            fig2 = plt.figure()
            ax2 = fig2.add_subplot(1, 1, 1)
            ax2.imshow(self.output)
            x_major = np.arange(0, self.output.shape[1], 5) - 0.5
            y_major = np.arange(0, self.output.shape[0], 5) - 0.5
            x_minor = np.arange(0, self.output.shape[1]) - 0.5
            y_minor = np.arange(0, self.output.shape[0]) - 0.5
            ax2.set_xticks(x_major, minor=False)
            ax2.set_yticks(y_major, minor=False)
            ax2.set_xticks(x_minor, minor=True)
            ax2.set_yticks(y_minor, minor=True)
            ax2.tick_params(colors='w')
            ax2.grid(which='major', color='w', linewidth=0.5)
            ax2.grid(which='minor', linewidth=0.25)
            fig2.tight_layout()
            fig2.savefig(self.outputFilename_withGrid,
                        dpi=max(self.ui.height_selector.value(), self.ui.width_selector.value(), 200)*5)
            fig2.clf()

            fig3 = plt.figure()
            ax3 = fig3.add_subplot(1, 1, 1)
            ax3.imshow(self.palette)
            fig3.tight_layout()
            fig3.savefig(self.outputFilename_palette, dpi=300)
            fig3.clf()

            msgBox = QMessageBox()
            msgBox.setWindowTitle('operation completed !')
            msgBox.setText("your pattern has been created !")
            msgBox.setInformativeText(
                "you'll find all the files in the same folder as the input")
            msgBox.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
