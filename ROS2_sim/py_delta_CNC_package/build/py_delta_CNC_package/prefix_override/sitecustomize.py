import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/damien/DeltaCNC/ROS2_sim/py_delta_CNC_package/install/py_delta_CNC_package'
