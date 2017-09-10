#!/usr/bin/env python
"""
Created by Alex Hopkins
on 9/6/17

Python code for the SDE model
"""
import numpy as np

# Constants
r = 0.05
epsilon = 1
g = 0.7

# Size of Ring network
N = 12

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
steps = 50

u_sol = np.zeros([N, steps])
u_sol[:, 0] = u_zero.transpose()

for k in range(0, steps):
	ukp1 = uk + r * (g - uk) + epsilon * (uk * (1 - uk)) * (0.5 * A * uk - g)
	
	a1, b1 = np.where(uk < 0)
	a2, b2 = np.where(uk > 0)
	
	uk[a1] = 0.005
	uk[a2] = 0.995
	
	uk = uk.transpose()
	u_sol[:, k] = ukp1[:, 0]
	
	uk = ukp1
