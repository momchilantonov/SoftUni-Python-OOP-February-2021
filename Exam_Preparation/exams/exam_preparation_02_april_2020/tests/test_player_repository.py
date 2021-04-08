import unittest

from project.player.advanced import Advanced
from project.player.player_repository import PlayerRepository


class TestPlayerRepository(unittest.TestCase):
    def setUp(self):
        self.pr = PlayerRepository()
        self.player = Advanced("Pesho")

    def test__init(self):
        self.assertEqual(self.pr.players, [])
        # self.pr.players.append(self.player)

    def test__count(self):
        self.assertEqual(self.pr.count, 0)

    def test__add_existing_player__raise_value_error(self):
        self.pr.add(self.player)
        with self.assertRaises(ValueError) as context:
            self.pr.add(self.player)
        expected_msg = str(context.exception)
        actual_msg = f"Player {self.player.username} already exists!"
        self.assertEqual(expected_msg, actual_msg)

    def test__add_player__append_player(self):
        self.pr.add(self.player)
        self.assertEqual(self.pr.players[0], self.player)

    def test__remove_player_with_empty_string__raise_value_error(self):
        self.pr.add(self.player)
        with self.assertRaises(ValueError) as context:
            self.pr.remove("")
        expected_msg = str(context.exception)
        actual_msg = "Player cannot be an empty string!"
        self.assertEqual(expected_msg, actual_msg)

    def test__remove_player__sub_him_from_the_list(self):
        self.pr.add(self.player)
        self.pr.remove("Pesho")
        self.assertEqual(self.pr.count, 0)

    def test__find_player(self):
        self.pr.add(self.player)
        player_to_find = self.pr.find("Pesho")
        self.assertEqual(self.player, player_to_find)


if __name__ == "__main__":
    unittest.main()
