import json


class MessageEncoder(json.JSONEncoder):

    def default(self, o):
        try:
            to_serialize = {
                'message': str(o.message),
            }
            return to_serialize
        except AttributeError:
            return super().default(o)
