class Coach:
    def __init__(self, team):
        self.team = team
        self.wins = 0
        self.losses = 0
        self.possession = False
        self.selected_play = None

    def choose_play(self, down, distance):
        if self.possession == True:
            self.choose_offensive_play(down, distance)
        else:
            self.choose_defensive_scheme(down, distance)
    
    def choose_offensive_play(down, distance)
        # sets self.selected_play
        pass

    def choose_defensive_scheme(down, distance):
        # sets self.selected_play
        return None