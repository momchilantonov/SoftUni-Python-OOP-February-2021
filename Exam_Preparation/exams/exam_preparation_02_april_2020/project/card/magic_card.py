from project.card.card import Card


class MagicCard(Card):
    # DMG = 5
    # HP = 80

    def __init__(self, name):
        super().__init__(name, 5, 80)

    # @staticmethod
    # def get_dmg():
    #     return MagicCard.DMG
    #
    # @staticmethod
    # def get_hp():
    #     return MagicCard.HP
