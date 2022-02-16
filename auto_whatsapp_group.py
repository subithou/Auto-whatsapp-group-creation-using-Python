from time import time
from pyautogui import hotkey, press, typewrite 

# move to whatsapp web 
hotkey('alt', 'tab')

# short key for open create new group in whatsapp web
# hotkey('ctrl', 'shift', 'n' )
hotkey('ctrl', 'alt','shift', 'n' )
# Specify how many groups you want to create
no_of_group = 1


for j in range(0,no_of_group*2): 
    for i in range(0,1):
        typewrite("unnikkuttan")  # Specify the contact name as per your phone with in double quote
        press('enter')
    
    press('enter')
    typewrite("GRP4") # Specify group name with in double quote
    press('enter')  # In this step we successfully complete the creation of a group
    hotkey('ctrl', 'shift', 'n' ) # short key for open create new group 

