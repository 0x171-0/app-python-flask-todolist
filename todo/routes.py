from todo import app
from flask import render_template, request
import json
import os

@app.route('/')
@app.route('/todo')
def home():
    print(os.getcwd())
    with open('todo/fixture/todo.json', 'r') as f:
        data = json.load(f)
        print(data)
    return render_template('home.html', todos=data)
    
@app.route('/todo/add',methods=['GET', 'POST'])
def addTodo():
    if request.method == 'GET':
        return render_template('addTodo.html')
    if request.method == 'POST':
        pass