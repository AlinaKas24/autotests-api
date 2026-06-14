import asyncio
import time


def fetch_data():
    print("Fetching data ...")
    time.sleep(2)


for _ in range(5):
    fetch_data()


async def async_fetch_data():
    print("Fetching data async...")
    await asyncio.sleep(2)


loop = asyncio.new_event_loop()
task = [
    loop.create_task(async_fetch_data()),
    loop.create_task(async_fetch_data()),
    loop.create_task(async_fetch_data()),
    loop.create_task(async_fetch_data()),
    loop.create_task(async_fetch_data()),
    loop.create_task(async_fetch_data()),
]
loop.run_until_complete(asyncio.wait(task))
