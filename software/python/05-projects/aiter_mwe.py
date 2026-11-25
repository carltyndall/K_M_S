import asyncio


async def numbers():
    yield 1
    yield 2


async def main():
    iterator = aiter(numbers())
    async for number in iterator:
        print("number:", number)


asyncio.run(main())