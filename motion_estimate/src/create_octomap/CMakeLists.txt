set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++0x -Wno-deprecated-declarations")

cmake_minimum_required(VERSION 2.8 FATAL_ERROR)
project(create_octomap)


################
add_executable(se-create-octomap create_octomap.cpp convert_octomap.cpp cloud_accumulate.cpp)
pods_use_pkg_config_packages(se-create-octomap  
    path-util ${REQUIRED_PACKAGES}
    pronto_vis  octomap eigen3
    octomap-util)
#    drc-utils
target_link_libraries (se-create-octomap lcm pronto_math 
                        boost_system boost_thread)
pods_install_executables(se-create-octomap )
