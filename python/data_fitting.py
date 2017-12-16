#!/usr/bin/env python
"""
data_fitting

Created by alex
on 12/15/17

Fits the GDP data into the CobbsDiscrete model to test
"""
import numpy as np
import pandas as pd

# Index_col=58 represents dropping out the unnamed column from the csv
df = pd.read_csv("data/North_America_GDP.csv", header=0, index_col=58)

# Creates a Dictionary with the values as the list of the Country's GDP in order of year from 1960 to 2016
gdp_dict = df.set_index('Country Name').T.to_dict('list')
