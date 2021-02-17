import asyncio
import websockets
import logging
import json

STATE = {"value": 0}

logging.basicConfig()

USERS = set()
mouse_moves = {}


async def hello(websocket, path):
    name = await websocket.recv()
    print(f"< {name}")
    greeting = f"Hello, {name}!"

    await websocket.send(greeting)
    print(f"> {greeting}")


def state_event():
    return json.dumps({"type": "state", **STATE})

def user_event():
    return json.dumps({"type": "users", "count": len(USERS)})

def cords_event():
    return json.dumps({"type": "mouse_move", "cords": [mouse_moves[ws] for ws in mouse_moves]})

async def notify_users():
    if USERS:   # asyncio doesn't accept an empty lsit
        message = user_event()
        await asyncio.wait([user.send(message) for user in USERS])

async def notify_state():
    if USERS:   # asyncio doesn't accept an empty lsit
        message = state_event()
        await asyncio.wait([user.send(message) for user in USERS])

async def notify_cords():
    if USERS:
        message = cords_event()
        await asyncio.wait([user.send(message) for user in USERS])

async def register(websocket):
    USERS.add(websocket)
    await notify_users()

async def unregister(websocket):
    USERS.remove(websocket)
    await notify_users()

async def counter(websocket, path):
    await register(websocket)
    try:
        await websocket.send(state_event())
        async for message in websocket:
            data = json.loads(message)
            print(data)
            if data["action"] == "minus":
                STATE["value"] -= 1
                await notify_state()
            elif data["action"] == "plus":
                STATE["value"] += 1
                await notify_state()
            elif data["action"] == "mouse_move":
                mouse_moves[websocket] = data["cords"]
                await notify_cords()

            else:
                logging.error(f"unsupported event: {data}")
    finally:
        await unregister(websocket)


start_server = websockets.serve(counter, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
