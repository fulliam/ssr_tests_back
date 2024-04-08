import logging
import uvicorn
from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.middleware.cors import CORSMiddleware
from routes import getCombinations
from datetime import datetime

# logging.getLogger().setLevel(logging.CRITICAL)
# logging.basicConfig(
#     level=logging.INFO,
#     format="%(asctime)s [%(levelname)s] %(message)s",
#     datefmt='%Y-%m-%d %H:%M:%S',
#     handlers=[logging.StreamHandler()]
# )

# log =

app = FastAPI(
    title='API',
    version='1.0.0',
    # debug=False
)

@app.middleware("http")
async def log_requests(request: Request, call_next):
    logging.info(f"Incoming request: {request.method} {request.url}")
    start_time = datetime.now()
    response = await call_next(request)
    process_time = (datetime.now() - start_time).total_seconds()
    logging.info(f"Request processing time: {process_time}s")
    return response

app.include_router(getCombinations.router, prefix="/api")

origins = [
    "http://127.0.0.1:8080",
    "http://127.0.0.1:8080/",
    "http://localhost:8080",
    "http://localhost:8080/",
    "http://localhost:8001",
    "http://localhost:8001/",
    # "http://192.168.1.39:8080",
    # "http://192.168.1.39:8080/",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == '__main__':
    uvicorn.run(
        'main:app', port=5050, host='0.0.0.0',
        reload=True)