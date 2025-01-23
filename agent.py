from utils.Point import Point
from utils.ssl.Navigation import Navigation
from utils.ssl.base_agent import BaseAgent
import math

class ExampleAgent(BaseAgent):
    def __init__(self, id=0, yellow=False):
        super().__init__(id, yellow)
        self.mycount = 1
        self.qlqrcoisa = 200
        self.oppAhead = False

    def decision(self):
        if len(self.targets) == 0:
            return
        
        # if self.mycount > 1:
        #     return
        # print(self.opponents)
        # print(self.pos)
        
        
        self.mycount += 1

        if self.qlqrcoisa == 0:
            target_velocity, target_angle_velocity = Navigation.goToPoint(self.robot, self.targets[0])
            # new_angle_vel = target_angle_velocity  + 1
            # anguloX = target_velocity.x * math.sin(Navigation.degrees_to_radians(self.body_angle))
            # anguloY = target_velocity.y * math.cos(Navigation.degrees_to_radians(self.body_angle))
            
            # angle = Point(-anguloX, -anguloY)
            # print("///////////////////////")
            # print(self.body_angle)
            # print(new_angle_vel)
            # print(target_angle_velocity)
            # print(angle)
            self.set_angle_vel(target_angle_velocity)
            self.set_vel(target_velocity)
        else:
            my_point = Point(1.0, 1.0)
            myVelocidade, myAngle = Navigation.goToPoint(self.robot, my_point)
            self.set_vel(myVelocidade)
            self.set_angle_vel(myAngle)
            self.qlqrcoisa -= 1
            print(self.qlqrcoisa)
        # print("////////////////////")
            print(f"rodou {self.qlqrcoisa} vez")
        
        # print(target_angle_velocity)
        # print(target_velocity)
        
        
        
        
        
        
        # print("///////////////////////////////////")
        # print(" ")
        # print("///////////////////////////////////")
        # print(" ")
        # print("///////////////////////////////////")
        # print(" ")
        # print("///////////////////////////////////")
        
        # print("ANGLE VELOCITY:")
        # print(self.angle_vel)
        # print('SELF.ROBOT:')
        # # print(self.robot.theta)
        # # print('TARGET:')
        # print(Navigation.goToPoint(self.robot, self.targets[0]))
        # print('rodou a primeira vez')

        return

    def post_decision(self):
        for i in range(0, 21):
            roboAtual = self.opponents.get(i)
            roboAtual_X = roboAtual.x
            roboAtual_Y = roboAtual.y
            self.pos.x
        
            print(roboAtual.x)
            
