import requests
import json
import os
import uvicorn
import pandas as pd

from fastapi import FastAPI
from twitter import Get_tweets

CONSUMER_KEY = os.getenv("CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_SECRET = os.getenv("ACCESS_SECRET")

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/twitter_post/{id_}")
def read_twitter(id_: str):

    #TWEET_ID = url #url.split(sep='/')[-1:]
    tweet_id = dict({'id':id_})

    get_tweets = Get_tweets(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET, id_)

    text, created_at, geo, coordinates, place, retweet_count = get_tweets.json_tweet_filter()

    result = model_request(json.dumps(dict({'text':text})))

    # TODO: add locations as extra functions
    print(tweet_id)
    response_body = response(tweet_id, result)

    return json.dumps(response_body)


"""def read_credentials():
    df = pd.read_csv('/Users/andang/Documents/workspace/wirvsvirus/twitter_access/twitter_access.csv')

    CONSUMER_KEY = df.CONSUMER_KEY.values[0]
    CONSUMER_SECRET = df.CONSUMER_SECRET.values[0]
    ACCESS_TOKEN = df.ACCESS_TOKEN.values[0]
    ACCESS_SECRET = df.ACCESS_SECRET.values[0]

    return CONSUMER_KEY, CONSUMER_SECRET,ACCESS_TOKEN, ACCESS_SECRET"""

def model_request(payload):

    headers = {'Content-type': 'application/json'}
    r = requests.post('http://185.244.195.79:8000/api/analyze', data=payload, headers=headers)
    data = r.json()

    return data

def response(tweet_id, result):
    # TODO: real location
    test_dict = {"derived": {
      "locations": [
        {
          "country": "Deutschland",
          "country_code": "DE",
          "locality": "Deutschland",
          "region": "Bundesland",
          "sub_region": "Landkreis",
          "full_name": "Heinsberg, Kreis Heinsberg, Nordrhein-Westfalen, 52525, Deutschland",
          "geo": {
            "coordinates": [
              51.0654268,
              6.0984461
            ],
            "type": "point"
          }
        }
      ]
    }
    }
    tweet_id.update(result)
    tweet_id.update(test_dict)
    return tweet_id


if __name__ == "__main__":
    port = os.getenv("PORT", 8000)
    host = os.getenv("HOST", "0.0.0.0")
    uvicorn.run(app, host=host, port=port)