from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()


class Automobiliai(db.Model):
    __tablename__ = "automobiliai"
    id = db.Column(db.Integer, primary_key=True)
    gamintojas = db.Column(db.String)
    modelis = db.Column(db.String)
    spalva = db.Column(db.String)
    pagaminimo_metai = db.Column(db.Integer)
    kaina = db.Column(db.Float)

    def __repr__(self):
        return f"id: {self.id} {self.gamintojas} {self.modelis} {self.spalva} {self.pagaminimo_metai} {self.kaina}"
