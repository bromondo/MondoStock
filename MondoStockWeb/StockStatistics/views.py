import datetime as dt
from django.shortcuts import render
import pandas as pd
import pandas_datareader.data as web
start = dt.datetime(2000,1,1)
end = dt.datetime(2017,8,27)
df = web.DataReader('TSLA', 'yahoo',start, end)

def index(request):
    return render(request, 'StockStatistics/home.html')

def contact(request):
    return render(request, "StockStatistics/basic.html", {'Company': df.head()})
