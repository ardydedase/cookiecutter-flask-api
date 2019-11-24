from app.use_cases import poem_request_objects as req


def test_build_poem_list_request_object_without_parameters():
    request_object = req.PoemListRequestObject()

    assert request_object.filters is None
    assert bool(request_object) is True


def test_build_file_list_request_object_from_empty_dict():
    request_object = req.PoemListRequestObject.from_dict({})

    assert request_object.filters is None
    assert bool(request_object) is True


def test_build_poem_list_request_object_with_empty_filters():
    request_object = req.PoemListRequestObject(filters={})

    assert request_object.filters == {}
    assert bool(request_object) is True


def test_build_poem_list_request_object_from_dict_with_empty_filters():
    request_object = req.PoemListRequestObject.from_dict({'filters': {}})

    assert request_object.filters == {}
    assert bool(request_object) is True


def test_build_poem_list_request_object_with_filters():
    request_object = req.PoemListRequestObject(filters={'a': 1, 'b': 2})

    assert request_object.filters == {'a': 1, 'b': 2}
    assert bool(request_object) is True


def test_build_poem_list_request_object_from_dict_with_filters():
    request_object = req.PoemListRequestObject.from_dict({'filters': {'a': 1, 'b': 2}})

    assert request_object.filters == {'a': 1, 'b': 2}
    assert bool(request_object) is True


def test_build_poem_list_request_object_from_dict_with_invalid_filters():
    request_object = req.PoemListRequestObject.from_dict({'filters': 5})

    assert request_object.has_errors()
    assert request_object.errors[0]['parameter'] == 'filters'
    assert bool(request_object) is False   