class Tweet(object):

    def __init__(self, tweet_id, user_name, text, location, verified_user):
        self.tweet_id = tweet_id
        self.user_name = user_name
        self.text = text
        self.location = location
        self.verified_user = verified_user

    @staticmethod
    def to_map(tweet):
        tweet_dict = dict(Id=tweet.tweet_id, UserName=tweet.user_name, Text=tweet.text, Location=tweet.location,
                          Verified=tweet.verified_user)

        return tweet_dict
