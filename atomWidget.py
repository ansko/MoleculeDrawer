#!/usr/bin/env python3
#coding utf-8

from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QBrush, QLinearGradient, QColor, QRadialGradient
from PyQt5.QtCore import Qt

from options import options

class AtomsDrawer(QWidget):
    def __init__(self, atoms, sizex=0, sizey=0, coord1=1, coord2=2, o=None):

        self.o = o
        self.atoms = atoms
        super().__init__()
        self.resize(self.o.multip * sizex + self.o.radius, 
                    self.o.multip * sizey + self.o.radius)
        self.coord1 = coord1
        self.coord2 = coord2
        self.show()

    def paintEvent(self, e):

        qp = QPainter()
        qp.begin(self)
        self.drawBrushes(qp, self.coord1, self.coord2)
        qp.end()

    def drawBrushes(self, qp, coord1, coord2):

        for atom in self.atoms:
            gradient = QRadialGradient(self.o.multip * atom[coord1], 
                                       self.o.multip * atom[coord2], 10)
            
            gradient.setColorAt(0.0, QColor(0, 0, 0))
            gradient.setColorAt(1.0, QColor(255, 0, 0))

            brush = QBrush(gradient)
            qp.setBrush(brush)
            qp.drawEllipse(self.o.multip * atom[coord1],
                           self.o.multip * atom[coord2],
                           self.o.radius, self.o.radius)

    def screenshot(self, fname='./1.png', format='png'):

        p = self.grab();
        p.save(fname, format, -1)
        self.hide()
