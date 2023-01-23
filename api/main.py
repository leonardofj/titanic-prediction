import time
from fastapi import FastAPI
from utils import predict

app = FastAPI()


@app.get("/time")
def get_current_time():
    return {"time": time.time()}


@app.get("/make-prediction")
def make_a_prediction(sex: int, passenger_class: int, age: float = 0):
    result = predict(sex, passenger_class)
    accuracy = 1
    return {"prediction": result, "accuracy": accuracy}


@app.get("/training-data")
def get_training_data():
    return {"training_data": "training_data"}
