import json
import uuid

from flask import Blueprint, request, Response

from app.shared import response_object as res
from app.use_cases import poem_request_objects as req
from app.repository import poem_repo as pr
from app.use_cases import poem_use_cases as uc
from app.serializers import poem_serializer as ser


blueprint = Blueprint('poem', __name__)


@blueprint.route('/api/poem/users/<username>/poems', methods=['GET'])
def get_poems_by_user(username):

    qrystr_params = {
        'filters': {'username': username},
    }    
    
    request_object = req.PoemListRequestObject.from_dict(qrystr_params)
    repo = pr.PoemRepo()

    use_case = uc.PoemListUseCase(repo)
    response = use_case.execute(request_object)

    return Response(json.dumps(response.value, cls=ser.PoemEncoder),
                    mimetype='application/json',
                    status=res.STATUS_CODES[response.type])


@blueprint.route('/api/poem/users/<username>/poems', methods=['POST'])
def write_poem(username):
    data = request.json
    post_params = {
        'data': {
            'username': username,
            'poem_body': data['poem_body'],
        }
    }

    request_object = req.PoemCreateRequestObject.from_dict(post_params)
    repo = pr.PoemRepo()

    use_case = uc.PoemCreateUseCase(repo)
    response = use_case.execute(request_object)

    return Response(json.dumps(response.value, cls=ser.PoemEncoder),
                    mimetype='application/json',
                    status=res.STATUS_CODES[response.type])                 


@blueprint.route('/api/poem/users/<username>/poems', methods=['DELETE'])
def delete_poem(username):
    data = request.json
    post_params = {
        'data': {
            'username': username,
            'poem_id': data['poem_id'],
        }
    }

    request_object = req.PoemDeleteRequestObject.from_dict(post_params)
    repo = pr.PoemRepo()

    use_case = uc.PoemDeleteUseCase(repo)
    response = use_case.execute(request_object)

    return Response(json.dumps(response.value, cls=ser.PoemEncoder),
                    mimetype='application/json',
                    status=res.STATUS_CODES[response.type])