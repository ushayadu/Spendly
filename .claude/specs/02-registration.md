# Spec: Registration

## Overview
Implement user registration for Spendly — the POST handler for `/register` that validates form input, hashes the password, inserts the new user into the database, and starts an authenticated session. This is the first step of the auth layer and the gateway through which all new users enter the app.

## Depends on
- Step 01 — Database setup (`get_db()`, `init_db()`, `users` table must exist)

## Routes
- `POST /register` — accepts name, email, password, confirm_password from the registration form — public

## Database changes
No database changes. The `users` table already exists with the correct schema:
- `id`, `name`, `email` (UNIQUE), `password_hash`, `created_at`

## Templates
- **Modify:** `templates/register.html` — ensure the form posts to `/register` with method `POST`; add fields for `name`, `email`, `password`, `confirm_password`; display flashed error/success messages

## Files to change
- `app.py` — add `POST /register` handler; set `app.secret_key`; import `session`, `redirect`, `url_for`, `request`, `flash` from Flask
- `templates/register.html` — ensure form fields and flash message display are present

## Files to create
No new files.

## New dependencies
No new dependencies.

## Rules for implementation
- No SQLAlchemy or ORMs — raw `sqlite3` only
- Parameterised queries only — no string formatting in SQL
- Passwords hashed with `werkzeug.security.generate_password_hash`
- Use CSS variables — never hardcode hex values
- All templates extend `base.html`
- Set `app.secret_key` to a hard-coded dev string (e.g. `"dev-secret-key"`) — document that it must be replaced in production
- Use `flask.flash` for user-facing error and success messages
- Validate in this order: all fields present → passwords match → email not already taken
- On duplicate email, catch the `sqlite3.IntegrityError` and flash a user-friendly message
- After successful registration, write `session["user_id"]` and `session["user_name"]`, then redirect to `/`
- Do not log the user in if registration fails — re-render the form

## Definition of done
- [ ] Submitting the form with valid data creates a new row in the `users` table
- [ ] The stored password is a hash, not plain text
- [ ] Submitting with mismatched passwords re-renders the form with an error message
- [ ] Submitting with an already-registered email re-renders the form with an error message
- [ ] Submitting with any blank field re-renders the form with an error message
- [ ] After successful registration the user is redirected to `/login` with email field autofilled
- [ ] `session["user_id"]` is set after a successful registration
- [ ] The app starts without errors (`python app.py`)
