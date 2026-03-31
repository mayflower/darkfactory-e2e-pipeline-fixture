#!/usr/bin/env python
"""
Simple verification script to check the Flask app structure.
"""

import os
import sys

def verify_structure():
    """Verify all required files exist."""
    required_files = [
        'app.py',
        'test_app.py',
        'requirements.txt',
        'README.md',
        'templates/index.html'
    ]
    
    missing = []
    for file in required_files:
        if not os.path.exists(file):
            missing.append(file)
    
    if missing:
        print("❌ Missing files:")
        for f in missing:
            print(f"  - {f}")
        return False
    
    print("✅ All required files exist")
    return True

def verify_imports():
    """Verify the app can be imported."""
    try:
        import app
        print("✅ app.py imports successfully")
        print(f"  - Routes: {[str(rule) for rule in app.app.url_map.iter_rules()]}")
        return True
    except Exception as e:
        print(f"❌ Failed to import app.py: {e}")
        return False

def verify_requirements():
    """Verify requirements.txt has correct dependencies."""
    try:
        with open('requirements.txt', 'r') as f:
            content = f.read()
            if 'Flask' in content and 'pytest' in content:
                print("✅ requirements.txt has Flask and pytest")
                return True
            else:
                print("❌ requirements.txt missing Flask or pytest")
                return False
    except Exception as e:
        print(f"❌ Failed to read requirements.txt: {e}")
        return False

if __name__ == '__main__':
    print("Flask Todolist App Structure Verification")
    print("=" * 50)
    
    checks = [
        verify_structure(),
        verify_requirements(),
        verify_imports()
    ]
    
    print("=" * 50)
    if all(checks):
        print("✅ All checks passed!")
        sys.exit(0)
    else:
        print("❌ Some checks failed")
        sys.exit(1)
