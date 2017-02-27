PROJECT(CrowTest)
cmake_minimum_required(VERSION 2.8)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
CONAN_BASIC_SETUP()

ADD_EXECUTABLE(include_crow include_crow.cc)
target_link_libraries(include_crow ${CONAN_LIBS})
