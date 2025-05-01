from flask_sqlalchemy import SQLAlchemy
from models import Piece
from service import GetPieceByTitle, GetPieceByID

db = SQLAlchemy()

class PieceManager():
    def CreateMovie(data):
        new_movie = Piece(
            title = data["title"],
            year = data["year"],
            rated = data["rated"],
            released = data["released"],
            runtime = data["runtime"],
            genre = data["genre"],
            writer = data["writer"],
            actors = data["actors"],
            plot = data["plot"],
            language = data["language"],
            country = data["country"],
            awards = data["awards"],
            poster = data["poster"],
            metascore = data["metascore"],
            imdb_rating = data["imdb_rating"],
            imdb_votes = data["imdb_votes"],
            imdb_id = data["imdb_id"],
            response = data["response"],
            director = data["director"],
        )
        db.session.add(new_movie)
        db.session.commit()
        return {"Message":"Movie Added"}

    def GetPieceByTitle(title):
        movies = db.session.query(Piece).filter(Piece.title == title).all()
        if movies == None:
            movie_data = GetPieceByTitle(title)
            PieceManager.CreateMovie(movie_data)
        return movie_data
    
    def GetPieceByID(imdbID):
        movies = db.session.query(Piece).filter(Piece.imdb_id == imdbID).all()
        if movies == None:
            movie_data = GetPieceByID(imdbID)
            PieceManager.CreateMovie(movie_data)
        return movie_data
