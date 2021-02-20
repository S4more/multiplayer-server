from events.join import Join
from .event_manager import EventManager
from user import Player

class ConnectionManager:
    connections = {}

    def __init__(self, eventManager: EventManager):
        ''' Creates the joinEvent on the eventManager '''
        # Also care about reconnections later
        self.joinE: Join = eventManager.add_event(Join)

    async def register(self, websocket) -> Player:
        # Can't make two connections from the same IP. That is bad.
        if websocket.remote_address[0] not in self.connections:
            self.connections[websocket.remote_address[0]] = Player(websocket)
            await self.joinE.notify(self.connections)
        else:
            self.connections[websocket.remote_address[0]].ws = websocket
            print('Someone reconnected!')
        return self.connections[websocket.remote_address[0]]

    async def unregister(self, websocket):
        del self.connections[websocket.remote_address[0]]
        await self.joinE.notify(self.connections)
