FROM python:3

EXPOSE 5000 80
ADD . /code
WORKDIR /code

COPY . .

RUN pip3 install --no-cache-dir -r requirements.txt

RUN echo "from run import db; db.create_all()" | python3 
RUN python3 run.py
