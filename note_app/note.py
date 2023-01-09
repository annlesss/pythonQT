from PySide6 import QtWidgets
from ui.notee import Ui_MainWindow

class Window(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initSignals()

    def initSignals(self):
        self.ui.tableWidget.setEnabled(True)


        self.ui.lineEdit.returnPressed.connect(self.get_text)
        self.ui.pushButton.setEnabled(True)
        self.ui.pushButton.clicked.connect(self.get_text)
        #self.ui.lineEdit.connect(self.lineEditChange)
        #self.ui.textEdit.connect(self.onTextChanged)
        #self.ui.timeEdit.connect(self.onTimeChanged)
        #self.ui.dateTimeEdit.connect(self.onTimeChanged)

    def lineEditChange(self):
        self.ui.lineEdit.setText()

    def onTextChanged(self):
        self.ui.textEdit.setText()

    def onTimeChanged(self):
        self.ui.timeEdit.setTime()

    def onDateTimeChanged(self):
        self.ui.dateTimeEdit.setDateTime()

    def get_text(self):
        table = QtWidgets.QTableWidget(self)

        heading = self.ui.lineEdit.text()
        note = self.ui.textEdit.toPlainText()
        time = self.ui.timeEdit.time().toString('HH:mm:ss')
        datetimee = self.ui.dateTimeEdit.time().toString('HH:mm:ss')

        data = [heading, note, time, datetimee]
        table.setColumnCount(4)
        table.setRowCount(len(data))


        table.setItem(0, 0, QtWidgets.QTableWidgetItem(str(data[0])))
        table.setItem(0, 1, QtWidgets.QTableWidgetItem(str(data[1])))
        table.setItem(0, 2, QtWidgets.QTableWidgetItem(str(data[2])))
        table.setItem(0, 3, QtWidgets.QTableWidgetItem(str(data[3])))

        #table.resizeColumnsToContents()
        print(data)




if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()

