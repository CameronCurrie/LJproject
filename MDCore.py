import MDUtilities as MDU


import Particlecreator as creator
import verletintegration as verlet
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
"""


PNUMBER = 27
rho = 1
temp = 10
dt = 0.1
numstep = 10

particles = creator.pNamer(PNUMBER)

#set intial veloicities and positions of particles using MDUtilities
MDU.setInitialPositions(rho,particles)
MDU.setInitialVelocities(temp,particles)

#Get Boxsize for use in minimum image convention and periodic image boundary
BOXSIZE = MDU.boxSize(rho,PNUMBER)

verlet.verletintegration(dt, particles, BOXSIZE, numstep)


