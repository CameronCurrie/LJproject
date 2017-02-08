"""
Exercise 3
Verlet velocity integration method for a 2D orbit
"""


import sys
import matplotlib.pyplot as pyplot
from Particle3D import Particle3D as p
import math 
import VectorMethods as vc


if len(sys.argv)!=2:
	print ("Wrong number of arguments.")
	print ("Usage: " + sys.argv[0] + " <output file>")
	quit()
else:
	outfileName = sys.argv[1]

#Open output file for writing data to
outfile = open(outfileName,"w")

#file handle allows us to easily create as many new particles as we want
file_handle = open("inFile.txt","r")


#Creation of new particles p1 is the orbiting particle and p2 is the centre mass
p1 = p.read(file_handle)
p2 = p.read(file_handle)


#set up simulation parameters
numstep = 100
time = 0.0
dt = 0.1


#set up data lists 
tValue = [time]
xposValue = [p1.position[0]]
yposValue = [p1.position[1]]
zposValue = [p1.position[2]]
potential = 4*((1/vc.mag(p.Seperation(p2.position, p1.position))**12)-(1/vc.mag(p.Seperation(p2.position, p1.position))**6))

#set up energy lists
kineticValue = [p1.kineticenergy()]
potentialValue = [potential]


energyValue = [p1.kineticenergy()+potential]
#Initial force

def VerletIntegration(dt,particle):
    Force = 48*((1/vc.mag(p.Seperation(p2.position, p1.position))**14)-(0.5/vc.mag(p.Seperation(p2.position, p1.position))**8))*p.Seperation(particle1,particle2)

"""We need to make this work for all particles"""
    for i in range(numstep):
        #Update the position given the initial force
        p1.leapPosition2nd(dt, Force)

        #Update force for the new position
        Force_new = 48*((1/vc.mag(p.Seperation(p2.position, p1.position))**14)-(0.5/vc.mag(p.Seperation(p2.position, p1.position))**8))*p.Seperation(particle1,particle2)

        #Update velocity based of the average of the two forces
        p1.leapVelocity(dt,0.5*(Force+Force_new))

        #Update the different types of energy
        potential = 4*((1/vc.mag(p.Seperation(p2.position, p1.position))**12)-(1/vc.mag(p.Seperation(p2.position, p1.position))**6))
        p1.kineticenergy()

        #Reset force
        Force = Force_new
    
        #update time
        time = time + dt
    
        #add new values to their respective lists
        tValue.append(time)
        kineticValue.append(p1.kineticenergy())
        potentialValue.append(potential)
        xposValue.append(p1.position[0])
        yposValue.append(p1.position[1])
        
        #write data to the file created earlier
        outfile.write("{0:f} {1:f} {2:f} {3:f} {4:f}\n".format(time, p1.position[0], p1.position[1],p1.kineticenergy(),potential))
    
outfile.close()

