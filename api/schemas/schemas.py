from pydantic import BaseModel
from typing import List

class InputData(BaseModel):
    prices: List[float]

class Prediction(BaseModel):
    predicted_price: float
