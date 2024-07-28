import joblib
import pandas as pd
from pathlib import Path
import openai,os,re

# Configure OpenAI API
openai.api_type = "azure"
openai.api_version = "2024-02-01"
API_KEY = os.getenv("OPENAI_API_KEY")
assert API_KEY, "ERROR: Azure OpenAI Key is missing"
openai.api_key = API_KEY

RESOURCE_ENDPOINT = os.getenv("OPENAI_RESOURCE_ENDPOINT")
assert RESOURCE_ENDPOINT, "ERROR: Azure OpenAI Endpoint is missing"
assert "openai.azure.com" in RESOURCE_ENDPOINT.lower(), "ERROR: Azure OpenAI Endpoint should be in the form: \n\n\t<your unique endpoint identifier>.openai.azure.com"
openai.api_base = RESOURCE_ENDPOINT

class MLModel:
    def __init__(self):
        current_directory = Path.cwd()
        model_path = current_directory / 'app' / 'thirdparty' / 'plant_growth_model.joblib'

        self.model = joblib.load(model_path)
    def predict(self,light_intensity,temperature,humidity,soil_moisture):
        input=pd.DataFrame({
            'Light Intensity': [float(light_intensity)],
            'Temperature': [float(temperature)],
            'Humidity': [float(humidity)],
            'Soil Moisture':[int(soil_moisture)]
        })
        predicted_status = self.model.predict(input)
        # return predicted_status
    # Recommendation variable
        # Set up OpenAI Chat API
        # CHAT_COMPLETIONS_MODEL = 'helping-farmers'
        ourNote = predicted_status[0]
        prompt = """I will input the state of a farmer's plant in Lagos. I want you to return a very comprehensive recommendation on what the farmer should do to the plant mainly in terms of light intensity, temperature, soil moisture and humidity of the plant. Note: for soil moisture, 0 represent very low, 1 represents medium, 2 represents High".
        Q: """ + ourNote + """
        A:"""
        response = openai.ChatCompletion.create(
        engine="helpingfarmers",
        messages = [{"role":"system", "content":"You are a helpful assistant."},
                    {"role":"user","content":prompt},])

        recommendation = response['choices'][0]['message']['content']
        recommendation = self.remove_markdown(recommendation)
        return {'prediction':ourNote, 'recommendation':recommendation}

    def remove_markdown(self,text):
        # Remove Markdown headings and insert newline after each heading
        text = re.sub(r'^(#+.*)$', r'\1\n\n', text, flags=re.MULTILINE)
        # Remove Markdown syntax
        text = re.sub(r'[*_`~]', '', text)
        # Remove Markdown links
        text = re.sub(r'\[([^]]+)\]\([^)]+\)', r'\1', text)
        # Remove Markdown images
        text = re.sub(r'\!\[([^]]+)\]\([^)]+\)', r'\1', text)
        return text