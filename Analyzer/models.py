import uuid
from cassandra.cqlengine import columns
from django_cassandra_engine.models import DjangoCassandraModel


class TweetModel(DjangoCassandraModel):
    tweet_id = columns.UUID(primary_key=True, default=uuid.uuid4)
    user_name = columns.Text(index=True)
    tweet_text = columns.Text(required=True)
    user_location = columns.Text(required=False)
    verified_user = columns.Boolean(required=False)


class Topic(DjangoCassandraModel):
    topic = columns.Text(primary_key=True)
