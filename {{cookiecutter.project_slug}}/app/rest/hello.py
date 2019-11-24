import json
import uuid

from flask import Blueprint, Response

from app.shared import response_object as res
from app.use_cases import message_request_objects as req
from app.use_cases import message_use_cases as uc
from app.serializers import message_serializer as ser


blueprint = Blueprint('hello', __name__)

# Use this for No DB option
@blueprint.route('/api/hello/<username>', methods=['GET'])
def hello(username):

    qrystr_params = {
        'params': {'username': username},
    }    
    
    request_object = req.MessageRequestObject.from_dict(qrystr_params)

    use_case = uc.MessageUseCase()
    response = use_case.execute(request_object)

    return Response(json.dumps(response.value, cls=ser.MessageEncoder),
                    mimetype='application/json',
                    status=res.STATUS_CODES[response.type])
