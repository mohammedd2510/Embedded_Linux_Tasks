# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.28

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = "/home/mohamed-osama/Embedded_Linux/Tasks/C++/Lecture 3/Backtrace_Task"

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = "/home/mohamed-osama/Embedded_Linux/Tasks/C++/Lecture 3/Backtrace_Task/build"

# Include any dependencies generated for this target.
include CMakeFiles/Backtrace.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/Backtrace.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/Backtrace.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/Backtrace.dir/flags.make

CMakeFiles/Backtrace.dir/main.cpp.o: CMakeFiles/Backtrace.dir/flags.make
CMakeFiles/Backtrace.dir/main.cpp.o: /home/mohamed-osama/Embedded_Linux/Tasks/C++/Lecture\ 3/Backtrace_Task/main.cpp
CMakeFiles/Backtrace.dir/main.cpp.o: CMakeFiles/Backtrace.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir="/home/mohamed-osama/Embedded_Linux/Tasks/C++/Lecture 3/Backtrace_Task/build/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/Backtrace.dir/main.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/Backtrace.dir/main.cpp.o -MF CMakeFiles/Backtrace.dir/main.cpp.o.d -o CMakeFiles/Backtrace.dir/main.cpp.o -c "/home/mohamed-osama/Embedded_Linux/Tasks/C++/Lecture 3/Backtrace_Task/main.cpp"

CMakeFiles/Backtrace.dir/main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing CXX source to CMakeFiles/Backtrace.dir/main.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E "/home/mohamed-osama/Embedded_Linux/Tasks/C++/Lecture 3/Backtrace_Task/main.cpp" > CMakeFiles/Backtrace.dir/main.cpp.i

CMakeFiles/Backtrace.dir/main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling CXX source to assembly CMakeFiles/Backtrace.dir/main.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S "/home/mohamed-osama/Embedded_Linux/Tasks/C++/Lecture 3/Backtrace_Task/main.cpp" -o CMakeFiles/Backtrace.dir/main.cpp.s

CMakeFiles/Backtrace.dir/Backtrace.cpp.o: CMakeFiles/Backtrace.dir/flags.make
CMakeFiles/Backtrace.dir/Backtrace.cpp.o: /home/mohamed-osama/Embedded_Linux/Tasks/C++/Lecture\ 3/Backtrace_Task/Backtrace.cpp
CMakeFiles/Backtrace.dir/Backtrace.cpp.o: CMakeFiles/Backtrace.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir="/home/mohamed-osama/Embedded_Linux/Tasks/C++/Lecture 3/Backtrace_Task/build/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object CMakeFiles/Backtrace.dir/Backtrace.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/Backtrace.dir/Backtrace.cpp.o -MF CMakeFiles/Backtrace.dir/Backtrace.cpp.o.d -o CMakeFiles/Backtrace.dir/Backtrace.cpp.o -c "/home/mohamed-osama/Embedded_Linux/Tasks/C++/Lecture 3/Backtrace_Task/Backtrace.cpp"

CMakeFiles/Backtrace.dir/Backtrace.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing CXX source to CMakeFiles/Backtrace.dir/Backtrace.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E "/home/mohamed-osama/Embedded_Linux/Tasks/C++/Lecture 3/Backtrace_Task/Backtrace.cpp" > CMakeFiles/Backtrace.dir/Backtrace.cpp.i

CMakeFiles/Backtrace.dir/Backtrace.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling CXX source to assembly CMakeFiles/Backtrace.dir/Backtrace.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S "/home/mohamed-osama/Embedded_Linux/Tasks/C++/Lecture 3/Backtrace_Task/Backtrace.cpp" -o CMakeFiles/Backtrace.dir/Backtrace.cpp.s

# Object files for target Backtrace
Backtrace_OBJECTS = \
"CMakeFiles/Backtrace.dir/main.cpp.o" \
"CMakeFiles/Backtrace.dir/Backtrace.cpp.o"

# External object files for target Backtrace
Backtrace_EXTERNAL_OBJECTS =

Backtrace: CMakeFiles/Backtrace.dir/main.cpp.o
Backtrace: CMakeFiles/Backtrace.dir/Backtrace.cpp.o
Backtrace: CMakeFiles/Backtrace.dir/build.make
Backtrace: CMakeFiles/Backtrace.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --bold --progress-dir="/home/mohamed-osama/Embedded_Linux/Tasks/C++/Lecture 3/Backtrace_Task/build/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_3) "Linking CXX executable Backtrace"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/Backtrace.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/Backtrace.dir/build: Backtrace
.PHONY : CMakeFiles/Backtrace.dir/build

CMakeFiles/Backtrace.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/Backtrace.dir/cmake_clean.cmake
.PHONY : CMakeFiles/Backtrace.dir/clean

CMakeFiles/Backtrace.dir/depend:
	cd "/home/mohamed-osama/Embedded_Linux/Tasks/C++/Lecture 3/Backtrace_Task/build" && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" "/home/mohamed-osama/Embedded_Linux/Tasks/C++/Lecture 3/Backtrace_Task" "/home/mohamed-osama/Embedded_Linux/Tasks/C++/Lecture 3/Backtrace_Task" "/home/mohamed-osama/Embedded_Linux/Tasks/C++/Lecture 3/Backtrace_Task/build" "/home/mohamed-osama/Embedded_Linux/Tasks/C++/Lecture 3/Backtrace_Task/build" "/home/mohamed-osama/Embedded_Linux/Tasks/C++/Lecture 3/Backtrace_Task/build/CMakeFiles/Backtrace.dir/DependInfo.cmake" "--color=$(COLOR)"
.PHONY : CMakeFiles/Backtrace.dir/depend

