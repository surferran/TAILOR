# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 00:34:47 2018

from
https://www.quantinsti.com/blog/basic-operations-stock-data-using-python/

about data actions
"""
#data = pd.DataFrame..

# Deleting the "TIME" column
del data['TIME']

# type of index:
type(data.index)

# Number of rows in the data set
print(data['CLOSE'].count())

# get index of the Close price where it is the maximum
data.CLOSE[data.CLOSE == max_price].index

'''
Let us compute the daily percentage change in closing price. 
We add a new column of ‘Percentage_Change’ to our existing data set. 
In the next line of code, we have filtered the percent change column for 
all the values greater than 1.0. The result has been presented below.
'''
# Compute the percentage change
data['Percent_Change'] = data['CLOSE'].pct_change()*100

# Filter the percent change column for all values greater than 1.0
dt = (data[data.Percent_Change > 1.0])

'''
Finally, let us add a couple of indicators. We compute the 20-day simple 
moving average and the 5-day average volume. We can add more indicators 
to our data frame and then analyze the stock trend to see whether it is 
bullish or bearish. You can learn more on how to create various technical 
indicators in Python here.
'''
# Closing near the 20-day SMA
ndays = 20
SMA = pd.Series((data['CLOSE']).rolling(window=ndays).mean(),name = 'SMA') 
data = data.join(SMA)

# Higher trade Quantity
Avg_vol = pd.Series((data['VOLUME']).rolling(window=5).mean(),name = '5day_AvgVol')
data = data.join(Avg_vol)
