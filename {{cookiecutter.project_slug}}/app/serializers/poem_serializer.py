import json


class PoemEncoder(json.JSONEncoder):

    def default(self, o):
        try:
            to_serialize = {
                'poem_id': str(o.poem_id),
                'poem_body': str(o.poem_body),
                'user_id': str(o.user_id),
                'likes': str(o.likes),
            }
            return to_serialize
        except AttributeError:
            return super().default(o)
