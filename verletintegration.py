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
        while p1.position[i] > BOXSIZE:
            p1.position[i] = p1.position[i] - BOXSIZE
            #print "The " +str(i) +" position is " +str(p1.position[i])
        while p1.position[i] < 0:
            p1.position[i] = p1.position[i] + BOXSIZE
        #print "The " +str(i) +" position is " +str(p1.position[i])
    return p1.position

#minimum image convention function
def mic(p1, p2, BOXSIZE):
    for i in range(3):
        if abs(p1.position[i]-p2.position[i]) > 0.5*BOXSIZE:
            if (p1.position[i]-p2.position[i]) > 0.5*BOXSIZE:
                p2.position[i] = p2.position[i] + BOXSIZE
            if (p1.position[i]-p2.position[i]) < 0.5*BOXSIZE:
                p2.position[i] = p2.position[i] - BOXSIZE
        else:
            p1.position[i] = p1.position[i]
            p2.position[i] = p2.position[i]
    return p.Seperation(p1, p2)

#force calculating fucntion
def force(p1, p2, BOXSIZE):
    r1 = (vc.mag(mic(p1, p2, BOXSIZE)))**14
    r2 = (vc.mag(mic(p1, p2, BOXSIZE)))**8
    force = 48*mic(p1, p2, BOXSIZE)*((1/r1)-(0.5/r2))
    return force

#class that enables the reading of initial conditions from some input file
class conditions(object):
    def __init__(self, rho, temp, timeinterval, numstep, nAtoms):
        self.density = rho
        self.temperature = temp
        self.timeinterval = timeinterval
        self.numstep = numstep
        self.numberofatoms = nAtoms
#Reads the conditions 
#from an input file formated: <density> <temperature> <timeinterval> <numberofsteps> <numberofatoms>
    @staticmethod
    def readconditions(inFile):
        line = inFile.readline()
        tokens = line.split()
        rho = float(tokens[0])
        temp = float(tokens[1])
        timeinterval = float(tokens[2])
        numstep = int(tokens[3])
        nAtoms = int(tokens[4])
        return conditions(rho, temp, timeinterval, numstep, nAtoms)

def verletintegration(timeinterval, particles, BOXSIZE, numstep, outfile):
    #calculates force between a pair of particles that aren't the same particle
    forceX = []
    forceY = []
    forceZ = []

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


                    F = force(p1, p2, BOXSIZE)

                    
                    forceX.append(F[0])
                    forceY.append(F[1])
                    forceZ.append(F[2])


            FORCE = np.array([sum(forceX), sum(forceY), sum(forceZ)])
            #print "force is " + str(FORCE)
            p1.leapPosition2nd(timeinterval, FORCE, BOXSIZE)
            #pbc(BOXSIZE, p1)
            forceX_NEW = []
            forceY_NEW = []
            forceZ_NEW = []
            #print "sep is " + str(p.Seperation(p1, p2))

            for p2 in particles:

                #list for summing each compenent of force
                if p1 != p2:


                    F = force(p1, p2, BOXSIZE)


                    forceX_NEW.append(F[0])
                    forceY_NEW.append(F[1])
                    forceZ_NEW.append(F[2])


            FORCE_NEW = np.array([sum(forceX_NEW), sum(forceY_NEW), sum(forceZ_NEW)])

            #Updatevelocity based of the average of the two forces
            p1.leapVelocity(timeinterval, 0.5*(FORCE+FORCE_NEW))

            #Set new force to force to be used later
            FORCE = FORCE_NEW
            i += 1
            outfile.write(str(p1) + "\n")
    outfile.close()
