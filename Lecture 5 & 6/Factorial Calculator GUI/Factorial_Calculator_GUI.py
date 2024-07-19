from customtkinter import *

window = CTk()
textvar = StringVar()
label2_text = StringVar()

def num_factorial(num):
    num_int = int(num)
    fact = 1
    for i in range(1,num_int+1):
        fact *= i
    return str(fact)    


def button_event():
    global textvar
    label2_text.set(f"Factorial of {textvar.get()} = {num_factorial(textvar.get())} ")
                    
window.geometry("400x200+500+200")
window.title("Num Factorial ")
set_appearance_mode("light")
label = CTkLabel(window, text="Enter The Number", fg_color="transparent").grid(row="0",column="2",padx="10")
entry =CTkEntry(window, textvariable=textvar,font=("Arial",16)).grid(row="0",column ="3",pady="3")
button = CTkButton(window, text="Calulate Factorial", command=button_event).grid(row="2",column="3")
label2 = CTkLabel(window, fg_color="transparent",textvariable=label2_text,font=("Arial",16)).grid(row="1",column="3")
window.mainloop()