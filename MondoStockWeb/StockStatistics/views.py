import datetime as dt
import urllib.request
from django.shortcuts import render
import pandas as pd
import pandas_datareader.data as web
start = dt.datetime(2000,1,1)
end = dt.datetime(2017,8,27)
from lxml import html

page = urllib.request.urlopen('http://localhost')
htm = page.text()
print(htm)
def index(request):
    return render(request, 'StockStatistics/home.html')

def StockPage(request):
    return render(request, "StockStatistics/basic.html", {'Company': web})
