
class Defensive_Scheme:
    def __init__(self, formation, strengths, weaknesses, blitzers, coverage):
        self.formation = formation
        self.weaknesses = weaknesses
        self.strengths = strengths
        self.blitzers = blitzers
        self.coverage = coverage

        # blitzers, strengths and weakness are lists of positions
        # strengths and weaknesses may be any defensive position
        # blitzers are any defensive position other than DL
        self.attackers = self.set_attackers()


        pass
    
    def reset_temporary_variables(self, team):
        # reset temporary variables such as is_blitzing, coverages, location etc
        pass

    def set_attackers(self, team)
        # set self.attackers to positions that are blitzing and DL as list
        #   e.g. if there are 4 DL and 1 LB is blitzing it would be this list: [E.DL, E.DL, E.DL, E.DL, E.LB]
        pass

    def set_coverage(self, team):
        # use coverage to assign players their coverage responsibility
        pass

    def enact(self, team):
        
        # resets temporary variables
        # applies strengths and weaknesses to scheme_mod
        # sets blitzers to is_blitzing = True
        # enacts coverage (ManCoverage or ZoneCoverage)
        # raise RequirementNotMet if asked for position that is not present

