# Flask Todo List Application

A simple, clean todo list web application built with Python and Flask.

## Features

- ✅ Add new todos
- ✅ Mark todos as completed
- ✅ Delete todos
- ✅ In-memory storage (no database required)
- ✅ Clean, responsive UI
- ✅ Comprehensive unit tests

## Requirements

- Python 3.11+
- Flask 3.0.0
- pytest 7.4.3 (for testing)

## Installation

1. Clone this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

Start the Flask development server:

```bash
python app.py
```

The application will be available at `http://localhost:5000`

## Running Tests

Run the unit tests with pytest:

```bash
pytest test_app.py -v
```

## Project Structure

```
.
├── app.py              # Main Flask application
├── templates/
│   └── index.html      # HTML template for the UI
├── test_app.py         # Unit tests
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## Usage

1. **Add a Todo**: Enter a task in the input field and click "Add Todo"
2. **Complete a Todo**: Click the "Complete" button next to a todo to mark it as done
3. **Delete a Todo**: Click the "Delete" button to remove a todo

## API Routes

- `GET /` - Display all todos
- `POST /add` - Add a new todo
- `POST /complete/<id>` - Mark a todo as completed
- `POST /delete/<id>` - Delete a todo

## Notes

- This application uses in-memory storage, so all todos will be lost when the server restarts
- No authentication or user management is implemented
- The secret key should be changed in production environments
