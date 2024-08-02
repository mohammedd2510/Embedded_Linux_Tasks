# Distributed under the OSI-approved BSD 3-Clause License.  See accompanying
# file Copyright.txt or https://cmake.org/licensing for details.

cmake_minimum_required(VERSION 3.5)

file(MAKE_DIRECTORY
  "/home/mohamed-osama/Embedded_Linux/Tasks/C++/Lecture 3/Backtrace_Task/build/_deps/backward-src"
  "/home/mohamed-osama/Embedded_Linux/Tasks/C++/Lecture 3/Backtrace_Task/build/_deps/backward-build"
  "/home/mohamed-osama/Embedded_Linux/Tasks/C++/Lecture 3/Backtrace_Task/build/_deps/backward-subbuild/backward-populate-prefix"
  "/home/mohamed-osama/Embedded_Linux/Tasks/C++/Lecture 3/Backtrace_Task/build/_deps/backward-subbuild/backward-populate-prefix/tmp"
  "/home/mohamed-osama/Embedded_Linux/Tasks/C++/Lecture 3/Backtrace_Task/build/_deps/backward-subbuild/backward-populate-prefix/src/backward-populate-stamp"
  "/home/mohamed-osama/Embedded_Linux/Tasks/C++/Lecture 3/Backtrace_Task/build/_deps/backward-subbuild/backward-populate-prefix/src"
  "/home/mohamed-osama/Embedded_Linux/Tasks/C++/Lecture 3/Backtrace_Task/build/_deps/backward-subbuild/backward-populate-prefix/src/backward-populate-stamp"
)

set(configSubDirs )
foreach(subDir IN LISTS configSubDirs)
    file(MAKE_DIRECTORY "/home/mohamed-osama/Embedded_Linux/Tasks/C++/Lecture 3/Backtrace_Task/build/_deps/backward-subbuild/backward-populate-prefix/src/backward-populate-stamp/${subDir}")
endforeach()
if(cfgdir)
  file(MAKE_DIRECTORY "/home/mohamed-osama/Embedded_Linux/Tasks/C++/Lecture 3/Backtrace_Task/build/_deps/backward-subbuild/backward-populate-prefix/src/backward-populate-stamp${cfgdir}") # cfgdir has leading slash
endif()
