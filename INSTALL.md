We suppose you have installed ROS2 and that it is sourced in your terminal

To run the system, the interfaces and packages must be built:

### build
In a first terminal (we will call it T1)
```bash
# In ROS2_sim folder (./Deltacnc/ROS"_sim)
colcon build --packages-select delta_cnc_interface py_delta_cnc_package --cmake-clean-cache
source install/setup.bash
```

### run
In a second terminal (We will call it T2)
```bash
# In ROS2_sim folder (./Deltacnc/ROS"_sim)
source install/setup.bash
ros2 run py_delta_cnc_package dummy_gcode_executer
```

Back in T1:
```bash
ros2 run py_delta_cnc_package gcode_reader -- ../test_gcode.gcode
```

### result
In T1 you should see:
```bash
[INFO] [1753396633.842938321] [gcode_reader]: Publishing position: x=190.099, y=-109.901, z=750.0
[INFO] [1753396634.863540689] [gcode_reader]: Received confirmation: processed
[INFO] [1753396634.864831178] [gcode_reader]: Publishing position: x=190.099, y=-109.901, z=375.0
[INFO] [1753396635.866657519] [gcode_reader]: Received confirmation: processed
[INFO] [1753396635.868981552] [gcode_reader]: Publishing position: x=190.099, y=-109.901, z=325.0
[INFO] [1753396636.871323457] [gcode_reader]: Received confirmation: processed
[INFO] [1753396636.873281065] [gcode_reader]: Publishing position: x=190.099, y=-109.901, z=324.653
[INFO] [1753396637.876449871] [gcode_reader]: Received confirmation: processed
[INFO] [1753396637.879029570] [gcode_reader]: Publishing position: x=190.099, y=-109.901, z=324.306
[INFO] [1753396638.883084130] [gcode_reader]: Received confirmation: processed
[INFO] [1753396638.886676311] [gcode_reader]: Publishing position: x=190.099, y=-109.901, z=323.958
[INFO] [1753396639.888581251] [gcode_reader]: Received confirmation: processed
[INFO] [1753396639.890171897] [gcode_reader]: Publishing position: x=190.099, y=-109.901, z=323.611
[INFO] [1753396640.893719027] [gcode_reader]: Received confirmation: processed
```

and in T2:
```bash
[INFO] [1753396633.861997932] [dummy_gcode_executer]: Received position: x=190.099, y=-109.901, z=750.0
[INFO] [1753396634.863641919] [dummy_gcode_executer]: Publishing confirmation: processed
[INFO] [1753396634.865299374] [dummy_gcode_executer]: Received position: x=190.099, y=-109.901, z=375.0
[INFO] [1753396635.866269554] [dummy_gcode_executer]: Publishing confirmation: processed
[INFO] [1753396635.869192473] [dummy_gcode_executer]: Received position: x=190.099, y=-109.901, z=325.0
[INFO] [1753396636.870951722] [dummy_gcode_executer]: Publishing confirmation: processed
[INFO] [1753396636.873679886] [dummy_gcode_executer]: Received position: x=190.099, y=-109.901, z=324.653
[INFO] [1753396637.875965590] [dummy_gcode_executer]: Publishing confirmation: processed
[INFO] [1753396637.879527748] [dummy_gcode_executer]: Received position: x=190.099, y=-109.901, z=324.306
[INFO] [1753396638.882493572] [dummy_gcode_executer]: Publishing confirmation: processed
[INFO] [1753396638.887271705] [dummy_gcode_executer]: Received position: x=190.099, y=-109.901, z=323.958
[INFO] [1753396639.888806498] [dummy_gcode_executer]: Publishing confirmation: processed
[INFO] [1753396639.890989272] [dummy_gcode_executer]: Received position: x=190.099, y=-109.901, z=323.611
[INFO] [1753396640.893089153] [dummy_gcode_executer]: Publishing confirmation: processed
```