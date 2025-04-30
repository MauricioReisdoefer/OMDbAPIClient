from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Piece(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    year = db.Column(db.String(50), nullable=False)
    rated = db.Column(db.String(10), nullable=True)
    released = db.Column(db.String(20), nullable=True)
    runtime = db.Column(db.String(20), nullable=True)
    genre = db.Column(db.String(100), nullable=True)
    writer = db.Column(db.String(200), nullable=True)
    actors = db.Column(db.Text, nullable=True)
    plot = db.Column(db.Text, nullable=True)
    language = db.Column(db.String(100), nullable=True)
    country = db.Column(db.String(100), nullable=True)
    awards = db.Column(db.Text, nullable=True)
    poster = db.Column(db.String(300), nullable=True)
    metascore = db.Column(db.String(10), nullable=True)
    imdb_rating = db.Column(db.String(10), nullable=True)
    imdb_votes = db.Column(db.String(20), nullable=True)
    imdb_id = db.Column(db.String(20), nullable=True, unique=True)
    type = db.Column(db.String(10), nullable=True)
    response = db.Column(db.String(10), nullable=True)
    director = db.Column(db.String(100), nullable=True)

class Movie(Piece):
    dvd = db.Column(db.String(20), nullable=True)
    box_office = db.Column(db.String(30), nullable=True)
    production = db.Column(db.String(100), nullable=True)
    website = db.Column(db.String(100), nullable=True)

class Serie(Piece):
    total_seasons = db.Column(db.Integer, nullable=True)
