from .tweet import Tweet
from django.core.cache import cache


class TweetDAO(object):

    @staticmethod
    def insert_tweet(tweet):
        tweet_map = Tweet.to_map(tweet)
        cache.set(tweet.tweet_id, tweet_map)

    @staticmethod
    def get_tweet(tweet_id):
        return cache.get(tweet_id)

