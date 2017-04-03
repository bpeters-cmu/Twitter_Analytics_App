import logging
import tweet_dao
import tweepy
from tweepy.api import API
from kafka import KafkaProducer


class TwitterAccess(object):

    CONSUMER_KEY = '03pXI5BPKQWodwfkRvlAd2tFD'
    CONSUMER_SECRET = 'UCzpOaUZYeXHieaXgPkBKk7kCriz3w8OGZ9MJAXegPcaI7Ij0X'

    ACCESS_TOKEN = '826516692087996416-nvoIh1WMVuTWFmY1M1MnVdaEQfu7Wxt'
    ACCESS_TOKEN_SECRET = '6JJBhRoH97hYE0t6wVCnCsUzRUd2dGV3EA7vAqYJ6ndZi'

    @staticmethod
    def get_stream(topic):
        auth = tweepy.OAuthHandler(TwitterAccess.CONSUMER_KEY, TwitterAccess.CONSUMER_SECRET)
        auth.set_access_token(TwitterAccess.ACCESS_TOKEN, TwitterAccess.ACCESS_TOKEN_SECRET)

        api = tweepy.API(auth)
        stream_listener = MyStreamListener(topic=topic)

        my_stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
        my_stream.filter(track=[topic], async=True)


class MyStreamListener(tweepy.StreamListener):
    def __init__(self, topic, api=None):
        self.api = api or API()
        self.topic = topic
        self.producer = KafkaProducer(bootstrap_servers='localhost:9092')

        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def on_status(self, status):
        tweet_dao.insert_tweet(status)
        if status.user.location is not None:
            self.logger.debug('location: {}'.format(status.user.location))
            self.producer.send(self.topic, status.user.location.encode())
        self.logger.debug(status.user.location)

    def on_error(self, status_code):
        if status_code == 420:
            return False
