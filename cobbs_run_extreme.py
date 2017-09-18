#!/usr/bin/env python
"""
Created by Alex Hopkins
on 9/6/17

Python code for the SDE model
"""
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.collections import PolyCollection
import matplotlib.pyplot as plt
from matplotlib import colors as mcolors
import numpy as np

# Constants
r = 0.05
epsilon = 1
g = 0.7

# Size of Ring network
N = 6

#   Creation of Ring network
A = np.zeros([N, N])
B = np.ones([N - 1])

A = np.diag(B, k=1) + np.diag(B, k=-1)

A[0, N - 1] = 1
A[N - 1, 0] = 1

# Initial value Constants
u_zero = np.zeros([N, 1])
u_zero[0: N // 2] = 0.35
u_zero[N // 2:] = 0.8

uk = u_zero
steps = 5

u_sol = np.zeros([N, steps+1])
u_sol[:, 0] = u_zero.transpose()

for k in range(0, steps):
	ukp1 = uk + r * (g - uk) + epsilon * (uk * (1 - uk)) * (0.5 * A * uk - g)
	
	ukp1.resize(N)

	a1 = np.where(uk < 0)

	a2 = np.where(uk > 0)

	uk[a1] = 0.005
	uk[a2] = 0.995
	
	uk = uk.transpose()
	u_sol[:, k + 1] = ukp1
	
	uk = ukp1

# fig = plt.figure()
# ax = fig.gca(projection='3d')
#
# xs = np.arange(1, N)
# verts = []
# zs = [0.0, 1.0, 2.0, 3.0]
#
# for z in zs:
# 	ys = np.random.rand(len(xs))
# 	ys[0], ys[-1] = 0, 0
# 	verts.append(list(zip(xs, ys)))
#
# poly = PolyCollection(verts, facecolors=['r', 'g', 'c', 'y'])
#
# ax.add_collection3d(poly, zs=zs, zdir='y')
#
# ax.set_xlabel('X')
# ax.set_xlim3d(1, N)
# ax.set_ylabel('Y')
# ax.set_ylim3d(1, N)
# ax.set_zlabel('Z')
# ax.set_zlim3d(0, 1)
#
# plt.show()
