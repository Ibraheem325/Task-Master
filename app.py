import os
from datetime import datetime, timezone

from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# SQLite by default; set DATABASE_URL (e.g. Postgres) to use another database.
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'DATABASE_URL', 'sqlite:///test.db').replace('postgres://', 'postgresql://', 1)
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    def __repr__(self):
        return '<Task %r>' % self.id


with app.app_context():
    db.create_all()


@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        task_content = request.form['content'].strip()
        if not task_content:
            return redirect('/')
        new_task = Todo(content=task_content[:200])

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except Exception:
            db.session.rollback()
            return "There was an issue adding your task"
    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html', tasks=tasks)


@app.route("/delete/<int:id>")
def delete(id):
    task_to_delete = db.get_or_404(Todo, id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except Exception:
        db.session.rollback()
        return "There was a problem deleting that task"


@app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    task = db.get_or_404(Todo, id)
    if request.method == "POST":
        content = request.form['content'].strip()
        if content:
            task.content = content[:200]

        try:
            db.session.commit()
            return redirect('/')
        except Exception:
            db.session.rollback()
            return "There was a problem updating that task"
    else:
        return render_template('update.html', task=task)


if __name__ == '__main__':
    app.run(debug=True)
