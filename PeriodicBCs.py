"""Periodic boundary conditions, 1D atm"""
#from Particle3D import Particle3D as particle
import numpy as np
#import MDUtilities as MDU

#MDU.boxSize = boxSize while developing code

#testing purposes we set boxsize

BOXSIZE = 5

#set test positions for our particle in each axis x,y,z
position = [0,0,0]
position[0] = -5.1
position[1] = 5.1
position[2] = 0


#for loop changing positions
for i in range(3):
    if position[i] > BOXSIZE:
        position[i] = -BOXSIZE
        print "The " +str(i) +" position is " +str(position[i])
    elif position[i] < -BOXSIZE:
        position[i] = BOXSIZE
        print "The " +str(i) +" position is " +str(position[i])
    else:
        print "The " +str(i) +" position is " +str(position[i])


"""

if position[1] > BOXSIZE:
    position[1] = -BOXSIZE
    print "The negative boxsize is" +str(-BOXSIZE)
    print "The y position is" +str(position[1])
"""