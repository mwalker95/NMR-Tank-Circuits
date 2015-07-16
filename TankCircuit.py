#!/usr/bin/env python3

import sys
import math


class TankCircuit():
	
	def __init__(self):
		self.transmissionI = 50 #Ohms
	
	def __init__(self, f, transmissionI, coilL, coilR):
		self.transmissionI = transmissionI #Ohms
		self.coilR = coilR #Ohms
		self.coilL = coilL/1e6 #micro Henrys
		self.w = (f*2*math.pi)*1e6 #MHz


	def setCoilR(self, coilR):
		self.coilR = coilR #Ohms

	def setCoilL(self, coilL):
		self.coilL = coilL/1e6 #micro Henrys
	
	def setW(self, f):
		self.w = (f*2*math.pi)*1e6 #MHz


	def tuneCap(self):
		w = self.w
		z = self.transmissionI
		l = self.coilL
		r = self.coilR

		cTune = (l*w*w*z - math.sqrt(r*z*math.pow(l*w*w,2) + math.pow(r,3)*w*w*z - math.pow(r*w*z,2)))/(math.pow(l*w*w,2)*z + z*math.pow(r*w,2))
		return cTune

	def matchCap(self):
		w = self.w
		z = self.transmissionI
		l = self.coilL
		r = self.coilR
		cTune = self.tuneCap()

		cMatch = (-1+2*cTune*l*w*w - math.pow(cTune*r*w,2) - math.pow(cTune*l*w*w,2))/(w*w*(-l + cTune*r*r + cTune*math.pow(l*w,2)))
		return cMatch


	def printAbout(self):
		print("Coil: r(Ohms) = ", self.coilR, " L(uHenrys) = ", self.coilL*1e6)
		print("Frequency(MHz): ", (self.w/(2*math.pi))*1e-6)
		print("Match Cap(pico Farad): ", self.matchCap()*1e12, " Tune Cap(pico Farad): ", self.tuneCap()*1e12)

	

		
		
		

