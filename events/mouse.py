import json
import asyncio
from .Events import Event

class Mouse(Event):
    type = "mouse_move"
    mouse_cords = {}

    def handle(self, player, cords):
        self.mouse_cords[player] = cords
        player.mouse_cords = cords


    def response(self):
        return json.dumps({"type": self.type, "cords": [self.mouse_cords[ws] for ws in self.mouse_cords]})

    async def notify(self, users):
        if users:
            message = self.response()
            await asyncio.wait([users[user].ws.send(message) for user in users])
