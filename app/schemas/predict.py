from pydantic import BaseModel

class InputVar(BaseModel):
    intensity:float
    temperature:float
    humidity:float
    soil_moisture:int

class Prediction(BaseModel):
    prediction:str
    recommendation:str