#!/usr/bin/env python

import pygame
import rospy
import tf
from OrcusGUI import OrcusGUI
from MotorController import *
from tf.transformations import euler_from_quaternion


"""
      Front

 FR_LF     FR_RT
   /---------\
  /|         |\
   |  FR_VT  |
   |    o    |
   |         |
   |    o    |
   |  BA_VT  |
  \|         |/
   \---------/
 BA_LF     BA_RT

"""


ser = None;
control = Control();


def connect(port_name):
    """Returns a Serial object that is connected to the port_name. Returns
    None if the connection could not be made."""

    try:
        return Serial(port_name, timeout = .5, writeTimeout = .5);
    except SerialException:
        print("connect: could not connect to port " + port_name);
        return None;


def onexit():
    control.trans_x, control.trans_y, control.yaw, control.rise = 0, 0, 0, 0;
    control.trans_x_tare, control.trans_y_tare = 0, 0;
    control.yaw_tare, control.rise_tare = 0, 0;
    update_motor_values();
    write_motor_values(ser);

def mainDrive():
    
    update_motor_values(control)

    # sets the motor values to the sliders
    motors[MOTOR.FR_LF].power = gui.frontLeft * 1.25
    motors[MOTOR.FR_RT].power = gui.frontRight * 1.25
    motors[MOTOR.BA_LF].power = gui.backLeft * 1.25 
    motors[MOTOR.BA_RT].power = gui.backRight * 1.25
    motors[MOTOR.FR_VT].power = gui.frontVert * 1.25
    motors[MOTOR.BA_VT].power = gui.backVert * 1.25

    gui.drawMotorStatus(motors)
    gui.estopControl()

    try:
        write_motor_values(ser);
    except SerialTimeoutException:
        print("write timeout");

    # try:
    #     (trans,rot) = listener.lookupTransform('W', 'A', rospy.Time(0))
    #     print 'translation: ',trans
    #     angles = euler_from_quaternion(rot)
    #     print 'rotation: ',[(180.0/math.pi)*i for i in angles]
    # except (tf.LookupException, tf.ConnectivityException):
    #     gui.after(1, mainDrive)


    gui.after(1, mainDrive) # loops the mainDrive method


if __name__=="__main__":
    rospy.init_node('autodrive')

    # Start gui and call mainDrive loop
    gui = OrcusGUI()
    gui.master.geometry("812x800") # make sure all widgets start inside
    gui.master.minsize(812, 800)
    gui.master.maxsize(812, 800)
    gui.master.title('ROV ORCUS')

    ser = connect("/dev/ttyACM0")

    # listener = tf.TransformListener()

    gui.after(1, mainDrive)
    gui.mainloop()
