#!/usr/bin/env python
"""
Created by alex 
on 2/23/18

Cleans the data of world_GDP into just north and south american countries
"""
import pandas as pd

country_df = pd.read_csv('data/country_list.csv')
gdp_df = pd.read_csv('data/world_GDP.csv')

# Take countries with continent declared as North America or South America, then rearrange the data frame to drop the
# Continent and convert to List
americas_list = country_df.loc[country_df['Continent'].isin(['North America', 'South America'])].drop(['Continent'],
                                                                                                      axis=1)
americas_list = list(americas_list['Country'])

# Find the GDP of the countries in the americas_list and then drop the unneeded columns from the data frame
americas_gdp = gdp_df.loc[gdp_df['Country Name'].isin(americas_list)].drop(['Country Code', 'Indicator Code',
                                                                            'Indicator Name'], axis=1)

americas_gdp.to_csv('data/americas_gdp.csv', index=False)
