from fastapi import FastAPI
from schemas import InputSchema, OutputSchema
from predict import make_prediction

app = FastAPI()

#batch predictions, the endpoint should accept the list of inputs 
@app.get('/')
def index():
    return {'message' : 'Welcome to the ML Model'}

@app.post('/prediction', response_model=OutputSchema)
def predict(user_input: InputSchema):
    prediction = make_prediction(user_input.model_dump())
    return OutputSchema(predicted_price=round(prediction,2))
