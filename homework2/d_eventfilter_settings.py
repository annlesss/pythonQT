"""
Реализация программу взаимодействия виджетов друг с другом:
Форма для приложения (ui/d_eventfilter_settings.ui)

Программа должна обладать следующим функционалом:

1. Добавить для dial возможность установки значений кнопками клавиатуры(+ и -),
   выводить новые значения в консоль

2. Соединить между собой QDial, QSlider, QLCDNumber
   (изменение значения в одном, изменяет значения в других)

3. Для QLCDNumber сделать отображение в различных системах счисления (oct, hex, bin, dec),
   изменять формат отображаемого значения в зависимости от выбранного в comboBox параметра.

4. Сохранять значение выбранного в comboBox режима отображения
   и значение LCDNumber в QSettings, при перезапуске программы выводить
   в него соответствующие значения
"""

from PySide6 import QtWidgets, QtGui, QtCore
from PySide6.QtGui import QShortcut, QKeySequence
from ui.evsig import Ui_Form




class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.initSignals()
        QShortcut(QKeySequence(QtCore.Qt.Key.Key_Plus), self, activated = self.onKeyPlus)
        QShortcut(QKeySequence(QtCore.Qt.Key.Key_Minus), self, activated = self.onKeyMinus)


    def initSignals(self):
        self.ui.comboBox.currentTextChanged.connect(self.onComboboxChange)



    def onComboboxChange(self):
        if self.ui.comboBox.currentText() == 'oct':
            self.ui.lcdNumber.setOctMode()

        elif self.ui.comboBox.currentText() == 'bin':
            self.ui.lcdNumber.setBinMode()

        elif self.ui.comboBox.currentText() == 'hex':
            self.ui.lcdNumber.setHexMode()

        else:

            self.ui.lcdNumber.setDecMode()

    def onKeyPlus(self):
        self.ui.dial.setValue(self.ui.dial.value()+1)

    def onKeyMinus(self):
        self.ui.dial.setValue(self.ui.dial.value()-1)





if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
