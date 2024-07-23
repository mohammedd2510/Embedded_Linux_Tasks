import os 
from datetime import datetime
now = datetime.now()
date_var = now.strftime("%d/%m/%Y %H:%M:%S")
name = input("Please Enter Your Name \n")
print(f"Hello mr {name}")
class_name = input("Please Enter Your Class Name\n")
namespace = input("Please Enter Your Namespace \n")
print(f"your class name is {class_name} ,your namespace is {namespace}")

with open(f"{class_name}.hpp","w")as file:
    file.write(f"""#pragma once
/************************************************/
//
//              CopyRight {name}
//
/************************************************/
/*
author: {name}
date: {date_var}
breif:
*/
namespace {namespace} 
{{
    class {class_name}
    {{
    public:
        {class_name}();
        ~{class_name}();
    private:
        
    }};
}};
               """)

flag = input(" Do you want the cpp file  Y/N")
flag=flag.lower()
if(flag == 'y'):
    with open(f"{class_name}.cpp","w")as file:
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
#include "{class_name}.hpp"
namespace {namespace} 
    {{
        {class_name}::{class_name}()
        {{

        }};
        {class_name}::~{class_name}()
        {{

        }};
            
    }};
                """)   