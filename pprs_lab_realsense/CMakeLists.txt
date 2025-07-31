cmake_minimum_required(VERSION 3.8)
project(pprs_lab_realsense)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
# uncomment the following section in order to fill in
# further dependencies manually.
# find_package(<dependency> REQUIRED)
find_package(PCL REQUIRED)
# find_package(pcl_conversions REQUIRED)


include_directories(
  $PCL INCLUDE_DIRS{}
  ${rclcpp_INCLUDE_DIRS}
#  ${pcl_converstions_INCLUDE_DIRS}
)

add_executable(pcl_example_1 src/pcl_example_1.cpp)
ament_target_dependencies(pcl_example_1 )


# add_executable(
#   rs-pcl
#   src/rs-pcl.cpp
# )

# target_link_libraries(
#   rs-pcl
#   ${PCL_LIBRARIES}
# #  ${rclcpp_LIBRARIES}
# #  ${pcl_conversions_LIBRARIES}
# )

# install(
#   TARGETS
#   rs-pcl
#   DESTINATION
#   lib/${PROJECT_NAME}
# )

install(
  DIRECTORY
  config
  launch
  DESTINATION
  share/${PROJECT_NAME}
)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # comment the line when a copyright and license is added to all source files
  set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # comment the line when this package is in a git repo and when
  # a copyright and license is added to all source files
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
