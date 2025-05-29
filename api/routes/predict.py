from fastapi.routing import APIRouter
from fastapi import HTTPException
from api.schemas.schemas import Prediction, InputData
from api.services.prediction_service import predict_price

router = APIRouter()


@router.post("/predict", response_model=Prediction)
async def predict(data: InputData):
    try:
        prediction = predict_price(data.prices)
        return {"predicted_price": prediction}
    except Exception as e:
        import traceback
        traceback.print_exc()  # Exibe o erro no terminal
        raise HTTPException(status_code=500, detail=str(e))
