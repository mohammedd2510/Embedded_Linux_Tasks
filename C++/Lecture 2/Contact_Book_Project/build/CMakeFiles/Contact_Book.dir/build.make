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
CMAKE_SOURCE_DIR = "/home/mohamed-osama/Embedded_Linux/Tasks/C++/Lecture 2/Contact_Book_Project"

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = "/home/mohamed-osama/Embedded_Linux/Tasks/C++/Lecture 2/Contact_Book_Project/build"

# Include any dependencies generated for this target.
include CMakeFiles/Contact_Book.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/Contact_Book.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/Contact_Book.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/Contact_Book.dir/flags.make

CMakeFiles/Contact_Book.dir/main.cpp.o: CMakeFiles/Contact_Book.dir/flags.make
CMakeFiles/Contact_Book.dir/main.cpp.o: /home/mohamed-osama/Embedded_Linux/Tasks/C++/Lecture\ 2/Contact_Book_Project/main.cpp
CMakeFiles/Contact_Book.dir/main.cpp.o: CMakeFiles/Contact_Book.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir="/home/mohamed-osama/Embedded_Linux/Tasks/C++/Lecture 2/Contact_Book_Project/build/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/Contact_Book.dir/main.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/Contact_Book.dir/main.cpp.o -MF CMakeFiles/Contact_Book.dir/main.cpp.o.d -o CMakeFiles/Contact_Book.dir/main.cpp.o -c "/home/mohamed-osama/Embedded_Linux/Tasks/C++/Lecture 2/Contact_Book_Project/main.cpp"

CMakeFiles/Contact_Book.dir/main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing CXX source to CMakeFiles/Contact_Book.dir/main.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E "/home/mohamed-osama/Embedded_Linux/Tasks/C++/Lecture 2/Contact_Book_Project/main.cpp" > CMakeFiles/Contact_Book.dir/main.cpp.i

CMakeFiles/Contact_Book.dir/main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling CXX source to assembly CMakeFiles/Contact_Book.dir/main.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S "/home/mohamed-osama/Embedded_Linux/Tasks/C++/Lecture 2/Contact_Book_Project/main.cpp" -o CMakeFiles/Contact_Book.dir/main.cpp.s

CMakeFiles/Contact_Book.dir/Contact_Book.cpp.o: CMakeFiles/Contact_Book.dir/flags.make
CMakeFiles/Contact_Book.dir/Contact_Book.cpp.o: /home/mohamed-osama/Embedded_Linux/Tasks/C++/Lecture\ 2/Contact_Book_Project/Contact_Book.cpp
CMakeFiles/Contact_Book.dir/Contact_Book.cpp.o: CMakeFiles/Contact_Book.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir="/home/mohamed-osama/Embedded_Linux/Tasks/C++/Lecture 2/Contact_Book_Project/build/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object CMakeFiles/Contact_Book.dir/Contact_Book.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/Contact_Book.dir/Contact_Book.cpp.o -MF CMakeFiles/Contact_Book.dir/Contact_Book.cpp.o.d -o CMakeFiles/Contact_Book.dir/Contact_Book.cpp.o -c "/home/mohamed-osama/Embedded_Linux/Tasks/C++/Lecture 2/Contact_Book_Project/Contact_Book.cpp"

CMakeFiles/Contact_Book.dir/Contact_Book.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing CXX source to CMakeFiles/Contact_Book.dir/Contact_Book.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E "/home/mohamed-osama/Embedded_Linux/Tasks/C++/Lecture 2/Contact_Book_Project/Contact_Book.cpp" > CMakeFiles/Contact_Book.dir/Contact_Book.cpp.i

CMakeFiles/Contact_Book.dir/Contact_Book.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling CXX source to assembly CMakeFiles/Contact_Book.dir/Contact_Book.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S "/home/mohamed-osama/Embedded_Linux/Tasks/C++/Lecture 2/Contact_Book_Project/Contact_Book.cpp" -o CMakeFiles/Contact_Book.dir/Contact_Book.cpp.s

# Object files for target Contact_Book
Contact_Book_OBJECTS = \
"CMakeFiles/Contact_Book.dir/main.cpp.o" \
"CMakeFiles/Contact_Book.dir/Contact_Book.cpp.o"

# External object files for target Contact_Book
Contact_Book_EXTERNAL_OBJECTS =

Contact_Book: CMakeFiles/Contact_Book.dir/main.cpp.o
Contact_Book: CMakeFiles/Contact_Book.dir/Contact_Book.cpp.o
Contact_Book: CMakeFiles/Contact_Book.dir/build.make
Contact_Book: CMakeFiles/Contact_Book.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --bold --progress-dir="/home/mohamed-osama/Embedded_Linux/Tasks/C++/Lecture 2/Contact_Book_Project/build/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_3) "Linking CXX executable Contact_Book"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/Contact_Book.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/Contact_Book.dir/build: Contact_Book
.PHONY : CMakeFiles/Contact_Book.dir/build

CMakeFiles/Contact_Book.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/Contact_Book.dir/cmake_clean.cmake
.PHONY : CMakeFiles/Contact_Book.dir/clean

CMakeFiles/Contact_Book.dir/depend:
	cd "/home/mohamed-osama/Embedded_Linux/Tasks/C++/Lecture 2/Contact_Book_Project/build" && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" "/home/mohamed-osama/Embedded_Linux/Tasks/C++/Lecture 2/Contact_Book_Project" "/home/mohamed-osama/Embedded_Linux/Tasks/C++/Lecture 2/Contact_Book_Project" "/home/mohamed-osama/Embedded_Linux/Tasks/C++/Lecture 2/Contact_Book_Project/build" "/home/mohamed-osama/Embedded_Linux/Tasks/C++/Lecture 2/Contact_Book_Project/build" "/home/mohamed-osama/Embedded_Linux/Tasks/C++/Lecture 2/Contact_Book_Project/build/CMakeFiles/Contact_Book.dir/DependInfo.cmake" "--color=$(COLOR)"
.PHONY : CMakeFiles/Contact_Book.dir/depend

