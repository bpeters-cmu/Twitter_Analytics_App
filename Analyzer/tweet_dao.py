from .models import TweetModel


def insert_tweet(status):

    tweet = TweetModel(user_name=status.user.name, tweet_text=status.text,
                       user_location=status.user.location, verified_user=status.user.verified)
    tweet.save()
