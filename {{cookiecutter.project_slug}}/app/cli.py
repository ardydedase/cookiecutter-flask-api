import uuid
from datetime import datetime

from flask import Flask
from flask.cli import AppGroup

from app.models.poem import PoemModel

app = Flask(__name__)
dynamo_cli = AppGroup('dynamo')

# Create dynamodb poem table and populate it with sample data.
@dynamo_cli.command("create-poem-table")
def create_poem_table():
    PoemModel.create_table(read_capacity_units=1, 
        write_capacity_units=1)
    poem_id = str(uuid.uuid4().hex)
    poem = PoemModel()
    poem.poem_id = poem_id
    poem.date_posted = datetime.now()   
    poem.poem_body = "Poem Body. hello world! %s" % poem_id
    poem.user_id = 'wickedmanok'
    poem.likes = 20 
    poem.save()

    # Print out the created entries
    my_poem = PoemModel.get('wickedmanok', poem_id)
    poems = PoemModel.query('wickedmanok')
    for p in poems:
        print(p.poem_id + " : " + p.poem_body)
    return 0


# Delete dynamodb table.
@dynamo_cli.command("delete-poem-table")
def delete_dynamo_table():    
    PoemModel.delete_table()

app.cli.add_command(dynamo_cli)