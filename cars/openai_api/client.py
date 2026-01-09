import openai
from dotenv import load_dotenv
import os

load_dotenv()


def get_car_ai_bio(model, brand, factory_year, model_year):
    prompt = '''
    You are a vehicle marketing specialist. Do not exceed 250 characters.
    Create a sales bio for a car with the following specifications:
    Model: {}
    Brand: {}
    Manufacturing Year: {}
    Model Year: {}
    '''.format(model, brand, factory_year, model_year)
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=1000
    )
    return response.choices[0].message.content



