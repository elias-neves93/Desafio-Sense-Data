# -*- coding: UTF-8 -*-

from flask import Flask, request, jsonify, render_template, flash
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
    status = db.Column(db.String(120), unique=True)

    def __init__(self, task, status):
        self.task = task
        self.status = status


class TaskSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('task', 'status')


task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)


@app.route("/")
def index(name=None):


    return render_template('index.html', name=name)

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
    result = tasks_schema.dump(all_task)
    return jsonify(result.data)

#deletar task
@app.route("/task/<id>", methods=["DELETE"])
def task_delete(id):
    task = Task.query.get(id)
    db.session.delete(task)
    db.session.commit()

    return task_schema.jsonify(task)


if __name__ == '__main__':
    app.run(debug=True)
