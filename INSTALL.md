We suppose you have installed ROS2 and that it is sourced in your terminal

To run the system, the interfaces and packages must be built:

### build
In a first terminal (we will call it T1)
```bash
# In ROS2_sim folder (./Deltacnc/ROS"_sim)
colcon build --packages-select delta_cnc_interface py_delta_cnc_package gazebo_sim --cmake-clean-cache
source install/setup.bash
```

### run
gazebo simulation:

```bash
source /opt/ros/jazzy/setup.bash
source install/setup.bash
gz sim -v 4 -r gazebo_sim/worlds/cnc_world.sdf
```

```bash
source install/setup.bash
ros2 run ros_gz_bridge parameter_bridge /world/cnc_world/set_pose@ros_gz_interfaces/srv/SetEntityPose
```

```bash
source install/setup.bash
ros2 run py_delta_cnc_package gcode_reader ~/DeltaCNC/test_gcode.gcode
```

```bash
# In ROS2_sim folder (./Deltacnc/ROS"_sim)
source install/setup.bash
ros2 run py_delta_cnc_package dummy_gcode_executer
```


### Result
You should see a small sphere moving in the gazebo world. A small delay before it starts is to be expected