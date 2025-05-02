from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes import PieceManager
from models import db
from urllib.parse import quote_plus
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path='db.env')

app = Flask(__name__)

# Montando a URI com dados do .env
user = os.getenv("DB_USER")
password = quote_plus(os.getenv("DB_PASS"))
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
dbname = os.getenv("DB_NAME")

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{user}:{password}@{host}:{port}/{dbname}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.before_request
def initiate():
    db.create_all()

@app.route("/")
def index():
    return {"Message": "Ok"}, 200

@app.route("/title_search/<title>")
def search_by_title(title):
    return PieceManager.GetPieceByTitle(title)

@app.route("/id_search/<id>")
def search_by_title(title):
    return PieceManager.GetPieceByID(id)

if __name__ == "__main__":
    app.run()