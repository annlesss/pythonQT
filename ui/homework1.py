# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'homework1.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QCheckBox, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPlainTextEdit, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QStatusBar, QTabWidget,
    QTextEdit, QToolBox, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(830, 709)
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.action_2 = QAction(MainWindow)
        self.action_2.setObjectName(u"action_2")
        self.action_QT = QAction(MainWindow)
        self.action_QT.setObjectName(u"action_QT")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 0, 781, 651))
        self.widget = QWidget()
        self.widget.setObjectName(u"widget")
        self.layoutWidget = QWidget(self.widget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 10, 701, 611))
        self.verticalLayout_7 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(92, 208))
        self.label.setMaximumSize(QSize(92, 16777215))

        self.verticalLayout.addWidget(self.label)

        self.radioButton = QRadioButton(self.layoutWidget)
        self.radioButton.setObjectName(u"radioButton")

        self.verticalLayout.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.layoutWidget)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.verticalLayout.addWidget(self.radioButton_2)

        self.radioButton_3 = QRadioButton(self.layoutWidget)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.verticalLayout.addWidget(self.radioButton_3)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.verticalLayout_5.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.checkBox = QCheckBox(self.layoutWidget)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout_2.addWidget(self.checkBox)

        self.checkBox_2 = QCheckBox(self.layoutWidget)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.verticalLayout_2.addWidget(self.checkBox_2)

        self.checkBox_3 = QCheckBox(self.layoutWidget)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.verticalLayout_2.addWidget(self.checkBox_3)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_4.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.toolBox = QToolBox(self.layoutWidget)
        self.toolBox.setObjectName(u"toolBox")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 341, 452))
        self.widget1 = QWidget(self.page)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(20, 10, 311, 431))
        self.verticalLayout_9 = QVBoxLayout(self.widget1)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_3 = QLabel(self.widget1)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_5.addWidget(self.label_3)

        self.lineEdit = QLineEdit(self.widget1)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_5.addWidget(self.lineEdit)


        self.verticalLayout_8.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_4 = QLabel(self.widget1)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_6.addWidget(self.label_4)

        self.lineEdit_2 = QLineEdit(self.widget1)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout_6.addWidget(self.lineEdit_2)


        self.verticalLayout_8.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_5 = QLabel(self.widget1)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_8.addWidget(self.label_5)

        self.lineEdit_3 = QLineEdit(self.widget1)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.horizontalLayout_8.addWidget(self.lineEdit_3)


        self.verticalLayout_8.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_6 = QLabel(self.widget1)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_7.addWidget(self.label_6)

        self.lineEdit_4 = QLineEdit(self.widget1)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.horizontalLayout_7.addWidget(self.lineEdit_4)


        self.verticalLayout_8.addLayout(self.horizontalLayout_7)


        self.verticalLayout_9.addLayout(self.verticalLayout_8)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer)

        self.toolBox.addItem(self.page, u"QLineEdit")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.textEdit_2 = QTextEdit(self.page_3)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(0, 0, 341, 470))
        self.toolBox.addItem(self.page_3, u"QTextEdit")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 341, 452))
        self.plainTextEdit = QPlainTextEdit(self.page_2)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(10, 0, 331, 451))
        self.toolBox.addItem(self.page_2, u"QPlainTextEdit")
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.calendarWidget = QCalendarWidget(self.page_4)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setGeometry(QRect(15, 20, 311, 281))
        self.toolBox.addItem(self.page_4, u"QCalendarWidget")

        self.verticalLayout_3.addWidget(self.toolBox)


        self.verticalLayout_6.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")

        self.verticalLayout_6.addLayout(self.verticalLayout_4)


        self.horizontalLayout_4.addLayout(self.verticalLayout_6)


        self.verticalLayout_7.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton = QPushButton(self.layoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_3.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_3.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.layoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_3.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.layoutWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_3.addWidget(self.pushButton_4)


        self.verticalLayout_7.addLayout(self.horizontalLayout_3)

        self.tabWidget.addTab(self.widget, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 830, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.action)
        self.menu_2.addAction(self.action_2)
        self.menu_2.addAction(self.action_QT)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.toolBox.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.action_2.setText(QCoreApplication.translate("MainWindow", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
        self.action_QT.setText(QCoreApplication.translate("MainWindow", u"\u041e QT", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"QRadioButtom", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"RadioButton 1", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"RadioButton 2", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"RadioButton 3", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"QCheckBox", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0432\u0430\u0448\u0443 \u0444\u0430\u043c\u0438\u043b\u0438\u044e", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f", None))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0432\u0430\u0448\u0435 \u0438\u043c\u044f", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0432\u0430\u0448\u0435 \u043e\u0442\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043b\u0435\u0444\u043e\u043d", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0432\u0430\u0448 \u0442\u0435\u043b\u0435\u0444\u043e\u043d", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("MainWindow", u"QLineEdit", None))
        self.textEdit_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.875pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">\u0422\u0435\u043a\u0441\u0442 \u043c\u043e\u0436\u0435\u0442 \u0431\u044b\u0442\u044c \u043f\u043e\u043b\u0443\u0436\u0438\u0440\u043d\u044b\u043c.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">\u0422\u0435\u043a\u0441\u0442 \u043c\u043e\u0436\u0435\u0442 \u0431\u044b\u0442\u044c \u043a\u0443\u0440\u0441\u0438\u0432\u043e\u043c.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margi"
                        "n-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0422\u0435\u043a\u0441\u0442 \u043c\u043e\u0436\u043d\u043e <span style=\" text-decoration: underline;\">\u043f\u043e\u0434\u0447\u0435\u0440\u043a\u043d\u0443\u0442\u044c.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0422\u0435\u043a\u0441\u0442 \u043c\u043e\u0436\u0435\u0442 \u0431\u044b\u0442\u044c <span style=\" vertical-align:super;\">\u043d\u0430\u0434\u0441\u0442\u0440\u043e\u0447\u043d\u044b\u043c</span>.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0422\u0435\u043a\u0441\u0442 \u043c\u043e\u0436\u0435\u0442 \u0431\u044b\u0442\u044c <span style=\" vertical-align:sub;\">\u043f\u043e\u0434\u0441\u0442\u0440\u043e\u0447\u043d\u044b\u043c</span>.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -"
                        "qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), QCoreApplication.translate("MainWindow", u"QTextEdit", None))
        self.plainTextEdit.setPlainText(QCoreApplication.translate("MainWindow", u"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum in semper nulla, sed feugiat turpis. Cras blandit suscipit pharetra. Aliquam vitae mollis magna. Curabitur a tortor nec risus venenatis vehicula. Proin a metus eu arcu tempus iaculis ut sed dui. Sed bibendum convallis tellus, eu viverra arcu pulvinar sit amet. Proin vitae lorem in tellus imperdiet rhoncus sed eget elit. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec efficitur molestie elit ac facilisis. Morbi ac volutpat dui, ut scelerisque lectus. Nunc dapibus eros sem, vitae molestie augue bibendum eu. Ut neque diam, ornare eu ligula eget, sagittis faucibus augue. Mauris tristique volutpat porta. Nunc eget nulla in leo viverra mattis. Proin malesuada enim quis scelerisque finibus. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"QPlainTextEdit", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_4), QCoreApplication.translate("MainWindow", u"QCalendarWidget", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u043d\u044e", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"?", None))
    # retranslateUi

