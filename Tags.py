from typing import List
from flask_restful import Resource
import csv


class Tag:

    def __init__(self, userId: int, movieId: int, tag: str, timestamp: str):
        self.userId = userId
        self.movieId = movieId
        self.tag = tag
        self.timestamp = timestamp

    def __str__(self) -> str:
        return f"userid: {self.userId}, movieid: {self.movieId}, " \
               f"tag: {self.tag}, timestamp: {self.timestamp}"


class Tags(Resource):

    tags: List[Tag] = []

    def __init__(self) -> None:
        super().__init__()
        with open("tags.csv", newline='') as csv_file:
            tag_rows = csv.reader(csv_file, delimiter=",")
            for row in tag_rows:
                self.tags.append(Tag(row[0], row[1], row[2], row[3]))

    def get(self):
        return [tag.__dict__ for tag in self.tags[1:]]
