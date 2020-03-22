from fastapi import FastAPI

from twitter import Get_tweets

import pandas as pd

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/twitter_post/{url}")
def read_twitter(url: str, hash_tag: str =None):
    TWEET_ID = url.split(sep='/')[-1:]

    CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET = read_credentials()
    
    get_tweets = Get_tweets(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET, TWEET_ID)

    text, created_at, geo, coordinates, place, retweet_count = get_tweets.json_tweet_filter()


    return {'text': text, 'created_at': created_at}


@app.get("/classification/")
def classification_result():
    return {'label': label, 'confidence': confidence}

@app.get("/evidence/")
def classification_result():
    return {'source_id': source_id, 'source_text': source_text}

@app.get("/classification/")
def classification_result():
    return {'hash_tag': hash_tag, 'geo': geo}


def read_credentials():
    df = pd.read_csv('/Users/andang/Documents/workspace/wirvsvirus/twitter_access/twitter_access.csv')

    CONSUMER_KEY = df.CONSUMER_KEY.values[0]
    CONSUMER_SECRET = df.CONSUMER_SECRET.values[0]
    ACCESS_TOKEN = df.ACCESS_TOKEN.values[0]
    ACCESS_SECRET = df.ACCESS_SECRET.values[0]

    return CONSUMER_KEY, CONSUMER_SECRET,ACCESS_TOKEN, ACCESS_SECRET