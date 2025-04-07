from app.database import get_dynamo_table
from app.schemas import ProblemResponse
from app.util import get_signed_image_url_s3
from os.path import basename
from random import choice

async def get_random_problem_dynamo() -> dict:
    response = get_dynamo_table().scan()
    items = response.get('Items', [])
    if not items:
        raise Exception('Random problem not found')

    item = choice(items)
    
    signed_urls = [get_signed_image_url_s3('images/' + basename(path)) for path in item.get('image_paths', [])]

    return {
        'problem': ProblemResponse.model_validate(item),
        'image_urls': signed_urls
    }
