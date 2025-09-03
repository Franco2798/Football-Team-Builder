from C02_Team import Team as T
from C01_Player import Player as P

'''
--------------------- secondary defense :   [0]
--------------------- linebackers:          [1]
--------------------- defensive line        [2]
--------------------- offensive line        [3]
--------------------- qb/ wrs off line      [4]
--------------------- shotgun qb/ fb        [5]
--------------------- rbs                   [6]
'''

'''
012345678901234567890
--------------------- secondary defense :   [0]
--------------------- linebackers:          [1]
--------------------- defensive line        [2]
--------TGCGT-------- offensive line        [3] T (on the left) location 71  and col,row 8,4 
--------------------- qb/ wrs off line      [4]
--------------------- shotgun qb/ fb        [5]
--------------------- rbs                   [6]
'''

class Field:
    COLS = 21
    ROWS = 7
    def __init__(self):
        self.grid = [[" - " for _ in range(self.ROWS)] for _ in range(self.COLS)]
    
    def update_grid(self, offense:T, defense:T):
        valid = False
        if offense is not None:
            players = offense.get_players_on_field()
            
            if players is not None:
                valid = True
                for player in players:
                    player:P
                    try:            
                        col, row = player.get_col_row_from_location()
                    except:
                        col, row = player.get_col_row_from_location()
                    try:
                        self.grid[col][row] = ' ' + player.position[1]
                    except:
                        print(col,row)
        
        if defense is not None:
            players = defense.get_players_on_field()
            if players is not None:
                valid = True
                for player in players:
                    player:P
                    try:            
                        col, row = player.get_col_row_from_location()
                    except:
                        col, row = player.get_col_row_from_location()
                    try:
                        self.grid[col][row] = ' ' + player.position[1]
                    except:
                        print(col,row)
                
            else:
                print('Empty field no players on offense or defense or their locations are not set.')
        if valid:
            return True
        else:
            print('No players detected on offense or defense')
            return False

    def display_grid(self):
        for rw in range(self.ROWS):
            row = ""
            for c in range(self.COLS):
                row += self.grid[c][rw]
            print(row)
            