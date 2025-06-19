# Audio Sample Comparison Tool

A simple Flask-based web app for comparing audio samples.

## Setup
```bash
pip install -r requirements.txt
python run.py
```

Place your audio samples in `app/audio/sample_01/a.mp3`, `b.mp3`, etc.

Results will be saved to `app/data/results.json`.

Visit `/admin/results` to see collected data.