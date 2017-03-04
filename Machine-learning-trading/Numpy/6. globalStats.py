## Statistics on time series.

import pandas as pd
import numpy as np

# to compute a stat on any dataframe, we can use the function that will compute the column wise stat on that dataframe.
stat = df1.mean()

# simillary we have functions for median, std, sum, prod, mode - All together 33 global statistics.

#Eg: 


dates = pd.date_range('2010-01-01', '2012-12-31')
symbols = ['SBY', 'GOOG', 'XOM', 'GLD']
