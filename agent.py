from utils.Point import Point
from utils.ssl.Navigation import Navigation
from utils.ssl.base_agent import BaseAgent

class ExampleAgent(BaseAgent):
    def __init__(self, id=0, yellow=False):
        super().__init__(id, yellow)
        self.mycount = 1
        self.qlqrcoisa = 50

    def decision(self):
        if len(self.targets) == 0:
            return

        # if self.mycount > 1:
        #     return
        # print(self.opponents)
        
        
        self.mycount += 1

        if self.qlqrcoisa == 0:
            target_velocity, target_angle_velocity = Navigation.goToPoint(self.robot, self.targets[0])
            self.set_angle_vel(target_angle_velocity)
            self.set_vel(target_velocity)
        else:
            myVelocidade = Point(0.8643012686810787, 0.8532089532712336)
            self.set_vel(myVelocidade)
            self.qlqrcoisa -= 1
            print(self.qlqrcoisa)
        # print("////////////////////")
        # print(target_angle_velocity)
        # print(target_velocity)
        
        
        
        
        
        
        # print("///////////////////////////////////")
        # print(" ")
        # print("///////////////////////////////////")
        # print(" ")
        # print("///////////////////////////////////")
        # print(" ")
        # print("///////////////////////////////////")
        # print(self.opponents)
        # print("ANGLE VELOCITY:")
        # print(self.angle_vel)
        # print('SELF.ROBOT:')
        # # print(self.robot.theta)
        # # print('TARGET:')
        # print(Navigation.goToPoint(self.robot, self.targets[0]))
        # print('rodou a primeira vez')

        return

    def post_decision(self):
        pass
