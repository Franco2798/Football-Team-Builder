from C07_Offensive_Play import Offensive_Play

class Offensive_Pass_Play(Offensive_Play):
    def __init__(self, name, formation, routes):
        super().__init__(self, name, formation)
        self.position_routes = routes #for simplicity sake these are assigned to eligible receivers in order. It is a list of (position, routes).
        self.blockers = []
        
        self.quick_routes = []
        self.medium_routes = []
        self.long_routes = []

        self.assign_routes()
        
    def assign_blockers(self):
        # this assigns any position that doesn't have a route to block
        pass

    def set_routes(self):
        # this populates the lists quick, medium and long routes with positions that run those routes
        pass
