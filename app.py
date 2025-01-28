from models import db, Automobiliai
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///automobiliai.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
with app.app_context():
    db.create_all()


@app.route("/")
def home():
    search_text = request.args.get("search")
    if search_text:
        filtered_rows = Automobiliai.query.filter(
            Automobiliai.gamintojas.ilike(f"{search_text}%") |
            Automobiliai.modelis.ilike(f"{search_text}%")
        )
        cars = filtered_rows
    else:
        cars = Automobiliai.query.all()
    all_p = db.session.query(db.func.sum(Automobiliai.kaina)).scalar()
    return render_template("index.html", cars=cars, total_price=all_p)


@app.route("/car/<int:car_id>")
def one_car(car_id):
    car = Automobiliai.query.get(car_id)
    if car:
        return render_template("one_p.html", car=car)
    else:
        return f"Automobilio su id {car_id} neegzistuoja"


@app.route("/car/edit/<int:car_id>", methods=["GET", "POST"])
def update_car(car_id):
    car = Automobiliai.query.get(car_id)
    if not car:
        return f"Automobilio su id {car_id} neegzistuoja"

    if request.method == "GET":
        return render_template("update_p.html", car=car)

    elif request.method == "POST":
        car.gamintojas = request.form.get("gamintojas")
        car.modelis = request.form.get("modelis")
        car.spalva = request.form.get("spalva")
        car.pagaminimo_metai = int(request.form.get("pagaminimo_metai"))
        car.kaina = float(request.form.get("kaina"))
        db.session.commit()
        return redirect(url_for("home"))


@app.route("/car/delete/<int:car_id>", methods=["POST"])
def delete_car(car_id):
    car = Automobiliai.query.get(car_id)
    if not car:
        return f"Automobilio su id {car_id} neegzistuoja"
    db.session.delete(car)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/car/new", methods=["GET", "POST"])
def create_car():
    if request.method == "GET":
        return render_template("create_car_form.html")
    if request.method == "POST":
        gamintojas = request.form.get("gamintojas")
        modelis = request.form.get("modelis")
        spalva = request.form.get("spalva")
        pagaminimo_metai = int(request.form.get("pagaminimo_metai"))
        kaina = float(request.form.get("kaina"))
        if gamintojas and modelis and spalva and pagaminimo_metai and kaina:
            new_car = Automobiliai(
                gamintojas=gamintojas,
                modelis=modelis,
                spalva=spalva,
                pagaminimo_metai=pagaminimo_metai,
                kaina=kaina
            )
            db.session.add(new_car)
            db.session.commit()
        return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(port=5001, debug=True)
