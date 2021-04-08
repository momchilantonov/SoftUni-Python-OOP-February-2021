class PlayerRepository:
    def __init__(self):
        self.players = []
        # self.count = 0

    @property
    def count(self):
        return len(self.players)

    def add(self, player):
        if any(p.username == player.username for p in self.players):
            raise ValueError(f"Player {player.username} already exists!")
        self.players.append(player)
        # for pl in self.players:
        #     if pl.username == player.username:
        #         raise ValueError(f"Player {player.username} already exists!")
        # self.count += 1
        # self.players.append(player)

    def remove(self, player):

        if player == "":
            raise ValueError("Player cannot be an empty string!")
        current_player = self.find(player)
        self.players.remove(current_player)
        # self.count -= 1

    def find(self, username):
        current_player = [p for p in self.players if p.username == username][0]
        return current_player
        # for pl in self.players:
        #     if pl.username == username:
        #         return pl
