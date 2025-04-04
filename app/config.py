from fastapi import HTTPException
from threading import Lock

request_lock = Lock()

def processing_limiter():
    if not request_lock.acquire(blocking=False):
        raise HTTPException(status_code=429, detail='⏳ Request already in progress. Please wait.')
