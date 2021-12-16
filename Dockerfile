FROM python:3.8

WORKDIR /home/purplecow

COPY ./requirements.txt /home/purplecow/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /home/purplecow/requirements.txt

COPY ./application /home/purplecow/