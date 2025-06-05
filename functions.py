import requests 
import json 
import os
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np

def requestData(index, size="compact"):
    with open("key.json","r") as file:
        key = json.load(file)
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={index}&outputsize={size}&apikey={key}"
    r = requests.get(url)
    data = r.json()
    return data

def loadData(index, size="compact"):
    dataPath = f"stock_data/{index}_{size}_data.json"

    if os.path.exists(dataPath):
        with open(dataPath,"r") as file:
            data = json.load(file)
        print("loaded data from file")
    else:
        data = requestData(index,size)
        print("loaded data from api")
        with open(dataPath,"w") as file:
            json.dump(data,file)
    
    return data

def plotStock(data):

    timeSeries = data['Time Series (Daily)']

    days = []
    prices = []

    for date,info in timeSeries.items():

        open = float(info['1. open'])
        close = float(info['4. close'])
        days.append(date+"T05:00:00")
        prices.append(open)
        days.append(date+"T20:00:00")
        prices.append(close)

    time = np.array(days,dtype='datetime64[D]')

    plt.plot(time, prices)
    