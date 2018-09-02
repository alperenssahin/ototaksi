from picar.SunFounder_PCA9685 import Servo
import sys
# class servo(Servo):
#     def __init__(self,pin_no):
#         self.servo = Servo.servo(pin_no)


srv = Servo.Servo(1)
srv.setup()
srv.write(int(sys.argv[1]))