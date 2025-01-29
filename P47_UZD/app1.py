from models import db, Automobiliai
from flask import Flask, render_template, request, redirect, url_for, jsonify
from serialaizers import CarsSchema
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///automobiliai.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
with app.app_context():
    db.create_all()


@app.route("/uzd")
def home():
    all_autos = Automobiliai.query.all()
    cars_json = [{
        "id": car.id,
        "gamintojas": car.gamintojas,
        "modelis": car.modelis,
        "spalva": car.spalva,
        "pagaminimo_metai": car.pagaminimo_metai,
        "kaina": car.kaina
    } for car in all_autos]
    return jsonify(cars_json)

# @app.route("/uzd")
# def home():
#     all_autos = Automobiliai.query.all()
#     cars_json = [CarsSchema.model_validate(car, from_attributes=True).model_dump() for car in all_autos]
#     return jsonify(cars_json)


if __name__ == "__main__":
    app.run(port=5001, debug=True)