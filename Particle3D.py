
"""
Exercise 3: Particle3D Class	
"""

import numpy as np

class Particle3D(object):

	# Initialise a Particle3D instance
    def __init__(self, position, velocity, mass, name):
        self.position = (position)
        self.velocity = (velocity)
        self.mass = mass
        self.name = name


    # Formatted output as String
    def __str__(self):
        return str(self.name) + " " + str(self.position[0]) + " " + str(self.position[1]) + " " + str(self.position[2])


    # Kinetic energy
    def kineticenergy(self):	
        return 0.5*self.mass*sum(self.velocity**2)


    # Time integration methods

    # First-order velocity update
    def leapVelocity(self, dt, force):
        self.velocity = self.velocity + dt*force/self.mass
        return self.velocity


    # First-order position update
    def leapPosition1st(self,dt):
        self.position = self.position + dt*self.velocity
        return self.position
        

    # Second-order position update
    def leapPosition2nd(self,dt,force):
        self.position = self.position + dt*self.velocity + 0.5*dt**2*force/self.mass
        return self.position


    #Reading from a file to create new particles
    @staticmethod
    def read(inFile):
        line = inFile.readline()
        tokens = line.split()
        position = np.array([float(tokens[0]),float(tokens[1]),float(tokens[2])])
        velocity = np.array([float(tokens[3]),float(tokens[4]),float(tokens[5])])
        mass = float(tokens[6])
        name = str(tokens[7])        
        return Particle3D(position,velocity,mass,name)


    #Seperation of two instances of the Particle3D class
    @staticmethod   
    def Seperation(particle1,particle2):
        return particle1.position - particle2.position
        
        
        """
        xsep = particle1[0] - particle2[0] 
        ysep = particle1[1] - particle2[1]
        zsep = particle1[2] - particle2[2]
        return np.array([xsep,ysep,zsep],float)
        """
