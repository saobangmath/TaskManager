from  flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# application setup
app = Flask(__name__)
# databases setup
app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///notes.db'
db = SQLAlchemy(app)
methods = ["POST" , "GET"]
# create a model
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.String(200), nullable = False)
    completed = db.Column(db.Integer, default = 0)
    date_created = db.Column(db.DateTime, default = datetime.utcnow)
    def __repr__(self):
        return '<Task {}'.format(self.id)

@app.route('/', methods = methods)
def index():
    if (request.method == 'POST'):
        task_content = request.form["content"]
        if (task_content != ""): # not empty!
            new_task = Todo(content = task_content)
            try:
                db.session.add(new_task)
                db.session.commit()
                return redirect("/")
            except:
                return "There was issues adding your task!"
        else:
            return "The task must not be empty!"
    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template("index.html", tasks = tasks)
@app.route("/delete/<int:id>")
def delete(id):
    deleted_task = Todo.query.get_or_404(id)
    try:
        db.session.delete(deleted_task)
        db.session.commit()
        return redirect("/")
    except:
        return "There is a problem in task deletion!"

@app.route("/update/<int:id>", methods = methods)
def update(id):
    task = Todo.query.get_or_404(id)
    if (request.method == "POST"):
        task.content = request.form["content"]
        try:
            db.session.commit()
            return redirect("/")
        except:
            return "Issues in updating the database"
    else:
        return render_template("update.html", task = task)

if __name__ == "__main__":
    db.create_all()
    print(db)
    app.run(debug = True)