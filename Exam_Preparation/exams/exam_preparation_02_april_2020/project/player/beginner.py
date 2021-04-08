from project.player.player import Player


class Beginner(Player):
    # INIT_HP = 50

    def __init__(self, username):
        super().__init__(username, 50)

    # @staticmethod
    # def get_init_hp():
    #     return Beginner.INIT_HP
