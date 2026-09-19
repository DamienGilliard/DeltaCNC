from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    return LaunchDescription([
        # Start Gazebo with our world
        ExecuteProcess(
            cmd=['gz', 'sim', '-s', '-r',
                 os.path.join(get_package_share_directory('gazebo_sim'),
                              'worlds', 'cnc_world.sdf')],
            output='screen'
        ),
        
        # Start the bridge - exposes Gazebo's set_pose service to ROS so
        # dummy_gcode_executer can actually move the sphere model.
        Node(
            package='ros_gz_bridge',
            executable='parameter_bridge',
            arguments=['/world/cnc_world/set_pose@ros_gz_interfaces/srv/SetEntityPose'],
            output='screen'
        ),
        
        # GCode reader
        Node(
            package='py_delta_cnc_package',
            executable='gcode_reader',
            arguments=['test_gcode.gcode'],
            output='screen'
        ),
        
        # Dummy executor
        Node(
            package='py_delta_cnc_package',
            executable='dummy_gcode_executer',
            output='screen'
        ),
    ])