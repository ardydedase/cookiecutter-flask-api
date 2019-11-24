from app.shared import use_case as uc
from app.shared import response_object as res
from app.shared.response_object import \
    ResponseSuccess,\
    ResponseCreateSuccess,\
    ResponseDeleteSuccess
from app.repository.poem_repo import PoemRepo


class PoemListUseCase(uc.UseCase):

    # return a list of poems
    def __init__(self, repo: PoemRepo):
        self.repo: PoemRepo = repo

    def process_request(self, request_object) -> ResponseSuccess:
        domain_usecase: list = self.repo.list(filters=request_object.filters)
        return res.ResponseSuccess(domain_usecase)

class PoemCreateUseCase(uc.UseCase):

    def __init__(self, repo: PoemRepo):
        self.repo: PoemRepo = repo

    def process_request(self, request_object) -> ResponseCreateSuccess:
        domain_usecase: dict = self.repo.create(data=request_object.data)
        return res.ResponseCreateSuccess(domain_usecase)

class PoemDeleteUseCase(uc.UseCase):

    def __init__(self, repo: PoemRepo):
        self.repo: PoemRepo = repo

    def process_request(self, request_object) -> ResponseDeleteSuccess:
        domain_usecase: dict = self.repo.delete(data=request_object.data)
        return res.ResponseDeleteSuccess(domain_usecase)        
