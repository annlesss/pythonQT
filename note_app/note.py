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
        self.ui.tableWidget.setRowCount(0)

        self.ui.lineEdit.returnPressed.connect(self.get_text)
        self.ui.pushButton.setEnabled(True)
        self.ui.pushButton.clicked.connect(self.get_text)
        self.ui.pushButton_2.clicked.connect(self.delete_row)

    def onTextChanged(self):
        self.ui.textEdit.setText()

    def onTimeChanged(self):
        self.ui.timeEdit.setTime()

    def onDateTimeChanged(self):
        self.ui.dateTimeEdit.setDateTime()

    def get_text(self):
        table = self.ui.tableWidget

        heading = self.ui.lineEdit.text()
        note = self.ui.textEdit.toPlainText()
        time = self.ui.timeEdit.time().toString('HH:mm:ss')
        datetimee = self.ui.dateTimeEdit.time().toString('HH:mm:ss')

        data = [heading, note, time, datetimee]
        table.setColumnCount(4)
        current_row = table.rowCount()
        table.setRowCount(table.rowCount()+1)


        table.setItem(current_row, 0, QtWidgets.QTableWidgetItem(str(data[0])))
        table.setItem(current_row, 1, QtWidgets.QTableWidgetItem(str(data[1])))
        table.setItem(current_row, 2, QtWidgets.QTableWidgetItem(str(data[2])))
        table.setItem(current_row, 3, QtWidgets.QTableWidgetItem(str(data[3])))

        #table.resizeColumnsToContents()
        # print(data)
    def delete_row(self):
        index_row = []
        for i in self.ui.tableWidget.selectedIndexes():
            index_row.append(i.row())
        index_row = list(set(index_row))
        for item in index_row:
            if self.ui.tableWidget.rowCount() > 0:
                self.ui.tableWidget.removeRow(item)





if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()

