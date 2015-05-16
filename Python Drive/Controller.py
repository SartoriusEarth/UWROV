import from PID *
import math

# import note for the math: 
#   - z is the axis pointing out of the dock
#   - y is height
#   - x is right left
#   - r is the radius from the dock
#   - gamma is the angle of the ROV relative to the dock

class Controller():
    def __init__(self, x, y, z):

        # control the radius from the dock,
        # the height of the ROV relative to the dock,
        # and the angle of the ROV relative to the dock (between pi and -pi)
        self.rDesired = math.sqrt(x**2 + z**2)
        self.yDesired = y
        self.gammaDesired = math.atan2(x, z)

        self.rPid = PID(Kp=2, Kd=3, Ki=0.5)
        self.yPid = PID(Kp=2, Kd=3, Ki=0.5)
        self.gammaPid  = PID(Kp=2, Kd=3, Ki=0.5)

    def setDesired(self, desired):
        self.desired = desired

    def update(self, current_value):
        error = desired - current_value
        return pid.update(error)

    def sendToRov(self):
        # something