#!/usr/bin/env python3
#coding utf-8

import math

import pprint
pprint = pprint.PrettyPrinter(indent=1).pprint

def computeRgyr(molecule):
    n = len(molecule)
    x = y = z = 0
    rx = ry = rz = 0
    errx = erry = errz = 0

    for i in range(n):
        x += molecule[i][1]
        y += molecule[i][2]
        z += molecule[i][3]
    x /= n
    y /= n
    z /= n

    for atom in molecule:
        rx += (atom[1] - x)**2
        ry += (atom[2] - y)**2
        rz += (atom[3] - z)**2

    rx /= n
    ry /= n
    rz /= n

    for atom in molecule:
        errx += (abs(atom[1] - x) - math.sqrt(rx))**2
        erry += (abs(atom[2] - y) - math.sqrt(ry))**2
        errz += (abs(atom[3] - z) - math.sqrt(rz))**2

    return [rx, ry, rz, errx / n, erry / n, errz / n]
