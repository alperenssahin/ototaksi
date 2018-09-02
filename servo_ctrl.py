from picar.SunFounder_PCA9685 import Servo
import sys
import time
# class servo(Servo):
#     def __init__(self,pin_no):
#         self.servo = Servo.servo(pin_no)


srv = Servo.Servo(0)
srv.setup()
srv.write(int(sys.argv[1]))
time.sleep(0.1)
sys.exit()