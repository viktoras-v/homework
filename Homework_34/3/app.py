from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# Dictionary to store user data
users = {}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        if name and email:
            users[name] = email
            return redirect(url_for("show_users"))
    return render_template("form.html")

@app.route("/users")
def show_users():
    return render_template("users.html", users=users)

if __name__ == "__main__":
    app.run(debug=True)
