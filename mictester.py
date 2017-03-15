import verletintegration as verlet
from Particle3D import Particle3D as Particle3D
import numpy as np



BOXSIZE = 3

p1 = Particle3D(1, np.array([0,0,0]), np.array([1,1,1]), 1)
p2 = Particle3D(2, np.array([1,2,5]), np.array([1,1,1]), 1)

print verlet.mic(p1, p2, BOXSIZE)