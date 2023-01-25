import pickle
from typing import Tuple
from fastapi import HTTPException
import pandas as pd

MODEL_FILE = "models/titanic_model.pkl"
MODEL_ACCURACY = 0.783


def predict(
    sex: str,
    passenger_class: int,
    age: int,
    sibsp: int = 0,
    parch: int = 0,
    fare: float = 0,
    port: str = "S",
) -> Tuple[bool, float]:
    """
    Loads the prediction model and get a survival prediction
    from passenger data.
    """

    input_data_dict = {
        "age": age,
        "sibsp": sibsp,
        "parch": parch,
        "fare": fare,
        "male": 1 if sex == "male" else 0,
        "Q": 1 if port == "Q" else 0,
        "S": 1 if port == "S" else 0,
        "2": 1 if passenger_class == 2 else 0,
        "3": 1 if passenger_class == 3 else 0,
    }
    input_data_df = pd.DataFrame([input_data_dict])

    # load the model
    try:
        my_model = pickle.load(open(MODEL_FILE, "rb"))
    except OSError as ex:
        raise HTTPException(status_code=404, detail="Model not found")

    # make a prediction
    prediction = my_model.predict(input_data_df)
    return prediction[0], MODEL_ACCURACY
