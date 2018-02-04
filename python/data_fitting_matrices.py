#!/usr/bin/python3
"""
created by alex on 2/2/18

Fits the GDP data into the Cobbs Discrete model using matrices
"""

from matplotlib import cm
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import numpy as np
import pandas as pd


def normalize(x, min_x, max_x):
	"""
	Goal of this function is to normalize passed data given the min and max of the data to fit in 0 - 1

	:param x: Array Like structure: The data to be normalized
	:param min_x: Float like: The minimum of the data set
	:param max_x: Float like: The maximum of the data set

	:return: Array: The normalized data in an array with values ranging from 0 to 1
	"""
	return (x - min_x) / (max_x - min_x)


# Index_col=58 represents dropping out the unnamed column from the csv
df = pd.read_csv("data/North_America_GDP.csv", header=0, index_col=58)

# Generates an numpy nd array with the indexes of 0th index as country array with 57 years as position in array and gdp
# Being the value at that 'year'. With index 0 being the name of the country
gdp_matrix = df.as_matrix()

# Find max/min of all years and all countries gdp and set up for construction of 3D array
gdp_list = []
countries = []
years = np.arange(1960, 2017, 1)

# Loop through the matrix, each array is a country and its gdp for each year so need double for loop
for country in gdp_matrix:
	for gdp in country:

		# If it is a string ignore it and continue (Strings are the 0th index in the array of each country
		if type(gdp) == str:
			countries.append(gdp)
			continue

		gdp_list.append(gdp)

gdp_min = np.nanmin(gdp_list)
gdp_max = np.nanmax(gdp_list)

# reshape array with rows as countries and columns as year
gdp_array = np.asarray(gdp_list).reshape(len(countries), len(years))

# Normalize the gdp from values of 0 to 1
normalized_gdp = normalize(gdp_array, gdp_min, gdp_max).reshape(len(countries), len(years))

# Plotting normalized gdp
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
#
# X, Y = np.meshgrid(range(len(years)), range(len(countries)))
# print(X.shape)
# print(Y.shape)
#
# surface = ax.plot_surface(X, Y, normalized_gdp, rstride=1, cstride=1, cmap=cm.coolwarm)
#
# ax.set_title('Normalized GDP of North American countries')
# ax.set_ylabel('countries corresponding to adjacency list')
# ax.set_xlabel('Time points in years')
#
# plt.savefig('figs/normalized_gdp.png')

# Data Fitting
# Setup
normalized_gdp_nans = normalized_gdp[~np.isnan(normalized_gdp)]
network_total = np.zeros((len(countries), len(years)))
network_tmp = np.zeros((1, len(years)))

adj_matrix = np.loadtxt("data/adjacencyAmericas.csv", delimiter=",", usecols=list(range(1, 19)), skiprows=1)

g = np.mean(normalized_gdp_nans)
r = 1
e = 1

for year in range(len(years)):
	for country in range(len(countries)):

		u_i = normalized_gdp[country][year]					# Current node value
		neighbors = np.where(adj_matrix[country] == 1)		# Check for the neighbors of the current node
		neighbors_i = -1

		if len(neighbors[0] > 0):							# Meaning if they have neighbors or not
			size = len(neighbors[0])

			while size > 0:									# Add up the neighbors
				size -= 1
				neighbors_i = normalized_gdp[neighbors[0][size]][year] + normalized_gdp[neighbors[0][size - 1]]

			neighbors_i = 0.5 * neighbors_i

			# the feedback effect to return to natural internal state G upon deviation
			fb_i = r * (g - u_i)

			# contribution of neighbors upon polarisation extent
			pol_i = e * u_i * (1 - u_i) * (neighbors_i - g)

			# put all the contributions together for the iteration
			u_i_t = u_i + fb_i + pol_i
			network_tmp = u_i_t
		network_total[country][:] = network_tmp

# Plotting
print(network_total)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

X, Y = np.meshgrid(range(len(years)), range(len(countries)))

surface = ax.plot_surface(X, Y, network_total, rstride=1, cstride=1, cmap=cm.coolwarm)

ax.set_title('Polarized model')
ax.set_ylabel('countries corresponding to adjacency list')
ax.set_xlabel('Time points in years')
ax.set_zlabel('Influence from other countries')

plt.savefig('figs/polarizations_reworked.png')
