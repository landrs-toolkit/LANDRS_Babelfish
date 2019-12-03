# Set minimums
cmake_minimum_required(VERSION 3.10)
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED True)

project(GeoMav VERSION 0.01)

# Add Mavlink2 Library
add_library(mavlink2 INTERFACE)
target_include_directories(mavlink2 INTERFACE
        $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/third_party/c_library_v2>
        $<INSTALL_INTERFACE:include/mavlink2>
        )

# Add the executable
add_executable(${PROJECT_NAME} geomavlink.cpp)
target_sources(${PROJECT_NAME} PUBLIC serial_port.cpp serial_port.h geomavlink.h autopilot_interface.cpp autopilot_interface.h)

# Link
target_link_libraries(${PROJECT_NAME} mavlink2 pthread)

