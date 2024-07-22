from pydantic import BaseModel

class InputVar(BaseModel):
    intensity:float
    temperature:float
    humidity:float

class Prediction(BaseModel):
    result:list