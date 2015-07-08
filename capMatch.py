#!/usr/bin/python

import sys
import math


def main():
    w = float (input("input frequency in MHz: "))
    z = float (input("input transmission line impedence: "))
    l = float (input("input inductance in uH: "))
    r = float (input("input coil resistance in Ohm: "))
    w = w*1e6
    l = l*1e-6
    cTune = (l*w*w*z - math.sqrt(r*z*math.pow(l*w*w,2) + math.pow(r,3)*w*w*z - math.pow(r*w*z,2)))/(math.pow(l*w*w,2)*z + z*math.pow(r*w,2))
    cMatch = (-1+2*cTune*l*w*w - math.pow(cTune*r*w,2) - math.pow(cTune*l*w*w,2))/(w*w*(-l + cTune*r*r + cTune*math.pow(l*w,2))) 

    print("cTune: ", cTune)
    print("cMatch: ", cMatch)

if __name__ == "__main__":
    main()



