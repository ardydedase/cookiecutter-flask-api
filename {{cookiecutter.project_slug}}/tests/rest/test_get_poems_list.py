import json
import uuid

from unittest import mock
from app.shared import response_object as res

poem1_dict = {
    'poem_id': '00000000000000001',
    'poem_body': 'poem 1',
    'user_id': str(uuid.uuid4()),
    'likes': '3',
}

poems = [poem1_dict]


@mock.patch('app.use_cases.poem_use_cases.PoemListUseCase')
def test_get(mock_use_case, client):
    mock_use_case().execute.return_value = res.ResponseSuccess(poems)

    http_response = client.get('/api/poem/users/wickedmanok/poems')

    print("json_loads:")
    print(json.loads(http_response.data.decode('UTF-8')))

    assert json.loads(http_response.data.decode('UTF-8')) == [poem1_dict]
    assert http_response.status_code == 200
    assert http_response.mimetype == 'application/json'


@mock.patch('app.use_cases.poem_use_cases.PoemListUseCase')
def test_get_failed_response(mock_use_case, client):
    mock_use_case().execute.return_value = \
        res.ResponseFailure.build_system_error('test message')

    http_response = client.get('/api/poem/users/wickedmanok/poems')

    assert json.loads(http_response.data.decode('UTF-8')) == \
        {'type': 'SYSTEM_ERROR', 'message': 'test message'}
    assert http_response.status_code == 500
    assert http_response.mimetype == 'application/json' 


@mock.patch(
    'app.use_cases.poem_use_cases.PoemListUseCase')
def test_request_object_initialisation_and_use_with_filters(
        mock_use_case, client):
    mock_use_case().execute.return_value = res.ResponseSuccess([])

    internal_request_object = mock.Mock()

    request_object_class = \
        'app.use_cases.poem_request_objects.PoemListRequestObject'
    with mock.patch(request_object_class) as mock_request_object:
        mock_request_object.from_dict.return_value = internal_request_object
        client.get('/api/poem/users/wickedmanok/poems')

    mock_request_object.from_dict.assert_called_with(
        {'filters': {'username': 'wickedmanok'}}
    )
    mock_use_case().execute.assert_called_with(internal_request_object)       


