from picar.SunFounder_PCA9685 import Servo
import sys
import time


class direction(Servo):
    def __init__(self,pin):
        self.srv = Servo.Servo(pin)
        self.srv.setup()

    def write(self,angle):
        if angle > 110:
            angle = 110
        elif angle < 70:
            angle = 70
        else:
            angle = angle

        self.srv.write(angle)