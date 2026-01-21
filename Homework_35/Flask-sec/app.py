
import os
from flask import Flask
from flask_security import SQLAlchemySessionUserDatastore, Security
from dotenv import load_dotenv

from database import db
from models.auth import User, Role

load_dotenv()

app = Flask(__name__)

app.config["SECRET_KEY"] = "cb49fb9a8acds51d"
app.config["SECURITY_PASSWORD_SALT"] = "ab3d3a04f5hka041509b097a7"
app.config["SECURITY_REGISTERABLE"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")

app.config["SECURITY_SEND_REGISTER_EMAIL"] = False
app.config["SECURITY_RECOVERABLE"] = False  
app.config["SECURITY_CONFIRMABLE"] = False 


db.init_app(app)
with app.app_context():
    db.create_all()

user_datastore = SQLAlchemySessionUserDatastore(db.session, User, Role)
security = Security(app, user_datastore)

@app.route("/")
def home():
    return "Hello, world!"


