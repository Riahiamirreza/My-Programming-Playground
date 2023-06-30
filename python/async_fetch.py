import asyncio
import secrets

import requests


URL = 'http://google.com/{sub}'

async def fetch(url: str):
    async def get(url: str):
        return requests.get(url)

    r = await get(url)
    return r

async def main():
    return await asyncio.gather(*(fetch(URL.format(sub=secrets.token_hex(10))) for _ in range(10)))


print(

    asyncio.run(main())    

)
