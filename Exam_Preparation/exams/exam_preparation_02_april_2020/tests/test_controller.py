import unittest

from project.card.card_repository import CardRepository
from project.card.magic_card import MagicCard
from project.controller import Controller
from project.player.advanced import Advanced
from project.player.player_repository import PlayerRepository


class TEstController(unittest.TestCase):
    def setUp(self):
        self.controller = Controller()
        self.player = Advanced("Pesho")
        self.card = MagicCard("Magic")

    def test__init(self):
        self.assertIsInstance(self.controller.player_repository, PlayerRepository)
        self.assertIsInstance(self.controller.card_repository, CardRepository)

    def test__add_player__return_msg(self):
        self.assertEqual(self.controller.add_player("Beginner", "Ivan"), "Successfully added player of type Beginner with username: Ivan")

    def test__add_card_return_msg(self):
        self.assertEqual(self.controller.add_card("Magic", "Magic"), "Successfully added card of type MagicCard with name: Magic")

    def test__add_player_card_return_msg(self):
        # self.player.card_repository.add(self.card)
        self.controller.player_repository.add(self.player)
        self.controller.card_repository.add(self.card)
        self.assertEqual(self.controller.add_player_card("Pesho", "Magic"), "Successfully added card: Magic to user: Pesho")

    def test__fight__return_msg(self):
        player2 = Advanced("Ivan")
        self.controller.player_repository.add(player2)
        self.controller.player_repository.add(self.player)
        self.assertEqual(self.controller.fight("Pesho", "Ivan"), f"Attack user health {self.player.health} - Enemy user health {player2.health}")

    def test__report__return_msg(self):
        self.player.card_repository.add(self.card)
        self.controller.player_repository.add(self.player)
        self.assertEqual(self.controller.report(), f"Username: Pesho - Health: 250 - Cards 1\n### Card: Magic - Damage: 5\n")