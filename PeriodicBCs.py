"""Periodic boundary conditions, 1D atm"""
#from Particle3D import Particle3D as particle
import numpy as np
#import MDUtilities as MDU

#MDU.boxSize = boxSize while developing code

#testing purposes we set boxsize

BOXSIZE = 5

#set test positions for our particle in each axis x,y,z
position = [0,0,0]
position[0] = -5.01
position[1] = -4
position[2] = -5.001


#for loop changing positions 
#there is a potential bug if the position update returns 
#a position that's >4*BOXSIZE
def pbc(self,BOXSIZE):
    for i in range(3):
        if position[i] > BOXSIZE:
            position[i] = -2*BOXSIZE+position[i]
            print "The " +str(i) +" position is " +str(position[i])
        elif position[i] < -BOXSIZE:
            position[i] = 2*BOXSIZE+position[i]
            print "The " +str(i) +" position is " +str(position[i])
        else:
            print "The " +str(i) +" position is " +str(position[i])

#to fix potential bug we could add another if
#-> 2*BS+position added 