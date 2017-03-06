import pandas as pd
import matplotlib.pyplot as plt

# user defined functions 
from util import get_data, plot_data

def compute_daily_returns(df)
  daily_returns = df.copy()
  daily_returns[1:] = (df[1:] / df[:-1]) -1
  daily_return.ix[0, :] = 0
  return daily_returns

def test_run():
    dates = pd.date_range('2009-01-01','2012-12-31')
    
    symbols = ['SPY']
    df = get_data(symbols, dates)
    plot_data(df)
    
    daily_returns = compute_daily_returns(df)
    plot_data(daily_returns, title ="Daily_returns", ylabel="daily_returns")
    
    # default is 10 bins
    daily_returns.hist(bins = 20)
    
    mean = daily_returns['SPY'].mean()
    std = daily_returns['SPY'].std()
    
    plt.axvline(mean, color='w', linestyle ='dashed', linewidth = 2)
    plt.axvline(std, color='r', linestyle='dashed', linewidth=2)
    plt.axvline(-std, color='r', linestyle='dashed', linewidth=2)
    plt.show()
    
    print daily_returns.kurtosis()
    
def test_run2():
    dates = pd.date_range('2009-01-01','2012-12-31')
    
    symbols = ['SPY', 'XOM']
    df = get_data(symbols, dates)
    plot_data(df)
    
    daily_returns = compute_daily_returns(df)
    plot_data(daily_returns, title ="Daily_returns", ylabel="daily_returns")
    
    daily_returns['SPY'].hist(bin = 20, label = 'SPY')
    daily_returns['XOM'].hist(bin = 20, label = 'XOM')
    plt.legend(loc = 'upper right')    
    
    plt.show()
