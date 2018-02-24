#!/usr/bin/env python
"""
data_fitting
Created by alex
on 12/15/17
Fits the GDP data into the Cobbs Discrete model to test
"""
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt
from matplotlib import cm
import numpy as np
import pandas as pd

# Index_col=58 represents dropping out the unnamed column from the csv
df = pd.read_csv("data/North_America_GDP.csv", header=0, index_col=58)

# Creates a Dictionary with the values as the list of the Country's GDP in order of year from 1960 to 2016
gdp_dict = df.set_index('Country Name').T.to_dict('list')

# Keys are year, values are mean gdp of all countries at that year
gdp_mean_dict = df.mean().to_dict()
# Find max/min of all years and all countries gdp
gdp_min = []
gdp_max = []

for country, gdp in gdp_dict.items():
	gdp_min.append(gdp)
	gdp_max.append(gdp)

gdp_min = np.nanmin(gdp_min)
gdp_max = np.nanmax(gdp_max)


def normalize(x, min_x, max_x):
	"""
	Goal of this function is to normalize passed data given the min and max of the data to fit in 0 - 1

	:param x: Array Like structure: The data to be normalized
	:param min_x: Float like: The minimum of the data set
	:param max_x: Float like: The maximum of the data set

	:return: Array: The normalized data in an array with values ranging from 0 to 1
	"""
	return (x - min_x) / (max_x - min_x)


# Reformat dictionary to show 1 as max gdp and 0 as lowest and some fraction of those in between
# Created a new dictionary to store the normalized data with the keys being the countries and the values are
# an array with index equivalent to the years from 1960 - 2016
normalized_dict = {}
for country, gdp in gdp_dict.items():
	temp_dict = {country: normalize(gdp, gdp_min, gdp_max)}
	normalized_dict.update(temp_dict)

# Plotting Normalized GDP

# normalized dictionary in a list for indexing 1st index is the country, 2nd index is to choose the place in the tuple,
# where 0 is the string of the country and 1 is the array, 3rd index is the place in the array if choosing in 2nd index
normalized_items = list(normalized_dict.items())
x = []
y = []
z = []
for i in range(len(normalized_items)):
	x.append(normalized_items[i][0])
	z.append(normalized_items[i][1])
	
for i in range(len(list(gdp_mean_dict.keys()))):
	y.append(int(list(gdp_mean_dict.keys())[i]))

X, Y = np.meshgrid(range(len(x)), y)
print(z[0][:])
for i, j in range(len(z)):
	pass
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
#
# surface = ax.plot_surface(X, Y, z, rstride=1, cstride=1, cmap=cm.coolwarm)
#
# ax.set_xlabel('countries corresponding to adjacency list')
# ax.set_ylabel('Time points in years')
# ax.set_zlabel('Normalized GDP')
#
# plt.show()

#  Data fitting
time_points = len(gdp_mean_dict.keys())
countries = list(gdp_dict.keys())
network_tmp = np.zeros((1, len(countries)))
network_total = np.zeros((time_points, len(countries)))

adj_matrix = np.loadtxt("data/adjacencyAmericas.csv", delimiter=",", usecols=list(range(1, 19)), skiprows=1)

gdp_mean = np.mean(list(gdp_mean_dict.values()))
g = normalize(gdp_mean, gdp_min, gdp_max)
r = 1
e = 1

for year in range(0, time_points):
	for i, country in enumerate(countries):

		u_i = normalized_dict[country][year]

		if country == countries[0]:
			neighbors_i = normalized_dict[countries[1]][year]

		elif country == countries[-1]:
			neighbors_i = normalized_dict[countries[-2]][year]

		else:
			neighbors_i = 0.5 * (normalized_dict[countries[i - 1]][year] + normalized_dict[countries[i + 1]][year])

		fb_i = r * (g - u_i)
		pol_i = e * u_i * (1 - u_i) * (neighbors_i - g)
		u_i_t = u_i + fb_i + pol_i

		if u_i_t < 0:
			u_i_t = 0
		elif u_i_t > 1:
			u_i_t = 1

		network_tmp[0, i] = u_i_t
	network_total[year, :] = network_tmp[0, :]

# Plotting

nx = len(countries)
ny = time_points

x = range(nx)
y = range(ny)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

X, Y = np.meshgrid(x, y)
surface = ax.plot_surface(X, Y, network_total, rstride=1, cstride=1, cmap=cm.coolwarm)

ax.set_xlabel('countries corresponding to adjacency list')
ax.set_ylabel('Time points in years')

# plt.show()
