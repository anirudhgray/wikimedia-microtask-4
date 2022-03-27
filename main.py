from fastapi import FastAPI
from pydantic import BaseModel


class UrlModel(BaseModel):
    url: str


app = FastAPI()


"""
Heuristic:
- No google search results.
"""


@app.post("/")
async def root(urlObject: UrlModel):
    url = urlObject.url
    print(url)
    return urlObject
