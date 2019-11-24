import collections
from app.shared.request_objects import InvalidRequestObject, ValidRequestObject


class PoemListRequestObject(ValidRequestObject):

    def __init__(self, filters=None):
        self.filters = filters

    @classmethod
    def from_dict(cls, adict):
        invalid_req = InvalidRequestObject()

        if 'filters' in adict and not isinstance(adict['filters'], collections.Mapping):
            invalid_req.add_error('filters', 'Is not iterable')

        if invalid_req.has_errors():
            return invalid_req

        return PoemListRequestObject(filters=adict.get('filters', None))


class PoemCreateRequestObject(ValidRequestObject):

    def __init__(self, data=None):
        self.data = data

    @classmethod
    def from_dict(cls, adict)        :
        invalid_req = InvalidRequestObject()

        if 'data' in adict and not isinstance(adict['data'], collections.Mapping):
            invalid_req.add_error('data', 'Is not iterable')

        if 'poem_body' not in adict['data']:
            invalid_req.add_error('poem_body', 'Is not set')

        if invalid_req.has_errors():
            return invalid_req

        return PoemCreateRequestObject(data=adict.get('data', None))


class PoemDeleteRequestObject(ValidRequestObject):

    def __init__(self, data=None):
        self.data = data

    @classmethod
    def from_dict(cls, adict)        :
        invalid_req = InvalidRequestObject()

        if 'data' in adict and not isinstance(adict['data'], collections.Mapping):
            invalid_req.add_error('data', 'Is not iterable')

        if 'poem_id' not in adict['data']:
            invalid_req.add_error('poem_id', 'Is not set')

        if invalid_req.has_errors():
            return invalid_req

        return PoemDeleteRequestObject(data=adict.get('data', None))