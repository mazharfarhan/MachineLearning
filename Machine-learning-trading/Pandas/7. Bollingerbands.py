# how to know the standard devation is deviating significantly from the mean so as to gain attention from a trading point of view ?

#sol: Bollinger band - if there is volatility in the stock, then we can discard the deviations towards the top and bottom of the mean. If the deviations are 2 standard deviation away from the mean, then we should pay attention. 

import os
import pandas as pd
import matplotlib.pyplot as plt


def plot_selected(df, columns, start_index, end_index):
    """Plot the desired columns over index values in the given range."""
    # TODO: Your code here
    # Note: DO NOT modify anything else!
    df = df.ix[start_index:end_index, columns]
    df.plot()
    plt.show()
    
    
def symbol_to_path(symbol, base_dir="data"):
    """Return CSV file path given ticker symbol."""
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))


def get_data(symbols, dates):
    """Read stock data (adjusted close) for given symbols from CSV files."""
    df = pd.DataFrame(index=dates)
    if 'SPY' not in symbols:  # add SPY for reference, if absent
        symbols.insert(0, 'SPY')

    for symbol in symbols:
        df_temp = pd.read_csv(symbol_to_path(symbol), index_col='Date',
                parse_dates=True, usecols=['Date', 'Adj Close'], na_values=['nan'])
        df_temp = df_temp.rename(columns={'Adj Close': symbol})
        df = df.join(df_temp)
        if symbol == 'SPY':  # drop dates SPY did not trade
            df = df.dropna(subset=["SPY"])

    return df


def plot_data(df, title="Stock prices"):
    """Plot stock prices with a custom title and meaningful axis labels."""
    ax = df.plot(title=title, fontsize=12)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    plt.show()
    
    
def test_run():
    # Define a date range
    dates = pd.date_range('2010-01-01', '2010-12-31')
    symbols = ['SPY']
    
    df = get_data(symbols, dates)
    ax = df['SPY'].plot(title = "SPY rolling mean", label = "SPY")
    
    #compute rolling mean using a 20-day rolling period.
    em_SPY = pd.rolling_mean(df['SPY'], window = 20 )
    
    em_SPY.plot(label = "Rolling mean", ax=ax)
    
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.legend(loc = "upper left")
    plt.show()
