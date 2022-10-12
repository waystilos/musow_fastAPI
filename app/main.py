from datetime import datetime

from fastapi import FastAPI

from app.twitter_service import get_twitter_response

app = FastAPI()


@app.get("/")
def time_root():
    return datetime.utcnow()


@app.get("/search/")
def read_item(word: str, start: datetime, end: datetime, token: str):
    query_response = {"word": word, "start": start, "end": end, "token": token}

    # call twit service to get back response
    twit_response = get_twitter_response(query_response)

    return query_response
