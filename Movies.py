from typing import List
from flask_restful import Resource
import csv


class Movie:
    def __init__(self, id: int, title: str, genres: List[str]) -> None:
        self.id = id
        self.title = title
        self.genres = genres

    def __str__(self) -> str:
        return f"Id: {self.id} Title: {self.title}, genre: {self.genres}"


class Movies(Resource):

    movies: List[Movie] = []

    def __init__(self) -> None:
        super().__init__()
        with open("movies.csv", "r", encoding="UTF-8", newline='') as csvfile:
            movieslines = csv.reader(csvfile, delimiter=",")
            for row in movieslines:
                self.movies.append(Movie(row[0], row[1], row[2]))

    def get(self) -> List:
        return [movie.__dict__ for movie in self.movies[1:]]
