# Popcorn Cinema — Web Applications Project (Checkpoint 1)

Web application for cinema ticket booking developed for the **Web Applications** course at Universidad Carlos III de Madrid (UC3M).

---

## 📌 Milestone Overview (Checkpoint 1)

This repository contains the deliverables for **Checkpoint 1**, which focuses on:
- Preliminary design and layout of core views using **Jinja2** templates and semantic **HTML5**.
- Custom responsive **CSS3** design following a retro/vintage ticket style.
- Base application architecture with **Flask** (application factory pattern, blueprints).
- Data model definitions with **SQLAlchemy ORM** (`cinema/model.py`), prepared for database integration in subsequent milestones.
- Static demonstration data for the main views (movie catalogue, movie details, authentication placeholders).

---

## 📂 Project Structure

```text
CINEMA-PROJECT-check1_definite_shown/
├── cinema/
│   ├── __init__.py           # Flask app factory, config & extensions initialization
│   ├── main.py               # Main blueprint routes (index, movie detail, login/signup)
│   ├── model.py              # SQLAlchemy models & schema definitions
│   ├── static/
│   │   ├── cinema.css        # Custom responsive stylesheet
│   │   └── posters/          # Sample movie posters
│   └── templates/
│       ├── base.html         # Base template with common navbar, styles & layout
│       ├── main/
│       │   ├── index.html         # Home view (movies catalogue as ticket cards)
│       │   └── movie_detail.html  # Movie detail view with showtime selection
│       └── auth/
│           ├── login.html         # Sign in view
│           └── signup.html        # Sign up view
├── Makefile                  # Build & automation shortcuts (install, run, clean)
├── requirements.txt          # Python library dependencies
├── .env.example              # Example environment variables template
├── .gitignore                # Git ignore rules for virtual environments, caches, DBs
└── README.md                 # Project documentation
```

---

## 🚀 Getting Started

### 1. Prerequisites
- Python 3.10+ (tested with Python 3.12)
- Virtual environment support (`venv`)
- `make` (optional, for automation shortcuts)

### 2. Quick Start with Make

```bash
# 1. Create virtual environment and install dependencies
make install

# 2. Run development server
make run
```

Open your browser at [http://localhost:5000](http://localhost:5000) or [http://127.0.0.1:5000](http://127.0.0.1:5000).

---

### 3. Manual Setup (Without Make)

#### On macOS / Linux:
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Create .env file (if not present)
echo "SECRET_KEY=dev-secret-key" > .env
echo "SQLALCHEMY_DATABASE_URI=sqlite:///cinema.db" >> .env

# Run the Flask app
flask --debug --app=cinema run
```

#### On Windows (Command Prompt / PowerShell):
```cmd
py -3 -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
flask --debug --app=cinema run
```

---

## 🛠️ Configuration (.env)

The application loads configuration parameters from a `.env` file in the root directory:

```ini
# Flask secret key for signing session cookies
SECRET_KEY=your_secret_key_here

# Database URI (SQLite for local testing, or MariaDB/MySQL for lab servers)
SQLALCHEMY_DATABASE_URI=sqlite:///cinema.db
# Example for UC3M lab MariaDB:
# SQLALCHEMY_DATABASE_URI=mysql+pymysql://<user>:<password>@localhost/<dbname>
```

---

## 📋 Available Make Commands

- `make install`: Creates the virtual environment and installs all dependencies from `requirements.txt`.
- `make run`: Starts the Flask development server with hot-reload enabled.
- `make clean`: Cleans up Python bytecode caches (`__pycache__`) and local test databases.
- `make clean-all`: Runs `clean` and removes virtual environment directories.
- `make help`: Displays command summary.

---

## 👥 Authors

- Web Applications — UC3M (Universidad Carlos III de Madrid)
