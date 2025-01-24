# ytmdpy - Youtube Music Desktop Python


A Python API wrapper for the companion server for [ytmdesktop/ytmdesktop](https://github.com/ytmdesktop/ytmdesktop)


## Very simple example client
```python
from asyncio import run
import asyncio
from ytmdpy.client import Client

APP_ID = 000000000000000000000 # Any int of 2-32 long
APP_NAME = "Any string here"
APP_VERSION = "0.0.1" # A formatted version string

async def main() -> None:
    client = Client(
        app_id=APP_ID,
        app_name=APP_NAME,
        app_version=APP_VERSION,
    )
    await client.authenticate()
    while True:
        # Change song every 10 seconds.
        await client.next()
        await asyncio.sleep(10)

if __name__ == "__main__":
    run(main())
```

## If you save the authentication tokens (recommended)
```python
await client.authenticate(token="YOUR SAVED TOKEN HERE")
```
