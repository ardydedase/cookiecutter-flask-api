import os
import shutil

print("Path to project: ", os.getcwd())  # prints /absolute/path/to/{{cookiecutter.project_slug}}

def remove(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)

def move(filepath, targetpath):
    if os.path.isfile(filepath):
        os.rename(filepath, targetpath)
    elif os.path.isdir(filepath):
        shutil.move(filepath, targetpath)

database = '{{cookiecutter.database}}'

# files and folders
main_file = os.path.join(os.getcwd(), 'app', 'main.py')
main_dynamodb_file = os.path.join(os.getcwd(), 'app', 'main_dynamodb.py')
poem_rest_file = os.path.join(os.getcwd(), 'app/rest', 'poem.py')
healthcheck_rest_file = os.path.join(os.getcwd(), 'app/rest', 'healthcheck.py')
poem_use_case_file = os.path.join(os.getcwd(), 'app/use_cases', 'poem_use_cases.py')
poem_request_object_file = os.path.join(os.getcwd(), 'app/use_cases', 'poem_request_objects.py')
poem_serializer_file = os.path.join(os.getcwd(), 'app/serializers', 'poem_serializer.py')
models_dir = os.path.join(os.getcwd(), 'app', 'models') 
repository_dir = os.path.join(os.getcwd(), 'app', 'repository') 
docker_compose_file = os.path.join(os.getcwd(), 'docker-compose.yml') 
docker_compose_dynamodb_file = os.path.join(os.getcwd(), 'docker-compose.dynamodb.yml') 

# Remove DB related files if No DB option is selected
if database != "DynamoDB":
    remove(main_dynamodb_file)
    remove(poem_rest_file)
    remove(healthcheck_rest_file)
    remove(poem_use_case_file)
    remove(poem_request_object_file)
    remove(repository_dir)
    remove(models_dir)
    remove(docker_compose_dynamodb_file)

# Use DynamoDB files only
if database == "DynamoDB":
    remove(main_file)
    move(main_dynamodb_file, main_file)

    remove(docker_compose_file)
    move(docker_compose_dynamodb_file, docker_compose_file)


message = """
+------------+         +-----------+        +------------+      +-----------+
|            |         |           |        |            |      |           |
|  Rest API  +-------->+  Use Case +------->+ Repository +----->+   Model   |
|            |         |           |        |            |      |           |
+------------+         +-----------+        +------------+      +-----------+

Run the following in your command line:

1. cd {{cookiecutter.project_slug}}
2. docker-compose up

Refer to the docs: https://github.com/ardydedase/cookiecutter-flask-api
"""

print(message)