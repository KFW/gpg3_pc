#!/usr/bin/env python

# wheel_encoder_logger.py
# log wheel encoders to see why robot not driving straight

import rospy
from std_msgs.msg import Float64

def callback_l(msg):
    rospy.loginfo('left: ' + str(msg.data))

def callback_r(msg):
    rospy.loginfo('right: ' + str(msg.data))

rospy.init_node('wheel_encoder_logger')

sub_l = rospy.Subscriber('/motor/encoder/left', Float64, callback_l)
sub_r = rospy.Subscriber('/motor/encoder/right', Float64, callback_r)

rospy.spin()

