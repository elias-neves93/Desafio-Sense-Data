# -*- coding: UTF-8 -*-

from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField


app = Flask(__name__)

class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])

@app.route("/")
def index():

    form = ReusableForm(request.form)

    print (form.errors)
    if request.method == 'POST':
        name=request.form['name']
        print (name)

        if form.validate():
            # Save the comment here.
            flash('Hello ' + name)
        else:
            flash('All the form fields are required. ')

    return render_template('index.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)
