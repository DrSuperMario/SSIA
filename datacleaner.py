#Webscraper 2.0
#
#Back Module for all the webscrapting business
#
#
#
#
#By : DrSuperMario AKA Mario Muuk



import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA
from socialdata import Socialmedia as social
import re, datetime
#from typing import List, Optional

sia = SIA()

class Cleaner():
    '''
    DOCSTRING

    DDATA CLEANER FOR GATHERED SOCIAL DATA
    '''

    def __init__(self):
        self.social = social

    
    def social_cleaner(self,social,source=None):

        if source == 'xml'.lower():
            headLineList = []
            for ra in social[::2]:
                sentencPolarity = sia.polarity_scores(ra)
                headLineList.append(sentencPolarity)
                
            newsColl = pd.DataFrame(headLineList)
            newsColl.index = pd.to_datetime(social[1::2])
            newsColl.index = newsColl.index.to_series().apply(lambda x : datetime.datetime.strftime(x, '%m-%d-%Y'))
            newsColl.index = pd.to_datetime(newsColl.index)
        
        else:

            newlist = [re.split("[>]",x) for x in social] 
            headLineList = []
            for ra in range(len(newlist)):
                take = newlist[ra][0]
                sentencPolarity = sia.polarity_scores(take)
                headLineList.append(sentencPolarity)

            newsColl = pd.DataFrame(headLineList, columns=sentencPolarity.keys(), 
                                     index=[newlist[x][1] for x in range(len(newlist))])

            
            if len(newlist[0][1]) >= 19:
                newsColl.index = pd.to_datetime(newsColl.index)
                newsColl.index = newsColl.index.to_series().apply(lambda x : datetime.datetime.strftime(x, '%m-%d-%Y'))
                newsColl.index = pd.to_datetime(newsColl.index)
            elif len(newlist[0][1]) >= 12:
                newsColl.index = pd.to_datetime(newsColl.index,unit='s')
                newsColl.index = newsColl.index.to_series().apply(lambda x : datetime.datetime.strftime(x, '%m-%d-%Y'))
                newsColl.index = pd.to_datetime(newsColl.index)
            else:
                newsColl.index = pd.to_datetime(newsColl.index)

        
        newsColl['pos'] = newsColl['pos'] * 100.0
        newsColl['neg'] = newsColl['neg'] * 100.0
        newsColl.drop(['neu','compound'], axis=1, inplace=True)
        newColl = newsColl.loc[(newsColl!=0.0).any(axis=1)]
        


        return newColl
        
       
if __name__ == "__main__":
    print("NOTHING TO CLEAN")
    pass

        