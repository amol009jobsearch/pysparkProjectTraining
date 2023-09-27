import pandas as pd


series1 = pd.Series([1, 2, 3, 4], name='Series1')
series2 = pd.Series(['A', 'B', 'C', 'D'], name='Series2')
series3 = pd.Series([10.1, 20.2, 30.3, 40.4], name='Series3')
series4 = pd.Series([True, False, True, False], name='Series4')

# Use zip to combine the Series into a DataFrame
for pv,fv,f,int in zip(series1, series2, series3, series4):
    print(type(pv))

# Display the resulting DataFrame
