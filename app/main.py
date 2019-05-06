from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles
from starlette.responses import HTMLResponse
import streamlink
import uvicorn


app = FastAPI()

origins = [
    "http://localhost:8081",
    "https://localhost.tiangolo.com",
    "http:localhost",
    "http:localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="app/static"), name="static")


@app.get("/")
def read_root():
    f = open("app/static/index.html", "r")
    html_content = f.read()
    return HTMLResponse(content=html_content, status_code=200)


@app.post("/url")
def api(url: str):
    streams = streamlink.streams(url)

    out = {}
    for quality, stream in streams.items():
        out[quality] = stream.url

    return {"data": {"streams": out}}


@app.get("/twitch/{user}")
def twitch(user: str):
    streams = streamlink.streams("http://twitch.tv/" + user)

    out = {}
    for quality, stream in streams.items():
        out[quality] = stream.url

    return {"data": {"streams": out}}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)