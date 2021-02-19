from events.join import Join
from .event_manager import EventManager

class ConnectionManager:
    connections = set()

    def __init__(self, eventManager: EventManager):
        self.joinE: Join = eventManager.add_event(Join)

    async def register(self, websocket):
        self.connections.add(websocket)
        await self.joinE.notify(self.connections)

    async def unregister(self, websocket):
        self.connections.remove(websocket)
        await self.joinE.notify(self.connections)
