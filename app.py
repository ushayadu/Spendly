import sqlite3
from flask import Flask, render_template, request, session, redirect, url_for
from werkzeug.security import generate_password_hash
from database.db import get_db, init_db, seed_db

app = Flask(__name__)
app.secret_key = "dev-secret-key"  # TODO: replace with env var in production


# ------------------------------------------------------------------ #
# Routes                                                              #
# ------------------------------------------------------------------ #

@app.route("/")
def landing():
    return render_template("landing.html")


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/register", methods=["POST"])
def register_post():
    name     = request.form.get("name", "").strip()
    email    = request.form.get("email", "").strip()
    password = request.form.get("password", "")
    confirm  = request.form.get("confirm_password", "")

    if not name or not email or not password or not confirm:
        return render_template("register.html", error="All fields are required.")

    if password != confirm:
        return render_template("register.html", error="Passwords do not match.")

    try:
        db = get_db()
        db.execute(
            "INSERT INTO users (name, email, password_hash) VALUES (?, ?, ?)",
            (name, email, generate_password_hash(password)),
        )
        db.commit()
        user = db.execute(
            "SELECT id FROM users WHERE email = ?", (email,)
        ).fetchone()
        session["user_id"]   = user["id"]
        session["user_name"] = name
        db.close()
    except sqlite3.IntegrityError:
        return render_template("register.html", error="An account with that email already exists.")

    return redirect(url_for("login", email=email))


@app.route("/login")
def login():
    email = request.args.get("email", "")
    return render_template("login.html", email=email)


# ------------------------------------------------------------------ #
# Placeholder routes — students will implement these                  #
# ------------------------------------------------------------------ #

@app.route("/terms")
def terms():
    return render_template("terms.html")


@app.route("/privacy")
def privacy():
    return render_template("privacy.html")


@app.route("/logout")
def logout():
    return "Logout — coming in Step 3"


@app.route("/profile")
def profile():
    return "Profile page — coming in Step 4"


@app.route("/expenses/add")
def add_expense():
    return "Add expense — coming in Step 7"


@app.route("/expenses/<int:id>/edit")
def edit_expense(id):
    return "Edit expense — coming in Step 8"


@app.route("/expenses/<int:id>/delete")
def delete_expense(id):
    return "Delete expense — coming in Step 9"


with app.app_context():
    init_db()
    seed_db()


if __name__ == "__main__":
    app.run(debug=True, port=5001)
