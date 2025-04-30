from flask_sqlalchemy import SQLAlchemy
from models import Movie, Serie
from service import GetPieceByTitle, GetPieceByID

db = SQLAlchemy()

class MovieManager():
    def CreateMovie(data):
        new_movie = Movie(
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
            dvd = data["dvd"],
            box_office = data["box_office"],
            production = data["production"],
            website = data["website"]
        )
        db.session.add(new_movie)
        db.session.commit()
        return {"Message":"Movie Added"}

    def GetMovieByTitle(title):
        movies = db.session.query(Movie).filter(Movie.title == title).all()
        if movies == None:
            movie_data = GetPieceByTitle(title)
            MovieManager.CreateMovie(movie_data)
        return movie_data
    
    def GetMovieByID(imdbID):
        movies = db.session.query(Movie).filter(Movie.imdb_id == imdbID).all()
        if movies == None:
            movie_data = GetPieceByTitle(imdbID)
            MovieManager.CreateMovie(movie_data)
        return movie_data