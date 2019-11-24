class ResponseSuccess(object):
    SUCCESS = 'SUCCESS'

    def __init__(self, value=None):
        self.type = self.SUCCESS
        self.value = value

    def __nonzero__(self):
        return True

    __bool__ = __nonzero__


class ResponseCreateSuccess(object):
    CREATED = 'CREATED'

    def __init__(self, value):
        self.type = self.CREATED
        self.value = value

    def __nonzero__(self):
        return True

    __bool__ = __nonzero__


class ResponseDeleteSuccess(object):
    DELETED = 'DELETED'

    def __init__(self, value):
        self.type = self.DELETED
        self.value = value

    def __nonzero__(self):
        return True

    __bool__ = __nonzero__


class ResponseFailure(object):
    """
    RESOURCE_ERROR contains all those errors that are related to the resources contained in the repository, 
    for instance when you cannot find an entry given its unique id. 
    PARAMETERS_ERROR describes all those errors that occur when the request parameters are wrong or missing. 
    SYSTEM_ERROR encompass the errors that happen in the underlying system at operating system level, such as a failure in a filesystem operation, or a network connection error while fetching data from the database.    
    """
    RESOURCE_ERROR = 'RESOURCE_ERROR'
    PARAMETERS_ERROR = 'PARAMETERS_ERROR'
    SYSTEM_ERROR = 'SYSTEM_ERROR'

    def __init__(self, type_, message):
        self.type = type_
        self.message = self._format_message(message)

    def _format_message(self, msg):
        if isinstance(msg, Exception):
            return "{}: {}".format(msg.__class__.__name__, "{}".format(msg))
        return msg

    @property
    def value(self):
        return {'type': self.type, 'message': self.message}

    def __nonzero__(self):
        return False

    __bool__ = __nonzero__

    @classmethod
    def build_resource_error(cls, message=None):
        return cls(cls.RESOURCE_ERROR, message)

    @classmethod
    def build_system_error(cls, message=None):
        return cls(cls.SYSTEM_ERROR, message)

    @classmethod
    def build_parameters_error(cls, message=None):
        return cls(cls.PARAMETERS_ERROR, message)

    @classmethod
    def build_from_invalid_request_object(cls, invalid_request_object):
        message = "\n".join(["{}: {}".format(err['parameter'], err['message'])
                             for err in invalid_request_object.errors])
        return cls.build_parameters_error(message)

STATUS_CODES = {
    ResponseSuccess.SUCCESS: 200,
    ResponseCreateSuccess.CREATED: 201,
    ResponseDeleteSuccess.DELETED: 204,
    ResponseFailure.RESOURCE_ERROR: 404,
    ResponseFailure.PARAMETERS_ERROR: 400,
    ResponseFailure.SYSTEM_ERROR: 500
}        