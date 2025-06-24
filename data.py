import requests 
import json 
import os
import functions as fn
import matplotlib.pyplot as plt
import numpy as np


dataIBM = fn.loadData("IBM","full")


fn.plotStock(dataIBM)
fn.plotStock(fn.loadData("AAPL","full"))

plt.show()
