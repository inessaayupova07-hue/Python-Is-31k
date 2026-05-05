import asyncio
import random

async def task(i):
    delay = random.randint(1, 3)
    await asyncio.sleep(delay)
    print(f"Task {i} finished after {delay}s")

async def main():
    await asyncio.gather(*(task(i) for i in range(5)))

asyncio.run(main())
