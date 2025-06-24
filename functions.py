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
    plt.legend()

class Stock:
    def __init__(self,symbol):
        self.symbol = symbol
        self.price = 0

    def updatePrice(self,newPrice):
        self.price = newPrice

    def getPrice(self):
        return self.price

    def __str__(self):
        return(f"{self.symbol}: Price = ${self.price}")

class Market:
    def __init__(self, startDate):
        self.stocks = {}
        self.date = startDate
        pass

    def addStocks(self, stocks=list):
        for symbol in stocks:
            self.stocks[symbol] = Stock(symbol)
    
    def updateMarket(self):
        for stock in self.stocks:
            pass
    
    def getStock(self,symbol):
        return self.stocks[symbol]

class Porfolio:
    def __init__(self, initCash, market = Market):
        self.cash = initCash
        self.assets = {}
        self.market = market
        for sybl in market.stocks.keys():
            self.assets[sybl] = 0
        pass

    def buyStock(self,symbol,quantity):
        stock = self.market.getStock(symbol)
        price = stock.getPrice()
        self.cash -= price*quantity
        self.assets[symbol] += quantity
        pass

    def sellStock(self,symbol,quantity):
        stock = self.market.getStock(symbol)
        price = stock.getPrice()
        self.cash += price*quantity
        self.assets[symbol] -= quantity

    def reportAssets():
        pass