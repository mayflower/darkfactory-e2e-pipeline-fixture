"""
Flask Todo List Application

A simple todo list web application with in-memory storage.
"""

from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'dev-secret-key-change-in-production'

# In-memory storage for todos
todos = []
next_id = 1


@app.route('/')
def index():
    """Display all todos."""
    return render_template('index.html', todos=todos)


@app.route('/add', methods=['POST'])
def add_todo():
    """Add a new todo item."""
    global next_id
    
    title = request.form.get('title', '').strip()
    
    if not title:
        flash('Todo title cannot be empty', 'error')
        return redirect(url_for('index'))
    
    todo = {
        'id': next_id,
        'title': title,
        'completed': False
    }
    
    todos.append(todo)
    next_id += 1
    
    flash('Todo added successfully', 'success')
    return redirect(url_for('index'))


@app.route('/complete/<int:todo_id>', methods=['POST'])
def complete_todo(todo_id):
    """Mark a todo as completed."""
    todo = next((t for t in todos if t['id'] == todo_id), None)
    
    if todo:
        todo['completed'] = True
        flash('Todo marked as completed', 'success')
    else:
        flash('Todo not found', 'error')
    
    return redirect(url_for('index'))


@app.route('/delete/<int:todo_id>', methods=['POST'])
def delete_todo(todo_id):
    """Delete a todo item."""
    global todos
    
    initial_length = len(todos)
    todos = [t for t in todos if t['id'] != todo_id]
    
    if len(todos) < initial_length:
        flash('Todo deleted successfully', 'success')
    else:
        flash('Todo not found', 'error')
    
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
