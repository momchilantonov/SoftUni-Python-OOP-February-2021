from project.player.player import Player


class Advanced(Player):
    # INIT_HP = 250

    def __init__(self, username):
        super().__init__(username, 250)

    # @staticmethod
    # def get_init_hp():
    #     return Advanced.INIT_HP
