import unittest
from project.card.card_repository import CardRepository
from project.player.advanced import Advanced


class TestAdvancedPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Advanced("IvanVeliki")

    def test_init(self):
        self.assertEqual(self.player.username, "IvanVeliki")
        self.assertEqual(self.player.health, 250)
        self.assertIsInstance(self.player.card_repository, CardRepository)

    def test__set_username_to_empty_string__raise_value_error(self):
        with self.assertRaises(ValueError) as context:
            self.player.username = ""
        expected_msg = str(context.exception)
        actual_msg = "Player's username cannot be an empty string."
        self.assertEqual(expected_msg, actual_msg)

    def test__set_player_hp_below_zero__raise_value_error(self):
        with self.assertRaises(ValueError) as context:
            self.player.health = -1
        expected_msg = str(context.exception)
        actual_msg = "Player's health bonus cannot be less than zero."
        self.assertEqual(expected_msg, actual_msg)

    def test__set_player_is_dead__return_true(self):
        self.player.health = 0
        self.assertTrue(self.player.is_dead)

    def test__set_player_not_dead_return_false(self):
        self.player.health = 10
        self.assertFalse(self.player.is_dead)

    def test__set_dmg_below_zero__raise_value_error(self):
        with self.assertRaises(ValueError) as context:
            self.player.take_damage(-1)
        expected_msg = str(context.exception)
        actual_msg = "Damage points cannot be less than zero."
        self.assertEqual(expected_msg, actual_msg)

    def test__set_dmg_above_zero__take_player_hp(self):
        self.player.health = 10
        self.player.take_damage(5)
        self.assertEqual(self.player.health, 5)


if __name__ == "__main__":
    unittest.main()
