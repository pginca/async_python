import asyncio
from time import time

from async_request import async_request


async def main():
    ts = time()

    results = []
    for id in range(1, 101):
        results.append(asyncio.create_task(async_request(id)))
    
    await asyncio.wait(results)

    print(f'Took {time() - ts} seconds')


if __name__ == '__main__':
    asyncio.run(main())