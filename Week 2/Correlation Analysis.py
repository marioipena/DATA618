# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 14:26:11 2022

@author: mpena
"""

#import libraries
import pandas as pd
missing_values = ["n/a", "na", "*", "-", " "]

#import gdp dataset from local folder and convert to time series
gdp_growth = pd.read_csv("C:/Users/mpena/Desktop/Mario/DATA618/Week 2/united-states-gdp-growth-rate.csv", skiprows = 16, na_values = missing_values)
gdp_growth['date'] = pd.to_datetime(gdp_growth['date'])
gdp_series = pd.Series(gdp_growth[' GDP Growth (%)'].values, index=gdp_growth['date'])

#import fed dataset from local folder, convert to time series, aggregate to yearly average and filter years to match gdp data rows.
fed_fund = pd.read_csv("C:/Users/mpena/Desktop/Mario/DATA618/Week 2/FEDFUNDS.csv", na_values = missing_values)
fed_fund['DATE'] = pd.to_datetime(fed_fund['DATE'])
fed_series = pd.Series(fed_fund['FEDFUNDS'].values, index=fed_fund['DATE'])
fed_series_filter = (fed_series.resample('Y').mean())
fed_series_filter2 = fed_series_filter[(fed_series_filter.index >= '1961-12-31') & (fed_series_filter.index <= '2021-12-31')]

print(gdp_series.corr(fed_series_filter2))

#import cpi dataset from local folder and filter for desired columns and rows
cpi = pd.read_csv("C:/Users/mpena/Desktop/Mario/DATA618/Week 2/CPI Data.csv", skiprows = 2, na_values = missing_values)
cpi['Year'] = pd.to_datetime(cpi['Year'])
cpi_filter = cpi[(cpi['Year'] >= '1954-12-31') & (cpi['Year'] <= '2022-12-31')]
cpi_filter2 = cpi_filter.filter(['Year', 'Dec-Dec'])


print(fed_fund['FEDFUNDS'].corr(cpi_filter2['Dec-Dec']))
