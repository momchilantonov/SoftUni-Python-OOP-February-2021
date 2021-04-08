import unittest
from project.card.card_repository import CardRepository
from project.player.beginner import Beginner


class TestBeginnerPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Beginner("IvanVeliki")

    def test_init(self):
        self.assertEqual(self.player.username, "IvanVeliki")
        self.assertEqual(self.player.health, 50)
        self.assertIsInstance(self.player.card_repository, CardRepository)


if __name__ == "__main__":
    unittest.main()
