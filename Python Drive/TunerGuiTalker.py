#!/usr/bin/env python 

from TunerGui import TunerGui
import rospy
from std_msgs.msg import String


def mainDrive():
	if not rospy.is_shutdown():
		sliders = gui.getConstants()
		string = ''		
		for x in sliders:
			string += ("," + str(x)) 

		#tempstring = 'temp'		
		rospy.loginfo(string)
        	pub.publish(string)
	gui.after(1, mainDrive) # loops the mainDrive method

if __name__ == "__main__":
	pub = rospy.Publisher('pidConstants', String, queue_size=10)
    	rospy.init_node('pidConstants', anonymous=True)	
	gui = TunerGui()	
	gui.after(1, mainDrive)
	gui.mainloop()
