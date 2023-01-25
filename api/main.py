from enum import Enum
from typing import Any, Dict, List
from lib.get_data import get_data
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from lib.predict import predict
from pydantic import BaseModel, Field, validator

description = "Receives passenger info and predicts survival on Titanic"
app = FastAPI(title="Titanic prediction", description=description)

origins = ["http://localhost:3000", "localhost:3000"]

# setting up CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Gender(str, Enum):
    male = "male"
    female = "female"


class Port(str, Enum):
    southampton = "Southampton"
    cherbourg = "Cherbourg"
    queenstown = "Queenstown"


class Prediction(BaseModel):
    survived: bool = Field(
        ..., description="Prediction of the passenger survival", example=True
    )
    accuracy: float = Field(..., description="Model accuracy", example=0.8)


class Data(BaseModel):
    name: str = Field(..., title="Passenger name", example="Bukater, Miss, Rose DeWitt")
    sex: Gender = Field(..., title="Gender", example="female", alias="gender")
    pclass: int = Field(
        ...,
        title="Ticket class",
        description="1 = 1st, 2 = 2nd, 3 = 3rd",
        example=1,
        alias="class",
    )
    survived: bool = Field(..., title="Survival", example=True)
    age: float | None = Field(title="Age in years", example="17")
    sibsp: int | None = Field(
        title="Number of siblings/spouses aboard", example=0, alias="siblings_spouses"
    )
    parch: int | None = Field(
        title="Numer of parents/children aboard", example=1, alias="parents_children"
    )
    ticket: str | None = Field(title="Ticket number", example="PC 17599")
    fare: float | None = Field(title="Passenger fare", example=150)
    cabin: str | None = Field(title="Cabin number", example="C85")
    embarked: Port | None = Field(
        title="Port of Embarkation",
        example="Southampton",
    )

    class Config:
        allow_population_by_field_name = True

    @validator("embarked", pre=True, always=True)
    def _set_port(cls, embarked: str):
        port_names = {"S": "Southampton", "C": "Cherbourg", "Q": "Queenstown"}
        return port_names.get(embarked)


@app.get("/api/make-prediction", response_model=Prediction, tags=["Prediction"])
def make_a_prediction(
    gender: Gender,
    passenger_class: int = Query(..., example=1, ge=1, le=3, alias="class"),
    age: int = Query(default=28, ge=0, le=120),
    siblings_spouses: int = Query(
        default=0, description="Number of siblings/spouses aboard"
    ),
    parents_children: int = Query(
        default=0, description="Number of parents/children aboard"
    ),
    fare: float = Query(default=0, description="Passenger fare"),
    port: Port | None = Query(default=None, description="Port of Embarkation"),
) -> Dict[str, Any]:
    """
    Uses a logistic regression model to make a prediction if the passenger
    survives or not, based on input passenger data.\n
    Example: /make-prediction?gender=male&class=1&age=32
    """
    result, accuracy = predict(
        gender,
        passenger_class,
        age,
        siblings_spouses,
        parents_children,
        fare,
        port,
    )
    return {"survived": result, "accuracy": accuracy}


@app.get(
    "/api/list-data",
    response_model=List[Data],
    tags=["Get data"],
)
def get_training_data() -> Dict[str, Any]:
    """
    Retrieves the data used to train the model.
    """
    return get_data()
