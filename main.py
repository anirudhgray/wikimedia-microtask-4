from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from utils import validate_url
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://127.0.0.1",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class UrlModel(BaseModel):
    url: str


@app.post("/", response_model=UrlModel)
async def root(urlObject: UrlModel):
    urlObject.url = urlObject.url.strip()
    error = validate_url(urlObject.url)
    if not error:
        return urlObject
    raise HTTPException(status_code=400, detail=error)
