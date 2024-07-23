import os 
from datetime import datetime
now = datetime.now()
date_var = now.strftime("%d/%m/%Y %H:%M:%S")
name = input("Please Enter Your Name \n")
print(f"Hello mr {name}")
Port_name = input("Please Enter Port Name\n(A,B,C,D)....")
Port_name =Port_name.upper()
port_value_str =""
for pin in range(8):    
    pin_value= input(f"Please Enter Bit {pin} Mode :\n(IN/OUT)....")
    pin_value = pin_value.upper()
    if (pin_value == 'OUT'):
        pin_value = '1'  
    elif (pin_value == "IN"):
        pin_value ='0'          
    port_value_str = pin_value + port_value_str

port_value_str = "0b"+port_value_str

print(port_value_str)
with open(f"Init_PORT{Port_name}_DIR.h","w")as file:
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
void Init_PORT{Port_name}_DIR(void);
               """)

with open(f"Init_PORT{Port_name}_DIR.c","w")as file:
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
#include "Init_PORT{Port_name}_DIR.h"

void Init_PORT{Port_name}_DIR(void)
{{
    DDR{Port_name} = {port_value_str};
}}
               """)                