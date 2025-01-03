from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    """paketlerin dizinlerini alp o şekilde devam etmek için"""
#   pkg_gazebo_ros = get_package_share_directory('gazebo_ros')
#   pkg_explorer_simulation = get_package_share_directory('explorer_simulation')
#   pkg_turtlebot3_gazebo = get_package_share_directory('turtlebot3_gazebo')
#   pkg_nav2_bringup = get_package_share_directory('nav2_bringup')
    use_sim_time = LaunchConfiguration('use_sim_time', default='false')

    map_dir = LaunchConfiguration(
    'map',
    default=os.path.join(
        get_package_share_directory('explorer_simulation'),
        'maps',
        'map.yaml'))

    nav2_launch_file_dir = os.path.join(get_package_share_directory('nav2_bringup'), 'launch')

    pkg_gazebo_ros = get_package_share_directory('gazebo_ros')

    world_file = os.path.join(
        get_package_share_directory('explorer_simulation'),
        'worlds',
        'multi_geo.world'
    )

    rviz_config_dir = os.path.join(
    get_package_share_directory('nav2_bringup'),
    'rviz',
    'nav2_default_view.rviz')

    # rviz_config = os.path.join(
    #     get_package_share_directory('explorer_simulation'),
    #     'rviz',
    #     'deneme.rviz'
    # )

    # Harita dosyası (Navigation için)
    # map_file = os.path.join(get_package_share_directory('explorer_simulation'), 'maps', 'map.yaml')


    # print(f"Map file path: {map_dir}")
    # print(f"RViz config file path: {rviz_config}")
    # print(f"Gazebo world file path: {world_file}")



    return LaunchDescription([

        DeclareLaunchArgument(
        'map',
        default_value=map_dir,
        description='Full path to map file to load'),

        DeclareLaunchArgument(
            'use_sim_time',
            default_value='false',
            description='Use simulation (Gazebo) clock if true'),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([nav2_launch_file_dir, '/bringup_launch.py']),
            launch_arguments={
                'map': map_dir,
                'use_sim_time': use_sim_time}.items(),
        ),
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
        
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(get_package_share_directory('turtlebot3_gazebo'), 'launch', 'spawn_turtlebot3.launch.py')
            )
        ),   

        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            arguments=['-d', rviz_config_dir],
            parameters=[{'use_sim_time': use_sim_time}],
            output='screen'),

        # # Nav2 Bringup
        # IncludeLaunchDescription(
        #     PythonLaunchDescriptionSource(
        #         os.path.join(get_package_share_directory('nav2_bringup'), 'launch', 'bringup_launch.py')
        #     ),
        #     launch_arguments={
        #         'map': map_file,
        #         'use_sim_time': LaunchConfiguration('use_sim_time')
        #     }.items()
        # ),
        
        # RViz
        # Node(
        #     package='rviz2',
        #     executable='rviz2',
        #     name='rviz2',
        #     output='screen',
        #     arguments=['-d', rviz_config]
        # ),

    #     DeclareLaunchArgument(
    #     'map',
    #     default_value=map_file,
    #     description='Path to the map file to use'
    # )
    ])
