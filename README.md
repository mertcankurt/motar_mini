# motar_mini v0.1
The motar_mini robot package is designed as a sub-version of the "Medical Autonomous Carrying Robot" main model. ROS Melodic is compatible.

For motar main model : https://github.com/mertcankurt/MOTAR

To watch the Demo: https://www.youtube.com/watch?v=6Ig-_KnUtJc

Rviz Launching:

    $ roslaunch motar_mini motar_rviz_amcl.launch
    
Gazebo Launching:

    $ roslaunch motar_mini motarmini_gazebo.launch
    
------------------------------------------------------------------------------
# motar_mini v0.2
-----------------------------
- Ultrasonic sensors added.

Requirements:

- In order for the sensors to work properly, "gazebo_ros_pkgs" files must be downloaded.

        $ cd ~/catkin_ws/src
        $ git clone https://github.com/ros-simulation/gazebo_ros_pkgs.git -b melodic-devel #on ubuntu 18.04
        $ git clone https://github.com/ros-simulation/gazebo_ros_pkgs.git -b kinetic-devel #on ubuntu 16.04
        $ catkin_make

----------------------------------------------------------------------------------
# motar_mini v0.3
-----------------------------

-   Available SLAM package usage (motarmini_slam.launch).
-   Added laser sensor.
-   Available mapping with laser sensor to gazebo maps.

Requirements:

- In order for the SLAM to work, "slam_gmapping" package must be downloaded.
    
        $ cd ~/catkin_ws/src
        $ git clone https://github.com/ros-perception/slam_gmapping.git -b melodic-devel #on ubuntu 18.04
        $ git clone https://github.com/ros-perception/slam_gmapping.git -b kinetic-devel #on ubuntu 16.04
        $ catkin_make

First Launch Gazebo:

    $ roslaunch motar_mini motar_with_map.launch
Then Launch SLAM:

    $ roslaunch motar_mini motarmini_slam.launch
Then Launch Rviz:

    $ roslaunch motar_mini motar_rviz_amcl.launch

------------------------------------------------------------------------------------------
# motar_mini v0.4
-----------------------------
-   Added point to point movement capability.
-   Added a launch file for opening both the map and the robot at the same time in gazebo(motar_with_map.launch)

First Launch Gazebo:

    $ roslaunch motar_mini motar_with_map.launch
Then Launch Rviz:

    $ roslaunch motar_mini motar_rviz_amcl.launch
Then Launch amcl launch file:

    $ roslaunch motar_mini amcl.launch

------------------------------------------------------------------------------------------
# motar_mini v0.5
-----------------------------
- Added Interface that can manually control the robot,and its speed  
- The interface also publishes patient,room,medicine and destination to topic motar_mini/dprm
- The interface has a login system. you can add a new account if you know the username and password of a viable account
- all the python codes are included

First Do a catkin_make,
Then open The file with no extension that is named Interface in the Folder motar_mini/scripts/Interface

If you want to open the interface from a python file open a terminal in the Interface Folder and type:

    python login.py


------------------------------------------------------------------------------------------
Contributors: 

Mertcan KURT

Burak KARGACI

Yeter ATEŞ

Musa ERTUĞRUL
