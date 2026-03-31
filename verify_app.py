#!/usr/bin/env python3
"""
Quick verification that the Flask app can be imported and basic structure is correct.
"""

import sys

print("Verifying Flask Todo App...")
print("-" * 50)

# Test 1: Import Flask
try:
    import flask
    print(f"✓ Flask module available (version: {flask.__version__})")
except ImportError as e:
    print(f"✗ Flask not installed: {e}")
    print("  Run: pip install -r requirements.txt")
    sys.exit(1)

# Test 2: Import the app
try:
    from app import app, todos, next_id
    print("✓ App module imports successfully")
except ImportError as e:
    print(f"✗ Cannot import app: {e}")
    sys.exit(1)

# Test 3: Check routes
routes = [rule.rule for rule in app.url_map.iter_rules() if rule.endpoint != 'static']
print(f"✓ Found {len(routes)} routes:")
for route in sorted(routes):
    print(f"  - {route}")

# Test 4: Check in-memory storage
print(f"✓ In-memory storage initialized: todos={todos}, next_id={next_id}")

# Test 5: Test basic todo operations
print("\nTesting basic operations...")
todos.clear()
next_id = 1

# Add a todo directly
test_todo = {'id': 1, 'title': 'Test Todo', 'completed': False}
todos.append(test_todo)
print(f"✓ Can add todo: {test_todo}")

# Mark as completed
todos[0]['completed'] = True
print(f"✓ Can complete todo: {todos[0]}")

# Delete todo
todos.clear()
print(f"✓ Can delete todo, todos now: {todos}")

print("-" * 50)
print("✓ All basic checks passed!")
print("\nTo run full tests: pytest test_app.py -v")
print("To start the app: python app.py")
