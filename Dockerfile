# pull official base image
FROM python:3.11.3-slim-buster

RUN apt-get update && apt-get install -y 
#postgresql-client-13

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app.py .
COPY database.py .
COPY model.py .
COPY cars.csv .
COPY store.csv .

EXPOSE 5000

CMD [ "python", "app.py"]