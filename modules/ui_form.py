# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QFrame, QGridLayout,
    QLabel, QLayout, QLineEdit, QPushButton,
    QRadioButton, QSizePolicy, QToolButton, QVBoxLayout,
    QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.setWindowModality(Qt.WindowModal)
        Widget.resize(500, 350)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Widget.sizePolicy().hasHeightForWidth())
        Widget.setSizePolicy(sizePolicy)
        Widget.setMinimumSize(QSize(500, 350))
        Widget.setMaximumSize(QSize(500, 350))
        self.verticalLayoutWidget = QWidget(Widget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 514, 351))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, 0, 20, 0)
        self.title_label = QLabel(self.verticalLayoutWidget)
        self.title_label.setObjectName(u"title_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.title_label.sizePolicy().hasHeightForWidth())
        self.title_label.setSizePolicy(sizePolicy1)
        palette = QPalette()
        self.title_label.setPalette(palette)
        font = QFont()
        font.setFamilies([u"Fira Sans Condensed ExtraBold"])
        font.setPointSize(40)
        font.setItalic(True)
        self.title_label.setFont(font)
        self.title_label.setAutoFillBackground(False)
        self.title_label.setFrameShape(QFrame.NoFrame)
        self.title_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.title_label)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(20, -1, 20, -1)
        self.file_line_edit = QLineEdit(self.verticalLayoutWidget)
        self.file_line_edit.setObjectName(u"file_line_edit")

        self.gridLayout.addWidget(self.file_line_edit, 0, 1, 1, 1)

        self.width_label = QLabel(self.verticalLayoutWidget)
        self.width_label.setObjectName(u"width_label")

        self.gridLayout.addWidget(self.width_label, 1, 0, 1, 1)

        self.nb_colors_selector = QDoubleSpinBox(self.verticalLayoutWidget)
        self.nb_colors_selector.setObjectName(u"nb_colors_selector")
        self.nb_colors_selector.setDecimals(0)
        self.nb_colors_selector.setValue(8.000000000000000)

        self.gridLayout.addWidget(self.nb_colors_selector, 5, 1, 1, 1)

        self.height_label = QLabel(self.verticalLayoutWidget)
        self.height_label.setObjectName(u"height_label")

        self.gridLayout.addWidget(self.height_label, 3, 0, 1, 1)

        self.conserve_proportion_label = QLabel(self.verticalLayoutWidget)
        self.conserve_proportion_label.setObjectName(u"conserve_proportion_label")

        self.gridLayout.addWidget(self.conserve_proportion_label, 4, 0, 1, 1)

        self.width_selector = QDoubleSpinBox(self.verticalLayoutWidget)
        self.width_selector.setObjectName(u"width_selector")
        self.width_selector.setDecimals(0)
        self.width_selector.setMaximum(1920.000000000000000)
        self.width_selector.setValue(1920.000000000000000)

        self.gridLayout.addWidget(self.width_selector, 1, 1, 1, 1)

        self.conserve_proportion_button = QRadioButton(self.verticalLayoutWidget)
        self.conserve_proportion_button.setObjectName(u"conserve_proportion_button")
        self.conserve_proportion_button.setChecked(True)

        self.gridLayout.addWidget(self.conserve_proportion_button, 4, 1, 1, 1)

        self.input_image_label = QLabel(self.verticalLayoutWidget)
        self.input_image_label.setObjectName(u"input_image_label")

        self.gridLayout.addWidget(self.input_image_label, 0, 0, 1, 1)

        self.choose_file_button = QToolButton(self.verticalLayoutWidget)
        self.choose_file_button.setObjectName(u"choose_file_button")

        self.gridLayout.addWidget(self.choose_file_button, 0, 2, 1, 1)

        self.nb_color_label = QLabel(self.verticalLayoutWidget)
        self.nb_color_label.setObjectName(u"nb_color_label")

        self.gridLayout.addWidget(self.nb_color_label, 5, 0, 1, 1)

        self.height_selector = QDoubleSpinBox(self.verticalLayoutWidget)
        self.height_selector.setObjectName(u"height_selector")
        self.height_selector.setDecimals(0)
        self.height_selector.setMaximum(1080.000000000000000)
        self.height_selector.setValue(1080.000000000000000)

        self.gridLayout.addWidget(self.height_selector, 3, 1, 1, 1)

        self.ok_button = QPushButton(self.verticalLayoutWidget)
        self.ok_button.setObjectName(u"ok_button")

        self.gridLayout.addWidget(self.ok_button, 6, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Generate your own cross stitch pattern !", None))
        self.title_label.setText(QCoreApplication.translate("Widget", u"the Stitcher", None))
        self.width_label.setText(QCoreApplication.translate("Widget", u"Width :", None))
        self.height_label.setText(QCoreApplication.translate("Widget", u"Height :", None))
        self.conserve_proportion_label.setText(QCoreApplication.translate("Widget", u"Conserve proportions :", None))
        self.conserve_proportion_button.setText("")
        self.input_image_label.setText(QCoreApplication.translate("Widget", u"Input image :", None))
        self.choose_file_button.setText(QCoreApplication.translate("Widget", u"...", None))
        self.nb_color_label.setText(QCoreApplication.translate("Widget", u"Number of colors desired :", None))
        self.ok_button.setText(QCoreApplication.translate("Widget", u"let's go !", None))
    # retranslateUi

