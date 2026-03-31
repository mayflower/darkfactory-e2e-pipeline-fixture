"""
Unit tests for the todolist Flask application.
"""

import pytest
from app import app, todos, next_id


@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


@pytest.fixture(autouse=True)
def reset_todos():
    """Reset todos and next_id before each test."""
    global todos, next_id
    import app as app_module
    app_module.todos.clear()
    app_module.next_id = 1
    yield
    app_module.todos.clear()
    app_module.next_id = 1


def test_index_empty(client):
    """Test index page with no todos."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'No todos yet' in response.data


def test_add_todo(client):
    """Test adding a new todo."""
    response = client.post('/add', data={'title': 'Test Todo'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Test Todo' in response.data
    
    # Verify todo was added to storage
    from app import todos
    assert len(todos) == 1
    assert todos[0]['title'] == 'Test Todo'
    assert todos[0]['completed'] is False


def test_add_empty_todo(client):
    """Test adding a todo with empty title."""
    response = client.post('/add', data={'title': '   '}, follow_redirects=True)
    assert response.status_code == 200
    
    # Verify no todo was added
    from app import todos
    assert len(todos) == 0


def test_add_multiple_todos(client):
    """Test adding multiple todos."""
    client.post('/add', data={'title': 'First Todo'})
    client.post('/add', data={'title': 'Second Todo'})
    client.post('/add', data={'title': 'Third Todo'})
    
    from app import todos
    assert len(todos) == 3
    assert todos[0]['title'] == 'First Todo'
    assert todos[1]['title'] == 'Second Todo'
    assert todos[2]['title'] == 'Third Todo'


def test_complete_todo(client):
    """Test completing a todo."""
    # Add a todo first
    client.post('/add', data={'title': 'Test Todo'})
    
    from app import todos
    todo_id = todos[0]['id']
    
    # Complete the todo
    response = client.post(f'/complete/{todo_id}', follow_redirects=True)
    assert response.status_code == 200
    
    # Verify todo is marked as completed
    assert todos[0]['completed'] is True


def test_complete_nonexistent_todo(client):
    """Test completing a todo that doesn't exist."""
    response = client.post('/complete/999', follow_redirects=True)
    assert response.status_code == 200
    
    # Should not raise an error, just redirect


def test_delete_todo(client):
    """Test deleting a todo."""
    # Add a todo first
    client.post('/add', data={'title': 'Test Todo'})
    
    from app import todos
    todo_id = todos[0]['id']
    
    # Delete the todo
    response = client.post(f'/delete/{todo_id}', follow_redirects=True)
    assert response.status_code == 200
    
    # Verify todo was deleted
    assert len(todos) == 0


def test_delete_nonexistent_todo(client):
    """Test deleting a todo that doesn't exist."""
    response = client.post('/delete/999', follow_redirects=True)
    assert response.status_code == 200
    
    # Should not raise an error, just redirect


def test_delete_with_multiple_todos(client):
    """Test deleting a specific todo when multiple exist."""
    # Add multiple todos
    client.post('/add', data={'title': 'First Todo'})
    client.post('/add', data={'title': 'Second Todo'})
    client.post('/add', data={'title': 'Third Todo'})
    
    from app import todos
    second_todo_id = todos[1]['id']
    
    # Delete the second todo
    client.post(f'/delete/{second_todo_id}')
    
    # Verify only the second todo was deleted
    assert len(todos) == 2
    assert todos[0]['title'] == 'First Todo'
    assert todos[1]['title'] == 'Third Todo'


def test_todo_ids_are_unique(client):
    """Test that each todo gets a unique ID."""
    client.post('/add', data={'title': 'First Todo'})
    client.post('/add', data={'title': 'Second Todo'})
    client.post('/add', data={'title': 'Third Todo'})
    
    from app import todos
    ids = [todo['id'] for todo in todos]
    
    # All IDs should be unique
    assert len(ids) == len(set(ids))
    
    # IDs should be sequential
    assert ids == [1, 2, 3]


def test_workflow_add_complete_delete(client):
    """Test a complete workflow: add, complete, then delete."""
    # Add a todo
    response = client.post('/add', data={'title': 'Workflow Test'}, follow_redirects=True)
    assert b'Workflow Test' in response.data
    
    from app import todos
    todo_id = todos[0]['id']
    
    # Complete it
    client.post(f'/complete/{todo_id}')
    assert todos[0]['completed'] is True
    
    # Delete it
    client.post(f'/delete/{todo_id}')
    assert len(todos) == 0
