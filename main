import sys
from random import randint

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QApplication, QWidget


class Example(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("Ui.ui", self)
        self.initUI()
        self.pushButton.clicked.connect(lambda x: self.repaint())

    def initUI(self):
        self.setWindowTitle('Git и желтые окружности')

    def paintEvent(self, event):
        qp = QPainter(self)
        qp.begin(self)
        self.draw(qp)
        qp.end()

    def draw(self, qp):
        qp.setBrush(Qt.yellow)
        for _ in range(3):
            w = randint(0, 100)
            qp.drawEllipse(randint(0, 500), randint(0, 500), w, w)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.setFixedSize(600, 600)
    ex.show()
    sys.exit(app.exec())
