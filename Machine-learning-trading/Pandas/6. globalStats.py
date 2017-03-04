## Statistics on time series.

import pandas as pd
import numpy as np

# to compute a stat on any dataframe, we can use the function that will compute the column wise stat on that dataframe.
stat = df1.mean()

# simillary we have functions for median, std, sum, prod, mode - All together 33 global statistics.

#Eg: 
dates = pd.date_range('2010-01-01', '2012-12-31')
symbols = ['SBY', 'GOOG', 'XOM', 'GLD']

# function to create a dataframe - userdefined
df = getData(symbols, dates)

# user defined function to plot data
plot_data(df)

# mean - average of set of values.  median - value oin the middle when the values is sorted.
print df.mean()
print df.median()

# measure of deviation from central value. Higher values indicate that it has varied a lot with time from the mean value.
print df.sd()
