# Spec: Login and Logout

## Overview
This step wires up credential-based login and session-clearing logout. Users submit their email and password via the existing `login.html` form; the handler verifies the password hash, starts a session, and redirects to the landing page. The logout route clears the session and redirects to `/login`. Together these two routes complete the authentication loop started in Step 02.

## Depends on
- Step 01 — Database setup (`users` table, `get_db()`)
- Step 02 — Registration (`app.secret_key`, `session`, `redirect`, `url_for` already imported; `password_hash` stored in `users`)

## Routes
- `POST /login` — verify email/password, start session — public
- `GET /logout` — clear session, redirect to `/login` — public (no guard needed yet)

## Database changes
No database changes. The `users` table already has `id`, `name`, `email`, `password_hash`.

## Templates
- **Modify:** `templates/login.html` — the `value="{{ email }}"` pre-fill is already in place; no further changes needed unless the error display is missing (it is already present via `{% if error %}`).

## Files to change
| File | Change |
|------|--------|
| `app.py` | Add `check_password_hash` import; add `POST /login` handler; replace `GET /logout` stub with real session-clearing handler |

## Files to create
None.

## New dependencies
No new dependencies. `check_password_hash` is part of `werkzeug.security`, which is already installed.

## Rules for implementation
- No SQLAlchemy or ORMs — raw `sqlite3` only
- Parameterised queries only — never string-format SQL
- Passwords verified with `werkzeug.security.check_password_hash`
- Use CSS variables — never hardcode hex values
- All templates extend `base.html`
- Pass `error=` as a template context variable on failure — do **not** use `flask.flash()`
- On successful login set `session["user_id"]` and `session["user_name"]`
- Logout must call `session.clear()` before redirecting

## Definition of done
- [ ] `POST /login` with correct credentials sets `session["user_id"]` and `session["user_name"]` and redirects to `/`
- [ ] `POST /login` with wrong password renders `login.html` with error "Invalid email or password."
- [ ] `POST /login` with an email that does not exist renders `login.html` with the same generic error (no user enumeration)
- [ ] `POST /login` with any field blank renders `login.html` with error "All fields are required."
- [ ] `GET /logout` clears the session and redirects to `/login`
- [ ] After logout, navigating to `/` does not show the previous user's session data
