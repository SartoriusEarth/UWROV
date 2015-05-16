#!/usr/bin/env python

import time

class PID():

    def __init__(self, Kp=0, Kd=0, Ki=0):
        self.Kp = Kp
        self.Kd = Kd
        self.Ki = Ki

        self.current_time = time.time()
        self.previous_time = self.current_time

        self.previous_error = 0

        # results stored in these variables
        self.Xp = 0
        self.Xd = 0
        self.Xi = 0

    def update(self, error):
        self.current_time = time.time()
        dt = self.current_time - self.previous_time
        self.previous_time = self.current_time

        self.Xp = self.Kp * error
        self.Xi += error * dt

        de = error - self.previous_error
        self.Xd = de/dt if dt > 0 else 0
        
        self.previous_error = error

        return self.Xp + (self.Kd * self.Xd) + (self.Ki * self.Xi)

    def reset(self):
        self.Xp = 0
        self.Xd = 0
        self.Xi = 0

if __name__=="__main__":
    pid = PID(Kp=2, Kd=50, Ki=0)

    desired = 0
    actual = 0
    print "desired, %s" % desired
    while actual != 4:
        # get measurement
        print "actual, %s" % actual

        # update from PID controller
        control = pid.update(1)

        # send control value to the ROV
        print "control, %s" % control