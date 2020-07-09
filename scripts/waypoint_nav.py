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
doRun=True

class GoToPose():
    def __init__(self):

        self.goal_sent = False

	# What to do if shut down (e.g. Ctrl-C or failure)
	rospy.on_shutdown(self.shutdown)
	
	# Tell the action client that we want to spin a thread by default
	self.move_base = actionlib.SimpleActionClient("move_base", MoveBaseAction)
	rospy.loginfo("Wait for the action server to come up")

	# Allow up to 5 seconds for the action server to come up
	self.move_base.wait_for_server(rospy.Duration(5))

    def goto(self, pos, quat):

        # Send a goal
        self.goal_sent = True
	goal = MoveBaseGoal()
	goal.target_pose.header.frame_id = 'map'
	goal.target_pose.header.stamp = rospy.Time.now()
        goal.target_pose.pose = Pose(Point(pos['x'], pos['y'], 0.000),
                                     Quaternion(quat['r1'], quat['r2'], quat['r3'], quat['r4']))

	# Start moving
        self.move_base.send_goal(goal)

	# Allow TurtleBot up to 60 seconds to complete task
	success = self.move_base.wait_for_result(rospy.Duration(120)) 

        state = self.move_base.get_state()
        result = False
    
        if success and state == GoalStatus.SUCCEEDED:
            # We made it!
            result = True
        else:
            self.move_base.cancel_goal()

        self.goal_sent = False
        return result

    def shutdown(self):
        if self.goal_sent:
            self.move_base.cancel_goal()
<<<<<<< HEAD
        #rospy.loginfo("Stop")
=======
        rospy.loginfo("Stop")
>>>>>>> 244be58827532844a99b053d9f15e62fba7c6915
        #rospy.sleep(1)

def dprmsub(data):
    global q
    if data.room>0:
        x=data.destination.position.x
        y=data.destination.position.y
        ox=data.destination.orientation.x
        oy=data.destination.orientation.y
        oz=data.destination.orientation.z
        ow=data.destination.orientation.w
        p=data.patient
        r=data.room
        m=data.medicine
        point=[x,y,ox,oy,oz,ow]
        q.append(point) 
    elif data.room==0:
        q.pop()

def odom_sub(data):
    global pose
    rospy.sleep(1)
    try:
        pose=data.pose.pose.position
    except Exception as err:
        print(err) 
   
def main():
    global q
    global doRun
    try:
        while(doRun):
            navigator = GoToPose()
            while(q and doRun):
                        
                temp=q.popleft()
                x=temp[0]
                y=temp[1]
<<<<<<< HEAD
                ox=temp[2]
                oy=temp[3]
                oz=temp[4]
                ow=temp[5]
                position = {'x': x, 'y' : y}
                quaternion = {'r1' : ox, 'r2' : oy, 'r3' : oz, 'r4' : ow}
=======
                position = {'x': x, 'y' : y}
                quaternion = {'r1' : 0.000, 'r2' : 0.000, 'r3' : 0.000, 'r4' : -1.000}
>>>>>>> 244be58827532844a99b053d9f15e62fba7c6915
                rospy.loginfo("Go to (%s, %s) pose", position['x'], position['y'])
                success = navigator.goto(position, quaternion)
                if (success) :
                    rospy.loginfo("I'm here now... (%s, %s) pose", position['x'], position['y'])
                else:
                    rospy.loginfo("The base failed to reach the desired pose")
<<<<<<< HEAD
                time.sleep(3)
            # Sleep to give the last log messages time to be sent
            rospy.sleep(1)
            
=======

            # Sleep to give the last log messages time to be sent
            rospy.sleep(1)
>>>>>>> 244be58827532844a99b053d9f15e62fba7c6915
    except rospy.ROSInterruptException:
        rospy.loginfo("Ctrl-C caught. Quitting")
        doRun=False

if __name__ == '__main__':
    
        rospy.init_node('nav_test', anonymous=False)
        dprm_sub = rospy.Subscriber("motar_mini/dprm",dprm,dprmsub)
        odmsb = rospy.Subscriber('odom',Odometry,odom_sub)
        
        #rospy.loginfo("Waiting for 10 seconds to get destination input(s)")
        #time.sleep(10)
        main()


<<<<<<< HEAD
    
=======
    
>>>>>>> 244be58827532844a99b053d9f15e62fba7c6915
