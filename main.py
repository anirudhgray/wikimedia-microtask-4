from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from utils import validate_url


class UrlModel(BaseModel):
    url: str


app = FastAPI()


@app.post("/", response_model=UrlModel)
async def root(urlObject: UrlModel):
    urlObject.url = urlObject.url.strip()
    error = validate_url(urlObject.url)
    if not error:
        return urlObject
    raise HTTPException(status_code=400, detail=error)
