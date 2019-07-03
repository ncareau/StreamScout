from fastapi import FastAPI, HTTPException
from starlette.middleware.gzip import GZipMiddleware
from starlette.staticfiles import StaticFiles
from starlette.responses import HTMLResponse
import uvicorn
from streamlink import NoStreamsError, NoPluginError, PluginError, Streamlink

app = FastAPI()

app.add_middleware(GZipMiddleware, minimum_size=1000)

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def read_root():
  f = open("static/index.html", "r")
  html_content = f.read()
  return HTMLResponse(content=html_content, status_code=200)


@app.get("/streamlink")
def api(url: str):
  streamlink = Streamlink()

  try:
    plugin = streamlink.resolve_url(url)
    streams = plugin.streams()
  except NoPluginError as e:
    raise HTTPException(status_code=500, detail="Streamlink is unable to handle the URL '{0}'".format(url))
  except PluginError as e:
    if e.__str__().startswith('Unable to find channel'):
      raise HTTPException(status_code=404, detail="Stream not found")
    raise HTTPException(status_code=500, detail="Error while fetching stream - " + str(e))
  except Exception:
    raise HTTPException(status_code=500, detail="Error while fetching stream")

  out = {}
  for quality, stream in streams.items():
    out[quality] = stream.url

  live = False
  if len(streams.items()) > 0:
    live = True

  try:
    id = plugin.channel_id
  except:
    id = plugin.video_id

  try:
    channel = plugin.channel
  except:
    channel = None

  return {'streams': out, 'url': url, 'channel': {'live': live, 'id': id, 'plugin': plugin.module, 'author': plugin.author, 'channel': channel, 'url': plugin.url, 'title': plugin.title}}

if __name__ == "__main__":
  uvicorn.run(app, host="0.0.0.0", port=8000)
