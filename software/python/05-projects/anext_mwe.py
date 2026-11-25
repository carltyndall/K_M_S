import asyncio


async def numbers():
    yield 10


async def main():
    iterator = aiter(numbers())
    print("first:", await anext(iterator))
    print("exhausted:", await anext(iterator, "no more"))


asyncio.run(main())