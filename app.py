from flask import Flask, request, jsonify
from flask_cors import CORS
from models import db, Todo

app = Flask(__name__)

import os

# use PostgreSQL in production, SQLite in development
database_url = os.environ.get('DATABASE_URL', 'sqlite://todos.db')

#Railway gives us a postgre:// URL, but SQLAlchemy needs postgresql://
if database_url.startwith('postgre://'):
    database_url = database_url.replace('postgres://', 'postgresql://', 1)

app.config['SQLALCHEMY_DATABASE_URI'] = database_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
db.init_app(app)
CORS(app)

# Create tables
with app.app_context():
    db.create_all()
    print("✅ Database tables created!")

# Routes

@app.route('/')
def home():
    return jsonify({
        'message': 'Todo API is running! 🚀',
        'endpoints': {
            'GET /todos': 'Get all todos',
            'POST /todos': 'Create new todo',
            'GET /todos/<id>': 'Get single todo',
            'PUT /todos/<id>': 'Update todo',
            'DELETE /todos/<id>': 'Delete todo',
            'GET /todos/stats': 'Get statistics'
        }
    })

@app.route('/todos', methods=['GET'])
def get_todos():
    """Get all todos, optionally filter by completion status"""
    completed = request.args.get('completed')
    
    if completed is not None:
        is_completed = completed.lower() == 'true'
        todos = Todo.query.filter_by(completed=is_completed).all()
    else:
        todos = Todo.query.all()
    
    return jsonify({
        'todos': [todo.to_dict() for todo in todos],
        'total': len(todos)
    })

@app.route('/todos', methods=['POST'])
def create_todo():
    """Create a new todo"""
    data = request.get_json()
    
    if not data or 'title' not in data:
        return jsonify({'error': 'Title is required'}), 400
    
    new_todo = Todo(
        title=data['title'],
        description=data.get('description', '')
    )
    
    db.session.add(new_todo)
    db.session.commit()
    
    return jsonify({
        'message': 'Todo created successfully',
        'todo': new_todo.to_dict()
    }), 201

@app.route('/todos/<int:id>', methods=['GET'])
def get_todo(id):
    """Get a single todo by ID"""
    todo = Todo.query.get(id)
    
    if not todo:
        return jsonify({'error': 'Todo not found'}), 404
    
    return jsonify({'todo': todo.to_dict()})

@app.route('/todos/<int:id>', methods=['PUT'])
def update_todo(id):
    """Update a todo"""
    todo = Todo.query.get(id)
    
    if not todo:
        return jsonify({'error': 'Todo not found'}), 404
    
    data = request.get_json()
    
    if 'title' in data:
        todo.title = data['title']
    if 'description' in data:
        todo.description = data['description']
    if 'completed' in data:
        todo.completed = data['completed']
    
    db.session.commit()
    
    return jsonify({
        'message': 'Todo updated successfully',
        'todo': todo.to_dict()
    })

@app.route('/todos/<int:id>', methods=['DELETE'])
def delete_todo(id):
    """Delete a todo"""
    todo = Todo.query.get(id)
    
    if not todo:
        return jsonify({'error': 'Todo not found'}), 404
    
    db.session.delete(todo)
    db.session.commit()
    
    return jsonify({'message': 'Todo deleted successfully'})

@app.route('/todos/stats', methods=['GET'])
def get_stats():
    """Get statistics about todos"""
    total = Todo.query.count()
    completed = Todo.query.filter_by(completed=True).count()
    pending = total - completed
    
    completion_rate = (completed / total * 100) if total > 0 else 0
    
    return jsonify({
        'total': total,
        'completed': completed,
        'pending': pending,
        'completion_rate': f"{completion_rate:.1f}%"
    })

# if __name__ == '__main__':
#     app.run(debug=True, port=5000)

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port = port, debug=False)
