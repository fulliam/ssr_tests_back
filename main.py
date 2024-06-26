import uvicorn
from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.middleware.cors import CORSMiddleware
from routes import getCombinations
from routes import getQuestions

app = FastAPI(
    title='API',
    version='1.0.0',
    # debug=False
)

app.include_router(getCombinations.router, prefix="/api")
app.include_router(getQuestions.router, prefix="/api")

origins = [
    "http://127.0.0.1:8080",
    "http://127.0.0.1:8080/",
    "http://localhost:8080",
    "http://localhost:8080/",
    "http://localhost:8001",
    "http://localhost:8001/",
    "http://192.168.1.94:8080",
    "http://192.168.1.94:8080/",
    "http://192.168.1.94",
    "http://192.168.1.94/",
    "http://192.168.1.126:8080",
    "http://192.168.1.126:8080/",
    "http://192.168.1.126",
    "http://192.168.1.126/",
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