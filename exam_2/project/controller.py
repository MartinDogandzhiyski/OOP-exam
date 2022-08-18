class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    def find_player_by_name(self, name):
        for pl in self.players:
            if pl.name == name:
                return pl
        return False

    def add_player(self, *args):
        added_names = []
        for pl in args:
            if not pl in self.players:
                self.players.append(pl)
                added_names.append(pl.name)
        return f"Successfully added: {', '.join(added_names)}"

    def add_supply(self, *args):
        self.supplies.extend(args)

    def sustain(self, player_name, sustenance_type):
        player = self.find_player_by_name(player_name)
        if player:
            if sustenance_type == 'Food' or sustenance_type == 'Drink':
                if player.stamina == 100:
                    return f"{player_name} have enough stamina."
                for supply in range(len(self.supplies) - 1, 0, -1):
                    name = self.supplies[supply].name
                    if self.supplies[supply].__class__.__name__ == sustenance_type:
                        if player.stamina + self.supplies[supply].energy >= 100:
                            player.stamina = 100
                        else:
                            player.stamina += self.supplies[supply].energy
                        self.supplies.pop(supply)
                        return f"{player_name} sustained successfully with {name}."
            if sustenance_type == 'Food':
                raise Exception("There are no food supplies left!")
            elif sustenance_type == 'Drink':
                raise Exception("There are no drink supplies left!")

    def duel(self, first_player_name, second_player_name):
        first_player = self.find_player_by_name(first_player_name)
        second_player = self.find_player_by_name(second_player_name)
        if first_player.stamina == 0 and second_player.stamina == 0:
            return f"Player {first_player_name} does not have enough stamina.\nPlayer {second_player_name} does not have enough stamina."
        elif first_player.stamina == 0:
            return f"Player {first_player_name} does not have enough stamina."
        elif second_player.stamina == 0:
            return f"Player {second_player_name} does not have enough stamina."
        if first_player.stamina < second_player.stamina:

            if second_player.stamina - 0.5 * first_player.stamina <= 0:
                second_player.stamina = 0
                return f"Winner: {first_player_name}"
            else:
                second_player.stamina -= 0.5 * first_player.stamina

            if first_player.stamina - 0.5 * second_player.stamina <= 0:
                first_player.stamina = 0
                return f"Winner: {second_player_name}"
            else:
                first_player.stamina -= 0.5 * second_player.stamina
        else:

            if first_player.stamina - 0.5 * second_player.stamina <= 0:
                first_player.stamina = 0
                return f"Winner: {second_player_name}"
            else:
                first_player.stamina -= 0.5 * second_player.stamina
            if second_player.stamina - 0.5 * first_player.stamina <= 0:

                second_player.stamina = 0
                return f"Winner: {first_player_name}"
            else:
                second_player.stamina -= 0.5 * first_player.stamina

        if first_player.stamina > second_player.stamina:
            return f"Winner: {first_player_name}"
        else:
            return f"Winner: {second_player_name}"

    def next_day(self):
        for pl in self.players:
            if pl.stamina - pl.age * 2 <= 0:
                pl.stamina = 0
            else:
                pl.stamina -= pl.age * 2
        for pl in self.players:
            self.sustain(pl.name, 'Food')
            self.sustain(pl.name, 'Drink')

    def __str__(self):
        result = ''
        for pl in self.players:
            result += str(pl) + '\n'
        for supply in self.supplies:
            result += supply.details() + '\n'
        return result.strip()

