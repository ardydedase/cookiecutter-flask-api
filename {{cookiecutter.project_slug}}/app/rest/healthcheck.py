from app.models.poem import PoemModel

def dynamodb_available():
    poem = PoemModel()
    poem.dumps()
    return True, "DynamoDB ok"