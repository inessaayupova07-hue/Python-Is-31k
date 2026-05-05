import asyncio

async def worker(name, q):
    while True:
        task = await q.get()
        if task is None:
            break
        print(f"{name} processing {task}")
        await asyncio.sleep(1)
        q.task_done()

async def main():
    q = asyncio.Queue()

    workers = [asyncio.create_task(worker(f"W{i}", q)) for i in range(3)]

    for i in range(5):
        await q.put(i)

    await q.join()

    for _ in workers:
        await q.put(None)

    await asyncio.gather(*workers)

asyncio.run(main())
