#!/usr/bin/env python

import rospy
from nav_msgs.srv import GetMap

def get_map_data():
    rospy.wait_for_service('/static_map')
    map_data = rospy.ServiceProxy('/static_map', GetMap)().map
    rospy.loginfo(f"Map Dimensions: {map_data.info.width} x {map_data.info.height}")
    rospy.loginfo(f"Map Resolution: {map_data.info.resolution} meters/pixel")

if __name__ == "__main__":
    rospy.init_node('map_service_client')
    get_map_data()
