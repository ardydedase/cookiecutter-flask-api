import datetime
import json
import uuid

import pytest

from app.serializers import poem_serializer as srs

def test_serialize_domain_poemo_wrong_type():
    with pytest.raises(TypeError):
        json.dumps(datetime.datetime.now(), cls=srs.PoemEncoder)
