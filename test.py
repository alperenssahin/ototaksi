from move import motor
from move import servo
import sys
import time

direction = servo.direction(0)
motor = motor.Back_wheels(4,5)

direction.write(90)
motor.write(2000)
time.sleep(1)
direction.write(100)
time.sleep(1)
direction.write(80)
time.sleep(1)
direction.write(90)
time.sleep(0.1)
motor.write(4095)
time.sleep(0.5)
sys.exit()


