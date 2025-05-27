from fastapi.routing import APIRouter
from api.schemas.schemas import Prediction, InputData
from api.services.prediction_service import predict_price

router = APIRouter()

@router.post("/predict", response_model=Prediction)
async def predict(data: InputData):
    prediction = predict_price(data.prices)
    return {"predicted_price": prediction}