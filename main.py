import asyncio
import websockets
import logging
import json

from user import Player

from managers.connection_manager import ConnectionManager
from managers.event_manager import EventManager

logging.basicConfig()
eventManager = EventManager()
connectionManager = ConnectionManager(eventManager)

async def counter(websocket, path): #CHANGE TO RECEIVER
    player = await connectionManager.register(websocket)
    try:
        #This needs to be changed for "on join" methods
        await websocket.send(eventManager.getEventByClassName("Vote").response())

        async for message in websocket: # It stays here until the user closes the connection.
            data = json.loads(message)
            await eventManager.forward_event(data, player, connectionManager.connections)
    finally:
        await connectionManager.unregister(websocket)


start_server = websockets.serve(counter, port=8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
