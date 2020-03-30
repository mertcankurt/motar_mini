#!/usr/bin/env python
import rospy

from geometry_msgs.msg import Twist

import RPi.GPIO as gpio

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(16,gpio.OUT)
gpio.setup(11,gpio.OUT)
gpio.setup(13,gpio.OUT)
gpio.setup(15,gpio.OUT)

def getctrlinst():
    rospy.init_node('motar_control_sub')

    rospy.Subscriber("cmd_vel", Twist)
    
    key=Twist()
    
    x = 0
    th = 0
    count = 0

    while(1):
        x = key.linear.x
        th = key.angular.z
        count = 0
        if x==1:
            gpio.output(16,False)
            gpio.output(11,True)        		   
            gpio.output(13,True)    		      
            gpio.output(15,False)
        elif x==-1:
            gpio.output(16,True)
            gpio.output(11,False)
            gpio.output(13,False)
            gpio.output(15,True)
        elif th==1:
            gpio.output(16,False)
            gpio.output(11,True)
            gpio.output(13,False)
            gpio.output(15,True)
        elif th==-1:
            gpio.output(16,True)
            gpio.output(11,False)
            gpio.output(13,True)
            gpio.output(15,False)
        elif x==0 and th==0:
            gpio.output(16,False)
            gpio.output(11,False) 
            gpio.output(13,False)
            gpio.output(15,False)
        else:
            count = count + 1
            
        if count > 4:
            x = 0
            th = 0
        if (x > 1 or th > 1):
            break
             
if __name__=="__main__":
    getctrlinst()