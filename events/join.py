import json
import asyncio
from .Events import Event

class Join(Event):
    type = "users"

    def handle(self, USERS, websocket):
        USERS.add(websocket)

    def response(self, USERS):
        return json.dumps({"type": "users", "count": len(USERS)})

    async def notify(self, USERS):
        if USERS:
            message = self.response(USERS)
            await asyncio.wait([user.send(message) for user in USERS])
