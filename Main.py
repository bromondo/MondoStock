import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

##start = dt.datetime(2000,1,1)
##end = dt.datetime(2017,8,27)
##df = web.DataReader('TSLA', 'yahoo',start, end)
df = pd.read_csv('tsla.csv')

print(df.head())
df['100ma'] = df['Adj Close'].rolling(window=100).mean()
print(df.tail())

ax1 = plt.subplot2grid(6,1,0,0,rowspan=5,colspan=1)
ax2 = plt.subplot2grid(6,1,5,0)

ax1.plot(df['Date'], df['100ma'])
plt.show()