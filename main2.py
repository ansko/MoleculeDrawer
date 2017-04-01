#!/usr/bin/env python3
#coding utf-8

import sys 
import math

from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QBrush, QLinearGradient, QColor, QRadialGradient
from PyQt5.QtCore import Qt

import lat
import lat.read_atoms

from atomWidget import AtomsDrawer
from makeMolecule import make_chain
from makeDisps import make_disps
from computeRgyr import computeRgyr
from options import options

def main():
    o = options('poly65856')
    fname = o.fname
    size_vs_z = [[0, 0, 0, 0] for i  in range(15)]

    ave_rx = 0
    ave_ry = 0
    ave_rz = 0

    ove_errx = ove_erry = ove_errz = 0
    [atoms, bounds, bonds, angles] = lat.read_atoms.read_atoms(fname)

    app = QApplication(sys.argv)

    if 1:
        for mol_num in range(o.polymer_chains):
            molecule = make_chain(atoms, bounds, mol_num, o)
            (molecule, max_x, max_y, max_z, cm_x, cm_y, cm_z) = make_disps(molecule)
            [rx, ry, rz, errx, erry, errz] = computeRgyr(molecule)
            ave_rx += rx
            ave_ry += ry
            ave_rz += rz
            ove_errx += errx
            ove_erry += erry
            ove_errz += errz

            ad12 = AtomsDrawer(molecule, max_x, max_y, 1, 2, o)
            ad12.screenshot('pics/' + str(mol_num) + '.12.png')

            ad13 = AtomsDrawer(molecule, max_x, max_y, 1, 3, o)
            ad13.screenshot('pics/' + str(mol_num) + '.13.png')

            ad23 = AtomsDrawer(molecule, max_x, max_y, 2, 3, o)
            ad23.screenshot('pics/' + str(mol_num) + '.23.png')

            del ad12
            del ad23
            del ad13

    print(math.sqrt(ave_rx / o.polymer_chains), ' +- ', math.sqrt(ove_errx / o.polymer_chains), '\n',
          math.sqrt(ave_ry / o.polymer_chains), ' +- ', math.sqrt(ove_erry / o.polymer_chains), '\n',
          math.sqrt(ave_rz / o.polymer_chains), ' +- ', math.sqrt(ove_errz / o.polymer_chains))

    sys.exit(app.exec_())

main()
