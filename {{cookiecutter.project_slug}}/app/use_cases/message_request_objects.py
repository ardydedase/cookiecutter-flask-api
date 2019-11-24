import collections
from app.shared.request_objects import InvalidRequestObject, ValidRequestObject


class MessageRequestObject(ValidRequestObject):

    def __init__(self, params=None):
        self.params = params

    @classmethod
    def from_dict(cls, adict):
        invalid_req = InvalidRequestObject()

        if 'params' in adict and not isinstance(adict['params'], collections.Mapping):
            invalid_req.add_error('params', 'Is not iterable')

        if invalid_req.has_errors():
            return invalid_req

        return MessageRequestObject(params=adict.get('params', None))
