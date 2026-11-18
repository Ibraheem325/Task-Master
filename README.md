# Task Master

A simple to-do list web app built with Flask and SQL. You can add tasks, edit them and delete
them. Tasks are stored in a database table and shown in a list with the date each was added.

I made it in 2024 to learn the basics of Flask and of working with a database (CRUD:
create, read, update, delete).

**Live demo:** https://task-master-96jv.onrender.com
(free hosting, so the first load after a period of inactivity can take up to about a minute)

## What it uses

- **Flask** for routes and Jinja2 templates
- **SQL via Flask-SQLAlchemy**: one `Todo` table (task text, creation date). It runs on SQLite by
  default and can use Postgres by setting `DATABASE_URL`.
- **HTML and CSS** for the page

Originally written with Python 3.11; the deployed version runs on Python 3.12.

## Project structure

```
app.py               routes and the Todo table
templates/           list page and edit page
static/main.css      styling
```

## Run locally

```bash
git clone https://github.com/Ibraheem325/Task-Master.git
cd Task-Master
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python app.py             # open http://127.0.0.1:5000
```
