from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from app.crud import get_random_problem_dynamo
from app.schemas import LLMResponse
from mangum import Mangum

app = FastAPI()

@app.get('/problems/random')
async def get_random_problem_route(request: Request):
    origin = request.headers.get("origin")
    result = await get_random_problem_dynamo()
    return JSONResponse(
        content=jsonable_encoder(result),
        headers={
            "Access-Control-Allow-Origin": origin,
            "Access-Control-Allow-Credentials": "true"
        }
    )

@app.get('/generate_feedback')
def generate_feedback_route(request: Request):
    print("✅ Received /generate_feedback request")
    demo_response = {
        'analysis': 'This version is only for demo purposes.',
        'suggestions': [],
        'score': 3
    }
    model = LLMResponse.model_validate(demo_response)
    return JSONResponse(
        content=jsonable_encoder(model),
        headers={
            "Access-Control-Allow-Origin": request.headers.get("origin"),
            "Access-Control-Allow-Credentials": "true"
        }
    )

handler = Mangum(app)
