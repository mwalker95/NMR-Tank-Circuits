#!/usr/bin/python

import sys
import math

w = input("input frequency in MHz: ")
z = input("input initial impedence: ")
l = input("input inductance in uH: ")
r = input("input internal resistance in Ohm: ")
w = math.pow(10,6)*w
l = l*math.pow(10,-6)



c1 = (l*w*w*z - math.sqrt(r*z*math.pow(l*w*w,2) + math.pow(r,3)*w*w*z - math.pow(r*w*z,2)))/(math.pow(l*w*w,2)*z + z*math.pow(r*w,2))

c2top = 2*l*w*w*(l*w*w*z -math.sqrt(r*z*math.pow(l*w*w,2) + r*z*math.pow(r*w,2) - math.pow(r*w*z,2)))/(z*math.pow(l*w*w,2) + z*math.pow(r*w,2)) -(math.pow(r*w,2)*(l*z*w*w - math.sqrt(r*z*math.pow(l*w*w,2) + r*z*math.pow(r*w,2) - math.pow(r*w*z,2))



print c1
