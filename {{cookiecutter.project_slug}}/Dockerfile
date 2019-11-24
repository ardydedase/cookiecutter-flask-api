FROM python:3.6

RUN mkdir -p /flask-service
WORKDIR /flask-service

# Copy files
COPY ./pytest.ini ./
COPY ./requirements.txt ./
COPY ./setup.cfg ./

# Copy folders
COPY ./app ./app
COPY ./requirements ./requirements
COPY ./tests ./tests

# Install packages
RUN pip install -r requirements.txt

# Initialise default value for args
ARG FLASK_ENV='docker'
ARG AWS_ACCESS_KEY_ID='your-key-here'
ARG AWS_SECRET_ACCESS_KEY='your-key-here'
ARG AWS_REGION='ap-southeast-1'

# Assign environment variable values
ENV FLASK_APP="app/main.py" 
ENV FLASK_DEBUG=1 
ENV FLASK_ENV=${FLASK_ENV} 
# AWS Keys should be passed as environment variables
ENV AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID} 
ENV AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY}
ENV AWS_REGION=${AWS_REGION}

# Run flask app
EXPOSE 5000
CMD ["flask", "run", "-h", "0.0.0.0"]