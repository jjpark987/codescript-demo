from app.config import add_cors_middleware
from app.crud import get_random_problem_dynamo
from app.schemas import LLMResponse
from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()
add_cors_middleware(app)

@app.get('/problems/random')
async def get_random_problem_route():
    return await get_random_problem_dynamo()

@app.get('/generate_feedback')
def generate_feedback_route():
    print("✅ Received /generate_feedback request")
    demo_response = {
        'analysis': 'This version is only for demo purposes.',
        'suggestions': [],
        'score': 3
    }
    return LLMResponse.model_validate(demo_response)

handler = Mangum(app)
