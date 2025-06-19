import os
import json
from flask import Blueprint, render_template, request, redirect, url_for, send_from_directory
import subprocess
import sys

main = Blueprint('main', __name__)

AUDIO_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), 'audio'))
RESULTS_FILE = os.path.join(os.path.dirname(__file__), 'data', 'results.json')

# Load all sample folder names
sample_dirs = sorted([d for d in os.listdir(AUDIO_DIR) if os.path.isdir(os.path.join(AUDIO_DIR, d))])

@main.route('/')
def index():
    return redirect(url_for('main.compare', index=0))

@main.route('/compare/<int:index>')
def compare(index):
    if index >= len(sample_dirs):
        return redirect(url_for('main.done'))
    folder = sample_dirs[index]
    return render_template('index.html', index=index, folder=folder)

@main.route('/submit', methods=['POST'])
def submit():
    index = int(request.form['index'])
    selected = request.form['selected']
    folder = sample_dirs[index]

    os.makedirs(os.path.dirname(RESULTS_FILE), exist_ok=True)
    if os.path.exists(RESULTS_FILE):
        with open(RESULTS_FILE, 'r') as f:
            results = json.load(f)
    else:
        results = []

    results.append({'sample': folder, 'selected': selected})

    with open(RESULTS_FILE, 'w') as f:
        json.dump(results, f, indent=2)

    return redirect(url_for('main.compare', index=index + 1))

@main.route('/done')
def done():
    return render_template('thankyou.html')

@main.route('/admin/results')
def admin():
    script_path = os.path.join(os.path.dirname(__file__), '..', 'admin', 'visualize_results.py')
    python_exe = sys.executable
    subprocess.run([python_exe, script_path], check=True)

    if not os.path.exists(RESULTS_FILE):
        return "No results yet."

    with open(RESULTS_FILE) as f:
        results = json.load(f)

    tally = {}
    for result in results:
        key = result['sample']
        vote = result['selected']
        if key not in tally:
            tally[key] = {'a': 0, 'b': 0}
        tally[key][vote] += 1

    return render_template('results.html', tally=tally)

@main.route('/audio/<folder>/<filename>')
def serve_audio(folder, filename):
    return send_from_directory(os.path.join(AUDIO_DIR, folder), filename)
