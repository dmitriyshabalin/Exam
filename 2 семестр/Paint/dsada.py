import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.setGeometry(600,600, 680, 300)
        self.setWindowTitle('13')
        self.show()


    def paintEvent(self, e):

        qp = QPainter()
        qp.begin(self)
        self.drawELL(qp)
        qp.end()


    def drawELL(self, qp):

        pen = QPen(Qt.yellow, 10, Qt.DiagCrossPattern)

        qp.setPen(pen)
        qp.setBrush(QColor(0, 0, 200))
        qp.drawRect(10, 15, 90, 60)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
