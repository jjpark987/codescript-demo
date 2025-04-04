from app.config import processing_limiter
from app.crud import get_random_problem_dynamo
from app.schemas import LLMResponse
from fastapi import FastAPI, Depends
from fastapi.staticfiles import StaticFiles

app = FastAPI()

@app.get('/problems/random')
async def get_random_problem_route():
    return await get_random_problem_dynamo()

@app.post('/generate_feedback', dependencies=[Depends(processing_limiter)])
def generate_feedback_route():
    demo_response = {
        'analysis': 'This version is only for demo purposes.',
        'suggestions': [],
        'score': 3
    }
    return LLMResponse.model_validate(demo_response)

app.mount('/', StaticFiles(directory='dist', html=True), name='dist')
