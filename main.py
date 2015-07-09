#!/usr/bin/python

import sys
import math
import TankCircuit

#tankCircuit = TankCircuit.TankCircuit()

def main():
	circuit = TankCircuit.TankCircuit(50,7,26e-6,20e6)
	circuit.printAbout()
main()

