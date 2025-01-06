# explorer_simulation
Simulation for path planning algorithm (Gazebo - rviz) 

ros2 launch explorer_simulation simple_world.launch.py

ros2 launch explorer_simulation multi_geo_world.launch.py

ros2 launch explorer_simulation square_world.launch.py

ros2 launch explorer_simulation complex_world.launch.py

Mapping :

ros2 launch slam_toolbox online_async_launch.py use_sim_time:=true
ros2 run turtlebot3_teleop teleop_keyboard
ros2 run nav2_map_server map_saver_cli -f map.pgm
