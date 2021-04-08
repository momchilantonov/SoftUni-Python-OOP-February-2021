class CardRepository:
    def __init__(self):
        # self.count = 0
        self.cards = []

    @property
    def count(self):
        return len(self.cards)

    def add(self, card):
        if any(c.name == card.name for c in self.cards):
            raise ValueError(f"Card {card.name} already exists!")
        self.cards.append(card)
        # for c in self.cards:
        #     if c.name == card.name:
        #         raise ValueError(f"Card {card.name} already exists!")
        # self.count += 1
        # self.cards.append(card)

    def remove(self, card):
        if card == "":
            raise ValueError("Card cannot be an empty string!")
        current_card = self.find(card)
        # self.count -= 1
        self.cards.remove(current_card)

    def find(self, name):
        current_card = [c for c in self.cards if c.name == name][0]
        return current_card
        # for c in self.cards:
        #     if c.name == name:
        #         return c
