FROM python:3.10

COPY . /app

WORKDIR /app

RUN pip install nltk

CMD ["python3", "cb.py"]


