from fastapi import FastAPI
from fastapi.responses import JSONResponse
from inference import Inference
from pydantic import BaseModel


# define body payload schema
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
    return JSONResponse(
        content={"message": "Hello World! - This message was sent from FastAPI"}
    )


@app.post("/predict")
async def make_prediction(data: Student):
    data = data.model_dump()

    data = {
        "gender": data["gender"].lower(),
        "race/ethnicity": data["race"],
        "parental level of education": data["parental_edu"].lower(),
        "lunch": data["lunch"].lower(),
        "test preparation course": data["test_prep"],
        "math score": data["math_score"],
        "reading score": data["read_score"],
        "writing score": data["write_score"],
    }

    infer = Inference()
    predicted = infer.make_prediction(data)

    return JSONResponse(content={"predicted_score": predicted["predicted_score"][0]})
