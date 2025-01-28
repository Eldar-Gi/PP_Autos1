from models import Automobiliai, db
from app import app


with app.app_context():
    cars = [
        Automobiliai(gamintojas="Lexus", modelis="LS600H", spalva="Juoda", pagaminimo_metai=2008, kaina=10000.0),
        Automobiliai(gamintojas="Toyota", modelis="Corolla", spalva="Raudona", pagaminimo_metai=2015, kaina=15000.0),
        Automobiliai(gamintojas="Honda", modelis="Civic", spalva="Juoda", pagaminimo_metai=2018, kaina=18000.0),
        Automobiliai(gamintojas="Ford", modelis="Focus", spalva="Melyna", pagaminimo_metai=2020, kaina=20000.0),
        Automobiliai(gamintojas="BMW", modelis="340i", spalva="Balta", pagaminimo_metai=2017, kaina=25000.0),
        Automobiliai(gamintojas="Audi", modelis="A4", spalva="Pilka", pagaminimo_metai=2019, kaina=30000.0),
        Automobiliai(gamintojas="Nissan", modelis="Qashqai", spalva="Raudona", pagaminimo_metai=2016, kaina=17000.0),
        Automobiliai(gamintojas="Tesla", modelis="Model 3", spalva="Juoda", pagaminimo_metai=2021, kaina=50000.0),
        Automobiliai(gamintojas="Volkswagen", modelis="Golf", spalva="Pilka", pagaminimo_metai=2019, kaina=22000.0),
        Automobiliai(gamintojas="Kia", modelis="Sportage", spalva="Melyna", pagaminimo_metai=2018, kaina=19000.0),
        Automobiliai(gamintojas="Mazda", modelis="CX-5", spalva="Raudona", pagaminimo_metai=2020, kaina=28000.0)
    ]
    db.session.add_all(cars)
    db.session.commit()
    print("Info is given above")
