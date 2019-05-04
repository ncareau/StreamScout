from fastapi import FastAPI
from starlette.staticfiles import StaticFiles
from starlette.responses import HTMLResponse

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/")
def read_root():
    f = open("app/static/index.html", "r")
    html_content = f.read()
    return HTMLResponse(content=html_content, status_code=200)

@app.get("/api/{url}")
def api(url: str):



    return {"url": url}

@app.get("/twitch/{user}")
def twitch(user: str):


    return {"user": user}