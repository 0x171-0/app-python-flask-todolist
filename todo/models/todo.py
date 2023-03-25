from todo import db

class Todo(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(length=300), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)
    done = db.Column(db.Boolean(), default=0)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))
    def __repr__(self):
        return f'Todo {self.title}'    