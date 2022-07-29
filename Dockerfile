FROM python:3.10-slim-bullseye

WORKDIR /code
ADD requirements.txt ./
RUN pip install -r requirements.txt

ADD . .
CMD ["python3", "./main.py"]