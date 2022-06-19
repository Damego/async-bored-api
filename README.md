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
  client = BoredClient()
  activity = await client.get_by_type(ActivityType.BUSYWORK)
  print(activity.activity)

asyncio.run(main())
```
