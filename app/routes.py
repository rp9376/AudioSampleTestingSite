import os
import json
from flask import render_template, request, redirect, url_for, session
from app import app

AUDIO_DIR = os.path.join(app.root_path, 'audio')
DATA_FILE = os.path.join(app.root_path, 'data', 'results.json')

@app.route('/')
def index():
    session.clear()
    sample_dirs = sorted(os.listdir(AUDIO_DIR))
    session['samples'] = sample_dirs
    session['results'] = []
    return render_template('index.html', sample=sample_dirs[0], idx=0, total=len(sample_dirs))

@app.route('/compare/<int:idx>', methods=['GET', 'POST'])
def compare(idx):
    sample_dirs = session.get('samples')
    if not sample_dirs or idx >= len(sample_dirs):
        return redirect(url_for('done'))
    sample = sample_dirs[idx]
    if request.method == 'POST':
        selected = request.form.get('selected')
        results = session.get('results', [])
        results.append({'sample': sample, 'selected': selected})
        session['results'] = results
        if idx + 1 < len(sample_dirs):
            return redirect(url_for('compare', idx=idx+1))
        else:
            return redirect(url_for('done'))
    return render_template('index.html', sample=sample, idx=idx, total=len(sample_dirs))

@app.route('/done', methods=['GET', 'POST'])
def done():
    if request.method == 'POST':
        results = session.get('results', [])
        os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r', encoding='utf-8') as f:
                all_results = json.load(f)
        else:
            all_results = []
        all_results.append(results)
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(all_results, f, indent=2)
        session.clear()
        return render_template('thankyou.html')
    return render_template('done.html')

@app.route('/admin/results')
def admin_results():
    return render_template('results.html')
