FROM python:3.8-slim-buster

WORKDIR /usr/src/app
COPY . /usr/src/app

RUN python -m pip install --upgrade pip && python -m pip install -r requirements.txt

CMD ["/usr/src/app/main.py"]
ENTRYPOINT ["python"]