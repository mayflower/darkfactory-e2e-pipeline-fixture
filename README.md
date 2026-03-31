# Todolist Web Application

A simple todolist web application built with Python and Flask.

## Features

- **List todos**: View all your todos on the main page
- **Add todos**: Create new todos with a title
- **Complete todos**: Mark todos as completed
- **Delete todos**: Remove todos from the list
- **In-memory storage**: All todos are stored in memory (resets on restart)

## Requirements

- Python 3.7+
- Flask 3.0.0
- pytest 7.4.3 (for running tests)

## Installation

1. Clone the repository or download the source code

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

## Usage

1. **Adding a todo**: Enter a title in the input field and click "Add Todo"
2. **Completing a todo**: Click the "Complete" button next to a todo to mark it as done
3. **Deleting a todo**: Click the "Delete" button to remove a todo

## Running Tests

Run the unit tests using pytest:

```bash
pytest test_app.py
```

For verbose output:

```bash
pytest test_app.py -v
```

## Project Structure

```
.
├── app.py              # Main Flask application
├── templates/          # HTML templates
│   └── index.html      # Main page template
├── test_app.py         # Unit tests
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## Implementation Details

- **Framework**: Flask web framework
- **Storage**: In-memory list (todos are not persisted)
- **Routes**:
  - `GET /` - Display all todos
  - `POST /add` - Add a new todo
  - `POST /complete/<id>` - Mark a todo as completed
  - `POST /delete/<id>` - Delete a todo
- **Testing**: Comprehensive unit tests with pytest

## Notes

- Todos are stored in memory and will be lost when the application restarts
- Each todo has a unique ID that increments automatically
- Empty or whitespace-only todo titles are rejected
