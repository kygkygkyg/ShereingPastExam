FROM python:3.7
ENV PYTHONUNBUFFERED 1
COPY requirements.txt /temp/
RUN pip3 install -r /temp/requirements.txt
COPY ./ /temp/
