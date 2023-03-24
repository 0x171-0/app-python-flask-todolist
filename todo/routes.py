from todo import app, db
from flask import render_template, request, flash, redirect, url_for
from todo.form import AddTodoForm
from todo.models.todo import Todo
import json


@app.route('/')
@app.route('/todo')
def home():
    todos = Todo.query.all()
    if len(todos) == 0:
        with open('todo/fixture/todo.json', 'r') as f:
            todos = json.load(f)
    return render_template('home.html', todos=todos)
    
@app.route('/todo/add',methods=['GET', 'POST'])
def addTodo():
    form = AddTodoForm()
    if form.validate_on_submit():
        todo_to_create = Todo(title=form.title.data, description=form.description.data)
        db.session.add(todo_to_create)
        db.session.commit()
        flash(f"Todo {todo_to_create.title} created successfully!", category='success')
        return redirect(url_for('addTodo'))
    if form.errors != {}: #If there are not errors from the validations
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category='danger')
    return render_template('addTodo.html', form=form)