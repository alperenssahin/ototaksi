from move import PCA9685


class Motor(object):
    '''Servo driver class'''
    _MIN_PULSE_WIDTH = 600
    _MAX_PULSE_WIDTH = 2400
    _DEFAULT_PULSE_WIDTH = 1500
    _FREQUENCY = 60

    _DEBUG = False
    _DEBUG_INFO = 'DEBUG "Servo.py":'

    def __init__(self, channel, offset=0, lock=True, bus_number=None, address=0x40):
        ''' Init a servo on specific channel, this offset '''
        if channel < 0 or channel > 16:
            raise ValueError("Servo channel \"{0}\" is not in (0, 15).".format(channel))
        if self._DEBUG:
            print
            self._DEBUG_INFO, "Debug on"
        self.channel = channel
        self.offset = offset
        self.lock = lock

        self.pwm = PCA9685.PWM(bus_number=bus_number, address=address)
        self.frequency = self._FREQUENCY
        self.write(90)

    def setup(self):
        self.pwm.setup()

    def _angle_to_analog(self, angle):
        ''' Calculate 12-bit analog value from giving angle '''
        pulse_wide = self.pwm.map(angle, 0, 180, self._MIN_PULSE_WIDTH, self._MAX_PULSE_WIDTH)
        analog_value = int(float(pulse_wide) / 1000000 * self.frequency * 4096)
        if self._DEBUG:
            print
            self._DEBUG_INFO, 'Angle %d equals Analog_value %d' % (angle, analog_value)
        return analog_value

    @property
    def frequency(self):
        return self._frequency

    @frequency.setter
    def frequency(self, value):
        self._frequency = value
        self.pwm.frequency = value

    @property
    def offset(self):
        return self._offset

    @offset.setter
    def offset(self, value):
        ''' Set offset for much user-friendly '''
        self._offset = value
        if self._DEBUG:
            print
            self._DEBUG_INFO, 'Set offset to %d' % self.offset

    def write(self, val):
        self.pwm.write(self.channel, 0, val)

    @property
    def debug(self):
        return self._DEBUG

    @debug.setter
    def debug(self, debug):
        ''' Set if debug information shows '''
        if debug in (True, False):
            self._DEBUG = debug
        else:
            raise ValueError('debug must be "True" (Set debug on) or "False" (Set debug off), not "{0}"'.format(debug))

        if self._DEBUG:
            print
            self._DEBUG_INFO, "Set debug on"
        else:
            print
            self._DEBUG_INFO, "Set debug off"