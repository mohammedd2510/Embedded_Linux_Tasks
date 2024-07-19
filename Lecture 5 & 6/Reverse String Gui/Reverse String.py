from customtkinter import *

window = CTk()
textvar = StringVar()
label2_text = StringVar()
def button_event():
    global textvar
    label2_text.set("Reversed String: "+textvar.get()[-1::-1])

window.geometry("400x200+500+200")
window.title("Reverse a String")
set_appearance_mode("light")
label = CTkLabel(window, text="Enter String", fg_color="transparent").grid(row="0",column="2",padx="10")
entry =CTkEntry(window, textvariable=textvar,font=("Arial",16)).grid(row="0",column ="3",pady="3")
button = CTkButton(window, text="Reverse", command=button_event).grid(row="2",column="3")
label2 = CTkLabel(window, fg_color="transparent",textvariable=label2_text,font=("Arial",16)).grid(row="1",column="3")
window.mainloop()
