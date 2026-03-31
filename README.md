# Dark Factory E2E Pipeline Fixture

## Flask Application

This is a Flask-based sandbox runtime API for executing commands and managing files.

### Project Structure

- `main.py` - Flask application entry point
- `routes.py` - API routes and endpoints
- `requirements.in` - Python dependencies
- `tests/` - Test suite

### Running the Application

```bash
pip install -r requirements.txt
python main.py
```

The server will start on `http://0.0.0.0:8000`

### Running Tests

```bash
pytest
```

### API Endpoints

- `GET /` - Health check
- `POST /execute` - Execute shell commands
- `POST /upload` - Upload files
- `GET /download/<path>` - Download files
- `GET /list/<path>` - List directory contents
- `GET /exists/<path>` - Check if file/directory exists
