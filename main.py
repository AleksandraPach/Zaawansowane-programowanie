from flask import Flask
from flask_restful import Api
from Movies import Movies

app = Flask(__name__)
api = Api(app)

api.add_resource(Movies, "/")

if __name__ == '__main__':
    app.run(debug=True)
