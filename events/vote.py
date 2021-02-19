import json
import asyncio
from .Events import Event

class Vote(Event):
    type = "plus"
    current = 0

    def handle(self, value):
        self.current = self.current + 1 if value == "plus" else self.current - 1

    def response(self):
        return json.dumps({"type": "current", "value": self.current})

    async def notify(self, USERS):
        if USERS:
            message = self.response()
            await asyncio.wait([user.send(message) for user in USERS])
