#! python3
# Produces a plot of the lorenz attractor, an
# idealized system of equations modelling 
# convection

# import third-party libraries
import numpy as np 
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
plt.style.use('dark_background')

def lorenz_attractor(x, y, z, a=12, b=24, c=2.67):
	'''A function to calculate the derivative at any
	point in 3D space specified by the Lorenz equations
	Inputs are args x, y, z specifying location in space, 
	kwargs a, b, c being constants. Returns derivatives 
	of each arg.
	'''
	x_dot = a*(y - x)
	y_dot = x*(b - z) - y
	z_dot = x * y - c * z
	return x_dot, y_dot, z_dot

#parameters
delta_t = 0.01
steps = 100000

# initialize solution array
X, Y, Z = np.zeros(steps), np.zeros(steps), np.zeros(steps)

# starting point
X[0], Y[0], Z[0] = (0, 0.2, 0.1001)

# evolution of the system
for i in range(steps-1):
	#calculate derivatives
	x_dot, y_dot, z_dot = lorenz_attractor(X[i], Y[i], Z[i])
	X[i + 1] = X[i] + x_dot * delta_t
	Y[i + 1] = Y[i] + y_dot * delta_t
	Z[i + 1] = Z[i] + z_dot * delta_t

fig = plt.figure(figsize=(8,8))
ax = fig.gca(projection='3d')
plt.gca().patch.set_facecolor('black')

plt.plot(X, Y, Z, '-', color='white',lw=0.05)

plt.axis('off')

'''
# optional: use if reference axes skeleton is desired,
# ie plt.axis is set to 'on'
ax.set_xticks([]), ax.set_yticks([]), ax.set_zticks([])

# make pane's have the same colors as background
ax.w_xaxis.set_pane_color((0.0, 0.0, 0.0, 1.0)), ax.w_yaxis.set_pane_color((0.0, 0.0, 0.0, 1.0)), ax.w_zaxis.set_pane_color((0.0, 0.0, 0.0, 1.0))
'''
plt.show()
plt.close()

