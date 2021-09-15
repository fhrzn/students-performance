from fastapi import FastAPI
from typing import Optional
from inference import Inference
from pydantic import BaseModel

# declare Student data structure class
class Student(BaseModel):
    gender: str
    race: str
    parental_edu: str
    lunch: str
    test_prep: str
    math_score: float
    read_score: float
    write_score: float

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello World! - This message was sent from FastAPI"}

@app.post('/predict')
async def make_prediction(data: Student):
    data = data.dict()

    data = {
        'gender': data['gender'].lower(),
        'race/ethnicity': data['race'],
        'parental level of education': data['parental_edu'].lower(),
        'lunch': data['lunch'].lower(),
        'test preparation course': data['test_prep'],
        'math score': data['math_score'],
        'reading score': data['read_score'],
        'writing score': data['write_score']
    }    

    infer = Inference()
    predicted = infer.make_prediction(data)

    return {
        'predicted_score': predicted['predicted_score'][0]
    }

@app.get('/predict')
async def make_prediction(
    gender: str,
    race: str,
    parental_edu: str,
    lunch: str,
    test_prep: str,
    math_score: float,
    read_score: float,
    write_score: float,
    ):
    data = {
        'gender': gender.lower(),
        'race/ethnicity': race,
        'parental level of education': parental_edu.lower(),
        'lunch': lunch.lower(),
        'test preparation course': test_prep,
        'math score': math_score,
        'reading score': read_score,
        'writing score': write_score
    }    

    infer = Inference()
    predicted = infer.make_prediction(data)

    return {
        'predicted_score': predicted['predicted_score'][0]
    }