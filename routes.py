"""Flask routes for the sandbox runtime."""
import subprocess
import os
import shlex
import logging

from flask import Blueprint, request, jsonify, send_file
from werkzeug.utils import secure_filename

bp = Blueprint('main', __name__)


def get_safe_path(file_path: str) -> str:
    """Sanitizes the file path to ensure it stays within /app."""
    base_dir = os.path.realpath("/app")
    # Remove leading slashes to ensure path is relative
    clean_path = file_path.lstrip("/")
    full_path = os.path.realpath(os.path.join(base_dir, clean_path))

    if os.path.commonpath([base_dir, full_path]) != base_dir:
        raise ValueError("Access denied: Path must be within /app")
    
    return full_path


@bp.route("/", methods=["GET"])
def health_check():
    """A simple health check endpoint to confirm the server is running."""
    return jsonify({"status": "ok", "message": "Sandbox Runtime is active."})


@bp.route("/execute", methods=["POST"])
def execute_command():
    """
    Executes a shell command inside the sandbox and returns its output.
    Uses shlex.split for security to prevent shell injection.
    """
    try:
        data = request.get_json()
        if not data or 'command' not in data:
            return jsonify({
                "stdout": "",
                "stderr": "Missing 'command' field in request",
                "exit_code": 1
            }), 400
        
        command = data['command']
        
        # Split the command string into a list to safely pass to subprocess
        args = shlex.split(command)
        
        # Execute the command, always from the /app directory
        process = subprocess.run(
            args,
            capture_output=True,
            text=True,
            cwd="/app" 
        )
        return jsonify({
            "stdout": process.stdout,
            "stderr": process.stderr,
            "exit_code": process.returncode
        })
    except Exception as e:
        return jsonify({
            "stdout": "",
            "stderr": f"Failed to execute command: {str(e)}",
            "exit_code": 1
        })


@bp.route("/upload", methods=["POST"])
def upload_file():
    """
    Receives a file and saves it to the /app directory in the sandbox.
    """
    try:
        if 'file' not in request.files:
            return jsonify({"error": "No file part in the request"}), 400
        
        file = request.files['file']
        
        if file.filename == '':
            return jsonify({"error": "No file selected"}), 400
        
        logging.info(f"--- UPLOAD_FILE CALLED: Attempting to save '{file.filename}' ---")
        filename = secure_filename(file.filename)
        file_path = os.path.join("/app", filename)
        
        file.save(file_path)
            
        return jsonify({
            "message": f"File '{filename}' uploaded successfully",
            "path": file_path
        }), 200
    except Exception as e:
        logging.error(f"Error uploading file: {str(e)}")
        return jsonify({"error": f"Failed to upload file: {str(e)}"}), 500


@bp.route("/download/<path:filename>", methods=["GET"])
def download_file(filename):
    """
    Downloads a file from the sandbox.
    """
    try:
        import urllib.parse
        decoded_path = urllib.parse.unquote(filename)
        safe_path = get_safe_path(decoded_path)
        
        if not os.path.exists(safe_path):
            return jsonify({"error": "File not found"}), 404
        
        if not os.path.isfile(safe_path):
            return jsonify({"error": "Path is not a file"}), 400
        
        return send_file(safe_path, as_attachment=True, download_name=os.path.basename(decoded_path))
    except ValueError as e:
        return jsonify({"error": str(e)}), 403
    except Exception as e:
        logging.error(f"Error downloading file: {str(e)}")
        return jsonify({"error": f"Failed to download file: {str(e)}"}), 500


@bp.route("/list/<path:directory>", methods=["GET"])
def list_files(directory):
    """
    Lists the contents of a directory under the /app directory in the sandbox.
    """
    import urllib.parse
    decoded_path = urllib.parse.unquote(directory)
    try:
        full_path = get_safe_path(decoded_path)
    except ValueError:
        return jsonify({"message": "Access denied"}), 403

    if not os.path.isdir(full_path):
        return jsonify({"message": "Path is not a directory"}), 404
    
    try:
        entries = []
        with os.scandir(full_path) as it:
            for entry in it:
                stats = entry.stat()
                entries.append({
                    "name": entry.name,
                    "size": stats.st_size,
                    "type": "directory" if entry.is_dir() else "file",
                    "mod_time": stats.st_mtime
                })
        return jsonify(entries), 200
    except Exception as e:
        return jsonify({"message": f"List files failed: {str(e)}"}), 500


@bp.route("/exists/<path:file_path>", methods=["GET"])
def exists(file_path):
    """
    Checks if a specified file or directory exists under the /app directory in the sandbox.
    """
    import urllib.parse
    decoded_path = urllib.parse.unquote(file_path)
    try:
        full_path = get_safe_path(decoded_path)
    except ValueError:
        return jsonify({"message": "Access denied"}), 403

    return jsonify({
        "path": decoded_path,
        "exists": os.path.exists(full_path)
    }), 200
