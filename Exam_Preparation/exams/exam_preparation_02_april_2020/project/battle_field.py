from project.player.beginner import Beginner
from project.player.player import Player
from project.card.card import Card


class BattleField:
    @staticmethod
    def fight(attacker, enemy):
        if attacker.is_dead or enemy.is_dead:
            raise ValueError("Player is dead!")

        # if isinstance(attacker, Beginner):
        #     attacker.health += 40
        #     for c in attacker.card_repository.cards:
        #         c.damage_points += 30
        #
        # if isinstance(enemy, Beginner):
        #     enemy.health += 40
        #     for c in enemy.card_repository.cards:
        #         c.damage_points += 30

        if attacker.__class__.__name__ == "Beginner":
            attacker.health += 40
            for c in attacker.card_repository.cards:
                c.damage_points += 30

        if enemy.__class__.__name__ == "Beginner":
            enemy.health += 40
            for c in enemy.card_repository.cards:
                c.damage_points += 30

        attacker.health += sum([c.health_points for c in attacker.card_repository.cards])
        enemy.health += sum([c.health_points for c in enemy.card_repository.cards])

        for c in attacker.card_repository.cards:
            # enemy.take_damage(c.damage_points)
            enemy.health -= c.damage_points

        for c in enemy.card_repository.cards:
            # attacker.take_damage(c.damage_points)
            attacker.health -= c.damage_points
