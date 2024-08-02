cmake_minimum_required(VERSION 3.10)
project(Backtrace)
add_executable(Backtrace main.cpp Backtrace.cpp)      

target_compile_definitions(Backtrace PRIVATE BOOST_STACKTRACE_USE_ADDR2LINE)
target_compile_options(Backtrace PRIVATE "-g;-fno-inline")
target_link_options(Backtrace PRIVATE "-no-pie")
target_link_libraries(Backtrace ${Boost_LIBRARIES}  dl)



