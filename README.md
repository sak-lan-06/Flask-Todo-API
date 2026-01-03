# Todo API

A simple REST API for managing your daily tasks. I built this while learning Flask and backend development!

# What it does

This API lets you:

- Create, view, update, and delete todos

- Mark todos as complete

- See progress stats

- I built it to learn how RESTful APIs work and how to store and manage data in a database.

# Why I built this

I wanted to understand how backend systems work and how apps like Todoist.
Through this project, I learned:

- How to design a REST API

- Working with databases using SQLAlchemy

- Handling CRUD operations

- Deploying apps to production

# Tech I used

Flask – Python web framework (simple and beginner-friendly)

SQLAlchemy – Database ORM for handling data

SQLite – Local database (planning to switch to PostgreSQL in production)

Postman – To test all the API endpoints

# Getting it running

If you want to try this project locally, here’s how:

1. Clone the repo
git clone https://github.com/sak-lan-06/Flask-Todo-API.git
cd todo-api

2. Set up a virtual environment
    - python -m venv venv
# On Windows
    - venv\Scripts\activate
# On Mac/Linux
    - source venv/bin/activate

3. Install dependencies
    - pip install -r requirements.txt

4. Run the API
    - python app.py


Visit http://localhost:5000 in your browser or API tool, and it should be running!

## How to use it
Get all todos
GET http://localhost:5000/todos

## Add a new todo
POST http://localhost:5000/todos
Content-Type: application/json

{
  "title": "Buy groceries",
  "description": "Milk, bread, eggs"
}

Mark a todo as done
PUT http://localhost:5000/todos/1
Content-Type: application/json

{
  "completed": true
}

## Delete a todo
DELETE http://localhost:5000/todos/1

See your stats
GET http://localhost:5000/todos/stats


Shows total todos, completed todos, and completion percentage.

# All endpoints
Todos:
- GET /todos – Get all todos
- GET /todos?completed=true – Show only finished todos
- GET /todos?completed=false – Show pending todos

Manage todos:
- POST /todos – Add a new todo
- GET /todos/1 – View a specific todo
- PUT /todos/1 – Update a todo
- DELETE /todos/1 – Delete a todo

Stats:
GET /todos/stats – View progress stats

## File structure
todo-api/
├── app.py          # API routes and logic
├── models.py       # Database structure for todos
├── requirements.txt# Python packages needed
├── .gitignore      # Files/folders Git should ignore
└── README.md       # This guide

## Testing
I used Postman to test everything:
- Created todos with missing fields to check validation
- Tried updating non-existent todos to check error handling
- Filtered todos by completion status

## Deployment

Planning to deploy on Railway. Live link will be added soon!


## Issues I ran into🐛
- Virtual environment wouldn’t activate on Windows → Fixed by running PowerShell as admin and changing execution policy

- Database wasn’t saving data → Forgot db.session.commit() after adding items

- CORS errors connecting frontend → Added flask-cors package

## What I learned🎓

- How REST APIs actually work

- Database design and relationships

- Error handling and validation

- Differences between development and production

- Deploying an app to the web

- Hardest part? Database sessions and commits—spent hours debugging until I remembered db.session.commit() 😅

## What’s next
- Add user accounts
- Add due dates and reminders
- Add categories or tags
- Maybe build a simple React frontend

# Contributing

I’m still learning, so if you spot anything or have suggestions, feel free to open an issue or PR!

# About me

I’m learning web development and building projects to improve my skills.

GitHub:sak-lan-06 https://github.com/sak-lan-06/Flask-Todo-API.git
LinkedIn: Sakshi Lanke (www.linkedin.com/in/sakshi-lanke-947374235)



Built with lots of coffee and debugging ☕🐛



This is my first real backend project, so the code might not be perfect. 
But it works, and I learned a ton building it!😅