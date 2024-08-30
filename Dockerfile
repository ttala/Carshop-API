# pull official base image
FROM python:3.11.3-slim-buster

RUN apt-get update
#postgresql-client-13

WORKDIR /carshop

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY carshop.py .
COPY model.py .
COPY cars.csv .
COPY store.csv .

EXPOSE 5000

CMD [ "python", "carshop.py"]