# Database HUD

Database HUD is a real-time, Git-aware PostgreSQL schema visualizer for developers.

It generates an interactive graph of your database schema where tables, columns, and relationships are visualized as a navigable network. Selecting a table highlights its full dependency graph (“blast radius”), helping developers understand the impact of schema changes instantly.

The tool is Git-aware and automatically updates the visualization when switching branches, keeping the schema context aligned with your codebase.

> This implementation focuses on validating core concepts such as schema visualization, graph-based exploration, and Git-aware workflows. 

> This project represents the Database HUD module of a larger in-progress developer platform (codename: Tabloid), focused on database observability and schema intelligence.

Future iterations will focus on performance, scalability, and cross-platform support.

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

Configure your database connection by updating the connection settings in the application.

---

## Key Features

- Interactive schema visualization of PostgreSQL databases
- Graph-based representation of tables and relationships
- Blast radius highlighting for dependency exploration
- Git-aware context switching between branches
- Persistent layout storage for consistent workspace state

---

## Roadmap

This implementation validates the core interaction model and architecture. Future work will focus on:

- Improving performance and scalability of the graph engine
- Enhancing real-time feedback during database interactions
- Expanding support for additional database systems
- Refining developer workflows around schema exploration and change awareness

---

## Author

Johnny Noah Moore — [github.com/NoMo-101](https://github.com/NoMo-101) — [linkedin.com/in/johnny-noah-moore](https://www.linkedin.com/in/johnny-moore/)
