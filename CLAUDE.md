# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the development server (port 5001)
python app.py

# Run tests
pytest

# Run a specific test file
pytest tests/test_auth.py

# Run a specific test
pytest tests/test_auth.py::test_register
```

## Architecture

This is **Spendly**, a Flask expense-tracking web app backed by SQLite. It is structured as a step-by-step student exercise — many routes and the entire database layer are stubs to be implemented.

**Entry point:** `app.py` — defines all Flask routes. Currently only GET routes for landing, login, and register are functional. POST handlers for auth (Step 3), profile (Step 4), and expense CRUD (Steps 7–9) are placeholders.

**Database layer:** `database/db.py` — intentionally empty stub. Students implement:
- `get_db()` — returns a SQLite connection with `row_factory = sqlite3.Row` and `PRAGMA foreign_keys = ON`
- `init_db()` — creates tables with `CREATE TABLE IF NOT EXISTS`
- `seed_db()` — inserts sample data

The SQLite file is `expense_tracker.db` (gitignored). There is no ORM — raw SQLite via Python's `sqlite3` module.

**Templates:** Jinja2 templates extending `base.html` (not yet committed). Auth templates (`login.html`, `register.html`) post to `/login` and `/register` respectively.

**Static:** `static/js/main.js` is a placeholder for JavaScript added as features are built.

**Sessions/auth:** Flask session-based auth is planned but not yet implemented. `app.secret_key` will need to be set before sessions work.

**Testing:** pytest + pytest-flask. Test files go in a `tests/` directory (not yet created).
