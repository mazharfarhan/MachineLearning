
def test_run2():
    dates = pd.date_range('2009-01-01','2012-12-31')
    
    symbols = ['SPY', 'XOM']
    df = get_data(symbols, dates)
    plot_data(df)
    
    daily_returns = compute_daily_returns(df)
    daily_returns.plot(kind='scatter')
   
