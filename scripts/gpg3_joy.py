#!/usr/bin/env python

# using X-box wired controller to move GoPiGo3

# import #
import rospy
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist   #turtle cmd_vel message type

# initialize globals
move = Twist()
stop = True

# node initialization #
rospy.init_node("gpg3_joy")

# definitions of functions #
def callback(msg):
    global move
    move.linear.x = msg.axes[1]     # left stick left/right
    move.angular.z = msg.axes[0]    # left stick up/down

# clean shutdown
def shutdownhook():
    global move
    move.linear.x = 0
    move.angular.z = 0
    pub.publish(move)
    rospy.loginfo("Shutting down gpg3_joy node - stopping robot")

# definition of publisher/subscriber and services #
rospy.Subscriber('joy', Joy, callback)
pub = rospy.Publisher('cmd_vel', Twist, queue_size=1) 

# main program #
rate = rospy.Rate(20)
rospy.on_shutdown(shutdownhook)

while not rospy.is_shutdown():
    pub.publish(move)
    rate.sleep()
