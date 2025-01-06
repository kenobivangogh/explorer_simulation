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
        ('share/' + package_name + '/launch', ['launch/empty_world.launch.py']),
        ('share/' + package_name + '/launch', ['launch/simple_world.launch.py']),
        ('share/' + package_name + '/launch', ['launch/complex_world.launch.py']),
        ('share/' + package_name + '/launch', ['launch/denemedegil.launch.py']),
        ('share/' + 'turtlebot3_gazebo' + '/launch', ['launch/robot_state_publisher.launch.py']),
        ('share/' + 'turtlebot3_gazebo' + '/launch', ['launch/spawn_turtlebot3.launch.py']),
        # Harita dosyaları
        ('share/' + package_name + '/maps', ['maps/empty.pgm.yaml', 'maps/empty.pgm.pgm']),
        ('share/' + package_name + '/maps', ['maps/simple.pgm.yaml', 'maps/simple.pgm.pgm']),
        ('share/' + package_name + '/maps', ['maps/complex.pgm.yaml', 'maps/complex.pgm.pgm']),
        ('share/' + package_name + '/worlds', ['worlds/complexos.world']),
        ('share/' + package_name + '/worlds', ['worlds/emptyos.world']),
        ('share/' + package_name + '/worlds', ['worlds/simpleos.world']),
        ('share/' + package_name + '/rviz', ['rviz/tb3_gazebo.rviz']),

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
