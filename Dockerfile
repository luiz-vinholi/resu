FROM python:3.8

WORKDIR /app
COPY . /app

RUN pip install pipenv
RUN pipenv install uvicorn
RUN pipenv install

EXPOSE 8000

CMD ["pipenv", "run", "start"]