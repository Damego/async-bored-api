# async-bored-api
The unofficial async API wrapper for http://www.boredapi.com/

## Installing
`pip install --upgrade bored_api`

## Usage
Here is simple example of usage.
```py
import asyncio

import bored_api

async def main():
  client = bored_api.BoredClient()
  activity = await client.get_by_type(bored_api.ActivityType.BUSYWORK)
  print(activity.activity)

asyncio.run(main())
```

## Documentation and API Reference:

https://damego.gitbook.io/async-bored-api/
