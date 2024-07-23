from customtkinter import *

window = CTk()
num1var = StringVar()
num2var = StringVar()
resultvar = StringVar()
radio_var = IntVar()
sum
def button_event():
    global num1var,num2var,resultvar,radio_var
    if radio_var.get() == 1:
        resultvar.set("SUM = "+str((int(num1var.get())+int(num2var.get()))))
    elif radio_var.get() == 2:
        resultvar.set("SUB = "+str((int(num1var.get())-int(num2var.get()))))
    else:
        resultvar.set("Check sum or sub please")    

window.geometry("400x200+500+200")
window.title("ADD_OR_SUB")
set_appearance_mode("light")
FirstNumlabel = CTkLabel(window, text="Enter The 1st num", fg_color="transparent").grid(row="0",column="1",padx="10")
SecondNumlabel = CTkLabel(window, fg_color="transparent",text="Enter The 2nd num").grid(row="1",column="1",padx="10")
FirstNumEntry =CTkEntry(window, textvariable=num1var,font=("Arial",16)).grid(row="0",column ="2",pady="3")
SecondNumEntry =CTkEntry(window, textvariable=num2var,font=("Arial",16)).grid(row="1",column ="2",pady="3")
ResultLabel=CTkLabel(window,textvariable= resultvar).grid(row=2,column=2)
button = CTkButton(window, text="Calculate", command=button_event).grid(row="3",column="2")
sumradiobutton = CTkRadioButton(window,text="Sum",variable=radio_var ,value=1).grid(row="3",column="1")
subradiobutton = CTkRadioButton(window,text="Sub",variable=radio_var ,value=2).grid(row="4",column="1")


window.mainloop()
