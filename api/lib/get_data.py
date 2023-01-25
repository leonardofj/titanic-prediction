import csv
from fastapi import HTTPException


DATA_FILE = "datasets/train.csv"


def get_data() -> dict:
    """
    Loads the training data file and returnds a list
    of objects.
    """
    data = []
    try:
        with open(DATA_FILE, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append({k: v for k, v in row.items() if v})
    except OSError as ex:
        raise HTTPException(status_code=404, detail="Data not found")

    return data
