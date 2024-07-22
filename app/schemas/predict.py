from pydantic import BaseModel

class InputVar(BaseModel):
    intensity:float
    temperature:float
    humidity:float

class Prediction(BaseModel):
    prediction:str
    recommendation:str