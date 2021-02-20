class Player:
    def __init__(self, websocket):
        self.ws = websocket
        self.mouse_cords = [0, 0]
        self.player_cords = [0, 0]
