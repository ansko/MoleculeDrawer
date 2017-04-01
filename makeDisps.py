#!/usr/bin/env python3
#coding utf-8

def make_disps(molecule):

    cm_x = 0
    cm_y = 0
    cm_z = 0

    min_x = molecule[0][1]
    max_x = molecule[0][1]
    min_y = molecule[0][2]
    max_y = molecule[0][2]
    min_z = molecule[0][3]
    max_z = molecule[0][3]

    for atom in molecule:
        if atom[1] < min_x:
            min_x = atom[1]
        if atom[1] > max_x:
            max_x = atom[1]
        if atom[2] < min_y:
            min_y = atom[2]
        if atom[2] > max_y:
            max_y = atom[2]
        if atom[3] < min_z:
            min_z = atom[3]
        if atom[3] > max_z:
            max_z = atom[3]

    for atom in molecule:
        atom[1] -= min_x
        atom[2] -= min_y
        atom[3] -= min_z

        cm_x += atom[1]
        cm_y += atom[2]
        cm_z += atom[3]
    
    return (molecule, max_x - min_x, max_y - min_y, max_z - min_z, cm_x / 382, cm_y / 382, cm_z / 382)
