#!/usr/bin/env python3

import sys
import math
import TankCircuit
#import FrequencyPlotter

circuit = TankCircuit.TankCircuit(50,7,26,20)

def main():

	circuit.printAbout()
#	plot = FrequencyPlotter.FrequencyPlotter(circuit, 6, 1e6, 3e6)
#	plot.plot()
main()

