"""first attempt at creating list of particles"""

"""
class particleList()

    def __init__(self,file_handle): 
"""
from Particle3D import Particle3D as Particle3D

#assigns a name to each particle
def pNamer(PNUMBER):
    particles = []
    for i in range(PNUMBER):
        position = 0
        velocity = 0
        mass = 1
        name = i + 1
        p=Particle3D(position,velocity, mass, name)
        particles.append(p)
    return particles
    #print particles[0]


"""
particles = pNamer(PNUMBER)
print particles[0]
"""





