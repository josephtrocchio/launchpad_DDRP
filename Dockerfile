FROM python:3.9

#Set enviroment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#Set working directory
WORKDIR /code

#Install dependecies
COPY requirements.txt /code/
RUN pip3 install -r requirements.txt

#Copy project
COPY . /code