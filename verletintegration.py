"""
Verlet integration code, contains: minimum image conventions, periodic boundary conditions,
force and sum of force calculator, potential and sum of potentials calculator, the verlet integration 
method which creates lists of energies, time and a xyz trajectory file.abs
Also contains the initial conditions class which allows for the reading of conditions from an input file
to set the initial positions and velocities using MDUtilities.
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
    #and move it
    for i in range(3):
        if p1.position[i] > BOXSIZE:
            #boxsize away is the number of boxsizes the particle is away from where it should be
            boxsizeaway = divmod(p1.position[i], BOXSIZE) #this returns two values but only first is needed
            boxsizeaway = boxsizeaway[0]
            p1.position[i] = p1.position[i] - boxsizeaway*BOXSIZE
        if p1.position[i] < 0:
            boxsizeaway = divmod(p1.position[i], BOXSIZE)
            boxsizeaway = boxsizeaway[0]
            p1.position[i] = p1.position[i] - boxsizeaway*BOXSIZE
    return p1.position

#minimum image convention function
def mic(p1, p2, BOXSIZE):
    #checks if the distance between two particles is greater than half the boxsize for each dimension
    #and applies the minimum image convention if they arent
    for i in range(3):
        if abs(p1.position[i]-p2.position[i]) > 0.5*BOXSIZE:
            if (p1.position[i]-p2.position[i]) > 0.5*BOXSIZE:
                p2.position[i] = p2.position[i] + BOXSIZE
            elif (p1.position[i]-p2.position[i]) < 0.5*BOXSIZE:
                p2.position[i] = p2.position[i] - BOXSIZE
    return p.Seperation(p1, p2)



#force calculating fucntion
def force(p1, p2, BOXSIZE):
    r1 = float((vc.mag(mic(p1, p2, BOXSIZE)))**14)
    r2 = float((vc.mag(mic(p1, p2, BOXSIZE)))**8)
    force = 48*mic(p1, p2, BOXSIZE)*((1/r1)-(0.5/r2))
    return force

#calculates potential between two particles
def potentialenergy(p1, p2, BOXSIZE):
    r1 = float(vc.mag(mic(p1, p2, BOXSIZE))**12)
    r2 = float(vc.mag(mic(p1, p2, BOXSIZE))**6)
    potential = 4*((1/r1) - (1/r2))
    return potential


def sumforce(p1, particles, BOXSIZE):
    forceX = []
    forceY = []
    forceZ = []
    for p2 in particles:
        #takes out particles interacting with themselves.
        if p1 != p2:
            #Calculates force if particle are closer than the LJ cutoff
            if vc.mag(mic(p1, p2, BOXSIZE)) < 3.5:
                F = force(p1, p2, BOXSIZE)

            #LJ cutoff if particle is more than 3.5 units away
            else:
                F = [0, 0, 0]

            #add force contribution from each particle to list of force
            forceX.append(F[0])
            forceY.append(F[1])
            forceZ.append(F[2])

        #sums force from each dimension and creates a force array
    FORCE = np.array([sum(forceX), sum(forceY), sum(forceZ)])
    return FORCE

def sumpotential(p1, particles, BOXSIZE):
        ParticlePotEn = []
        for p2 in particles:
            #takes out particles interacting with themselves.
            if p1 != p2:

                #Calculates force if particle are closer than the LJ cutoff
                if vc.mag(mic(p1, p2, BOXSIZE)) < 3.5:
                    Potential = potentialenergy(p1, p2, BOXSIZE)

                    #LJ cutoff if particle is more than 3.5 units away
                else:
                    Potential = 0

                ParticlePotEn.append(Potential)
        return sum(ParticlePotEn)    
                

def verletintegration(timeinterval, particles, BOXSIZE, numstep, outfile):
    #calculates force between a pair of particles that aren't the same particle

    #Creates list of the time of the simulation
    time = []
    #list for total energies of system
    KinEn = []
    PotEn = []
    TotEn = []
    nAtoms = len(particles)


    for i in range(numstep):
        
        #Creates list of the time of the simulation
        currenttime = i*timeinterval
        time.append(currenttime)
        IntervalKinEnergy = []
        #Point tells the xyz file which point we are at in the integral
        point = "Point " + str(i + 1)
        #writing to xyz file in correct format
        outfile.write(str(nAtoms) + "\n" + str(point) + "\n")

        #updates particles based on interaction with other particles
        for p1 in particles:

            #calculates force
            FORCE = sumforce(p1, particles, BOXSIZE)

            p1.leapPosition2nd(timeinterval, FORCE, BOXSIZE)

            #pbc(BOXSIZE, p1)
            #update force
            FORCE_NEW = sumforce(p1, particles, BOXSIZE)

            #Updatevelocity based of the average of the two forces
            p1.leapVelocity(timeinterval, 0.5*(FORCE+FORCE_NEW))
            pbc(BOXSIZE, p1)

            #work out energies for particle
            ParticlePotEn = sumpotential(p1, particles, BOXSIZE)

            #Set new force to force to be used later
            FORCE = FORCE_NEW
            i += 1
            outfile.write(str(p1) + "\n")
            IntervalKinEnergy.append(p.kineticenergy(p1))



        #
        KinEn.append(sum(IntervalKinEnergy))
        PotEn.append(ParticlePotEn)
        TotalEnergy = sum(IntervalKinEnergy) + ParticlePotEn
        TotEn.append(TotalEnergy)


    #plot graphs using the lists of the energies and time.
    pyplot.plot(time, KinEn)
    pyplot.title("Kinetic Energy")
    pyplot.show()
    pyplot.plot(time, PotEn)
    pyplot.title("Potential Energy")
    pyplot.show()
    pyplot.plot(time, TotEn)
    pyplot.show()
    outfile.close()


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
