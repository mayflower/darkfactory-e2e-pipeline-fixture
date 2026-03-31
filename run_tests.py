#!/usr/bin/env python3
"""
Script to verify installation and run tests
"""
import sys
import os

# Add current directory to path
sys.path.insert(0, '/')

print("=" * 70)
print("STEP 1: CHECKING IMPORTS")
print("=" * 70)

# Try to import Flask
try:
    import flask
    print(f"✓ Flask is installed (version {flask.__version__})")
    flask_installed = True
except ImportError as e:
    print(f"✗ Flask is NOT installed: {e}")
    flask_installed = False

# Try to import pytest
try:
    import pytest
    print(f"✓ pytest is installed (version {pytest.__version__})")
    pytest_installed = True
except ImportError as e:
    print(f"✗ pytest is NOT installed: {e}")
    pytest_installed = False

if not flask_installed or not pytest_installed:
    print("\n" + "=" * 70)
    print("STEP 2: INSTALLING DEPENDENCIES")
    print("=" * 70)
    import subprocess
    result = subprocess.run(
        [sys.executable, "-m", "pip", "install", "-r", "/requirements.txt"],
        capture_output=True,
        text=True
    )
    print(result.stdout)
    if result.stderr:
        print("STDERR:", result.stderr)
    
    # Try imports again
    try:
        import flask
        import pytest
        print("\n✓ Dependencies installed successfully!")
    except ImportError as e:
        print(f"\n✗ Still cannot import dependencies: {e}")
        sys.exit(1)
else:
    print("\n✓ All dependencies are already installed")

# Now run the tests
print("\n" + "=" * 70)
print("STEP 3: RUNNING UNIT TESTS")
print("=" * 70)
print()

# Import pytest and run tests
import pytest
exit_code = pytest.main(['/test_app.py', '-v', '--tb=short'])

print("\n" + "=" * 70)
print("TEST EXECUTION COMPLETE")
print("=" * 70)

sys.exit(exit_code)
