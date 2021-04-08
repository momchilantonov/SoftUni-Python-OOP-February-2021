import unittest

from project.card.card_repository import CardRepository
from project.card.magic_card import MagicCard


class TestCardRepository(unittest.TestCase):
    def setUp(self):
        self.cr = CardRepository()
        self.card = MagicCard("Pfuuu")

    def test__init(self):
        self.assertEqual(self.cr.cards, [])

    def test__count(self):
        self.assertEqual(self.cr.count, 0)

    def test__add_existing_card__raise_value_error(self):
        self.cr.add(self.card)
        with self.assertRaises(ValueError) as context:
            self.cr.add(self.card)
        expected_msg = str(context.exception)
        actual_msg = f"Card {self.card.name} already exists!"
        self.assertEqual(expected_msg, actual_msg)

    def test__add_card__append_player(self):
        self.cr.add(self.card)
        self.assertEqual(self.cr.cards[0], self.card)

    def test__remove_card_with_empty_string__raise_value_error(self):
        self.cr.add(self.card)
        with self.assertRaises(ValueError) as context:
            self.cr.remove("")
        expected_msg = str(context.exception)
        actual_msg = "Card cannot be an empty string!"
        self.assertEqual(expected_msg, actual_msg)

    def test__remove_card__sub_it_from_the_list(self):
        self.cr.add(self.card)
        self.cr.remove("Pfuuu")
        self.assertEqual(self.cr.count, 0)

    def test__find_card(self):
        self.cr.add(self.card)
        card_to_find = self.cr.find("Pfuuu")
        self.assertEqual(self.card, card_to_find)
