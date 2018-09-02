from picar.SunFounder_PCA9685 import PCA9685
import sys
import time

pwm = PCA9685.PWM() # address is 0x40 by default
pwm.frequency = 60

while True:
        for i in range(0, 4095, 10):
                print i
                pwm.write(4,0, i)
                time.sleep(0.0001)
        for i in range(4095, -1, -10):
                print i
                pwm.write(5,0, i)
                time.sleep(0.0001)
        sys.exit()