from flask import Flask
from database import db, init_db
from routes import register_routes

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

    init_db(app)
    register_routes(app)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
