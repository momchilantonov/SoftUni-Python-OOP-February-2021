from project.player import Player


class Guild:
    def __init__(self, name):
        self.name = name
        self.list_of_players = []

    def assign_player(self, p):
        if p.guild == "Unaffiliated":
            p.guild = self.name
            self.list_of_players.append(p)
            return f"Welcome player {p.name} to the guild {self.name}"
        if p.guild == self.name:
            return f"Player {p.name} is already in the guild."
        return f"Player {p.name} is in another guild."

    def kick_player(self, player_name):
        for p in self.list_of_players:
            if p.name == player_name:
                p.guild = "Unaffiliated"
                self.list_of_players.remove(p)
                return f"Player {player_name} has been removed from the guild."
        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        result = f"Guild: {self.name}\n"
        for p in self.list_of_players:
            result += p.player_info()
        return result


# player = Player("George", 50, 100)
# print(player.add_skill("Shield Break", 20))
# print(player.player_info())
# guild = Guild("UGT")
# print(guild.assign_player(player))
# print(guild.guild_info())


"""
Skill Shield Break added to the collection of the player George
Name: George
Guild: Unaffiliated
HP: 50
MP: 100
===Shield Break – 20

Welcome player George to the guild UGT
Guild: UGT
Name: George
Guild: UGT
HP: 50
MP: 100
===Shield Break – 20

"""