# Decisions Log - DWD-48

## Task: Set up Flask project structure and dependencies

### Key Decisions:

1. **Framework Migration: FastAPI → Flask**
   - **Decision**: Complete conversion from FastAPI to Flask
   - **Rationale**: Task title explicitly states "Set up Flask project structure"
   - **Impact**: All endpoints converted, async/await removed, Pydantic models replaced with Flask request handling

2. **Project Structure: Flat vs Package**
   - **Decision**: Used flat structure (routes.py in root) instead of nested package
   - **Rationale**: 
     - Simpler for small project
     - Fewer import complications
     - Matches existing single-file pattern
   - **Alternative considered**: `app/` package with `__init__.py` and multiple modules

3. **Dependency Management**
   - **Decision**: Updated `requirements.in` with Flask, werkzeug, pytest
   - **Rationale**: Minimal dependencies for Flask web server and testing
   - **Note**: Did not regenerate `requirements.txt` with hashes - left for build pipeline

4. **Blueprint Pattern**
   - **Decision**: Used Flask Blueprint for routes
   - **Rationale**: Best practice for Flask, allows modular route organization
   - **Implementation**: Single blueprint 'main' registered in main.py

5. **Test Structure**
   - **Decision**: Created pytest-based test suite
   - **Rationale**: pytest is industry standard, more feature-rich than unittest
   - **Coverage**: Basic tests for main endpoints (health, execute, upload)

6. **File Operations Security**
   - **Decision**: Kept existing `get_safe_path()` function
   - **Rationale**: Maintains security boundary preventing path traversal attacks
   - **Note**: Additional `secure_filename()` added for upload safety

7. **Error Handling**
   - **Decision**: Return JSON error responses with appropriate HTTP status codes
   - **Rationale**: Maintains API contract from FastAPI version
   - **Pattern**: Try/except blocks with jsonify() responses

### Technical Considerations:

- **Port**: Kept port 8000 for consistency
- **Working Directory**: Commands execute from `/app` (runtime container path)
- **Logging**: Maintained existing logging for debugging
- **URL Encoding**: Added urllib.parse.unquote() for path parameters
