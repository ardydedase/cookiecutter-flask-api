from app.shared import use_case as uc
from app.shared import response_object as res
from app.shared.response_object import ResponseSuccess

class MessageUseCase(uc.UseCase):

    def process_request(self, request_object) -> ResponseSuccess:
        # simple use case that returns a message
        domain_usecase: dict = {"message": "hello %s" % request_object.params['username']}
        return res.ResponseSuccess(domain_usecase)
