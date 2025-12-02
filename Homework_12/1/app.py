from flask import Flask
import redis
import os

app = Flask(__name__)

r = redis.Redis(
    host=os.getenv("REDIS_HOST", "redis"),
    port=int(os.getenv("REDIS_PORT", 6379)),
    decode_responses=True
)

@app.route("/")
def index():
    r.incr("counter")
    return f"Counter: {r.get('counter')}"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
