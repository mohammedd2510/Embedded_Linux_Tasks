import os
import shutil
from datetime import datetime
now = datetime.now()
date_var = now.strftime("%d/%m/%Y %H:%M:%S")
name = input("Please Enter Your Name \n")
print(f"Hello mr {name}")
project_name = input("Enter Project Name \n")
#1-clean
if os.path.exists(project_name):
    shutil.rmtree(project_name)
    print("Folder Deleted")

#2-Create Files
os.system(f"mkdir -p {project_name}/src")
os.system(f"mkdir -p {project_name}/build")
os.system(f"mkdir -p {project_name}/test")
os.system(f"touch {project_name}/src/main.cpp")
os.system(f"touch {project_name}/CMakeLists.txt")

#3- Update main.cpp
with open(f"{project_name}/src/main.cpp","w")as file:
    file.write(f"""/************************************************/
//
//              CopyRight {name}
//
/************************************************/
/*
author: {name}
date: {date_var}
breif:
*/
#include <iostream>

int main()
{{
    std::cout << "Hello World" << std::endl;

    return 0;
}}
                """) 

#4- Update CMakeLists.txt      
with open(f"{project_name}/CMakeLists.txt","w")as file:
    file.write(f"""cmake_minimum_required(VERSION 3.10)
project({project_name})
add_executable({project_name} src/main.cpp)                
                """)
           
#5- build
os.chdir(f"{project_name}/build")
os.system(f"cmake .. && make -j && ./{project_name}")
print("Done")