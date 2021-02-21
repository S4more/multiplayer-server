import json
import asyncio
from .Events import Event

class Mouse(Event):
    type = "mouse_move"

    def handle(self, player, cords):
        player.mouse_cords = cords


    def response(self, users):
        return json.dumps({"type": self.type, "cords": [user.mouse_cords for user in users]})

    async def notify(self, users):
        if users:
            message = self.response(users)
            await asyncio.wait([users[user].ws.send(message) for user in users])
