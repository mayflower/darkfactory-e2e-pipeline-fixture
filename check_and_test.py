#!/usr/bin/env python3
"""
Script to check dependencies and run tests
"""
import sys
import subprocess
import importlib.util

def check_package(package_name):
    """Check if a package is installed."""
    spec = importlib.util.find_spec(package_name)
    return spec is not None

def run_command(cmd):
    """Run a shell command and return the result."""
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            capture_output=True,
            text=True,
            timeout=30
        )
        return result.returncode, result.stdout, result.stderr
    except subprocess.TimeoutExpired:
        return 1, "", "Command timed out"
    except Exception as e:
        return 1, "", str(e)

def main():
    print("=" * 60)
    print("CHECKING FLASK TODO APP INSTALLATION")
    print("=" * 60)
    
    # Check Flask
    print("\n1. Checking Flask installation...")
    flask_installed = check_package('flask')
    print(f"   Flask installed: {flask_installed}")
    
    # Check pytest
    print("\n2. Checking pytest installation...")
    pytest_installed = check_package('pytest')
    print(f"   pytest installed: {pytest_installed}")
    
    # If not installed, try to install
    if not flask_installed or not pytest_installed:
        print("\n3. Installing dependencies from requirements.txt...")
        returncode, stdout, stderr = run_command("pip install -r /requirements.txt")
        if returncode == 0:
            print("   ✓ Dependencies installed successfully")
            if stdout:
                print(f"   Output: {stdout[:200]}")
        else:
            print(f"   ✗ Installation failed!")
            print(f"   Error: {stderr}")
            return 1
    else:
        print("\n3. All dependencies already installed ✓")
    
    # Run the tests
    print("\n" + "=" * 60)
    print("RUNNING UNIT TESTS")
    print("=" * 60)
    
    returncode, stdout, stderr = run_command("pytest /test_app.py -v")
    
    print(stdout)
    if stderr:
        print("STDERR:")
        print(stderr)
    
    print("\n" + "=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    
    if returncode == 0:
        print("✓ All tests passed!")
    else:
        print("✗ Some tests failed or there were errors")
    
    return returncode

if __name__ == "__main__":
    sys.exit(main())
