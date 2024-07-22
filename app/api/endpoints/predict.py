from fastapi import APIRouter,Depends,HTTPException,status
from core.config import settings
from schemas.predict import InputVar, Prediction
from thirdparty.predict import MLModel
from core.auth import oauth2_scheme, get_current_user,JWTBearer
from pathlib import Path

# Construct the path to the model file from the root directory
router = APIRouter()


@router.post('/predict', status_code=200, response_model=Prediction,dependencies=[Depends(JWTBearer())])
def login(form_data:InputVar):
    model = MLModel()
    try:
        result = model.predict(light_intensity=form_data.intensity, temperature=form_data.temperature, humidity=form_data.humidity)
        return {"result":result}
    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Could not make predictions", headers={"WWW-Aunthenticate":"Bearer"})
