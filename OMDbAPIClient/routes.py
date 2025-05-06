from flask_sqlalchemy import SQLAlchemy
from models import Piece, db
from service import GetPieceByTitle as ApiGetPieceByTitle, GetPieceByID as ApiGetPieceByID

class PieceManager:
    @staticmethod
    def CreateMovie(data):
        try:
            new_movie = Piece(
                title = data.get("Title"),
                year = data.get("Year"),
                rated = data.get("Rated"),
                released = data.get("Released"),
                runtime = data.get("Runtime"),
                genre = data.get("Genre"),
                writer = data.get("Writer"),
                actors = data.get("Actors"),
                plot = data.get("Plot"),
                language = data.get("Language"),
                country = data.get("Country"),
                awards = data.get("Awards"),
                poster = data.get("Poster"),
                metascore = data.get("Metascore"),
                imdb_rating = data.get("imdbRating"),
                imdb_votes = data.get("imdbVotes"),
                imdb_id = data.get("imdbID"),
                response = data.get("Response"),
                director = data.get("Director"),
            )
            db.session.add(new_movie)
            db.session.commit()
            return {"Message": "Movie Added"}
        except Exception as e:
            db.session.rollback()
            return {"error": str(e)}


    @staticmethod
    def GetPieceByTitle(title):
        movie = db.session.query(Piece).filter(Piece.title.ilike(title)).first()
        if movie:
            return movie.serialize()

        movie_data = ApiGetPieceByTitle(title)

        if movie_data.get("Response", "False") == "True":
            PieceManager.CreateMovie(movie_data)
            return movie_data
        else:
            return {"error": movie_data.get("Error", "Unknown error")}


    @staticmethod
    def GetPieceByID(imdb_id):
        movie = db.session.query(Piece).filter(Piece.imdb_id == imdb_id).first()
        if movie:
            return movie.serialize()

        movie_data = ApiGetPieceByID(imdb_id)

        if movie_data.get("Response", "False") == "True":
            PieceManager.CreateMovie(movie_data)
            return movie_data
        else:
            return {"error": movie_data.get("Error", "Unknown error")}
