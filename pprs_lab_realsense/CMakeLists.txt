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
find_package(PCL 1.5 REQUIRED)
# find_package(pcl_conversions REQUIRED)
find_package(OpenCV REQUIRED)
find_package(realsense2 REQUIRED)


include_directories(${PCL_INCLUDE_DIRS} ${rclcpp_INCLUDE_DIRS}) # ${pcl_converstions_INCLUDE_DIRS} )
link_directories(${PCL_LIBRARY_DIRS})
add_definitions(${PCL_DEFINITIONS})

add_executable(pcl_filtering_example_1 src/pcl_filtering_example_1.cpp)
# ament_target_dependencies(pcl_filtering_example_1 )
target_link_libraries(pcl_filtering_example_1 ${PCL_LIBRARIES})

add_executable(pcl_filtering_example_2 src/pcl_filtering_example_2.cpp)
target_link_libraries(pcl_filtering_example_2 ${PCL_LIBRARIES})

add_executable(pcl_yt_example_1 src/pcl_yt_example_1.cpp)
target_link_libraries(pcl_yt_example_1 ${PCL_LIBRARIES})

add_executable(opencv_example_1 src/opencv_example_1.cpp)
target_link_libraries(opencv_example_1 ${OpenCV_LIBS})

add_executable(rs_example_1 src/rs_example_1.cpp)
target_link_libraries(rs_example_1 realsense2)

add_executable(rs_example_2 src/rs_example_2.cpp)
target_link_libraries(rs_example_2 realsense2 ${OpenCV_LIBS})

add_executable(pcl_interactive_icp_1 src/pcl_interactive_icp_1.cpp)
target_link_libraries(pcl_interactive_icp_1 ${PCL_LIBRARIES})

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

install(
  TARGETS
  # rs-pcl
  pcl_filtering_example_1
  pcl_filtering_example_2
  pcl_yt_example_1
  opencv_example_1
  rs_example_1
  rs_example_2
  pcl_interactive_icp_1
  DESTINATION
  lib/${PROJECT_NAME}
)

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
