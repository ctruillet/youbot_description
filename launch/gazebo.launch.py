from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess


def generate_launch_description():
        return LaunchDescription([
            ExecuteProcess(
            #    cmd=['gazebo', '--verbose', 'sdf/world.sdf', '-s libgazebo_ros_factory.so'],
                cmd=['gazebo', '--verbose', 'sdf/world.sdf'],
                output='screen'
            ),
            Node(
                package='teleop_twist_keyboard',
                namespace='teleop_twist_keyboard',
                executable='teleop_twist_keyboard',
                remappings=[
                    ('/teleop_twist_keyboard/cmd_vel','/youbot/cmd_vel')
                ],
                output='screen',
                prefix = 'xterm -e'
            )
    ])