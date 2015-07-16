#!/usr/bin/env python3

import sys
import math
import TankCircuit
#import FrequencyPlotter


def main():

	circuit = TankCircuit.TankCircuit(1.68, 50, 97.7, 17.8)
	circuit.printAbout()
	plot = FrequencyPlotter.FrequencyPlotter(circuit, 100, 1e6, 3e6)
	plot.plot()
main()

