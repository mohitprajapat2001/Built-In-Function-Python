import asyncio


async def async_iter():
    for num in range(4):
        await asyncio.sleep(2)
        yield num


async def main():
    async for res in aiter(async_iter()):
        print(res)


asyncio.run(main())