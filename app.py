from flask import Flask
from dotenv import load_dotenv
import pandas as pd
from database import db
import os
from model import *

app = Flask(__name__)

load_dotenv(override=True)
#engine = create_engine(os.environ.get("DATABASE_URL"))
app.config ['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL") 
db.init_app(app)

def reset_db():
        db.drop_all()
        db.create_all()
        data = pd.read_csv(r"store.csv")
        df = pd.DataFrame(data)
        for index, row in df.iterrows():
            new_store = StoreModel(name=row["store_name"], address=row["store_address"])
            db.session.add(new_store)
            db.session.commit()
        data = pd.read_csv(r"cars.csv")
        df = pd.DataFrame(data)
        for index, row in df.iterrows():
            new_car = CarModel(name=row["car_name"], color=row["car_color"], model=row["car_model"], 
                            price=row["car_price"], store=row["store"])
            db.session.add(new_car)
            db.session.commit()

with app.app_context():
    reset_db()
    
@app.get("/")
def get_index():
    return {"Project name": "ShopCars"}

@app.get("/cars")
def get_cars():
    cars = CarModel.query.all()
    results = [
            {
                "name": car.car_name,
                "model": car.car_model,
                "color": car.car_color,
                "price": car.car_price
            } for car in cars]

    return {"count": len(results), "cars": results}

@app.route('/cars/<car_id>', methods=['GET'])
def get_car(car_id):
    car = CarModel.query.get_or_404(car_id)

    response = {
            "name": car.car_name,
            "model": car.car_model,
            "color": car.car_color,
            "price": car.car_price
        }
    return {"message": "success", "car": response}

@app.get("/stores")
def get_stores():
    stores = StoreModel.query.all()
    results = [
            {
                "name": store.store_name,
                "address": store.store_address,
            } for store in stores]

    return {"count": len(results), "stores": results}

@app.route('/stores/<store_id>', methods=['GET'])
def get_store(store_id):
    store = StoreModel.query.get_or_404(store_id)

    response = {
            "name": store.store_name,
            "address": store.store_address,
        }
    return {"message": "success", "store": response}

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)