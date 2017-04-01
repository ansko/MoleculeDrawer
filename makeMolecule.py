#!/usr/bin/env python3
#coding utf-8

from options import options

def make_chain(atoms, bounds, MoleculeNumber=0, o=None):
    molecule = []

    lx = bounds[1] - bounds[0]
    ly = bounds[3] - bounds[2]
    lz = bounds[5] - bounds[4]

    startatom_number = ((MoleculeNumber // o.chains_per_cell) * o.systemsize + 
                        o.delta + 
                        (MoleculeNumber % o.chains_per_cell) * o.polymer_len)
    start_x = atoms[startatom_number][4]
    start_y = atoms[startatom_number][5]
    start_z = atoms[startatom_number][6]
    molecule.append([startatom_number, start_x, start_y, start_z])

    for i in range(o.polymer_len - 2):
        nearest_number = startatom_number + 1
        nearest_x = atoms[nearest_number][4]
        nearest_y = atoms[nearest_number][5]
        nearest_z = atoms[nearest_number][6]
        r2old = 1000000
        coords = [0, 0, 0]
        for x in [-1, 0, 1]:
            nx = nearest_x + x * lx
            dx = abs(nx - start_x)
            for y in [-1, 0, 1]:
                ny = nearest_y + y * ly
                dy = abs(ny - start_y)
                for z in [-1, 0, 1]:
                    nz = nearest_z + z * lz
                    dz = abs(nz - start_z)
                    r2new = dx**2 + dy**2 + dz**2
                    if r2new < r2old:
                        r2old = r2new 
                        coords = [x, y, z]
        molecule.append([nearest_number,
                         nearest_x + coords[0] * lx,
                         nearest_y + coords[1] * ly,
                         nearest_z + coords[2] * lz])
        startatom_number = nearest_number
        start_x = nearest_x + coords[0] * lx                    
        start_y = nearest_y + coords[1] * ly        
        start_z = nearest_z + coords[2] * lz

    return molecule
