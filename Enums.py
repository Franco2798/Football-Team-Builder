
class E:
# THESE ARE FOR REFERENCE!!! YOU CAN NOT CHANGE THIS I USE MY OWN COPY!!!!!
    #2:      941                      942                      943                      944               
    #2:         931                               932                            933
    #1:                     531                                     532         
    #1:        201   202   203  204     51    52  53  54    57        206      207      208      209
    #DEFENSE   LEFT ELIGIBLE            90 91 92 93 94 95 96 97            RIGHT ELIGIBLE
    #OFFENSE   801   802   803  804      80 71 72 73 74 75 86         806      807      808      809
    #0:                                           03 
    #1:                                        42 43 44
    #2:                                     21 22 23 24 25
    #                                      BACKFIELD ELIGIBLE
    # RUNNING ZONE  800 (1-4)             0   1  2   3  4  5  6 7                800 (6-9)
    
    
 
    
    # PASS ZONES
    #             41                42               43                        44
    #               31                       32                        33
    #               LEFT CURL/HOOK       MIDDLE CURL/HOOK       RIGHT CURL/HOOK
    #           LEFT FLAT                                                    RIGHT FLAT
    
    
    # formation should specify location in addition to position for WR, RB, TE, FB
    # offense and defense always have 11 players on the field
    QB = 13, 'QB',2   # Quarterback (1)
    
    # formation should specify location in addition to position for WR, RB, TE, FB
    WR = 800, 'WR',5   # Wide Receiver (1-5)
    RB = 20, 'RB',3   # Running Back (0-2)
    TE = 80, 'TE',3   # Tight End (0-3)
    FB = 40, 'FB',1   # Fullback (0-1)
    
    LT = 71, 'LT',2   # Left Tackle
    LG = 72, 'LG',2   # Left Guard
    C = 73, 'CC',2     # Center
    RG = 74, 'RG' ,2  # Right Guard
    RT = 75, 'RT',2   # Right Tackle

    DL = 90, 'DL',6   # DL + location
    LB = 50, 'LB',6   # LB + location
    
    # assigned either a zone or an eligible number and side
    CB = 22, 'CB',5   # Cornerback (2-3 on the field)
    S =  25, 'S',4   # Safeties (1-2 on the field)
        
    
    # Serve their purpose but never need location information
    K = 131,'K',1 # Kicker
    P = 132,'P',1 # Punter
    KR = 133,'KR',1 # Kick returner
    PR = 134,'PR',1 # Punt returner
    LS = 135,'LS',1 # Long snapper
    HL = 135,'HL',1 # Holder for PAT
    
    
    # # Serve their purpose but never need location information
    # K = 131,'K' # Kicker
    # P = 132,'P' # Punter
    # KR = 133,'KR' # Kick returner
    # PR = 134,'PR' # Punt returner
    # LS = 135,'LS' # Long snapper
    # HL = 135,'HL' # Holder for PAT
    
    POSITIONS = [QB,WR,RB,LT,LG,C,RG, RT, FB,TE,LB,CB,DL,S,K,P,KR,PR,LS,HL]

   

    # offense and defense always have 11 players on the field
    PLAYER_VARS = ['first_name','last_name','name','position','is_blitzing','on_field','scheme_mod', 'number']
    COMP_VARS = ['offensive_position', 'defensive_position','offensive_attribute', 'defensive_attribute','offensive_depth', 'defensive_depth']
    
    MIN = 0
    MAX = 255

    # players without defined location

class O:    # outcomes
    TURNOVER = 900
    TOUCHDOWN = 906
    FIELD_GOAL = 903
    SAFETY = 902
    EXTRA_POINT = 901
    
    RUN =  191
    PASS = 292
        
    # PASS ZONES
    #             41                42               43                        44
    #               31                       32                        33
    #               LEFT CURL/HOOK       MIDDLE CURL/HOOK       RIGHT CURL/HOOK
    #           LEFT FLAT                                                    RIGHT FLAT
    

    
class Routes:
    SHORT = "SHORT"
    MEDIUM = "MEDIUM"
    LONG = "LONG"

    POST = {
    "name": "Post",
    "length": "LONG",
    "zones": [42, 43, 32]
    }

    STREAK = {
    "name": "Post",
    "length": "LONG",
    "zones": [44, 41]
    }

    
    
class RequirementNotMet(Exception):
    pass

class AttributeDoesNotExist(Exception):
    pass


