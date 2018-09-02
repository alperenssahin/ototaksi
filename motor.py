from picar.SunFounder_PCA9685 import PCA9685
import sys
import time

pwm = PCA9685.PWM(1 , 0x40) # address is 0x40 by default
pwm.frequency = 60
pwm.write(4,0,4000)
sys.exit()
