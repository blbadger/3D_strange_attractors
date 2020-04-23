#!python3
# A program to display the Rossler attractor. 
# Based on Vedran Sekara's write-up found here
# https://vedransekara.github.io/2016/11/14/strange_attractors.html

# import third-party libraries
import numpy as np 
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
plt.style.use('dark_background')

# ODE definition
def rossler_attractor(x, y, z, a=0.1, b=0.1, c=14):
	'''A function to compute the next location of the 
	Rossler ODE, given a current location.  Arguments
	x, y, and z denote location in 3D space, and kwargs
	a, b, and c are constants supplied here.
	'''
	x_dot = - y - z
	y_dot = x + a*y
	z_dot = b + z*(x - c)

	return x_dot, y_dot, z_dot

# initialize solution array
steps = 2000000
xx = np.empty((steps + 1))
yy = np.empty((steps + 1))
zz = np.empty((steps + 1))

# initialization of starting points and time step size
xx[0], yy[0], zz[0] = (3, 3, 3)
delta_t = 0.01

# evolution of the system
for i in range(steps):
	x_dot, y_dot, z_dot = rossler_attractor(xx[i], yy[i], zz[i])
	xx[i + 1] = xx[i] + (x_dot * delta_t)
	yy[i + 1] = yy[i] + (y_dot * delta_t)
	zz[i + 1] = zz[i] + (z_dot * delta_t)

# matplotlib figure specifications
fig = plt.figure(figsize=(10,10))
ax = fig.gca(projection='3d')
plt.gca().patch.set_facecolor('black')

# make 
plt.plot(xx, yy, zz, '-', color='white',lw=0.01)
plt.axis('off')
plt.show()
plt.close()

