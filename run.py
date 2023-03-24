from todo import app
from todo.models.todo import Todo

#Checks if the run.py file has executed directly and not imported
if __name__ == '__main__':
    app.run(debug=True)