from typing import List
from flask_restful import Resource
import csv


class Movie:
    def __init__(self, movieid: int, title: str, genres: List[str]) -> None:
        self.movieid = movieid
        self.title = title
        self.genres = genres

    def __str__(self) -> str:
        return f"Movie {self.movieid}: {self.title}, genres: {self.genres}"

class Movies(Resource):

    movies: List[str] = []

    def __init__(self) -> None:
        super().__init__()
        with open("movies.csv", "r", encoding="UTF-8", newline='') as csvfile:
            movieslines = csv.reader(csvfile, delimiter=",")
            for row in movieslines:
                self.movies.append(Movie(row[0], row[1], row[2]))

    def get(self) -> List:
        return [movie.__dict__ for movie in self.movies[1:]]
