

Example:

    #!/usr/bin/env python

    from capMatch import *

    f = 1670000
    zo = 50
    r = 15

    for i in range(32,130,1):
        print("    coil inductance:  "+str(i*10e-6)+"     ")
        print("tune cap:  "+str(c_tune(f,i*10e-6, zo, r)))
        print("match cap:  "+str(c_match(f, i*10e-6, zo, r)))
        print(" ")

you can run main with or without command line args for frequency, impedance, inducance, and coil losses

    scientist@computer ~$: ./capMatch 1.7 50 74 11
    cTune:  2.4936037164132177e-09
    cMatch:  2.223563013209137e-09    
