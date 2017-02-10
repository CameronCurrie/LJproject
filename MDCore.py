import MDUtilities as MDU
import numpy as np
import math
import VectorMethods as VM
#import VerletVelocity as Ver
from Particle3D import Particle3D as p
import Particlecreator as creator

"""
if len(sys.argv)!=3:
	print "Wrong number of arguments."
	print "Usage: " + sys.argv[0] + " <output file>"
	quit()
else:
	outfileName = sys.argv[1]
    conditions = sys.argv[2]
#Open output file for writing data to
outfile = open(outfileName,"w")

file_handle = open(conditions,"r")

#set up the intial positions of all particles
InitialPositions = MDU.setInitialPositions(rho, particles)
InitialVelocities = MDU.setInitialVelocities(temp)
"""
PNUMBER = 20
rho = 1
temp = 10


MDU.setInitialPositions(rho,creator.pNamer(PNUMBER))
MDU.setInitialVelocities(temp,creator.pNamer(PNUMBER)) #We need to give particle positions


