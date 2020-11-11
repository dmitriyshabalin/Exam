from PyQt5 import Qt
import pandas as pd #Библиотека для работы с Excel
import os 

tb = pd.read_excel('Ex.xlsx')  # Считывание данных из файла Ex.xlsx

print(tb)

if __name__ == '__main__':
    app = Qt.QApplication([])

    printer = Qt.QPrinter()

    text = Qt.QPlainTextEdit()
    text.appendPlainText(str(tb)) #Запись содержимого файла Excel в QPlainTextEdit
    text.show()

    print_dialog = Qt.QPrintDialog(printer) # Диалоговое окно принтера
    if print_dialog.exec() == Qt.QDialog.Accepted:
        text.print(printer)

    app.exec()
