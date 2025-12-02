from flask import Flask
import redis

app = Flask(__name__)
r = redis.Redis(host="redis", port=6379, db=0)

@app.route("/")
def index():
    return "Flask is running!\n"

@app.route("/add/<job>")
def add(job):
    r.lpush("jobs", job)
    return f"Job '{job}' added!\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
