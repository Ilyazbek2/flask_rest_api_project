from flask import Flask
from flask_restful import Api

def create_app():
    app = Flask(__name__)
    api = Api(app)

    # Import routes here
    from app.routes import BookList
    api.add_resource(BookList, '/api/books')

    return app
