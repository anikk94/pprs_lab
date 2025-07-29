from launch_ros.actions import Node
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare


print("global scope: Hello!")


realsense_stream = IncludeLaunchDescription(
    PythonLaunchDescriptionSource(
        PathJoinSubstitution([
            FindPackageShare('realsense2_camera'),
            'launch',
            'rs_launch.py',
        ]),
    ),
    launch_arguments={
        'pointcloud.enable': 'True',
    }.items(),
)

rviz = Node(
    package='rviz2',
    executable='rviz2',
    arguments=['-d', PathJoinSubstitution([
        FindPackageShare('pprs_lab_realsense'),
        'config',
        'rviz_config_1.rviz'
        ]),
    ]
)   




def generate_launch_description():
    return LaunchDescription([
        realsense_stream,
        rviz
    ])
