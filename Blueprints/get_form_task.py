from flask import Blueprint, Flask, render_template, flash, request, jsonify
from model import Todo
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import json


get_form_task = Blueprint("get_form_task",__name__)

@get_form_task.route("/")
def index():

    class ReusableForm(Form):
        name = TextField('Name:', validators=[validators.required()])

    form = ReusableForm(request.form)

    print (form.errors)
    if request.method == 'POST':
        name=request.form['name']
        print (name)

        if form.validate():
            # Save the comment here.
            flash('Hello ' + name)
        else:
            flash('All the form fields are required.')

    return render_template('index.html', form=form)

@get_form_task.route("/task/",methods=["POST"])
def add_task():
    try:
        data = request.get_json()
        t = Todo()

        t.task = 'Teste task'
        t.user = 'Elias'
        t.status = False
        t.save()
        for key in data.keys():

            #setattr(t,key,data['{}'.format(key)])

            t.task = data['{}'.format(key)]
            t.user = key
        u.save()
        return jsonify({"message":"Task cadastrado com sucesso!"})
    except Exception as e:
        return jsonify({"message":"Falhou ao cadastrar: {}".format(e)})
