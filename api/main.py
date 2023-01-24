from enum import Enum
from typing import Any, Dict, List
from lib.get_data import get_data
from fastapi import FastAPI, Query
from lib.predict import predict
from pydantic import BaseModel, Field
import uvicorn

app = FastAPI(title="Titanic prediction", description="Predicts survival on Titanic")


class Gender(str, Enum):
    MALE = "male"
    FEMALE = "female"


class Prediction(BaseModel):
    survived: bool = Field(
        ..., description="Prediction of the passenger survival", example=True
    )
    accuracy: float = Field(..., description="Prediction accuracy", example=0.94)


class Row(BaseModel):
    name: str = Field(..., title="Passenger name", example="Bukater, Miss, Rose DeWitt")
    sex: Gender = Field(..., title="Sex", example="female")
    pclass: int = Field(
        ..., title="Ticket class", description="1 = 1st, 2 = 2nd, 3 = 3rd", example=1
    )
    survived: bool = Field(..., title="Survival", example=True)
    age: float | None = Field(title="Age in years", example="17")
    sibSp: int | None = Field(title="Siblings/spouses aboard", example=0)
    parch: int | None = Field(title="Parents/children aboard", example=1)
    ticket: str | None = Field(title="Ticket number", example="PC 17599")
    fare: float | None = Field(title="Passenger fare", example=150)
    cabin: str | None = Field(title="Cabin number", example="C85")
    embarked: str | None = Field(
        title="Port of Embarkation",
        description="C = Cherbourg, Q = Queenstown, S = Southampton",
        example="S",
    )


class Data(BaseModel):
    training_data: List[Row]
    total: int = Field(example=1)


@app.get("/make-prediction", response_model=Prediction, tags=["Prediction"])
def make_a_prediction(
    sex: Gender,
    passenger_class: int = Query(..., example=1, ge=1, le=3, alias="class"),
    age: int | None = Query(default=None, ge=0, le=120),
) -> Dict[str, Any]:
    """
    Makes a prediction if the passenger survived or not, based on
    passenger data.\n
    Example: /make-prediction?sex=male&class=1&age=32
    """
    result = predict(sex, passenger_class, age)
    accuracy = 1
    return {"survived": result, "accuracy": accuracy}


@app.get(
    "/training-data",
    response_model=Data,
    response_model_exclude_unset=True,
    tags=["Get data"],
)
def get_training_data() -> Dict[str, Any]:
    """
    Retrieves the data used to train the model.
    """
    return get_data()
