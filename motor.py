from picar.SunFounder_PCA9685 import PCA9685
import sys
import time

pwm = PCA9685.PWM(4 , adresse=0x40) # address is 0x40 by default
pwm.frequency = 60
pwm.write_all_value(0,4000)
time.sleep(2)
sys.exit()
