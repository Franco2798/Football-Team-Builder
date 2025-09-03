from Enums import E
from C01_Player import Player

class Team:
    # this is a skeleton class it will be added to later.
    
    def __init__(self, name = 'Default Team', players=[]):
        self.players = players
        self.name = name

    def add_player(self, player):
        self.players.append(player)
    
    def get_players_at_position(self, position):
        # returns a list of players with whose position == position
        players_with_position = [player for player in self.players if player.position[1] == position]
        return players_with_position

    # you can add stuff here that makes your life easier. I have included some of the ones I used below.

    def get_players_on_field(self):
        # this is a helper function
        # returns a list of players where on_field == True
        players_on_field = [player for player in self.players if player.on_field == True]
        return players_on_field
        
    def create_default_team(self):
        # this populates the team with players the number for each position is the third argument in E positions
        # E.QB[2] --> 2
        # E.RB[2] --> 3
        # reminder E.POSITIONS is a list of all positions
        self.players = []
        for p in E.POSITIONS:
            for _ in range(p[2]):
                player = Player(p)
                self.players.append(player)
                  
    def get_name_and_position_of_players_on_field(self):
        # this is used for testing purposes it is not directly necessary
        players_on_field = self.get_players_on_field()
        name_and_position = []
        for player in players_on_field:
            name = player.name
            position = player.position
            # name_and_position.append([name, position[1]])
            name_and_position.append(player.location)
        return name_and_position

def main_test_team():
    print('main test team:')
    t = Team()
    t.create_default_team()
    
    
    print(f"Team name: {t.name}")
    print(f"Total players: {len(t.players)}")
    
   
    print("\nPlayers in team:")
    for player in t.players:
        print(f"Name: {player.name}, Position: {player.position[1]}, Jersey Number: {player.number}")


    position = 'LG'
    players_at_position = t.get_players_at_position(position)
    print(f"\nPlayers at position {position}:")
    for player in players_at_position:
        print(f"Name: {player.name}, Position: {player.position[1]}, Jersey Number: {player.number}")
    
    players_on_field = t.get_players_on_field()
    print("\nPlayers on field:")
    for player in players_on_field:
        print(f"Name: {player.name}, Position: {player.position[1]}, Jersey Number: {player.number}")
    
    name_and_position = t.get_name_and_position_of_players_on_field()
    print("\nName and position of players on field:")
    for name, position in name_and_position:
        print(f"Name: {name}, Position: {position}")
