import pytest
import uuid

from app.repository import poem_repo

def test_repository_list_with_filters_unknown_filter():
    repo = poem_repo.PoemRepo()

    with pytest.raises(ValueError):
        repo.list(filters={'nousername': 'wickedmanok'})


def test_repository_create_with_data_unknown_data():
    repo = poem_repo.PoemRepo()

    with pytest.raises(ValueError):
        repo.create(data={'nousername': 'wickedmanok'})        
