"""Periodic boundary conditions, 1D atm"""
#from Particle3D import Particle3D as particle

#import MDUtilities as MDU

#MDU.boxSize = boxSize while developing code

#testing purposes we set boxsize

BOXSIZE = 5

#set test positions for our particle in each axis x,y,z
position = [0,0,0]
position[0] = 500.01
position[1] = 4000004.124352
position[2] = -5.001


#for loop changing positions 
#there is a potential bug if the position update returns 
#a position that's >4*BOXSIZE
#def pbc(self,BOXSIZE):
"""
for i in range(3):
    if position[i] > BOXSIZE:
        position[i] = -2*BOXSIZE+position[i]
        print "The " +str(i) +" position is " +str(position[i])
    elif position[i] < 0:
        position[i] = 2*BOXSIZE+position[i]
        print "The " +str(i) +" position is " +str(position[i])
    else:
        print "The " +str(i) +" position is " +str(position[i])
"""

#periodic boundary conditions 
#def pbc(BOXSIZE, p1):
    #checks for each dimension if the particle is outside the box
for i in range(3):
    while position[i] > BOXSIZE:
        position[i] = position[i] - 4*BOXSIZE
    while position[i] < 0:
        position[i] = position[i] + BOXSIZE
    print "The " +str(i) +" position is " +str(position[i])

#to fix potential bug we could add another if
#-> 2*BS+position added however this wont be a problem if dt is small
