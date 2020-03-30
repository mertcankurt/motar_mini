cmake_minimum_required(VERSION 2.8.3)

project(motar_mini)

find_package(catkin REQUIRED)

find_package(catkin REQUIRED COMPONENTS
  geometry_msgs
  message_generation
  message_runtime
  rospy
  std_msgs
  roslaunch
)

add_message_files(
   FILES
   dprm.msg
)

 generate_messages(
   DEPENDENCIES
   geometry_msgs   
   std_msgs
 )

catkin_package()

foreach(dir config launch meshes urdf)
	install(DIRECTORY ${dir}/
		DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/${dir})
endforeach(dir)
