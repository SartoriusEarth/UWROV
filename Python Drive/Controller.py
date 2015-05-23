#!/usr/bin/env python

from PID import *
from MotorController import Control
import math

# import note for the math: 
#   - z is the axis pointing out of the dock
#   - y is height
#   - x is right left
#   - r is the radius from the dock
#   - gamma is the angle of the ROV relative to the dock

class Controller():
    def __init__(self, trans):

        x,y,z = trans

        # control:
        # 1. the radius from the dock,
        # 2. the height of the ROV relative to the dock,
        # 3. the angle of the ROV relative to the dock (between pi and -pi)
        self.desired = ( math.sqrt(x**2 + z**2), y, math.atan2(x, z) )

        self.pid = ( PID(Kp=2, Kd=3, Ki=0.5), PID(Kp=2, Kd=3, Ki=0.5), PID(Kp=2, Kd=3, Ki=0.5) )

    def setDesired(self, trans):
        x,y,z = trans
        self.desired = ( math.sqrt(x**2 + z**2), y, math.atan2(x, z) )

    def update(self, trans):
        error = [desired_i - trans_i for desired_i, trans_i in zip(self.desired, trans)]
        
        # these are in r y gamma format and we need to go back to x y z
        r,y,gamma = [ self.pid[i].update(error[i]) for i in range(3) ]

        return [ r * math.cos(gamma), y, r * math.sin(gamma) ]



    