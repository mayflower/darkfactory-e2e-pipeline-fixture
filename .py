"""
Flask todolist web application.
Provides routes for managing todos with in-memory storage.
"""

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for todos
todos = []
next_id = 1


@app.route('/')
def index():
    """Display all todos."""
    return render_template('index.html', todos=todos)


@app.route('/add', methods=['POST'])
def add_todo():
    """Add a new todo."""
    global next_id
    title = request.form.get('title', '').strip()
    if title:
        todo = {
            'id': next_id,
            'title': title,
            'completed': False
        }
        todos.append(todo)
        next_id += 1
    return redirect(url_for('index'))


@app.route('/complete/<int:todo_id>', methods=['POST'])
def complete_todo(todo_id):
    """Mark a todo as completed."""
    for todo in todos:
        if todo['id'] == todo_id:
            todo['completed'] = True
            break
    return redirect(url_for('index'))


@app.route('/delete/<int:todo_id>', methods=['POST'])
def delete_todo(todo_id):
    """Delete a todo."""
    global todos
    todos = [todo for todo in todos if todo['id'] != todo_id]
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
