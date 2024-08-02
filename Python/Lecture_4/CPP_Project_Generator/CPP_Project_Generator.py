import os
import shutil
from datetime import datetime
now = datetime.now()
date_var = now.strftime("%d/%m/%Y %H:%M:%S")
name = "Mohamed Osama"
print(f"Hello mr {name}")
project_name = input("Enter Project Name \n")

#2-Create Files
os.chdir(f"~/Embedded_Linux/Tests/
")
os.system(f"mkdir -p {project_name}/build")
os.system(f"mkdir -p {project_name}/test")
os.system(f"touch {project_name}/main.cpp")
os.system(f"touch {project_name}/CMakeLists.txt")

#3- Update main.cpp
with open(f"{project_name}/main.cpp","w")as file:
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