# -*- coding: utf-8 -*-
"""Data_download.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nuL_-jLVwKAVi2RvM2TmbBDMg2deqUWA
"""

!pip install snscrape

import snscrape.modules.twitter as sntwitter
from tqdm.notebook import tqdm
import pandas as pd

Scraper= sntwitter.TwitterSearchScraper("words you want to search for") #exaple #python , internship,intern etc.
tweets=[]
n_tweets= 'Number of tweet you want to get in your dataset '
for i, tweet in tqdm(enumerate(Scraper.get_items()), total=n_tweets):
  data=[tweet.content]
  tweets.append(data)
  if i>n_tweets:
    break
#Creating a Data frame for easy accessibility
#using pandas
Tweets_df=pd.DataFrame(tweets,columns=['Content'])

print(Tweets_df[:5])

Tweets_df.to_csv("Twitter_data.csv",index=False)

