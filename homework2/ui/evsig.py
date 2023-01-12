# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'evsig.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDial, QHBoxLayout,
    QLCDNumber, QSizePolicy, QSlider, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(357, 427)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.dial = QDial(Form)
        self.dial.setObjectName(u"dial")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dial.sizePolicy().hasHeightForWidth())
        self.dial.setSizePolicy(sizePolicy)
        self.dial.setMaximum(100)
        self.dial.setWrapping(True)
        self.dial.setNotchesVisible(True)

        self.horizontalLayout.addWidget(self.dial)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.comboBox = QComboBox(Form)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setContextMenuPolicy(Qt.PreventContextMenu)
        self.comboBox.setEditable(True)
        self.comboBox.setInsertPolicy(QComboBox.InsertAlphabetically)
        self.comboBox.setMinimumContentsLength(0)

        self.verticalLayout.addWidget(self.comboBox)

        self.lcdNumber = QLCDNumber(Form)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setMode(QLCDNumber.Oct)



        self.verticalLayout.addWidget(self.lcdNumber)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalSlider = QSlider(Form)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.verticalLayout_2.addWidget(self.horizontalSlider)


        self.retranslateUi(Form)
        self.dial.valueChanged.connect(self.lcdNumber.display)
        self.dial.valueChanged.connect(self.horizontalSlider.setValue)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"oct", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"hex", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Form", u"bin", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Form", u"dec", None))

        self.comboBox.setCurrentText(QCoreApplication.translate("Form", u"oct", None))
    # retranslateUi

