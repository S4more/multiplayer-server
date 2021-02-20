import json
import asyncio
from .Events import Event

class Vote(Event):
    type = "vote"
    current = 0

    def handle(self, player, value):
        print(f"Player {player.ws.remote_address} just voted")
        self.current = self.current + 1 if value == "plus" else self.current - 1

    def response(self):
        return json.dumps({"type": "current", "value": self.current})

    async def notify(self, USERS):
        if USERS:
            message = self.response()
            await asyncio.wait([USERS[user].ws.send(message) for user in USERS])
