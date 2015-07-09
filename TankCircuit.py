#!/usr/bin/python

import sys
import math
import matplotlib.pyplot as plts


class TankCircuit():
	
	def __init__(self):
		self.internalI = 50 #Ohms
	
	def __init__( self, internalI, coilR, coilL, w):
		self.internalI = internalI #Ohms
		self.coilR = coilR #Ohms
		self.coilL = coilL #Henrys
		self.w = w #Hz


	def setCoilR(self, coilR):
		self.coilR = coilR #Ohms

	def setCoilL(self, coilL):
		self.coilL = coilL #Henrys
	
	def setW(self, w):
		self.w = w #Hz

	def tuneCap(self):
		w = self.w
		z = self.internalI
		l = self.coilL
		r = self.coilR

		cTune = (l*w*w*z - math.sqrt(r*z*math.pow(l*w*w,2) + math.pow(r,3)*w*w*z - math.pow(r*w*z,2)))/(math.pow(l*w*w,2)*z + z*math.pow(r*w,2))
		return cTune

	def matchCap(self):
		w = self.w
		z = self.internalI
		l = self.coilL
		r = self.coilR
		cTune = self.tuneCap()

		cMatch = (-1+2*cTune*l*w*w - math.pow(cTune*r*w,2) - math.pow(cTune*l*w*w,2))/(w*w*(-l + cTune*r*r + cTune*math.pow(l*w,2)))
		return cMatch


	def printAbout(self):
		print("Coil: r = ", self.coilR, " L = ", self.coilL)
		print("Frequency: ", self.w)
		print("Match Cap: ", self.matchCap(), " Tune Cap: ", self.tuneCap())

	

		
		
		

