from C07_Offensive_Play import Offensive_Play
from Enums import E, RequirementNotMet

class Offensive_Run_Play(Offensive_Play):
    def __init__(self, name, formation, ball_carrier, zone):
        super().__init__(self, name, formation)
        # ball_carrier is position
        # zone is a number reflecting location on field
        self.ball_carrier = ball_carrier
        self.zone = zone
        self.name = name
        self.formation = formation
        if self.ball_carrier not in E.POSITIONS:
            raise RequirementNotMet
        if self.zone not in formation.players_map:
            raise RequirementNotMet

    def stage1(self, blocking_positions_1=[]):
        # this should get the positions that will block at the point of attack
        for position in blocking_positions_1:
            if position not in self.formation.set_positions():
                raise RequirementNotMet
            
        return blocking_positions_1
        
    def stage2(self, blocking_positions_2=[]):
        # this should get the positions that will block at the second level
        for position in blocking_positions_2:
            if position not in self.formation.set_positions():
                raise RequirementNotMet
            
        return blocking_positions_2
