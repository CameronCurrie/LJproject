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



#periodic boundary conditions 
def pbc(BOXSIZE, p1, p2):
    #checks for each dimension if the particle is outside the box
    for i in range(3):
        if p1.position[i] > BOXSIZE:
            p1.position[i] = -2*BOXSIZE+p1.position[i]
            #print "The " +str(i) +" position is " +str(p1.position[i])
        elif p1.position[i] < -BOXSIZE:
            p1.position[i] = 2*BOXSIZE+p1.position[i]
            #print "The " +str(i) +" position is " +str(p1.position[i])
        #else:
            #print "The " +str(i) +" position is " +str(p1.position[i])



#minimum image convention function
def mic(p1, p2, BOXSIZE):
    if vc.mag(p.Seperation(p1, p2)) > math.sqrt(3*(BOXSIZE/2)**2):
        p1.position[0] + BOXSIZE
        if vc.mag(p.Seperation(p1, p2)) > math.sqrt(3*(BOXSIZE/2)**2):
            p1.position[1] + BOXSIZE
            if vc.mag(p.Seperation(p1, p2)) > math.sqrt(3*(BOXSIZE/2)**2):
                p1.position[2] + BOXSIZE
    return vc.mag(p.Seperation(p1, p2))


#force calculating fucntion
def force(p1, p2):
    F = 48*(1/vc.mag(p.Seperation(p1, p2)**14)-(0.5/vc.mag(p.Seperation(p1, p2))**8))*p.Seperation(p1,p2)
    return F


def verletintegration(timeinterval, particles, BOXSIZE, numstep, outfile):
    for p1 in particles:
        for p2 in particles:
            print p1
            print p2

            if p1 != p2:

                force(p1, p2)
                for i in range(numstep):
                    mic(p1, p2, BOXSIZE)
                    pbc(BOXSIZE, p1, p2)
                    #Updatethe position given the initial force
                    p1.leapPosition2nd(timeinterval, force)
                    p2.leapPosition2nd(timeinterval, force)
                    #Updateforce for the new position
                    force_new = force(p1, p2)

                    #Updatevelocity based of the average of the two forces
                    p1.leapVelocity(timeinterval,0.5*(force+force_new))
                    p2.leapVelocity(timeinterval,0.5*(force+force_new))
                    #Update the different types of energy
                    potential = 4*((1/vc.mag(p.Seperation(p1, p2))**12)-(1/vc.mag(p.Seperation(p1, p2))**6))
                    p1.kineticenergy()


                    #this might need changing
                    #Reset force
                    force = force_new
                    i += 1
                    outfile.write(str(particles))
                outfile.close()
