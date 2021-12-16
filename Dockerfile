FROM python:3.8

WORKDIR /home/purplecow

COPY ./requirements.txt /home/purplecow/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /home/purplecow/requirements.txt

COPY ./application /home/purplecow/application

CMD [ "uvicorn", "application.services.items:app", "--host", "0.0.0.0", "--port", "3000" ]