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
def pbc(BOXSIZE, p1):
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
    return force(p1, p2)


#force calculating fucntion
def force(p1, p2):
    F = 48*(1/vc.mag(p.Seperation(p1, p2)**14)-(0.5/vc.mag(p.Seperation(p1, p2))**8))*p.Seperation(p1,p2)
    return F


def verletintegration(timeinterval, particles, BOXSIZE, numstep, outfile):
    for i in range(numstep):

        #Point tells the xyz file which point we are at in the integral
        nAtoms = len(particles)
        point = "Point " + str(i + 1)
        outfile.write(str(nAtoms) + "\n" + str(point) + "\n")
        for p1 in particles:
            
            #calculates force between a pair of particles that aren't the same particle
            forceX = []
            forceY = []
            forceZ = []

            for p2 in particles:

                #list for summing each compenent of force
                if p1 != p2:

                    
                    F = mic(p1, p2, BOXSIZE)


                    forceX.append(F[0])
                    forceY.append(F[1])
                    forceZ.append(F[2])


            FORCE = np.array([sum(forceX), sum(forceY), sum(forceZ)])
            #Updatethe positions given the initial force
            p1.leapPosition2nd(timeinterval, FORCE)


            #applies minimum image convention
            #applies periodic boundary conditions
            pbc(BOXSIZE, p1)
            #Updateforce for the new position
            FORCE_NEW = 0
            #Updatevelocity based of the average of the two forces
            p1.leapVelocity(timeinterval, 0.5*(FORCE + FORCE_NEW))


            #Set new force to force to be used later
            FORCE = FORCE_NEW
            i += 1
            outfile.write(str(p1) + "\n")
    outfile.close()