"""
Author : Bappy Ahmed
Email : bappymalik4161@gmail.com
Date : 11 sept 2020
"""

import pyautogui  #To automates our keyboards and mouse
from PIL import Image, ImageGrab #pip install pillow
import time
# from numpy import asarray

#for press up and down button
def hit(key):
    pyautogui.keyDown(key)
    return

#For taking a screenshot (auto)
def takeScreenshot():
    image = ImageGrab.grab().convert('L') #To converts into gray scale
    return image
    

def isCollide(data):
    #birds
    for i in range(170,220):
        for j in range(320,450):
            if data[i,j] < 100:
                hit("down")
                return 
    
    #cactus
    for i in range(180,250):
        for j in range(460,540):
            if data[i,j] < 100:
                hit("up")
                return 
    return 




if __name__ == "__main__":
    print("The game will start within 3 sec")
    time.sleep(2)
    hit("up")
    image = takeScreenshot()
        
    data = image.load()
        # print(asarray(image))
    
    while True:
        image = takeScreenshot()
        
        data = image.load()
        # print(asarray(image))
        isCollide(data)
            
        

        # #Draw the rectangle for cactus
        # for i in range(180,250):
        #     for j in range(460,540):
        #         data[i,j] = 0
        # image.show()

        # #Draw the rectangle for birds
        # for i in range(160,220):
        #     for j in range(320,450):  
        #         data[i,j] = 171
        # image.show()
        # break

   
   

            
   
        

