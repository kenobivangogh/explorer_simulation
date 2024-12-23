from setuptools import find_packages, setup
#import os
#from glob import glob

package_name = 'explorer_simulation'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/simple_world.launch.py']),
        ('share/' + package_name + '/launch', ['launch/multi_geo_world.launch.py']),
        ('share/' + package_name + '/launch', ['launch/square_world.launch.py']),
        ('share/' + package_name + '/launch', ['launch/complex_world.launch.py']),
        ('share/' + package_name + '/launch', ['launch/high_complex_world.launch.py']),
        ('share/' + package_name + '/launch', ['launch/test.launch.py']),
        ('share/' + package_name + '/launch', ['launch/deneme123.launch.py']),
        ('share/' + package_name + '/launch', ['launch/cartographer.launch.py']),
        ('share/' + 'turtlebot3_gazebo' + '/launch', ['launch/robot_state_publisher.launch.py']),
        ('share/' + 'turtlebot3_gazebo' + '/launch', ['launch/spawn_turtlebot3.launch.py']),
        #('share/' + 'nav2_bringup' + '/launch', ['launch/bringup_launch.py']),
        ('share/' + package_name + '/worlds', ['worlds/simple.world']),
        ('share/' + package_name + '/worlds', ['worlds/multi_geo.world']),
        ('share/' + package_name + '/worlds', ['worlds/square.world']),
        ('share/' + package_name + '/worlds', ['worlds/complex.world']),
        ('share/' + package_name + '/worlds', ['worlds/high_complex.world']),
        ('share/' + package_name + '/worlds', ['worlds/deneme.world']),
        ('share/' + package_name + '/rviz', ['rviz/tb3_gazebo.rviz']),
        ('share/' + package_name + '/rviz', ['rviz/cartographer.rviz']),
        ('share/' + package_name + '/rviz', ['rviz/turtle_carto.rviz']),
        ('share/' + package_name + '/rviz', ['rviz/tb3_cartographer.rviz']),
        ('share/' + package_name + '/rviz', ['rviz/deneme.rviz']),
   #     ('share/' + package_name + '/turtlebot3_cartographer', 
      #   glob('/opt/ros/humble/share/turtlebot3_cartographer/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='obivan',
    maintainer_email='007kaplankaplan@gmail.com',
    description='Simulation package',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
