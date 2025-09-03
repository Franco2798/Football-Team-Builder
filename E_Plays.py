from C08_Offensive_Play_Run import Offensive_Run_Play
from C09_Offensive_Play_Pass import Offensive_Play_Pass
from C11_Defensive_Scheme import C11_Defensive_Scheme

from Enums import E


class Plays:

    of1 = OffensiveFormation('Single Back',tes = [80], fbs = [], rbs = [23], wrs = [801,803,806])
    of2 = OffensiveFormation('I-Back', tes = [86], fbs=[33],rbs=[23],wrs=[801,806])
    of3 = OffensiveFormation('Trips Right', tes=[80],wrs=[805,806,807], rbs = [23], shotgun=True)



    r1 = Offensive_Run_Play("Left Outside", E.RB, 80)
    r2 = Offensive_Run_Play("Left Off Tackle", E.RB, 71)
    r3 = Offensive_Run_Play("Right Off Tackle", E.RB, 75)
    r4 = Offensive_Run_Play("Right Off Tackle", E.RB, 86)
    r5 = Offensive_Run_Play("Dive", E.RB, 73)

    p1 = Offensive_Play_Pass('All Go')