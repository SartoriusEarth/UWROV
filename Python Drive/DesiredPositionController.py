#!/usr/bin/env python
import rospy
import tf
from sensor_msgs.msg import Joy

def callback(data):
    transX = data.axes[2] # how much we move in the x axis
    transY = data.axes[3] # how much we move in the y axis
    
    br.sendTransform((transX, transY, 0),
                 tf.transformations.quaternion_from_euler(0, 0, 0),
                 rospy.Time.now(),
                 "desired_position_controller",     # child
                 "marker_origin"                    # parent
                 )

def main():
    # starts the node
    rospy.init_node('DesiredPositionController')

    # broadcasting object
    br = tf.TransformBroadcaster()

    # subscribed to joystick inputs on topic "joy"
    rospy.Subscriber("joy", Joy, callback)

    # run the node until it is destroyed
    rospy.spin()

if __name__ == '__main__':
    main()