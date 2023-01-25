import pickle
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score


def train_titanic_model():
    """
    Model training based on https://risx3.github.io/titanic-analysis/
    """

    train = pd.read_csv("../api/datasets/train.csv")
    print("Number of passengers in train dataset: " + str(len(train)))

    # Concat new features in train data
    sex = pd.get_dummies(train["sex"], drop_first=True)
    embark = pd.get_dummies(train["embarked"], drop_first=True)
    pcl = pd.get_dummies(train["pclass"], drop_first=True)
    train = pd.concat([train, sex, embark, pcl], axis=1)

    # Dropping columns from train dataset
    train.drop(
        ["pclass", "sex", "embarked", "cabin", "passengerid", "name", "ticket"],
        axis=1,
        inplace=True,
    )

    # Handling NULL values
    train_values = {"age": round(np.mean(train["age"]))}
    train = train.fillna(value=train_values)
    train.columns = train.columns.astype(str)

    # Preparing data
    X = train.drop("survived", axis=1)
    y = train["survived"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=1
    )

    # Define Model
    logmodel = LogisticRegression(solver="liblinear")

    # Fit Model
    logmodel.fit(X_train, y_train)
    LogisticRegression(
        C=1.0,
        class_weight=None,
        dual=False,
        fit_intercept=True,
        intercept_scaling=1,
        l1_ratio=None,
        max_iter=100,
        multi_class="auto",
        n_jobs=None,
        penalty="l2",
        random_state=None,
        solver="liblinear",
        tol=0.0001,
        verbose=0,
        warm_start=False,
    )

    # Model Evaluation
    predictions = logmodel.predict(X_test)
    print(classification_report(y_test, predictions))
    print(confusion_matrix(y_test, predictions))
    print(accuracy_score(y_test, predictions))

    pickle.dump(logmodel, open("../api/models/titanic_model.pkl", "wb"))


if __name__ == "__main__":
    train_titanic_model()
