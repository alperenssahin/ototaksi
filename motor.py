from motor_ctrl import Back_Wheels
import time
import sys
motor = Back_Wheels()
motor.speed(100)
motor.forward()
time.sleep(0.1)
motor.stop()
sys.exit()