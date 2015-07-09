#!/usr/bin/python

import sys
import math
import TankCircuit
import FrequencyPlotter

#tankCircuit = TankCircuit.TankCircuit()

def main():
	circuit = TankCircuit.TankCircuit(50,7,26e-6,20e6)
	circuit.printAbout()
	plot = FrequencyPlotter.FrequencyPlotter(circuit, 6, 1e6, 3e6)
	plot.plot()
main()

