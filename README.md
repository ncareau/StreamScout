StreamScout

A website and API to get stream information

![StreamScout Example](https://github.com/ncareau/StreamScout/raw/master/demo/demo.gif)

## Requirements

- Node with Yarn
- Python 3.7

## Configuration and running

### Docker

```bash
docker run -d --name streamscout \
    -p 80:80 \
    ncareau/streamscout
```

With a different port and API_URL

```bash
docker run -d --name streamscout \
    -p 8000:80 \
    -e VUE_APP_API_URL=http://localhost:8000
    ncareau/streamscout
```
