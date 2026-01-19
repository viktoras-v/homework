from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"  # Редирект на /login, если не авторизован

# Модель пользователя
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

with app.app_context():
    db.create_all()

# Загрузка пользователя по id
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Главная страница
@app.route("/")
def home():
    return render_template("home.html")

# Защищённая страница
@app.route("/protected")
@login_required
def protected():
    return render_template("protected.html", username=current_user.username)

# Логин
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            flash("Logged in successfully!")
            return redirect(url_for("protected"))
        else:
            flash("Invalid username or password")
    return render_template("login.html")

# Логаут
@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Logged out successfully!")
    return redirect(url_for("home"))

@app.route("/add_user", methods=["GET", "POST"])
def add_user():
    if request.method == "POST":
        name = request.form.get("name")
        password = request.form.get("password")
        hashed_password = generate_password_hash(password)
        if name and password:
            hashed_password = generate_password_hash(password)
            new_user = User(username=name, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for("login"))
    return render_template("add_user.html")

## Создание тестового пользователя (для демонстрации)
#@app.route("/create_user")
#def create_user(username, password):
#    if User.query.filter_by(username=username).first():
#        return "User already exists!"
#    hashed_password = generate_password_hash(password, method="sha256")
#    new_user = User(username=username, password=hashed_password)
#    db.session.add(new_user)
#    db.session.commit()
#    return f"User {username} created!"

if __name__ == "__main__":
    app.run(debug=True)
