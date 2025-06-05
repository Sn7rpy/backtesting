import requests 
import json 
import os
import functions as fn
import matplotlib.pyplot as plt
import numpy as np


dataIBM = fn.loadData("IBM")


fn.plotStock(dataIBM)
fn.plotStock(fn.loadData("AAPL"))

plt.show()