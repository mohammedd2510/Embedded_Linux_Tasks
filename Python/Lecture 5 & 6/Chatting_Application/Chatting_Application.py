
import socket
import threading
from customtkinter import *
from time import sleep
# ***************** Global Variables ***************

server = ""
ip = ""
client = ""
address = " "
window = CTk()
ServerMessage = StringVar()
RecievedMessage= StringVar()
Server_Message_Status = 0
Client_Connected_Status = 0
Connected_Status_String = StringVar()
#***************************************************


def Server_Sends_Task():
     global server , client ,ip,address,ServerMessage,Server_Message_Status
     while True:
        if (Server_Message_Status == 1):
            try:
                client.send((ServerMessage.get()+"\r\n").encode("UTF-8"))
                print(f"server sends :  {ServerMessage.get()}")
            except:
                print("client not connected")
            Server_Message_Status = 0    
                    

def Server_Recieves_Task():
     global server , client ,ip,address ,RecievedMessage ,Connected_Status_String
     while True:
        client,address = server.accept()
        Connected_Status_String.set("Server Connected to Client")
        print (f" Server Connected to client of Address {address}")
        while True:
            rodata = client.recv(4096)
            if(rodata.decode("UTF-8")==""):
                Connected_Status_String.set("Server Not Connected")
                print("Server Disconnected")
                break 
            print(f'Client Sends : {rodata.decode("UTF-8")}') 
            RecievedMessage.set(rodata.decode("UTF-8")) 
       
def Server_Init():
    global server , client ,ip,address
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ip = "192.168.1.11"
    print(f"Your Ip Address is {ip}")
    print("="*20)
    server.bind((ip,5000))
    server.listen(5) 

def button_event():
    global ServerMessage,RecievedMessage,Server_Message_Status
    Server_Message_Status = 1
        

def Gui_Init():
    global window,ServerMessage,RecievedMessage,Connected_Status_String
    window.geometry("540x200+500+200")
    window.title("Chatting Application")
    set_appearance_mode("light")
    ServerSendLabel = CTkLabel(window, text="Server :", fg_color="transparent").grid(row="0",column="1",padx="10")
    ClientSendlabel = CTkLabel(window, fg_color="transparent",text="Client : ").grid(row="1",column="1")
    ServerMsgEntry =CTkEntry(window, textvariable=ServerMessage, width=300).grid(row="0",column ="2",pady="3")
    ResultLabel=CTkLabel(window,textvariable= RecievedMessage,anchor="w").grid(row=1,column=2,sticky="w")
    button = CTkButton(window, text="Send", command=button_event).grid(row="0",column="3")
    Connected_Status_Label = CTkLabel(window,textvariable= Connected_Status_String).grid(row=4,column=2)
    Connected_Status_String.set("Server Not Connected")

if (__name__ == "__main__"):
    Server_Init()
    Gui_Init()
    Server_Sends_Thread = threading.Thread(target=Server_Sends_Task)
    Server_Sends_Thread.daemon = True
    Server_Sends_Thread .start()
    Server_Recieves_Thread =threading.Thread(target=Server_Recieves_Task)
    Server_Recieves_Thread.daemon = TRUE
    Server_Recieves_Thread.start()
    window.mainloop()









    
     
