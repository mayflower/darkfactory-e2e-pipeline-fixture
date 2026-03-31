"""
Unit tests for the Flask Todo List Application
"""

import pytest
from app import app, todos, next_id


@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False
    
    with app.test_client() as client:
        yield client
    
    # Clean up after each test
    todos.clear()
    import app as app_module
    app_module.next_id = 1


def test_index_empty(client):
    """Test index route with no todos."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'No todos yet' in response.data
    assert b'Todo List' in response.data


def test_add_todo(client):
    """Test adding a new todo."""
    response = client.post('/add', data={'title': 'Test Todo'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Test Todo' in response.data
    assert b'Todo added successfully' in response.data
    assert len(todos) == 1
    assert todos[0]['title'] == 'Test Todo'
    assert todos[0]['completed'] is False


def test_add_empty_todo(client):
    """Test that adding an empty todo shows an error."""
    response = client.post('/add', data={'title': ''}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Todo title cannot be empty' in response.data
    assert len(todos) == 0


def test_add_whitespace_todo(client):
    """Test that adding a whitespace-only todo shows an error."""
    response = client.post('/add', data={'title': '   '}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Todo title cannot be empty' in response.data
    assert len(todos) == 0


def test_add_multiple_todos(client):
    """Test adding multiple todos."""
    client.post('/add', data={'title': 'First Todo'})
    client.post('/add', data={'title': 'Second Todo'})
    client.post('/add', data={'title': 'Third Todo'})
    
    response = client.get('/')
    assert response.status_code == 200
    assert b'First Todo' in response.data
    assert b'Second Todo' in response.data
    assert b'Third Todo' in response.data
    assert len(todos) == 3


def test_complete_todo(client):
    """Test completing a todo."""
    # Add a todo first
    client.post('/add', data={'title': 'Todo to Complete'})
    todo_id = todos[0]['id']
    
    # Complete it
    response = client.post(f'/complete/{todo_id}', follow_redirects=True)
    assert response.status_code == 200
    assert b'Todo marked as completed' in response.data
    assert todos[0]['completed'] is True


def test_complete_nonexistent_todo(client):
    """Test completing a todo that doesn't exist."""
    response = client.post('/complete/999', follow_redirects=True)
    assert response.status_code == 200
    assert b'Todo not found' in response.data


def test_delete_todo(client):
    """Test deleting a todo."""
    # Add a todo first
    client.post('/add', data={'title': 'Todo to Delete'})
    todo_id = todos[0]['id']
    
    # Delete it
    response = client.post(f'/delete/{todo_id}', follow_redirects=True)
    assert response.status_code == 200
    assert b'Todo deleted successfully' in response.data
    assert len(todos) == 0


def test_delete_nonexistent_todo(client):
    """Test deleting a todo that doesn't exist."""
    response = client.post('/delete/999', follow_redirects=True)
    assert response.status_code == 200
    assert b'Todo not found' in response.data


def test_delete_middle_todo(client):
    """Test deleting a todo from the middle of the list."""
    # Add multiple todos
    client.post('/add', data={'title': 'First'})
    client.post('/add', data={'title': 'Second'})
    client.post('/add', data={'title': 'Third'})
    
    middle_id = todos[1]['id']
    
    # Delete the middle one
    client.post(f'/delete/{middle_id}')
    
    assert len(todos) == 2
    assert todos[0]['title'] == 'First'
    assert todos[1]['title'] == 'Third'


def test_todo_id_increment(client):
    """Test that todo IDs increment correctly."""
    client.post('/add', data={'title': 'First'})
    first_id = todos[0]['id']
    
    client.post('/add', data={'title': 'Second'})
    second_id = todos[1]['id']
    
    assert second_id == first_id + 1


def test_workflow_add_complete_delete(client):
    """Test a complete workflow: add, complete, then delete."""
    # Add a todo
    client.post('/add', data={'title': 'Workflow Test'})
    assert len(todos) == 1
    assert todos[0]['completed'] is False
    
    # Complete it
    todo_id = todos[0]['id']
    client.post(f'/complete/{todo_id}')
    assert todos[0]['completed'] is True
    
    # Delete it
    client.post(f'/delete/{todo_id}')
    assert len(todos) == 0


def test_index_shows_completed_status(client):
    """Test that the index page correctly shows completed todos."""
    # Add and complete a todo
    client.post('/add', data={'title': 'Completed Todo'})
    todo_id = todos[0]['id']
    client.post(f'/complete/{todo_id}')
    
    # Check the response shows it as completed
    response = client.get('/')
    assert response.status_code == 200
    assert b'Completed Todo' in response.data
    assert b'completed' in response.data


def test_multiple_operations(client):
    """Test multiple operations on different todos."""
    # Add 3 todos
    client.post('/add', data={'title': 'Todo 1'})
    client.post('/add', data={'title': 'Todo 2'})
    client.post('/add', data={'title': 'Todo 3'})
    
    # Complete the first one
    client.post(f'/complete/{todos[0]["id"]}')
    
    # Delete the second one
    client.post(f'/delete/{todos[1]["id"]}')
    
    # Should have 2 todos left
    assert len(todos) == 2
    assert todos[0]['title'] == 'Todo 1'
    assert todos[0]['completed'] is True
    assert todos[1]['title'] == 'Todo 3'
    assert todos[1]['completed'] is False
