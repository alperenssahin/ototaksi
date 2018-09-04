from move import motor_ctrl

class Back_wheels():
    def __init__(self,motor1,motor2):
        self.mtr1 = motor_ctrl.Motor(motor1)
        self.mtr2 = motor_ctrl.Motor(motor2)
        self.mtr1.setup()
        self.mtr2.setup()
        self.speed = 0

    def write(self,val):
        self.mtr1.write(val)
        self.mtr2.write(val)