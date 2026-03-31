"""Tests for Flask routes."""
import pytest
import json
import os
import tempfile
from io import BytesIO

import main


@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    main.app.config['TESTING'] = True
    
    with main.app.test_client() as client:
        yield client


def test_health_check(client):
    """Test the health check endpoint."""
    response = client.get('/')
    assert response.status_code == 200
    
    data = json.loads(response.data)
    assert data['status'] == 'ok'
    assert 'message' in data


def test_execute_command_success(client):
    """Test executing a successful command."""
    response = client.post('/execute',
                          data=json.dumps({'command': 'echo hello'}),
                          content_type='application/json')
    
    assert response.status_code == 200
    
    data = json.loads(response.data)
    assert 'hello' in data['stdout']
    assert data['exit_code'] == 0


def test_execute_command_missing_field(client):
    """Test executing a command with missing command field."""
    response = client.post('/execute',
                          data=json.dumps({}),
                          content_type='application/json')
    
    assert response.status_code == 400
    
    data = json.loads(response.data)
    assert 'Missing' in data['stderr']


def test_upload_file_success(client):
    """Test uploading a file."""
    data = {
        'file': (BytesIO(b'test content'), 'test.txt')
    }
    
    response = client.post('/upload',
                          data=data,
                          content_type='multipart/form-data')
    
    assert response.status_code == 200
    
    response_data = json.loads(response.data)
    assert 'uploaded successfully' in response_data['message']


def test_upload_file_no_file(client):
    """Test upload endpoint with no file."""
    response = client.post('/upload',
                          data={},
                          content_type='multipart/form-data')
    
    assert response.status_code == 400
    
    data = json.loads(response.data)
    assert 'No file part' in data['error']
