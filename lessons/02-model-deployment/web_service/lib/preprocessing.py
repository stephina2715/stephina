from fastapi import Request
import numpy as np
from pydantic import BaseModel
from typing import List
import pandas as pd
from sklearn.feature_extraction import DictVectorizer
import pickle

# class PredictDurationInput(BaseModel):
#     PULocationID: int = 264
#     DOLocationID: int = 264
#     passenger_count: int = 1

# def input_values(input_data) -> np.ndarray:
#     if isinstance(input_data, PredictDurationInput):
#         data = np.array([input_data.PULocationID, input_data.DOLocationID, input_data.passenger_count])
#     else:
#         data = np.array([input_data["PULocationID"], input_data["DOLocationID"], input_data["passenger_count"]])

#     # Convert all elements to strings
#     data = data.astype(str)

#     return data

def encode_categorical_cols(df: pd.DataFrame, categorical_cols: List[str] = None) -> pd.DataFrame:
    if categorical_cols is None:
        categorical_cols = ["PULocationID", "DOLocationID", "passenger_count"]
    df[categorical_cols] = df[categorical_cols].fillna(-1).astype("int")
    df[categorical_cols] = df[categorical_cols].astype("str")
    return df

def load_preprocessor(PATH_TO_PREPROCESSOR: str):
    try:
        with open(PATH_TO_PREPROCESSOR, "rb") as f:
            preprocessor = pickle.load(f)
        return preprocessor
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found at path: {PATH_TO_PREPROCESSOR}")
    except Exception as e:
        raise Exception(f"Error loading preprocessor: {e}")
