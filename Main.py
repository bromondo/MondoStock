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
print(df[['High','Low']].head())
df['High'].plot(kind='bar')
plt.show()