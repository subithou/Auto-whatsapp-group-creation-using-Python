# Auto whatsapp group creation using python
* Automatically create multiple whatsapp group for specific contacts using python.  
* You can create groups how much you want. 

## Requirements
* Download and install the Whatsapp Desktop version : https://www.whatsapp.com/download  
* Install the Python modules
```python
pip install pyautogui
```

## Python code
* First  open the **Whatsapp desktop version** (Not whatsapp web)
* Save the below code as filename.py extension in your computer and run the code.
  
```python
from time import time
from pyautogui import hotkey, press, typewrite 
import time

# move to whatsapp desktop version
hotkey('alt', 'tab')

# short key for open create new group in whatsapp desktop version
hotkey('ctrl', 'shift', 'n' )

# Specify how many groups you want to create
no_of_group = 1


for j in range(0,no_of_group): 
    for i in range(0,1):
        typewrite("unnikkuttan")  # Specify the contact name as per your phone with in double quote
        press('enter')
    
    press('enter')
    typewrite("GRP4") # Specify group name with in double quote
    press('enter')  # In this step we successfully complete the creation of a group
    time.sleep(3)
    hotkey('ctrl', 'shift', 'n' ) # short key for open create new group 

```


