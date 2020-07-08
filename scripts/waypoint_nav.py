#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import sensor_msgs.msg
import random
import numpy as np
from geometry_msgs.msg import Twist,Pose, Point, Quaternion
from nav_msgs.msg import Odometry
from operator import itemgetter
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
import actionlib
from actionlib_msgs.msg import *
from trajectory_msgs.msg import *
from visualization_msgs.msg import *
from itertools import *
import time

from motar_mini.msg import dprm 
from collections import deque

q = deque() 
pose=[]


class GoToPose():
    def __init__(self):
        self.pos=0
        self.goal_sent = False

	# What to do if shut down (e.g. Ctrl-C or failure)
	#rospy.on_shutdown(self.shutdown)
	
	# Tell the action client that we want to spin a thread by default
	self.move_base = actionlib.SimpleActionClient("move_base", MoveBaseAction)
	rospy.loginfo("Wait for the action server to come up")

	# Allow up to 5 seconds for the action server to come up
	self.move_base.wait_for_server(rospy.Duration(5))

    def goto(self, pos, quat):
        # Send a goal
        self.pos=pos
        self.goal_sent = True

	goal = MoveBaseGoal()
	goal.target_pose.header.frame_id = 'map'
	goal.target_pose.header.stamp = rospy.Time.now()
        goal.target_pose.pose = Pose(Point(pos['x'], pos['y'], 0.000),
                                     Quaternion(quat['r1'], quat['r2'], quat['r3'], quat['r4']))

	# Start moving
        self.move_base.send_goal(goal)

	# Allow TurtleBot up to 60 seconds to complete task
	success = self.move_base.wait_for_result(rospy.Duration(90)) 

        state = self.move_base.get_state()
        result = False

        global pose
        rospy.loginfo(str(pos['x'])+" "+str(pos['y']))
        if (self.pos['x']>(pose.x-1) and self.pos['x']<=(pose.x+1)) and (self.pos['y']>(pose.y-1) and self.pos['y']<=(pose.y+1)) :
            result = True
            GoalStatus.SUCCEEDED==True
            success=True
        else:
            self.move_base.cancel_goal()

        self.goal_sent = False
        return result

    def shutdown(self):
        if self.goal_sent:
            self.move_base.cancel_goal()
        rospy.loginfo("Stop")
        rospy.sleep(1)

def dprmsub(data):
    global q
    if data.room>0:
        x=data.destination.x
        y=data.destination.y
        p=data.patient
        r=data.room
        m=data.medicine
        point=[x,y]
        q.append(point) 
    elif data.room==0:
        q.pop()

def odomsub(data):
    global pose
    rospy.sleep(1)
    try:
        pose=data.pose.pose.position
    except Exception as err:
        print(err) 
    
def main():
    global q
    
    try:
        navigator = GoToPose()
        while(q):
                
            temp=q.popleft()
            x=temp[0]
            y=temp[1]
            position = {'x': x, 'y' : y}
            quaternion = {'r1' : 0.000, 'r2' : 0.000, 'r3' : 0.000, 'r4' : -1.000}
            rospy.loginfo("Go to (%s, %s) pose", position['x'], position['y'])
            success = navigator.goto(position, quaternion)
            if (success) :
                rospy.loginfo("I'm here now... (%s, %s) pose", position['x'], position['y'])
            else:
                rospy.loginfo("The base failed to reach the desired pose")

        # Sleep to give the last log messages time to be sent
        
        rospy.sleep(1)

    except rospy.ROSInterruptException:
        rospy.loginfo("Ctrl-C caught. Quitting")
        stored_exception=sys.exc_info()



if __name__ == '__main__':
    stored_exception=None
    try:
        rospy.init_node('nav_test', anonymous=False)
        dprm_sub = rospy.Subscriber("motar_mini/dprm",dprm,dprmsub)
        rospy.Subscriber('odom',Odometry,odomsub)
        
        rospy.loginfo("Waiting for 10 seconds to get destination input(s)")
        time.sleep(10)
        main()
            

    except Exception as err:
        print(err)
    
