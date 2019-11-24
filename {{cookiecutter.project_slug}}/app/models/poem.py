import os
from app.config import get_env_config

from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, UTCDateTimeAttribute, NumberAttribute


class PoemModel(Model):
    """
    DynamoDB Poem Table
    """
    class Meta:
        table_name: str = "poem"
        # replace this with production hostname when going live.
        flask_env: str = os.environ.get('FLASK_ENV', 'test')
        if flask_env in ['development', 'docker']:
            env_config: str = get_env_config(flask_env)
            host: str = env_config.DYNAMODB_HOST
        aws_access_key_id: str = os.environ.get('AWS_ACCESS_KEY_ID', '')
        aws_secret_access_key: str = os.environ.get('AWS_SECRET_ACCESS_KEY', '')
        region: str = os.environ.get('AWS_REGION', 'ap-southeast-1')
    poem_id: str = UnicodeAttribute(range_key=True)
    date_posted: str = UTCDateTimeAttribute()
    poem_body: str = UnicodeAttribute()
    user_id: str = UnicodeAttribute(hash_key=True)
    likes: int = NumberAttribute(default=0)
