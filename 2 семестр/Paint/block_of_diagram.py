import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor, QFont
 
 
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
       
    def initUI(self):
        self.setGeometry(420, 550, 420, 300)
        self.setWindowTitle('13')
        self.show()
         
    def paintEvent(self, event):
        self.qp = QPainter()
        self.qp.begin(self)

        
    def paintEvent(self, qp):
        
        pen = QPen(Qt.black, 10, Qt.SolidLine)
        
        
        qp.setPen(pen)
        
        qp.setBrush(QColor(200, 0, 0))
       
        qp.drawEllipse(10, 10, 400, 50)
        

        

        self.qp.end()
                 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
