from todo import app, db
from flask import render_template, request, flash, redirect, url_for
from todo.form import AddTodoForm, LoginForm, RegisterForm
from todo.models.todo import Todo
from todo.models.user import User
from flask_login import login_user, logout_user, login_required, current_user
import json

@app.route('/')
@app.route('/home')
@app.route('/todo')
@login_required
def home():
    todos = Todo.query.all()
    if len(todos) == 0:
        with open('todo/fixture/todo.json', 'r') as f:
            todos = json.load(f)
    return render_template('home.html', todos=todos)
    
@app.route('/todo/add',methods=['GET', 'POST'])
@login_required
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


@app.route('/user/login', methods=['POST', 'GET'])
def login_page():
    form = LoginForm()
    # validate submit
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password_correction(attempted_password=form.password.data):
            login_user(user)
            flash(f'Success! You are logged in as: {user.email}', category='success')
            return redirect(url_for('home'))    
        else:
            flash('Username and password are not match! Please try again', category='danger')
    return render_template('login.html', form=form)

@app.route('/user/register', methods=['POST', 'GET'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(email=form.email.data, password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        flash(f"Account created successfully! You are now logged in as {user_to_create.email}", category='success')
        return redirect(url_for('home'))
    if form.errors != {}: #If there are not errors from the validations
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category='danger')

    return render_template('register.html', form=form)

    pass

@app.route('/user/logout', methods=['GET'])
def logout_page():
    logout_user()
    flash("You have been logged out!", category='info')
    return redirect(url_for("home"))