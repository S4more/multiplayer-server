import asyncio
import websockets
import logging
import json
from events.mouse import Mouse
from events.join import Join
from events.vote import Vote

from managers.connection_manager import ConnectionManager
from managers.event_manager import EventManager

STATE = {"value": 0}

logging.basicConfig()

eventManager = EventManager()
connectionManager = ConnectionManager(eventManager)

USERS = set()
mouse = Mouse()

async def counter(websocket, path): #CHANGE TO RECEIVER
    await connectionManager.register(websocket)
    try:
        #This needs to be changed for "on join" methods
        await websocket.send(eventManager.getEventByClassName("Vote").response())
        async for message in websocket: # It stays here until the user closes the connection.
            data = json.loads(message)


            #We are not passing who is the caller to the event. Should everyone
            #have the right to access the caller socket? What if we had something like
            #a class that holds a reference to the connections, to the caller... etc

            await eventManager.forward_event(data, connectionManager.connections)
            if data["action"] == "mouse_move":
                mouse.handle(websocket, data["cords"])
                await mouse.notify(USERS)
            else:
                logging.error(f"unsupported event: {data}")
    finally:
        await connectionManager.unregister(websocket)


start_server = websockets.serve(counter, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
