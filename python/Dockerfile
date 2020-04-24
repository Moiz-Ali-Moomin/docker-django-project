FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /mycode
WORKDIR /mycode
ADD requirements.txt /mycode/
RUN pip install -r requirements.txt
ADD . /mycode/
