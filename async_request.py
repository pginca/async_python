import aiohttp


async def async_request(id):
    print(f'Start request with id {id}')
    async with aiohttp.ClientSession() as session:
        async with session.get(f'https://jsonplaceholder.typicode.com/todos/{id}') as response:
            await response.json()
    print(f'Done request with id {id}')
