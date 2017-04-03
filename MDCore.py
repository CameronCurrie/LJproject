"""
Main code that runs the functions
"""

import MDUtilities as MDU
import Particlecreator as creator
import verletintegration as verlet
import sys

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
CUTOFF = initialconditions.cutoff

#names and creates the particles
particles = creator.pNamer(PNUMBER)

#set intial veloicities and positions of particles using MDUtilities
MDU.setInitialPositions(RHO, particles)
MDU.setInitialVelocities(TEMP, particles)

#Get Boxsize for use in minimum image convention and periodic image boundary
BOXSIZE = MDU.boxSize(RHO, PNUMBER)

#run integration code which produces energy graphs and xyz file.
verlet.verletintegration(DT, particles, BOXSIZE, NUMSTEP, CUTOFF, outfile)

verlet.msd(particles, DT, NUMSTEP, CUTOFF)
