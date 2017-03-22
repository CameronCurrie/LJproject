Cameron Currie s1527695
Blaise Smyth s1508543


	MDCore.py	This is the main code, it takes two arguments in the terminal. 
			The first argument is the name of the output file (must be xyz you 				wish to write to e.g. TEST.xyz. The second argument is the input file
			which provides the initial conditions of the system in the format of:
		     <density> <temperature> <timestep> <numberofsteps> <numberofparticles>
			
			For optimal results of the code, a timestep of =< 0.002 should be 				used with a number of steps ~2000. The code can take a several 				minutes to run especially with high particle number. 
			Several graphs will also be saved with names corresponding to what
			they show.
			Correct usage of this in the terminal is shown below:

		python MDCore.py <outputfilename>.xyz <initialconditions>.txt

	Particle3D.py	This is the particle3D class that is used to create instance of a
			particle and to updates its positions and velocity. This class also
			provides the kinetic energy of a particle as well as the seperation
			of two particles.

   Particlecreator.py	This creates N instances of Particle3D where N is the number of 
			particles provided by the initial conditons. This also names the 				particles with numbers starting at 1.

	MDUtilities.py	This set the initial positions and velocities of the particles and
			also provides the length of the simualtion box's side.

  verletintegration.py	This is the code that applies the minimum image conventions and  				periodic boundary conditions. The force acting on a particle due to
			another particle and the sum of these forces acting on a particle.
			It also does the same for potential energy.
			The verletintegration function runs updates the forces, positions,
			velocities, energies, time and produces graphs of energy versus
			time and the xyz file which is used in vmd to visualised the system.
			Also contains the initial conditions class which allows for the 			reading of conditions from an input file to set the initial 				positions and velocities using MDUtilities.

    VectorMethods.py	Used to find the magnitude of seperation vectors.

