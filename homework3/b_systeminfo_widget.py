"""
Реализовать виджет, который будет работать с потоком SystemInfo из модуля a_threads

Создавать форму можно как в ручную, так и с помощью программы Designer

Форма должна содержать:
1. поле для ввода времени задержки
2. поле для вывода информации о загрузке CPU
3. поле для вывода информации о загрузке RAM
4. поток необходимо запускать сразу при старте приложения
5. установку времени задержки сделать "горячей", т.е. поток должен сразу
реагировать на изменение времени задержки
"""

from PySide6 import QtWidgets
from a_threads import SystemInfo
from ui.systemwidget import Ui_Form
import psutil


class Window(QtWidgets.QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.initThreads()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        #self.system_info = SystemInfo()
        self.initSignals()

    #def filling(self):
        #self.ui.lineEdit.textChanged.connect(self.restart_thread)

    def initSignals(self):
        self.system_info.systemInfoReceived.connect(self.initThreads)



    #def onGettingInfo(self, info):
        #cpu_value, ram_value = info
        #self.ui.lineEdit_2.appendText(cpu_value)
        #self.ui.lineEdit_3.appendText(ram_value)
    def cpu_ram_data(self):
        self.system_info.systemInfoReceived()


    def initThreads(self):
        self.system_info = SystemInfo()
        self.system_info.start()

    def closeEvent(self) -> None:
        self.system_info.terminate()

    #def restart_thread(self):
        #pass


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()









