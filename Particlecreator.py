"""first attempt at creating list of particles"""

"""
class particleList()

    def __init__(self,file_handle): 
"""
from Particle3D import Particle3D as particle

PNUMBER = 20
#assigns a name to each particle
def pNamer(PNUMBER):
    pList = []
    for i in range(PNUMBER):
        position = 0
        velocity = 0
        mass = 0
        name = i
        particle(position,velocity, mass, name)
        pList.append(particle)
    return pList

print pNamer(PNUMBER)






