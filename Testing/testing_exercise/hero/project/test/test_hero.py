import unittest
from Testing.testing_exercise.hero.project.project.hero import Hero
# from project.hero import Hero


class HeroTests(unittest.TestCase):
    def setUp(self):
        username = "Brand"
        health = 100.0
        damage = 100.0
        level = 1
        self.hero = Hero(username, level, health, damage)
        username_enemy_1 = "Brand"
        health_enemy_1 = 100.0
        damage_enemy_1 = 100.0
        level_enemy_1 = 1
        self.enemy_1 = Hero(username_enemy_1, level_enemy_1, health_enemy_1, damage_enemy_1)
        username_enemy_2 = "Leona"
        health_enemy_2 = 100.0
        damage_enemy_2 = 100.0
        level_enemy_2 = 1
        self.enemy_2 = Hero(username_enemy_2, level_enemy_2, health_enemy_2, damage_enemy_2)
        username_enemy_3 = "Garen"
        health_enemy_3 = 10.0
        damage_enemy_3 = 5.0
        level_enemy_3 = 1
        self.enemy_3 = Hero(username_enemy_3, level_enemy_3, health_enemy_3, damage_enemy_3)
        username_enemy_4 = "Vayne"
        health_enemy_4 = 200.0
        damage_enemy_4 = 150.0
        level_enemy_4 = 1
        self.enemy_4 = Hero(username_enemy_4, level_enemy_4, health_enemy_4, damage_enemy_4)

    def test_init(self):
        self.assertEqual(self.hero.username, "Brand")
        self.assertEqual(self.hero.level, 1)
        self.assertEqual(self.hero.health, 100.0)
        self.assertEqual(self.hero.damage, 100.0)

    def test_battle_same_hero_name_raise_exception(self):
        with self.assertRaises(Exception) as context:
            self.hero.battle(self.enemy_1)
        expected_msg = str(context.exception)
        actual_msg = "You cannot fight yourself"
        self.assertEqual(expected_msg, actual_msg)

    def test_battle_hero_health_less_than_zero_raise_exception(self):
        with self.assertRaises(ValueError) as context:
            self.hero.health = -1
            self.hero.battle(self.enemy_2)
        expected_msg = str(context.exception)
        actual_msg = "Your health is lower than or equal to 0. You need to rest"
        self.assertEqual(expected_msg, actual_msg)

    def test_battle_enemy_health_less_than_zero_raise_exception(self):
        with self.assertRaises(ValueError) as context:
            self.enemy_2.health = -1
            self.hero.battle(self.enemy_2)
        expected_msg = str(context.exception)
        actual_msg = f"You cannot fight {self.enemy_2.username}. He needs to rest"
        self.assertEqual(expected_msg, actual_msg)

    def test_battle_draw_game(self):
        battle = self.hero.battle(self.enemy_2)
        self.assertEqual(battle, "Draw")

    def test_battle_hero_win(self):
        battle = self.hero.battle(self.enemy_3)
        self.assertEqual(battle, "You win")
        self.assertEqual(self.hero.level, 2)
        self.assertEqual(self.hero.health, 100)
        self.assertEqual(self.hero.damage, 105)

    def test_battle_enemy_win(self):
        battle = self.hero.battle(self.enemy_4)
        self.assertEqual(battle, "You lose")
        self.assertEqual(self.enemy_4.level, 2)
        self.assertEqual(self.enemy_4.health, 105)
        self.assertEqual(self.enemy_4.damage, 155)

    def test_str(self):
        expected_str = self.hero.__str__()
        actual_str = f"Hero Brand: 1 lvl\nHealth: 100.0\nDamage: 100.0\n"
        self.assertEqual(expected_str, actual_str)


if __name__ == "__main__":
    unittest.main()
