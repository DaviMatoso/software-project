from utils.ssl.Navigation import Navigation
from utils.ssl.base_agent import BaseAgent

class ExampleAgent(BaseAgent):
    def __init__(self, id=0, yellow=False):
        super().__init__(id, yellow)
        self.oppAhead = False

    def decision(self):
        if len(self.targets) == 0:
            return

        target_velocity, target_angle_velocity = Navigation.goToPoint(self.robot, self.targets[0])
        self.set_vel(target_velocity)
        self.set_angle_vel(target_angle_velocity)

        return

    def post_decision(self):
        for robo_id, roboAtual in self.opponents.items():
            roboAtual_X = roboAtual.x
            roboAtual_Y = roboAtual.y
            my_loc = self.pos
            opponent_loc = (roboAtual_X, roboAtual_Y)

            new_opp_loc = Navigation.New_point(opponent_loc, my_loc, self.body_angle)

            if new_opp_loc[0, 0] > my_loc[0] and new_opp_loc[0, 0] < (my_loc[0] + 2):
                if new_opp_loc[1, 0] > (my_loc[0] + 0.45) and new_opp_loc[1, 0] < (my_loc[1] - 0.45):
                    self.oppAhead = True
                    