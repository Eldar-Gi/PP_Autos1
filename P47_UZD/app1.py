from models import db, Automobiliai
from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///automobiliai.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
with app.app_context():
    db.create_all()


@app.route("/uzd")
def home():
    cars = Automobiliai.query.all()
    cars_json = [{
        "id": car.id,
        "gamintojas": car.gamintojas,
        "modelis": car.modelis,
        "spalva": car.spalva,
        "pagaminimo_metai": car.pagaminimo_metai,
        "kaina": car.kaina
    } for car in cars]
    return jsonify(cars_json)


if __name__ == "__main__":
    app.run(port=5001)
