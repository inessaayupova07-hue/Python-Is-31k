import asyncio

async def read_file(name):
    await asyncio.sleep(1)
    print(f"Read {name}")

async def main():
    await asyncio.gather(*(read_file(f"file{i}") for i in range(3)))

asyncio.run(main())
