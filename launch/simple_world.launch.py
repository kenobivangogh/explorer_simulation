from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    pkg_gazebo_ros = get_package_share_directory('gazebo_ros')
    world_file = os.path.join(
        get_package_share_directory('explorer_simulation'),
        'worlds',
        'simple.world'
    )
    rviz_config = os.path.join(
        get_package_share_directory('explorer_simulation'),
        'rviz',
        'turtlebot3_config.rviz'  # Eğer bir RViz ayar dosyası kullanmak isterseniz
    )

    return LaunchDescription([
        # Gazebo'yu başlat
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(pkg_gazebo_ros, 'launch', 'gazebo.launch.py')
            ),
            launch_arguments={'world': world_file}.items()
        ),
        # RViz'i başlat
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', rviz_config]
        )
    ])
