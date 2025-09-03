from C02_Team import Team as Team

class GameController:
    def __init__(self, coach1, coach2):
        self.coach1 = coach1
        self.coach2 = coach2
        
        self.los = None # line of scrimmage (where the play starts)
        self.line_to_gain = None # yardline needed to get first down
        self.score1 = 0
        self.score2 = 0
        # you will need to add variables here I have given you some.
        # validation at this stage will use only the variables above and
        #   returns from your functions

    def coin_flip(self):
        # determine which team starts with the ball
        #   the other team receives the second half kickoff
        # set the appropriate coach to possession = True

        pass

    def turnover(self):
        # change possession of ball
        pass

    def kickoff(self, yardline = 35):
        # use kicker stats to determine distance
        # change possession of ball
        # set the line of scrimmage
        # if kick is in endzone likely no return
        # if not: return using E.KR position skill
        pass

    def end_of_quarter(self):
        # each quarter is 15 minutes
        # at the end of the second quarter the team that started
        #   the game with possession kicks off
        pass

    def get_yard_line(self)
        # in football the field is broken into halfs
        #   the center is the 50 yard line
        #   the side further from the team's goal is the offensive team's side
        #   and the side closer to the team's goal is defensive team's
        #  e.g team 'Apple' receives the kickoff on their 20
        #   APPLE GOAL  10  20  30  40  50  40  30  20  10 BANANNA GOAL
        #                   start
        #   APPLE completes a pass for 30 yards
        #   APPLE GOAL  10  20  30  40  50  40  30  20  10 BANANNA GOAL
        #                   x ----------->
        #   APPLE is now at midfield
        #   APLLE tries to run but loses 5 yards
        #   APPLE GOAL  10  20  30  40  50  40  30  20  10 BANANNA GOAL
        #                             <--x
        #   APPLE is now on their 45 yard line
        #   APPLE completes another pass for 15 yards
        #   APPLE GOAL  10  20  30  40  50  40  30  20  10 BANANNA GOAL
        #                             ------->
        #   APPLE is now on BANANNA's 40 yard line

        #   an example return for this function is BANANNA's 40 yard line
        pass

    def get_down_and_distance(self):
        # in football you have 4 tries to get 10 yards.
        # each try is called a down
        # e.g.
        #   1st and 10 on APPLE's 30 yard line.
        #   APPLE gains 3 yards
        #   2nd and 7 on APPLE'S 33 yard line.
        #   APPLE gains 10 yards
        #   1st and 10 on APPLE's 43 yard line.
        # example return: 1st and 10
        pass

    def field_goal_or_extra_point(self):
        # use the kicker, holder, and long_snapper (E.K), (E.HL), (E.LS)
        # refer to NFL statistics to determine a reasonable function based
        # on distance. There should a negligible chance that the HL or LS mess up
        # this chance should be modified based on skill
        pass

    def process_touchdown(self):
        # increase score by 6
        # kick extra point (field goal from the 15 yard line)
        # kickoff to other team
        pass

    def process_safety(self):
        # add two points to defensive team
        #   occurs when player is tackled in their own endzone
        # safety
        # kickoff from 20
        pass

    def process_yards_from_play(self, yards):
            # update the line of scrimmage (los) based on gain.
            # if 4th down and yards do not get past the line to gain turnover
            # if a touchdown process score
            pass

    def handle_run_play(self, offense_coach, defense_coach):
        offensive_play = offense_coach.selected_play
        defensive_scheme = defense_coach.selected_play

        available_defensive_players = [] # populate with players on the field

        # stage 1
        blockers_stage1 = offensive_play.stage1()
        defenders_stage1 = defensive_scheme.formation.get_players_within_d_distance_of_location(offensive_play.zone,1)
        # decide the result of this stage
        # remove the defenders that were used in stage 1 from available_defensive_players

        # stage 2: if stage 1 did not end in a tackle
        blockers_stage2 = offensive_play.stage2()
        defenders_stage2 = defensive_scheme.formation.get_players_within_d_distance_of_location(offensive_play.zone,2)
        # decide the result of this stage
        # remove the defenders that were used in stage 2 from available_defensive_players

        # stage 3: if stage 2 did not end in a tackle
        #   remove DL from available_defensive_players
        # decide the result of this stage (all remaining players should attempt to tackle the runner, if none do he should score.)

    def process_throw_and_catch(self, route, qb, receiver, defenders):
        # note there may be more than 1 defender
        throw_quality = None    # apply some logic to determine if it is a good throw (longer throws are harder)
        catch_quality = None    # apply some logic to determine if the ball is caught (this is harder with bad throws and longer throws. If the throw is bad enough it is impossible)
        # process each defender
        #   if the defender is good and the throw quality is bad it may be an interception
        #   if the defender is good and the throw quality is good it may be a deflection
        #   ... there are lots of these in short better outcomes for the offense with good throw quality and good catch quality

    def process_run_after_catch(self,route, ball_carrier, defenders):
        # based on the route there will be more potential defenders
        # a short route should have more defenders than a long route
        # establish all players that could make tackle
        #   this should start with the defenders in process_throw_and_catch
        #   if quick throw check half lbs
        #   either way check
        #   if they miss check safeties
        #   then score
        # return result, ball_carrier, yards, tackler (where tackler is None if score)
        # result: FUMBLE, TOUCHDOWN or None
        # tackler and ball_carrier (player)
        # yards (a number may be negative)
        pass


    def handle_pass_play(self, offensive_coach, defensive_coach):
        # stage 1
        # check blocking
        offensive_play = offense_coach.selected_play
        defensive_scheme = defensive_coach.selected_play

        blockers = offensive_play.blockers
        attackers = defensive_scheme.attachers

        # process attackers and blockers any unblocked player may attempt to tackle qb
        # if there are more blockers than attackers apply a scheme mod to all blockers

        # stage 2
        quick_routes = offensive_play.quick_routes
        # process each route and decide which defensive player or players is covering the route
        # decide if the qb chooses to throw the ball to one of the routes
        #   if so process throw and catch
        #   else move on to stage 3

        # stage 3
        # check blockers and attackers again
        #   assign a positive scheme_mod to attackers
        # apply the same logic as stage 2 to medium routes

        # stage 4
        # check blockers and attackers again
        #   assign a larger positive scheme_mod to attackers
        # apply the same logic as stage 2 to long routes

        # process throw and catch
        # process run after catch
        # return result of play, qb, wr, tackler, yards, covering_defender
        #   result: SACK, COMPLETION, INCOMPLETION, FUMBLE, INTERCEPTION, DEFLECTION
        #   qb: quarterback 
        #   wr: wide receiver (may be None)
        #   tackler: player that tackled wr or quarterback (may be None)
        #   covering_defender: if DEFLECTION or INTERCEPTION (may be None)
        pass

    def enact_play(self):
        # get offensive play and defensive play
        # handle them
        # process results of play
        #   yards gained or lost
        #   time elapsed
        #       if incomplete pass clock stops
        #       if close to end of half teams use less time per play
        #       in general ~ 30 seconds elapse between plays unless one team is in a hurry
        pass
    
    
        

    