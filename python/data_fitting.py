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

# Reformat dictionary to show 1 as max gdp and 0 as lowest and some fraction of those in between



# Creation of the ring network for North America
N = len(gdp_dict.keys())
