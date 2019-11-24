import uuid

from datetime import datetime
from app.models.poem import PoemModel


class PoemRepo:

    def list(self, filters: dict = None) -> list:
        username: str = filters.get('username', None)
        if username is None:
            raise ValueError('missing username')
        poems: list = []
        for poem in PoemModel.query(username):
            poems.append({
                'poem_id': poem.poem_id,
                'poem_body': poem.poem_body,
                'user_id': poem.user_id,
                'likes': poem.likes,
            })

        return poems

    
    def create(self, data: dict = None) -> dict:
        username: str = data.get('username', None)
        if username is None:
            raise ValueError('missing username')
        
        poem: PoemModel = PoemModel(username, str(uuid.uuid4().hex))
        poem.poem_body = data['poem_body']
        poem.date_posted = datetime.now()
        poem.save()

        return {"message": "Poem created"}

    
    def delete(self, data: dict = None) -> dict:
        username: str = data.get('username', None)
        poem_id: str = data.get('poem_id', None)

        if username is None:
            raise ValueError('missing username')
        if poem_id is None:
            raise ValueError('missing poem_id')
        
        poem: PoemModel = PoemModel(username, data['poem_id'])
        poem.delete()

        return {"message": "Poem deleted"}        