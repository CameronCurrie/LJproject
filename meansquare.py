import MDUtilities as MDU
import Particlecreator as creator
import verletintegration as verlet
import sys
from Particle3D import Particle3D as p
import VectorMethods as vc
import numpy as np
import matplotlib.pyplot as pyplot

#Must run code with two arguments, the file you wish to write to and the file you are reading from
if len(sys.argv)!=3:
	print ("\nWrong number of arguments.")
	print ("Usage: " + sys.argv[0] + " <output file>" + "<input file>")
	quit()
else:
    outfileName = sys.argv[1]
    inputfileName = sys.argv[2]

#Open output file for writing data to
outfile = open(outfileName, "w")
inputfile = open(inputfileName, "r")


#reads initial condition from the file containing them
initialconditions = verlet.conditions.readconditions(inputfile)

#Gets initial conditions using conditons class
PNUMBER = initialconditions.numberofatoms
RHO = initialconditions.density
TEMP = initialconditions.temperature
DT = initialconditions.timeinterval
NUMSTEP = initialconditions.numstep

#names and creates the particles
particles = creator.pNamer(PNUMBER)

#set intial veloicities and positions of particles using MDUtilities
MDU.setInitialPositions(RHO, particles)
MDU.setInitialVelocities(TEMP, particles)

#Get Boxsize for use in minimum image convention and periodic image boundary
BOXSIZE = 100000000000000000000

#mean squared distance function
def msd(particles, DT, NUMSTEP, BOXSIZE):
    time = []
    msd = []
    for i in range(NUMSTEP):
        msdtime = []
        currenttime = i*DT
        time.append(currenttime)
        for p1 in particles:
            if i == 0:
                initialposition = p1.position
            
            #calculates force
            FORCE = verlet.sumforce(p1, particles, BOXSIZE)
            p1.leapPosition2nd(DT, FORCE, BOXSIZE)
            #update force
            FORCE_NEW = verlet.sumforce(p1, particles, BOXSIZE)
            #Updatevelocity based of the average of the two forces
            p1.leapVelocity(DT, 0.5*(FORCE+FORCE_NEW))
            #Set new force to force to be used later
            FORCE = FORCE_NEW

            distancesquared = (vc.mag(p1.position-initialposition))**2
            #print distancesquared
            currentmsd = distancesquared
            #print currentmsd
            msdtime.append(currentmsd)
        msd.append(sum(msdtime)/PNUMBER)


    pyplot.plot(time, msd)
    pyplot.title("Mean Squared Distance over time")
    pyplot.show()

msd(particles, DT, NUMSTEP, BOXSIZE)




def rdf(timeinterval, particles, BOXSIZE, numstep):
    nAtoms = len(particles)
    numberdensity = nAtoms/(BOXSIZE**3)

