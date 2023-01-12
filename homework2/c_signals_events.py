"""
Реализация программу проверки состояния окна:
Форма для приложения (ui/c_signals_events.ui)

Программа должна обладать следующим функционалом:

1. Возможность перемещения окна по заданным координатам.
2. Возможность получения параметров экрана (вывод производить в plainTextEdit + добавлять время).
    * Кол-во экранов
    * Текущее основное окно
    * Разрешение экрана
    * На каком экране окно находится
    * Размеры окна
    * Минимальные размеры окна
    * Текущее положение (координаты) окна
    * Координаты центра приложения
    * Отслеживание состояния окна (свернуто/развёрнуто/активно/отображено)
3. Возможность отслеживания состояния окна (вывод производить в консоль + добавлять время).
    * При перемещении окна выводить его старую и новую позицию
    * При изменении размера окна выводить его новый размер
"""


from PySide6 import QtWidgets, QtGui, QtCore
from ui.c_sigev import Ui_Form


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.initSignals()
        # set plain text
        # данные экрана
        #print(QtWidgets.QApplication.screens())
        # где расположены приложения
        #current_screen = QtWidgets.QApplication.screenAt(self.pos())
        #print(current_screen.size().width(), current_screen.size().height()



    def initSignals(self) -> None:
        """
        Инициализация сигналов
        :return: None
        """
        self.ui.pushButtonLT.clicked.connect(lambda: self.move(0, 0))
        self.ui.pushButtonRT.clicked.connect(self.moveRightTop) # по аналогии остальные кнопки
        self.ui.pushButtonLB.clicked.connect(self.moveLeftBelow)
        self.ui.pushButtonRB.clicked.connect(self.moveRightBelow)
        self.ui.pushButtonCenter.clicked.connect(self.moveCentre)
        self.ui.pushButtonGetData.clicked.connect(self.onButtonGetData)


    def moveRightTop(self):

        current_screen = QtWidgets.QApplication.screenAt(self.pos()) # ссылка на текущий экран
        screen_width = current_screen.size().width() # печать ширины окна, ширина hight
        pos_x = screen_width - self.width()

        self.move(pos_x, 0) # положение экрана в центре

    def moveLeftBelow(self):
        current_screen = QtWidgets.QApplication.screenAt(self.pos())
        screen_height = current_screen.size().height()
        pos_y = screen_height - self.height()

        self.move(0, pos_y)


    def moveRightBelow(self):
        current_screen = QtWidgets.QApplication.screenAt(self.pos()) # вычисляем положение окна
        screen_height = current_screen.size().height() # вычисляем высоту окна
        screen_width = current_screen.size().width() # вычисляем ширину окна
        pos_y = screen_height - self.height() #
        pos_x = screen_width - self.width() #

        self.move(pos_x, pos_y)

    def moveCentre(self):
        current_screen = QtWidgets.QApplication.screenAt(self.pos())
        screen_height = current_screen.size().height()
        screen_width = current_screen.size().width()
        pos_y = screen_height / 2 - self.height()/2
        pos_x = screen_width/ 2 - self.width()/2

        self.move(pos_x, pos_y)

    def onButtonGetData(self):
        current_screen = QtWidgets.QApplication.screenAt(self.pos()).name()
        self.ui.plainTextEdit.appendPlainText(f"текущее время: {QtCore.QDateTime.currentDateTime().toString('HH:mm:ss dd.MM.yy t')}")
        self.ui.plainTextEdit.setPlainText(f"текущий монитор: {current_screen}")
        app_data = QtWidgets.QApplication.screens()
        self.ui.plainTextEdit.appendPlainText(f"количество мониторов: {len(app_data)}")
        self.ui.plainTextEdit.appendPlainText(f"разрешение экрана: {self.screen().size().width()}, {self.screen().size().height()}")
        self.ui.plainTextEdit.appendPlainText(f"окно находится на экране: {self.screen().name()}")
        self.ui.plainTextEdit.appendPlainText(f"размеры окна: {self.width()}, {self.height()}")
        self.ui.plainTextEdit.appendPlainText(f"минимальные размеры окна: {self.minimumWidth()}, {self.minimumHeight()}")
        self.ui.plainTextEdit.appendPlainText(f"текущие координаты окна: {self.geometry().getCoords()}")
        self.ui.plainTextEdit.appendPlainText(f"координаты положения центра: {self.geometry().center()}")
        self.ui.plainTextEdit.appendPlainText(f"состояние окна: {QtGui.QGuiApplication.applicationState().name}")

    def event(self, event):
        if event.type() == QtCore.QEvent.Type.Move:
            print(f"{QtCore.QDateTime.currentDateTime().toString('HH.mm.ss dd.MM.yyyy')}, произошло перемещение окна\n"
                  f"прежняя позиция окна: {event.oldPos()}\n" f"новая позиция окна: {event.pos()}")

        if event.type() == QtCore.QEvent.Type.Resize:
            print(f"{QtCore.QDateTime.currentDateTime().toString('HH.mm.ss dd.MM.yyyy')}, произошло изменение размера окна\n"
                  f"новый размер окна: {event.size().width()}, {event.size().height()}")
        return super(Window, self).event(event)

if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
