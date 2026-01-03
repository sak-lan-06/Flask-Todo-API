from flask_sqlalchemy import SQLAlchemy
from datetime import datetime,  timezone

db = SQLAlchemy()

class Todo(db.Model):
    __tablename__ = 'todos'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    completed = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, 
                      default=lambda: datetime.now(timezone.utc),
                      onupdate=lambda: datetime.now(timezone.utc))
    def to_dict(self):
        return{
            'id' : self.id,
            'title' : self.title,
            'description' : self.description,
            'completed' : self.completed,
            'created_at' : self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            'updated_at' : self.updated_at.strftime('%Y-%m-%d %H:%M:%S')

        }
    
    def __repr__(self):
        return f'<Todo {self.id}: {self.title}>'