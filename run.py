# -*- coding: UTF-8 -*-

#from flask import Flask, render_template, flash, request
#from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
#from Blueprints.get_form_task import get_form_task
#
import json

from flask import Flask, request, jsonify

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'banco.sqlite')



db = SQLAlchemy(app)
ma = Marshmallow(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(80), unique=True)
    status = db.Column(db.Boolean(120), unique=True)

    def __init__(self, username, email):
        self.task = task
        self.status = status


class TaskSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('task', 'status')


task_schema = TaskSchema()
task_schema = TaskSchema(many=True)

# Criar nova task
@app.route("/task", methods=["POST"])
def add_task():
    task = request.json['task']
    status = request.json['status']

    new_task = Task(task, status)

    db.session.add(new_task)
    db.session.commit()

    return jsonify(new_task)


# Mostrar todas task
@app.route("/task", methods=["GET"])
def get_task():
    all_task = Task.query.all()
    result = task_schema.dump(all_task)
    return jsonify(result.data)


## endpoint to get user detail by id
#@app.route("/user/<id>", methods=["GET"])
#def user_detail(id):
#    user = User.query.get(id)
#    return user_schema.jsonify(user)


## endpoint to update user
#@app.route("/user/<id>", methods=["PUT"])
#def user_update(id):
#    user = User.query.get(id)
#    username = request.json['username']
#    email = request.json['email']
#
#    user.email = email
#    user.username = username
#
#    db.session.commit()
#    return user_schema.jsonify(user)


#deletar task
@app.route("/task/<id>", methods=["DELETE"])
def task_delete(id):
    task = Task.query.get(id)
    db.session.delete(user)
    db.session.commit()

    return task_schema.jsonify(task)


if __name__ == '__main__':
    app.run(debug=True)
