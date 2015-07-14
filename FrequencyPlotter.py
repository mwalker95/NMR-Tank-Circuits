#!/usr/bin/env python3
import sys
import math
import matplotlib.pyplot as plt
from TankCircuit import TankCircuit



#this class takes a TankCircuit object, the number of points you want plotted, and start and end frequencies
#then it plots both the matchCap vs frequency and tuneCap vs frequency
#the plot function will automatically set your circuits w to the start frequency given.

class FrequencyPlotter():
        def __init__(self, circuit,  n, startF, endF):
                self.n = n
                self.startF = startF
                self.endF = endF
		self.circuit = circuit

        def plot(self):

                step = (self.endF-self.startF)/self.n
                frequencies = []
                matchCaps = []
                tuneCaps = []
		
		self.circuit.setW(self.startF)
                w = self.startF
		
                #fills 3 lists with values between the starting and ending frequencies with step of step
                for i in range((self.n) + 1):
                        frequencies.append(w)
                        matchCaps.append(self.circuit.matchCap())
                        tuneCaps.append(self.circuit.tuneCap())
                        w +=step
                        self.circuit.setW(w)

                plt.plot(frequencies, matchCaps)
                plt.plot(frequencies, tuneCaps)
		plt.xlabel('Frequency')
		plt.ylabel('Capacitance')
		plt.show()
