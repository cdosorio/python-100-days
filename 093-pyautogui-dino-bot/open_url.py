import pyautogui, time 

def crometest():  
    screenWidth, screenHeight = pyautogui.size()  
    pyautogui.moveTo(0,screenHeight)  
    pyautogui.click()  
    pyautogui.typewrite('Chrome', interval=0.25)  
    pyautogui.press('enter')  
    time.sleep(2)  
    pyautogui.keyDown('alt')  
    pyautogui.press(' ')  
    pyautogui.press('x')  
    pyautogui.keyUp('alt')  
    pyautogui.click(250,22)  
    pyautogui.click(371,51)  
    pyautogui.typewrite('https://javatpoint.com/python-tutorial')  
    pyautogui.press('enter')  


pyautogui.FAILSAFE = False
crometest()  