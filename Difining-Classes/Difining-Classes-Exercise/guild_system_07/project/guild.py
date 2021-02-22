from player import Player


class Guild:
    def __init__(self, name):
        self.name = name
        self.list_of_players = []

    def assign_player(self, player):
        if player.guild == "Unaffiliated":
            player.guild = self.name
            self.list_of_players.append(player)
            return f"Welcome player {player.name} to the guild {self.name}"
        if player.guild == self.name:
            return f"Player {player.name} is already in the guild."
        return f"Player {player.name} is in another guild."

    def kick_player(self, player_name):
        for player in self.list_of_players:
            if player.name == player_name:
                player.guild = "Unaffiliated"
                self.list_of_players.remove(player)
                return f"Player {player_name} has been removed from the guild."
        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        result = f"Guild: {self.name}\n"
        for p in self.list_of_players:
            result += p.player_info()
        return result


player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())
print(guild.kick_player(player))
