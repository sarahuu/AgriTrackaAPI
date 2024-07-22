from fastapi import APIRouter,Depends,HTTPException,status
from app.core.config import settings
from app.schemas.predict import InputVar, Prediction
from app.thirdparty.predict import MLModel
from app.core.auth import oauth2_scheme, get_current_user,JWTBearer
from pathlib import Path

# Construct the path to the model file from the root directory
router = APIRouter()


@router.post('/predict', status_code=200, response_model=Prediction,dependencies=[Depends(JWTBearer())])
def predict(form_data:InputVar):
    """
    Predicts the outcome using environmental data.

    **Parameters:**
    - `form_data` (InputVar): Contains light intensity (`intensity`), temperature (`temperature`), and humidity (`humidity`).

    **Returns:**
    - `Prediction`: Prediction result from the model.

    **Errors:**
    - `HTTP 400 Bad Request`: For errors during prediction.

    **Authentication:**
    - Requires Bearer token.
    """
    model = MLModel()
    try:
        result = model.predict(light_intensity=form_data.intensity, temperature=form_data.temperature, humidity=form_data.humidity)
        return result
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e), headers={"WWW-Aunthenticate":"Bearer"})
