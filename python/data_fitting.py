#!/usr/bin/env python
"""
data_fitting

Created by alex
on 12/15/17

Fits the GDP data into the Cobbs Discrete model to test
"""
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


# Data fitting
N = len(gdp_dict.keys())
cols = list(range(1, 19))

adj_matrix = np.loadtxt("data/adjacencyAmericas.csv", delimiter=",", usecols=list(range(1, 19)), skiprows=1)

gdp_mean = np.mean(list(gdp_mean_dict.values()))
g = normalize(gdp_mean, gdp_min, gdp_max)

