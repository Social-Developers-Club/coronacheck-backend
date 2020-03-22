import tweepy

class Get_tweets:

    def __init__(self, CONSUMER_KEY, CONSUMER_SECRET,ACCESS_TOKEN, ACCESS_SECRET, TWEET_ID):
        self.CONSUMER_KEY = CONSUMER_KEY
        self.CONSUMER_SECRET = CONSUMER_SECRET
        self.ACCESS_TOKEN = ACCESS_TOKEN
        self.ACCESS_SECRET = ACCESS_SECRET
        self.TWEET_ID = TWEET_ID

    def con_2_twitter(self):

        auth = tweepy.OAuthHandler(self.CONSUMER_KEY, self.CONSUMER_SECRET)
        auth.set_access_token(self.ACCESS_TOKEN, self.ACCESS_SECRET)
        api = tweepy.API(auth)
        return api

    def get_tweet(self):
        api = self.con_2_twitter()
        tweets = api.get_status(self.TWEET_ID)

        return tweets

    def json_tweet_filter(self):

        tweets = self.get_tweet()

        text = tweets.text
        created_at = tweets.created_at
        geo = tweets.geo
        coordinates = tweets.coordinates
        place = tweets.place
        retweet_count = tweets.retweet_count

        return text, created_at, geo, coordinates, place, retweet_count
