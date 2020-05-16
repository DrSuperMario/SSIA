#STockdata 2.0
#
#
#Flexible module for gettind stock prices
#
##
#
#
#BY: DrSuperMario AKA Mario Muuk


import pandas as pd 
from pandas_datareader import data, wb
#import numpy as np


##stockdata chart
class Stockdata():
    '''
    DOCSTRING

    FINDING STOCK PRICES FOR CERTAIN PERIODS

    USE SAVE == "YES" FOR SAVING DATA TO TEMP FOLDER WITH A CSV FORMAY
    '''
    
    def __init__(self, stockname=None, startfrom=None , endto=None, sourcename='yahoo', save='no'):
        self.stockname = stockname
        self.sourcename = sourcename
        self.startfrom = startfrom
        self.endto = endto
        self.save = save.lower()
        
    def stockdata(self):
        
        get_data = data.DataReader(self.stockname,self.sourcename,self.startfrom,self.endto)
        if self.save == 'yes'.lower():
            pd.DataFrame(get_data).to_csv("temp/temp_{}_{}.csv".format(self.stockname,
            self.sourcename))
        return get_data

if __name__ == "__main__":
    print("NOTHING TO RUN")
    pass
