# Database HUD

A real-time, Git-aware PostgreSQL schema visualizer for developers.

Database HUD connects to your local PostgreSQL database and generates an interactive visual map of your entire schema — every table, every column, every foreign key relationship rendered as a graph you can explore. Click any table to instantly see its blast radius — every connected table highlights so you can understand the full impact of a change before you make it.

It also hooks into Git. When you switch branches, Database HUD detects the change automatically so your schema view always reflects your current code environment.

> This is the Python prototype. The production version (Tabloid) will be rebuilt in Rust + Tauri as a native desktop app for Mac, Windows, and Linux.

---

## What it does

- Connects to a local PostgreSQL database and fetches the full schema
- Renders tables as nodes and foreign key relationships as edges on an interactive canvas
- Click any table to highlight its connected tables (blast radius visualization)
- Watches your `.git/HEAD` file and detects branch switches in real time
- Persists your canvas layout to a local SQLite database so your schema map remembers where you left it

---

## Tech stack

- Python 3.12
- psycopg3 — PostgreSQL driver
- NetworkX — graph layout algorithms (Kamada-Kawai)
- PyQt6 — desktop GUI and canvas rendering
- SQLite — local app state persistence
- watchdog — filesystem watching for git branch detection
- GitPython — reading git repository state

---

## Project structure

```
database-hud/
├── tabloid/
│   ├── db/
│   │   ├── connector.py      # PostgreSQL connection management
│   │   └── inspector.py      # Schema fetching via information_schema
│   ├── engine/
│   │   └── layout.py         # NetworkX graph construction and layout
│   ├── storage/
│   │   └── local_db.py       # SQLite persistence (layouts, connections, snapshots)
│   ├── git/
│   │   └── watcher.py        # Git branch detection via .git/HEAD watching
│   ├── ui/
│   │   ├── main_window.py    # PyQt6 main window
│   │   └── canvas.py         # Clickable node with blast radius interaction
│   └── main.py               # App entry point
├── tests/
├── data/
└── requirements.txt
```

---

## Getting started

### Prerequisites

- Python 3.12
- PostgreSQL (local or Docker)
- WSL2/Ubuntu or Linux/macOS

### Setup

```bash
git clone https://github.com/NoMo-101/database-hud.git
cd database-hud
python3.12 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Configure your database

Open `tabloid/ui/main_window.py` and update the connection details in `load_schema()`:

```python
conn = DBConnector("127.0.0.1", 5432, "your_user", "your_password", "your_dbname")
```

### Run

```bash
python3 -m tabloid.main
```

---

## How it works

**Schema fetching** — queries PostgreSQL's `information_schema` to extract tables, columns, and foreign key relationships without touching your actual data.

**Graph layout** — builds a NetworkX graph where tables are nodes and foreign keys are edges. Runs the Kamada-Kawai layout algorithm to place nodes so connected tables are near each other and edge crossings are minimized.

**Blast radius** — each table node is a clickable `QGraphicsRectItem`. On click, it uses the NetworkX graph to find all neighboring tables and highlights them in yellow. The clicked table highlights in blue. Everything else resets to white.

**Git watching** — a background `watchdog` observer watches `.git/HEAD` for file system events. When the file changes (branch switch), `GitPython` reads the new branch name. Handles `on_modified`, `on_created`, and `on_moved` events to cover all the ways git writes to HEAD across different platforms.

**Local persistence** — SQLite stores layout positions, connection profiles, and schema snapshots. Layout positions are upserted on every drag so the canvas state survives app restarts.

---

## Roadmap

This prototype proves the core concepts. The production version (Tabloid) will:

- Rebuild the engine in Rust for performance
- Wrap in Tauri for native cross-platform distribution (Mac, Windows, Linux)
- Add real-time WAL streaming to pulse tables as your backend code runs queries against them
- Add transaction time travel to visualize what your database looked like at any point in history
- Add schema diffing between git branches so you can see exactly what changed
- Support MySQL, SQLite, and pgvector in addition to PostgreSQL

---

## Author

Johnny Noah Moore — [github.com/NoMo-101](https://github.com/NoMo-101) — [linkedin.com/in/johnny-noah-moore](https://www.linkedin.com/in/johnny-moore/)
