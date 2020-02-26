# motar_mini v0.1
The HAMER_Mini robot package is designed as a sub-version of the "Medical Autonomous Carrying Robot" main model. ROS Melodic is compatible.

For motar main model : https://github.com/mertwlf/MOTAR

Rviz Launching:

    $ roslaunch motar_mini motarmini_rviz.launch model:=motar_mini.urdf
    
Gazebo Launching:

    $ roslaunch motar_mini motarmini_gazebo.launch
    
------------------------------------------------------------------------------
# motar_mini v0.2
-----------------------------
- Ultrasonic sensors added.

Requirements:

- In order for the sensors to work properly, "gazebo_ros_pkgs" files must be downloaded.

        $ cd ~/catkin_ws/src
        $ git clone https://github.com/ros-simulation/gazebo_ros_pkgs.git -b melodic-devel
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
        $ git clone https://github.com/ros-perception/slam_gmapping.git -b melodic-devel
        $ catkin_make

SLAM Launching:

        $ roslaunch motar_mini motarmini_slam.launch

------------------------------------------------------------------------------------------
# motar_mini v0.4
-----------------------------
-   Added point to point movement capability.

First Launch Gazebo:

    $ roslaunch motar_mini motar_with_map.launch
Then Launch Rviz amcl launch file:

    $ roslaunch motar_mini amcl.launch


------------------------------------------------------------------------------------------
Contributors: 
Mertcan KURT
Burak KARGACI
Yeter ATEŞ
Musa ERTUĞRUL
