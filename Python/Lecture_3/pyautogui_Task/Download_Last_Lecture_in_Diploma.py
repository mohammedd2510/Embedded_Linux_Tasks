import pyautogui 
from time import sleep
import webbrowser

webbrowser.open_new_tab("https://drive.google.com/drive/folders/1bWC1vrs4NwLqyS5tnQ_2SjdwJIMhUNsE")
sleep(2)
while True:    
    try:
        loc=pyautogui.locateOnScreen('img1.png')
    except:
        print('image not found')
    else:
        break
pyautogui.click(466,364)
pyautogui.click()
sleep(1)
pyautogui.rightClick()
pyautogui.press('down',presses=2)
pyautogui.press('enter')
