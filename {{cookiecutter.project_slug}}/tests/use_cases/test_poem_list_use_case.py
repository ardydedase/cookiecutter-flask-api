import uuid

import pytest
from unittest import mock

from app.shared import response_object as res
from app.use_cases import poem_request_objects as req
from app.use_cases import poem_use_cases as uc


def test_poem_list_handles_generic_error():
    repo = mock.Mock()
    repo.list.side_effect = Exception('Just an error message')

    poem_list_use_case = uc.PoemListUseCase(repo)
    request_object = req.PoemListRequestObject.from_dict({})

    response_object = poem_list_use_case.execute(request_object)

    assert bool(response_object) is False
    assert response_object.value == {
        'type': res.ResponseFailure.SYSTEM_ERROR,
        'message': "Exception: Just an error message"
    }


def test_poem_list_handles_bad_request():
    repo = mock.Mock()

    poem_list_use_case = uc.PoemListUseCase(repo)
    request_object = req.PoemListRequestObject.from_dict({'filters': 5})

    response_object = poem_list_use_case.execute(request_object)

    assert bool(response_object) is False
    assert response_object.value == {
        'type': res.ResponseFailure.PARAMETERS_ERROR,
        'message': "filters: Is not iterable"
    }
