from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Setup DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

# User class
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)


# Create tables
with app.app_context():
    db.create_all()

# Homepage
@app.route("/", methods=["GET", "POST"])
def add_user():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        if name and email:
            user = User(name=name, email=email)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("list_users"))
    return render_template("add_user.html")

# List users
@app.route("/users")
def list_users():
    users = User.query.all()
    return render_template("users.html", users=users)

# Search by ID
@app.route("/search", methods=["GET", "POST"])
def search_user():
    user=None
    if request.method == "POST":
        user_id = request.form.get("id")
        if user_id:
            user = User.query.get(int(user_id))
    return render_template("search.html", user=user)

if __name__ == "__main__":
    app.run(debug=True)
