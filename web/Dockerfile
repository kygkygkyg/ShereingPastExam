FROM python:3.7
ENV PYTHONUNBUFFERED 1
COPY requirements.txt /temp/
RUN pip3 install -r /temp/requirements.txt && apt-get update && apt-get -y install vim
COPY ./ /temp/
