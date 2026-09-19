# generated from rosidl_cmake/cmake/rosidl_cmake_aggregate_target-extras.cmake.in

# Create a convenience aggregate target tutorial_interfaces::tutorial_interfaces
# that links all generated interface targets, so downstream packages can use
# a single modern CMake target name instead of ${tutorial_interfaces_TARGETS}.
if(tutorial_interfaces_TARGETS AND NOT TARGET tutorial_interfaces::tutorial_interfaces)
  add_library(tutorial_interfaces::tutorial_interfaces INTERFACE IMPORTED)
  set_target_properties(tutorial_interfaces::tutorial_interfaces PROPERTIES
    INTERFACE_LINK_LIBRARIES "${tutorial_interfaces_TARGETS}")
endif()
