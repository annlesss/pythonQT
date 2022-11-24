from PySide6 import QtWidgets
from ui.practice_1_ui import Ui_Form

class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.initUi()

    def initUi(self)-> None:
        """
        Донастройка Ui
        :return: None
        """
        self.setWindowTitle("Авторизация")

        #self.setMinimumSize(300, 170)
        #self.setMaximumSize(300, 170)
        self.setFixedSize(300, 250)

        self.ui.lineEdit.setPlaceholderText("Введите логин")
        self.ui.lineEdit_2.setPlaceholderText("Введите пароль")
        self.ui.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.EchoMode.PasswordEchoOnEdit)
        self.ui.lineEdit.setText("annlesss")

        #self.show() вместо window.show()
        #self.pb_1 = QtWidgets.QPushButton("Кнопка", self)

    def initSignals(self) -> None:
        """

        :return: None
        """
        self.pb_1.clicked.connect(self.print_hello)

    def initChilds(self):
        """
        Инициализация дочерних окон
        :return: None
        """
        self.win_2 = ChildWindow()
        pass

    def print_hello(self):
        print("hello")


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    window = Window() #экземпляр класса
    window.show()


    app.exec() # закрытие окна