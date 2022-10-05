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
    QRadioButton, QSizePolicy, QTabWidget, QToolButton,
    QVBoxLayout, QWidget)

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
        self.verticalLayout.setContentsMargins(20, 0, 20, 20)
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

        self.tabWidget = QTabWidget(self.verticalLayoutWidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tab_easy = QWidget()
        self.tab_easy.setObjectName(u"tab_easy")
        self.layoutWidget = QWidget(self.tab_easy)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(2, 2, 471, 231))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(20, 0, 20, 0)
        self.ok_button = QPushButton(self.layoutWidget)
        self.ok_button.setObjectName(u"ok_button")

        self.gridLayout.addWidget(self.ok_button, 5, 1, 1, 1)

        self.width_selector = QDoubleSpinBox(self.layoutWidget)
        self.width_selector.setObjectName(u"width_selector")
        self.width_selector.setDecimals(0)
        self.width_selector.setMaximum(1920.000000000000000)
        self.width_selector.setValue(1920.000000000000000)

        self.gridLayout.addWidget(self.width_selector, 1, 1, 1, 1)

        self.conserve_proportion_label = QLabel(self.layoutWidget)
        self.conserve_proportion_label.setObjectName(u"conserve_proportion_label")

        self.gridLayout.addWidget(self.conserve_proportion_label, 3, 0, 1, 1)

        self.height_label = QLabel(self.layoutWidget)
        self.height_label.setObjectName(u"height_label")

        self.gridLayout.addWidget(self.height_label, 2, 0, 1, 1)

        self.nb_color_label = QLabel(self.layoutWidget)
        self.nb_color_label.setObjectName(u"nb_color_label")

        self.gridLayout.addWidget(self.nb_color_label, 4, 0, 1, 1)

        self.width_label = QLabel(self.layoutWidget)
        self.width_label.setObjectName(u"width_label")

        self.gridLayout.addWidget(self.width_label, 1, 0, 1, 1)

        self.input_image_label = QLabel(self.layoutWidget)
        self.input_image_label.setObjectName(u"input_image_label")

        self.gridLayout.addWidget(self.input_image_label, 0, 0, 1, 1)

        self.height_selector = QDoubleSpinBox(self.layoutWidget)
        self.height_selector.setObjectName(u"height_selector")
        self.height_selector.setDecimals(0)
        self.height_selector.setMaximum(1080.000000000000000)
        self.height_selector.setValue(1080.000000000000000)

        self.gridLayout.addWidget(self.height_selector, 2, 1, 1, 1)

        self.file_line_edit = QLineEdit(self.layoutWidget)
        self.file_line_edit.setObjectName(u"file_line_edit")

        self.gridLayout.addWidget(self.file_line_edit, 0, 1, 1, 1)

        self.choose_file_button = QToolButton(self.layoutWidget)
        self.choose_file_button.setObjectName(u"choose_file_button")

        self.gridLayout.addWidget(self.choose_file_button, 0, 2, 1, 1)

        self.nb_colors_selector = QDoubleSpinBox(self.layoutWidget)
        self.nb_colors_selector.setObjectName(u"nb_colors_selector")
        self.nb_colors_selector.setDecimals(0)
        self.nb_colors_selector.setValue(8.000000000000000)

        self.gridLayout.addWidget(self.nb_colors_selector, 4, 1, 1, 1)

        self.conserve_proportion_button = QRadioButton(self.layoutWidget)
        self.conserve_proportion_button.setObjectName(u"conserve_proportion_button")
        self.conserve_proportion_button.setChecked(True)

        self.gridLayout.addWidget(self.conserve_proportion_button, 3, 1, 1, 1)

        self.tabWidget.addTab(self.tab_easy, "")
        self.tab_pro = QWidget()
        self.tab_pro.setObjectName(u"tab_pro")
        self.layoutWidget_2 = QWidget(self.tab_pro)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(0, 0, 471, 231))
        self.gridLayout_2 = QGridLayout(self.layoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_2.setContentsMargins(20, 0, 20, 0)
        self.width_selector_2 = QDoubleSpinBox(self.layoutWidget_2)
        self.width_selector_2.setObjectName(u"width_selector_2")
        self.width_selector_2.setDecimals(0)
        self.width_selector_2.setMaximum(1920.000000000000000)
        self.width_selector_2.setValue(1920.000000000000000)

        self.gridLayout_2.addWidget(self.width_selector_2, 2, 1, 1, 1)

        self.height_label_2 = QLabel(self.layoutWidget_2)
        self.height_label_2.setObjectName(u"height_label_2")

        self.gridLayout_2.addWidget(self.height_label_2, 4, 0, 1, 1)

        self.width_label_2 = QLabel(self.layoutWidget_2)
        self.width_label_2.setObjectName(u"width_label_2")

        self.gridLayout_2.addWidget(self.width_label_2, 2, 0, 1, 1)

        self.file_line_edit_2 = QLineEdit(self.layoutWidget_2)
        self.file_line_edit_2.setObjectName(u"file_line_edit_2")

        self.gridLayout_2.addWidget(self.file_line_edit_2, 0, 1, 1, 1)

        self.height_selector_2 = QDoubleSpinBox(self.layoutWidget_2)
        self.height_selector_2.setObjectName(u"height_selector_2")
        self.height_selector_2.setDecimals(0)
        self.height_selector_2.setMaximum(1080.000000000000000)
        self.height_selector_2.setValue(1080.000000000000000)

        self.gridLayout_2.addWidget(self.height_selector_2, 4, 1, 1, 1)

        self.choose_palette_button_2 = QToolButton(self.layoutWidget_2)
        self.choose_palette_button_2.setObjectName(u"choose_palette_button_2")

        self.gridLayout_2.addWidget(self.choose_palette_button_2, 1, 2, 1, 1)

        self.input_image_label_2 = QLabel(self.layoutWidget_2)
        self.input_image_label_2.setObjectName(u"input_image_label_2")

        self.gridLayout_2.addWidget(self.input_image_label_2, 0, 0, 1, 1)

        self.input_palette_label_2 = QLabel(self.layoutWidget_2)
        self.input_palette_label_2.setObjectName(u"input_palette_label_2")

        self.gridLayout_2.addWidget(self.input_palette_label_2, 1, 0, 1, 1)

        self.conserve_proportion_label_2 = QLabel(self.layoutWidget_2)
        self.conserve_proportion_label_2.setObjectName(u"conserve_proportion_label_2")

        self.gridLayout_2.addWidget(self.conserve_proportion_label_2, 5, 0, 1, 1)

        self.conserve_proportion_button_2 = QRadioButton(self.layoutWidget_2)
        self.conserve_proportion_button_2.setObjectName(u"conserve_proportion_button_2")
        self.conserve_proportion_button_2.setChecked(True)

        self.gridLayout_2.addWidget(self.conserve_proportion_button_2, 5, 1, 1, 1)

        self.ok_button_2 = QPushButton(self.layoutWidget_2)
        self.ok_button_2.setObjectName(u"ok_button_2")

        self.gridLayout_2.addWidget(self.ok_button_2, 6, 1, 1, 1)

        self.choose_file_button_2 = QToolButton(self.layoutWidget_2)
        self.choose_file_button_2.setObjectName(u"choose_file_button_2")

        self.gridLayout_2.addWidget(self.choose_file_button_2, 0, 2, 1, 1)

        self.palette_line_edit_2 = QLineEdit(self.layoutWidget_2)
        self.palette_line_edit_2.setObjectName(u"palette_line_edit_2")

        self.gridLayout_2.addWidget(self.palette_line_edit_2, 1, 1, 1, 1)

        self.tabWidget.addTab(self.tab_pro, "")

        self.verticalLayout.addWidget(self.tabWidget)


        self.retranslateUi(Widget)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Generate your own cross stitch pattern !", None))
        self.title_label.setText(QCoreApplication.translate("Widget", u"the Stitcher", None))
#if QT_CONFIG(tooltip)
        self.tabWidget.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.ok_button.setText(QCoreApplication.translate("Widget", u"let's go !", None))
        self.conserve_proportion_label.setText(QCoreApplication.translate("Widget", u"Conserve proportions :", None))
        self.height_label.setText(QCoreApplication.translate("Widget", u"Height :", None))
        self.nb_color_label.setText(QCoreApplication.translate("Widget", u"Number of colors desired :", None))
        self.width_label.setText(QCoreApplication.translate("Widget", u"Width :", None))
        self.input_image_label.setText(QCoreApplication.translate("Widget", u"Input image :", None))
        self.choose_file_button.setText(QCoreApplication.translate("Widget", u"...", None))
        self.conserve_proportion_button.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_easy), QCoreApplication.translate("Widget", u"Easy mode", None))
        self.height_label_2.setText(QCoreApplication.translate("Widget", u"Height :", None))
        self.width_label_2.setText(QCoreApplication.translate("Widget", u"Width :", None))
#if QT_CONFIG(tooltip)
        self.choose_palette_button_2.setToolTip(QCoreApplication.translate("Widget", u"<html><head/><body><p>A palette is a image with a height of 1 pixel and as many row as you want ! Each pixel is a color the algorithm will be able to use.</p><p><br/></p><p>format : [ <span style=\" font-weight:700;\">1</span> x <span style=\" font-weight:700;\">number of colors wanted</span> ]</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.choose_palette_button_2.setText(QCoreApplication.translate("Widget", u"...", None))
        self.input_image_label_2.setText(QCoreApplication.translate("Widget", u"Input image :", None))
#if QT_CONFIG(tooltip)
        self.input_palette_label_2.setToolTip(QCoreApplication.translate("Widget", u"<html><head/><body><p>A palette is a image with a height of 1 pixel and as many row as you want ! Each pixel is a color the algorithm will be able to use.</p><p><br/></p><p>format : [ <span style=\" font-weight:700;\">1</span> x <span style=\" font-weight:700;\">number of colors wanted</span> ]</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.input_palette_label_2.setText(QCoreApplication.translate("Widget", u"Input palette :", None))
        self.conserve_proportion_label_2.setText(QCoreApplication.translate("Widget", u"Conserve proportions :", None))
        self.conserve_proportion_button_2.setText("")
        self.ok_button_2.setText(QCoreApplication.translate("Widget", u"Trust me! It will be fabulous.", None))
        self.choose_file_button_2.setText(QCoreApplication.translate("Widget", u"...", None))
#if QT_CONFIG(tooltip)
        self.palette_line_edit_2.setToolTip(QCoreApplication.translate("Widget", u"<html><head/><body><p>A palette is a image with a height of 1 pixel and as many row as you want ! Each pixel is a color the algorithm will be able to use.</p><p><br/></p><p>format : [ <span style=\" font-weight:700;\">1</span> x <span style=\" font-weight:700;\">number of colors wanted</span> ]</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_pro), QCoreApplication.translate("Widget", u"I'm a pro", None))
    # retranslateUi

