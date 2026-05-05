import asyncio

async def task(name):
    await asyncio.sleep(1)
    print(name)

async def main():
    tasks = [task(str(i)) for i in range(3)]
    await asyncio.gather(*tasks)

asyncio.run(main())
