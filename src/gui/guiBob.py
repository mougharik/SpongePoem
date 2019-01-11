from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import *
import sys

class Spongebob(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup()

    def setup(self):
        self.setWindowTitle('Spongebob Poetry')
        self.setGeometry(50, 50, 800, 600)
        
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('game.jpg'))
        self.label.setGeometry(0,0,800,600)

        self.draw_sponge = DrawSponge(self)
        self.setCentralWidget(self.draw_sponge)

        self.direction = 180
        self.a1 = 65
        self.b1 = 0
        self.c1 = 130
        
        self.a2 = -50
        self.b2 = 20
        self.c2 = 90
        
        self.eng = QtWidgets.QPushButton("English",self)
        self.eng.move(100,50)
        self.eng.clicked.connect(self.toeng)
        
        self.span = QtWidgets.QPushButton("Spanish",self)
        self.span.move(200,50)
        self.span.clicked.connect(self.tospan)
        
        self.fr = QtWidgets.QPushButton("French",self)
        self.fr.move(300,50)
        self.fr.clicked.connect(self.tofre)
        
        self.germ = QtWidgets.QPushButton("German",self)
        self.germ.move(400,50)
        self.germ.clicked.connect(self.togerm)

        self.show()

    def toeng(self):
        #x = poem.split()
        #dictionary = PyDictionary('red')
        print("en")

    def tospan(self):
        #x = poem.split()
        #dictionary = PyDictionary('red')
        print("es")

    def tofre(self):
        #x = poem.split()
        #dictionary = PyDictionary('red')
        print("fr")

    def togerm(self):
        #x = poem.split()
        #dictionary = PyDictionary('red')
        print("de")

class DrawSponge(QtWidgets.QWidget):
                              
    def __init__(self, parent):
        QtWidgets.QWidget.__init__(self,parent)
        

    def paintEvent(self, event):
        
        qp = QtGui.QPainter()
        qp.begin(self)

        pen = qp.pen()
        qp.setPen(pen)

        brush = QtGui.QBrush(QtCore.Qt.SolidPattern)
        brush.setColor(QtCore.Qt.white)
        qp.setBrush(brush)

        pen.setColor(QtCore.Qt.transparent)
        qp.setPen(pen)
        brush.setColor(QtCore.Qt.yellow)
        qp.setBrush(brush)
        qp.drawRect(350, 150, 300,250)

        pen.setColor(QtCore.Qt.transparent)
        qp.setPen(pen)
        brush.setColor(QtGui.QColor(255,185,60,200))
        qp.setBrush(brush)
        qp.drawRect(350, 400, 300,100)

        pen.setColor(QtCore.Qt.transparent)
        qp.setPen(pen)
        brush.setColor(QtGui.QColor('White'))
        qp.setBrush(brush)
        qp.drawRect(350, 400, 300,30)


        pen.setColor(QtCore.Qt.black)
        qp.setPen(pen)       
        qp.drawEllipse(QtCore.QPointF(550, 250), 40, 40)

        brush.setColor(QtGui.QColor('Cyan'))
        qp.setBrush(brush)
        qp.drawEllipse(QtCore.QPointF(540, 250), 20, 20)

        brush.setColor(QtGui.QColor('Black'))
        qp.setBrush(brush)
        qp.drawEllipse(QtCore.QPointF(540, 250), 10, 10)

        brush.setColor(QtCore.Qt.white)
        qp.setBrush(brush)
        qp.drawEllipse(QtCore.QPointF(450, 250), 40, 40)

        brush.setColor(QtGui.QColor('Cyan'))
        qp.setBrush(brush)
        qp.drawEllipse(QtCore.QPointF(460, 250), 20, 20)

        brush.setColor(QtGui.QColor('Black'))
        qp.setBrush(brush)
        qp.drawEllipse(QtCore.QPointF(460, 250), 10, 10)

        brush.setColor(QtGui.QColor('Darkred'))
        qp.setBrush(brush)
        qp.drawPie((self.width() / 2) - self.parentWidget().a2, (self.height() / 2) - self.parentWidget().b2,
                    self.parentWidget().c2, self.parentWidget().c2,
                    self.parentWidget().direction * 16, 180 * 16)
        
        brush.setColor(QtGui.QColor('White'))
        qp.setBrush(brush)
        qp.drawRect(505, 325, 15,20)

        brush.setColor(QtGui.QColor('White'))
        qp.setBrush(brush)
        qp.drawRect(475, 325, 15,20)

        qp.end()
    
class InputWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = 'Input (up to 40 chars)'
        self.top = 180
        self.left = 180
        self.width = 450
        self.height = 130
        self.setup()

    def setup(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.textbox = QLineEdit(self)
        self.textbox.resize(350,40)
        self.textbox.move(20, 2)
        self.button = QPushButton('Enter', self)
        self.button.move(20,80)
        self.button.clicked.connect(self.clicked)
        self.show()

    @pyqtSlot()
    def clicked(self):
        textboxValue = self.textbox.text()
        # here we want to 'send' the input
        self.textbox.setText("")
        
class OutputWindow(QLabel):
    def __init__(self):
        QLabel.__init__(self, 'this is the output')

        self.title = 'Output'
        self.sizea = 600
        self.sizeb = 400
        self.setup()

    def setup(self):
        self.setWindowTitle(self.title)
        self.setMinimumSize(QSize(self.sizea, self.sizeb))
        self.setAlignment(Qt.AlignLeft)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = Spongebob()
    inu = InputWindow()
    ou = OutputWindow()
app.exec()
