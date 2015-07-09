
#!/usr/bin/python
#!/usr/bin/env python3

import sys
import math

w = float (input("input frequency in MHz: "))
z = float (input("input initial impedence: "))
l = float (input("input inductance in uH: "))
r = float (input("input internal resistance in Ohm: "))
w = w*1e6
l = l*1e-6



cTune = (l*w*w*z - math.sqrt(r*z*math.pow(l*w*w,2) + math.pow(r,3)*w*w*z - math.pow(r*w*z,2)))/(math.pow(l*w*w,2)*z + z*math.pow(r*w,2))

cMatch = (-1+2*cTune*l*w*w - math.pow(cTune*r*w,2) - math.pow(cTune*l*w*w,2))/(w*w*(-l + cTune*r*r + cTune*math.pow(l*w,2))) 

print("cTune: ", cTune)
print("cMatch: ", cMatch)
def c_tune(w,l,z,r):
    c = (l*w*w*z - math.sqrt(r*z*math.pow(l*w*w,2) + math.pow(r,3)*w*w*z - math.pow(r*w*z,2)))/(math.pow(l*w*w,2)*z + z*math.pow(r*w,2))
    return c

def c_match(w,l,z,r):
    c = (-1+2*c_tune(w,l,z,r)*l*w*w - math.pow(c_tune(w,l,z,r)*r*w,2) - math.pow(c_tune(w,l,z,r)*l*w*w,2))/    (w*w*(-l + c_tune(w,l,z,r)*r*r + c_tune(w,l,z,r)*math.pow(l*w,2))) 
    return c


def main():

    if len(sys.argv) == 5:
        w, z, l, r = map(float, (sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]) )
    else:    
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


