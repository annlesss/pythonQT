from PySide6 import QtWidgets
from ui.homework1 import Ui_MainWindow


class Window(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initui()
        self.show()

    def initui(self) -> None:
        self.setWindowTitle("Тренировка")


if __name__ == "__main__":
    app = QtWidgets.QApplication()
    window = Window()
    window.show()
    app.exec()


