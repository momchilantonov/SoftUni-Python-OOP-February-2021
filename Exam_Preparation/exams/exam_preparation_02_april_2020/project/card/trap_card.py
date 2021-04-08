from project.card.card import Card


class TrapCard(Card):
    # DMG = 120
    # HP = 5

    def __init__(self, name):
        super().__init__(name, 120, 5)

    # @staticmethod
    # def get_dmg():
    #     return TrapCard.DMG
    #
    # @staticmethod
    # def get_hp():
    #     return TrapCard.HP
