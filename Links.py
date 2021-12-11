from typing import List
from flask_restful import Resource
import csv


class Link:

    def __init__(self, movieId: int, imdbId: int, tmdbId: int):
        self.movieId = movieId
        self.imdbId = imdbId
        self.tmdbId = tmdbId

    def __str__(self) -> str:
        return f"movieId: {self.movieId}, imdbId: {self.imdbId}, " \
               f"tmdbId: {self.tmdbId}"


class Links(Resource):

    links: List[Link] = []

    def __init__(self) -> None:
        super().__init__()
        with open("links.csv", newline='') as csv_file:
            links_rows = csv.reader(csv_file, delimiter=",")
            for row in links_rows:
                self.links.append(Link(row[0], row[1], row[2]))

    def get(self):
        return [link.__dict__ for link in self.links[1:]]
