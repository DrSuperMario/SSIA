#Webscraper 2.0
#
#Back Module for all the webscrapting business
#
#
#
#
#By : DrSuperMario AKA Mario Muuk



import praw
from bs4 import BeautifulSoup
import requests, datetime, re
import tweepy
import json


#DEFAULT HEADER FOR PARSER#default header
header_t =  {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}

##default parser's
parser_t = ['html5lib',
            'lxml',
            'html.parser']

#reddit API key and INFP
reddit = praw.Reddit(client_id='RssjiSClzNYEbg',
                    client_secret='I4HopxhOsvtGflgcuhin9VfgXbk',
                    user_agent='SSAT',
                    username='DrSuperMario',
                    password='dd$$b7@bkZnbeX7')
#Twitter API keys 
twitter_consumer_key='vJLlLpJ82bugjPjfyNMCPqLTp'
twitter_consumer_secret='6p4bgoge6MX9I1PYULnBerFGJzSHnwsFd628fxhc6Mqaq7sNLO'
auth_twitter = tweepy.AppAuthHandler(twitter_consumer_key, twitter_consumer_secret)
twitter_api = tweepy.API(auth_twitter)



class Webscraper():
    '''
    DOCSTRING 

    MODULE FOR GETTING ANF GATHERING NEWS AND TITLES FROM DIFFRENT SOURCES

    '''
    def __init__(self,url=None,header=header_t):
        self.url = url
        self.header = header
        #self.parsers = parsers
        
    def scrapedata(self, parsers=parser_t[0]):
        req = requests.get(self.url, headers=self.header)
        con = req.content
        soup = BeautifulSoup(con, parser=parsers)
        #find_tags = soup.find_all("title")
        #final = soup.prettify().encode(encode_t)
        return soup

    def scrapexml(self):
        req = requests.get(self.url, headers=header_t)
        con = req.content
        soup = BeautifulSoup(con, features=parser_t[1])
        #find_tags = soup.find_all(name='title')
        #final = soup.prettify().encode('UTF-8')
        findata = [x.text for x in soup.find_all(['pubdate','title'])]
        del findata[:3] 
        return findata  
    
    def scrapenews(self,keywords=None):

        url = ('https://newsapi.org/v2/everything?'
       'language=en&'
       'q={}&'
       'from=2020-04-20&'
       'to=2020-05-10&'
       'sortBy=popularity&'
       'apiKey=8b06f370aeff4c6783d07563c1c7a6ec').format(keywords)

        response = requests.get(url)
        con = response.content
        news = json.loads(con)
        newsdata = [x['title'] + '>' + x['publishedAt'] for x in news['articles']]
        return newsdata             


    

class Socialmedia():
    
    def __init__(self, subreddit=None, limit=1, keywords=None, lang='en'):
        self.subreddit = subreddit
        self.limit = int(limit)
        self.keywords = keywords
        self.lang = lang
    
    def reddit(self):
        red = reddit.subreddit(self.subreddit)
        if self.keywords is not '':
             out = [pg.title + '>' + str(pg.created_utc) for pg in red.search(self.keywords, limit=self.limit)]
        else:
            out = [pg.title + '>' + str(pg.created_utc) for pg in red.new(limit=self.limit)]
        
        return out
    
    def twitter(self):
        twitter_list = []
        for tweet in tweepy.Cursor(twitter_api.search, q=self.keywords, lang=self.lang).items(10):
            tweet_date = datetime.datetime.strftime(tweet.created_at, '%m-%d-%Y')
            twitter_list.append(tweet.text + '>' + tweet_date)
        
        return twitter_list
           

if __name__ == "__main__":
    print("NOTHING TO SCRAPE")
    pass
