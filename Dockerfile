FROM python:3

NETWORK:BRIGDE
EXPOSE 5000
ADD . /code
WORKDIR /code

COPY . .

RUN pip3 install --no-cache-dir -r requirements.txt

RUN echo "from run import db; db.create_all()" | python3 && python3 run.py


