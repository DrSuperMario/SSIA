# SSIA

## Stock Scraber and Social Analyzer

Scrapes stock related news articles from different sources and analyzes the impact of a tweet or a title

## Social

Right now I am using Twitter API and Reddit API (Praw) to get the social data

```
reddit = praw.Reddit(client_id='<<Id goes here>>',
                    client_secret='<<secret goes here>>',
                    user_agent='SSAT',
                    username='<<user goes here>>',
                    password='<<passwd goes here>>')
#Twitter API keys 
twitter_consumer_key='<<Twitter goes here>>'
twitter_consumer_secret='<<Secret here>>'

```

## XML

There is alsoe a possibility to get data from news outlets by RSS feeds

## News API

I implanted News API as well to check the latest headlines and analyze them

```
url = ('https://newsapi.org/v2/everything?'
       'language=en&'
       'q={}&'
       'from=2020-04-20&'
       'to=2020-05-10&'
       'sortBy=popularity&'
       'apiKey=<<API Key here>>').format(keywords)
```

# IMPORTANT

You have to get keys for all the different APIs to use it eg. Twitter, Reddit, and NEWS API In the future I would like to implement this without using 3rd party APIs but right now it was much quicker.

Also I would like to add a deep learning curve for predicting the stock prices from social headlines
