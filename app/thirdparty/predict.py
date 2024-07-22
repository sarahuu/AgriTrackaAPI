import joblib
import pandas as pd
from pathlib import Path

class MLModel:
    def __init__(self):
        current_directory = Path.cwd()
        model_path = current_directory / 'app' / 'thirdparty' / 'plant_growth_model.joblib'

        self.model = joblib.load(model_path)
        # joblib.dump(self.model, '/app/thirdparty/new_model.joblib')
    def predict(self,light_intensity,temperature,humidity):
        input=pd.DataFrame({
            'Light Intensity': [float(light_intensity)],
            'Temperature': [float(temperature)],
            'Humidity': [float(humidity)]
        })
        predicted_status = self.model.predict(input)
        return predicted_status
