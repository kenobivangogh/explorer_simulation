from setuptools import find_packages, setup

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
        ('share/' + package_name + '/launch', ['launch/deneme.launch.py']),
        ('share/' + 'turtlebot3_gazebo' + '/launch', ['launch/robot_state_publisher.launch.py']),
        ('share/' + 'turtlebot3_gazebo' + '/launch', ['launch/spawn_turtlebot3.launch.py']),
        ('share/' + package_name + '/worlds', ['worlds/simple.world']),
        ('share/' + package_name + '/worlds', ['worlds/multi_geo.world']),
        ('share/' + package_name + '/worlds', ['worlds/square.world']),
        ('share/' + package_name + '/worlds', ['worlds/complex.world']),
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
