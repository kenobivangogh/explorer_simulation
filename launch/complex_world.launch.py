from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    """paketlerin dizinlerini alp o şekilde devam etmek için"""
#   pkg_gazebo_ros = get_package_share_directory('gazebo_ros')
#   pkg_explorer_simulation = get_package_share_directory('explorer_simulation')
#   pkg_turtlebot3_gazebo = get_package_share_directory('turtlebot3_gazebo')

    pkg_gazebo_ros = get_package_share_directory('gazebo_ros')
    world_file = os.path.join(
        get_package_share_directory('explorer_simulation'),
        'worlds',
        'complex.world'
    )
#   world_file = os.path.join(pkg_explorer_simulation, 'worlds', 'simple.world')
#    if not os.path.exists(world_file):
#        raise FileNotFoundError(f"World file not found: {world_file}")

    rviz_config = os.path.join(
        get_package_share_directory('explorer_simulation'),
        'rviz',
        'tb3_gazebo.rviz'
    )
#   rviz_config = os.path.join(pkg_explorer_simulation, 'rviz', 'turtlebot3_config.rviz')
#    if not os.path.exists(rviz_config):
#        raise FileNotFoundError(f"RViz config file not found: {rviz_config}")

    return LaunchDescription([
        # Gazebo
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(pkg_gazebo_ros, 'launch', 'gazebo.launch.py')
            ),
            launch_arguments={'world': world_file}.items()
        ),

                # TurtleBot3
     
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(get_package_share_directory('turtlebot3_gazebo'), 'launch', 'robot_state_publisher.launch.py')
            )
        ),
        # TurtleBot3'ü simülasyona ekle
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(get_package_share_directory('turtlebot3_gazebo'), 'launch', 'spawn_turtlebot3.launch.py')
            )
        ),   
        # RViz
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', rviz_config]
        )
    ])
