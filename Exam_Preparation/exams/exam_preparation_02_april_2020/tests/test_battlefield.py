import unittest

from project.battle_field import BattleField
from project.card.magic_card import MagicCard
from project.player.advanced import Advanced
from project.player.beginner import Beginner


class TestBattleField(unittest.TestCase):
    def setUp(self):
        self.attacker = Advanced("Pesho")
        self.enemy = Beginner("Gosho")
        self.card = MagicCard("FukUFuk")
        self.battlefield = BattleField()

    def test__attacker_is_dead__raise_value_error(self):
        self.attacker.health = 0
        with self.assertRaises(ValueError) as context:
            self.battlefield.fight(self.attacker, self.enemy)
        expected_msg = str(context.exception)
        actual_msg = "Player is dead!"
        self.assertEqual(expected_msg, actual_msg)

    def test__enemy_bonus_when_beginner(self):
        self.enemy.card_repository.cards.append(self.card)
        self.battlefield.fight(self.attacker, self.enemy)
        self.assertEqual(self.enemy.health, 170)
        self.assertEqual(self.card.damage_points, 35)

    def test__player_taken_dmg(self):
        self.enemy.card_repository.cards.append(self.card)
        self.battlefield.fight(self.attacker, self.enemy)
        self.assertEqual(self.attacker.health, 215)


if __name__ == "__main__":
    unittest.main()
