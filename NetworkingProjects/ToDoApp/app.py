from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) #Creating Flask instance

#Creating SQL database
app.config['SQLALCHEMY_DATABSE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app) # instantiating database instance as 'db'

#creating model class for notes database with id, title, and task completed flag
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)

#creating the root/home web page
@app.route('/')
def home():
    todo_list = Todo.query.all()
    return render_template("base.html", todo_list = todo_list)

#method for adding todo item using POST
@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")
    new_todo = Todo(title=title, complete=False) #creating new todo item
    db.session.add(new_todo)
    db.session.commit() # adding and committing new item to DB
    return redirect(url_for("home"))

#method for updating existing todo notes (from not complete to complete or vice versa)
@app.route("/update/<int:todo_id>")
def update(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first() #finding existing todo by primary key (ID)
    todo.complete = not todo.complete # flipping the "COMPLETED" status of todo
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()  #finding existing todo by primary key (ID)
    db.session.delete(todo)
    db.session.commit() #deleting todo and commiting db
    return redirect(url_for("home"))

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
