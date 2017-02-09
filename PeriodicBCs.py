from Particle3D import Particle3D as particle


nDim = 5
if particle.leapPosition2nd > nDim:
    particle.leapPosition2nd = -nDim
elif particle.leapPosition2nd < -nDim:
    particle.leapPosition2nd = nDim
else:
    particle.leapPosition2nd = particle.leapPosition2nd

