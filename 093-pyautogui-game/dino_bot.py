import pyautogui
import time
import PIL.ImageGrab as ImageGrab
pyautogui.FAILSAFE = True

PIXEL_R_ON = 172
PIXEL_G_ON = 172
PIXEL_B_ON = 172

box_area1 = (248, 268, 286, 318) #box coordinates(x1,y1, x2,y2) to detect obstacles

pixel_plant1 = (19, 9) #pixel coordinates(x1,y1) to detect plants
pixel_plant2 = (11, 21) #pixel coordinates(x1,y1) to detect plants
pixel_plant3 = (29, 15) #pixel coordinates(x1,y1) to detect plants
pixel_plant4 = (20, 33) #pixel coordinates(x1,y1) to detect plants
pixel_plant5 = (20, 42) #pixel coordinates(x1,y1) to detect plants

def jump():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    pyautogui.keyUp('space')
    print('Jump')

time.sleep(2)
print('Starting bot')

play = True
while play:
    try:
        box = ImageGrab.grab(box_area1)
        #box.show()
        #play = False
        p1 = box.getpixel(pixel_plant1)
        p2 = box.getpixel(pixel_plant2)
        p3 = box.getpixel(pixel_plant3)
        p4 = box.getpixel(pixel_plant4)
        p5 = box.getpixel(pixel_plant5)
    
        if (p1 == (PIXEL_R_ON, PIXEL_G_ON, PIXEL_B_ON) or 
            p2 == (PIXEL_R_ON, PIXEL_G_ON, PIXEL_B_ON) or 
            p3 == (PIXEL_R_ON, PIXEL_G_ON, PIXEL_B_ON) or 
            p4 == (PIXEL_R_ON, PIXEL_G_ON, PIXEL_B_ON) or 
            p5 == (PIXEL_R_ON, PIXEL_G_ON, PIXEL_B_ON)):
            #print(p1, p2, p3, p4, p5)
            jump()
            time.sleep(0.06)
    except Exception as e:
        play = False
        print(e)