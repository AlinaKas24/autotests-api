import asyncio
import websockets


async def client():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        message = "Hi,server!"
        print(f"Send:{message}")
        await websocket.send(message)
        for _ in range(5):
            response = await websocket.recv()
            print(f"Request from server:{response}")


asyncio.run(client())
