
class Coverage:
    def __init__(self, name):
        self.name = name

    def enact(self, defense, offense_formation):
        raise Requirement('This is the default call of enact and should not be called.')

    def get_players_in_coverage(self, team):
        # a player is covering if they are not blitzing and not DL.
        pass

class ManCoverage(Coverage):
    def __init__(self, name):
        super().__init__(name)
    
    def enact(self, defense, offense_formation)
        # this assigns each player to an eligible receiver on the opponents side for coverage
        # it also sets their location to one apositioncross from their assigned player
        pass

class ZoneCoverage(Coverage):

    def __init__(self, name):
        super().__init__(name)
    
    def enact(self, defense, offense_formation):
        # this assigns each player to a zone on the field
        #   lbs prefer CURL/FLAT
        #   cbs prefer 31, 33, 41, 44
        #   safeties prefer 33, 42, 43
        #   if there are more players in coverage than there are assigned zones raise Requirement not met
        pass