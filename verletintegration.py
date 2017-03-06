"""
Code to generate trajectory files for particles
I absolutely fucked up and deleted everything but this, thank god for github

"""




import sys
import matplotlib.pyplot as pyplot
from Particle3D import Particle3D as p
import math 
import VectorMethods as vc
import numpy as np

#need to import initial particles here

"""
seperation of two particles, i and j, 
in the n direction (either x,y,z)
"""
n = 1
dt = 0.01
BOXSIZE = 5

def pbc(self, BOXSIZE, p1, p2):
    for i in range(3):
        if p1.position[i] > BOXSIZE:
            p1.position[i] = -2*BOXSIZE+p1.position[i]
            print "The " +str(i) +" position is " +str(p1.position[i])
        elif p1.position[i] < -BOXSIZE:
            p1.position[i] = 2*BOXSIZE+p1.position[i]
            print "The " +str(i) +" position is " +str(p1.position[i])
        else:
            print "The " +str(i) +" position is " +str(p1.position[i])


def verletintegration(timeinterval, particles, particlenumber):
    for p1 in particles:
        for p2 in particles:
            if p != p2:
                seperation = vc.diff(p1, p2)
                distance = vc.mag(seperation)

                Force = Force = 48*((1/vc.mag(p.Seperation(p2.position, p1.position))**14)-(0.5/vc.mag(p.Seperation(p2.position, p1.position))**8))*p.Seperation(p1,particle2)
                for i in range(numstep):
                    #Updatethe position given the initial force
                    p1.leapPosition2nd(dt, Force)
                
                    #Updateforce for the new position
                    Force_new = 48*((1/vc.mag(p.Seperation(p2.position, p1.position))**14)-(0.5/vc.mag(p.Seperation(p2.position, p1.position))**8))*p.Seperation(particle1,particle2)
                
                    #Updatevelocity based of the average of the two forces
                    p1.leapVelocity(dt,0.5*(Force+Force_new))
                
                    #Updatethe different types of energy
                    potentil = 4*((1/vc.mag(p.Seperation(p2.position, p1.position))**12)-(1/vc.mag(p.Seperation(p2.position, p1.position))**6))
                    p1.kineticenergy()
                
                    #Reset orce
                    Force = Force_new

"""
    if xsep > boxSize/2:
        set xsep to boxSize + xpos 
        calculate force
        set distance back to what they were
"""
