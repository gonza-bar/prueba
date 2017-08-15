#!/usr/bin/python2
# -*- coding: utf-8 -*-

import sys

def generarCUIT(dni):
    xy = '30'
    dniStr = xy+str(dni)
    numbers = [5,4,3,2,7,6,5,4,3,2] 
    ac = 0
    for idx, val in enumerate(dniStr):
        ac += int(dniStr[idx]) * numbers[idx]
    div = ac / 11
    rest = ac - (div*11)
    if rest ==0:
        z=0
    elif rest == 1:
        z=9
    else: 
        z = 11 - rest
    return "%s-%s-%i" % (xy,dni,z) #retorna cuit
    

if __name__ == "__main__":
     print generarCUIT(int(sys.argv[1]))
