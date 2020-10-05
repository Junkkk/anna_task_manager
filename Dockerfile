FROM python:3.7

COPY . /app
WORKDIR /app

RUN pip install pipenv
COPY Pipfile /app/
COPY Pipfile.lock /app/
RUN pipenv install --deploy --system

WORKDIR /app/anna_task_manager
CMD pipenv run python main.py
