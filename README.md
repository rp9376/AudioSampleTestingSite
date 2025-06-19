# Audio Sample Comparison Tool

A modern Flask-based web app for comparing audio samples, collecting user preferences, and visualizing results.

---

## Features
- **Audio A/B Comparison:** Users listen to two audio samples per round and select their preference.
- **Result Collection:** Votes are saved to a JSON file for later analysis.
- **Admin Dashboard:** View live voting results in a styled table and as a bar chart.
- **Clear Results:** Admins can reset all votes with a single click.
- **Live Visualization:** Results chart is regenerated every time the admin page is loaded.
- **Docker Support:** Run and develop the app in a container with live code reloading.

---

## Project Structure

```
AudioSampleTestingSite/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── audio/           # Place your sample folders here (sample_01, sample_02, ...)
│   ├── data/
│   │   └── results.json # Voting results
│   ├── static/
│   │   └── styles.css   # Custom CSS
│   └── templates/
│       ├── index.html   # Main voting page
│       ├── results.html # Admin results page
│       ├── thankyou.html# Thank you page
│       └── done.html    # (Optional, not used)
├── admin/
│   └── visualize_results.py # Script to generate results chart
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── run.py
└── README.md
```

---

## Setup (Local)

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
2. **Run the app:**
   ```bash
   python run.py
   ```
3. **Open your browser:**
   Visit [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## Setup (Docker, with Live Editing)

1. **Build and run with Docker Compose:**
   ```bash
   docker-compose up
   ```
2. **Edit code locally:**
   Changes are reflected instantly in the running container.
3. **Stop the app:**
   Press `Ctrl+C` in the terminal, or run:
   ```bash
   docker-compose down
   ```

---

## Usage

- **Add audio samples:**
  - Place your audio files as `a.mp3` and `b.mp3` in folders like `app/audio/sample_01/`, `app/audio/sample_02/`, etc.
- **Voting:**
  - Users are presented with pairs of audio samples and select which one they prefer.
- **Results:**
  - Admins can view results at `/admin/results`.
  - The page shows a table and a live-updating bar chart.
  - Use the "Clear Results" button to reset all votes.

---

## File/Folder Explanations

- `app/routes.py`: Main Flask routes, including voting, results, and audio serving.
- `app/templates/`: HTML templates for all pages.
- `app/static/`: Static files (CSS, generated chart image).
- `app/data/results.json`: Stores all voting results.
- `admin/visualize_results.py`: Generates the bar chart for results.
- `Dockerfile` & `docker-compose.yml`: For containerized development with live code reload.
- `Microsoft/`: PowerShell history/config (ignored by git).

---

## Development Notes
- **Live reload:** Flask runs in development mode for instant feedback.
- **Results chart:** Always up-to-date; regenerated on every admin page load.
- **Security:** Do not use this setup in production without further hardening.

---

## License
MIT License (or specify your own)

---

## Credits
- Built with [Flask](https://flask.palletsprojects.com/)
- Visualization by [matplotlib](https://matplotlib.org/)

---

For questions or contributions, open an issue or pull request!