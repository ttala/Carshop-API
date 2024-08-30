from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class CarModel(db.Model):
    __tablename__ = "cars"

    car_id = db.Column(db.Integer, primary_key=True)
    car_name = db.Column(db.String(80), unique=True, nullable=False)
    car_color = db.Column(db.String(80), unique=True, nullable=False)
    car_price = db.Column(db.Float(precision=2), unique=False, nullable=False)
    car_model = db.Column(db.String(80), unique=True, nullable=False)
    store_id = db.Column(
        db.Integer, db.ForeignKey("store.store_id"), unique=False, nullable=False
    )
    store = db.relationship("StoreModel", back_populates="cars")


    def __init__(self, name, model, color, price, store):
        self.car_name = name
        self.car_model = model
        self.car_color = color
        self.car_price = price
        self.store_id = store

    def __repr__(self):
        return f"<Car {self.car_name}, {self.car_model}>"
    

class StoreModel(db.Model):
    __tablename__ = "store"

    store_id = db.Column(db.Integer, primary_key=True)
    store_name = db.Column(db.String(80), unique=True, nullable=False)
    store_address = db.Column(db.String(200), unique=True, nullable=False)
    cars = db.relationship("CarModel", back_populates="store", lazy="dynamic")

    def __init__(self, name, address):
        self.store_name = name
        self.store_address = address


    def __repr__(self):
        return f"<Store {self.store_name}, {self.store_address}>"