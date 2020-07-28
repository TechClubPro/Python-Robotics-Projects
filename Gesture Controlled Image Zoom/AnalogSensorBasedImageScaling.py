"""
Program to scale an Image 
depending on the values read through IR Distance Sensor.

IR Distance Sensor is connected at IO pin 1 (Pin 27 of ESP32)

scaling width & Height is adjusted by mapping 
Highest Width(700), Highest Height (640) 
to Heighest Analog Reading by sensor(4095)

IO Pin 1 is configured to Analog Input, to read analog values from sensor

We used floor operator to get integer values of Width and Height
"""
import phygital_v2 as phy
from time import sleep as s
import pygame

pygame.init()


""" Set the Dimension of the Screen"""
Width = 700
Height = 640

""" Set the Screen"""
screen = pygame.display.set_mode((Width,Height))


""" Set The Title of Screen"""
pygame.display.set_caption("Sensor Based Display")

""" Load the Image"""
screenImg = pygame.image.load("Images/background.jpg")

""" Display Image at Specific Co-Ordinate"""

screen.blit(screenImg,(0,0))

img=pygame.image.load("Images/apple.jpg")
screen.blit(img,(60,60))

phy.pinMode(1,"ainput")
phy.init("COM13")

while True:
    try:
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                phy.close()
                EventStatus="Quit"
                break
            
        
        data=phy.aRead(1)
        print(data)
        
        newWidth=data//8
        newHeight= data//8
        
        # print(bright)
        screenImg = pygame.image.load("Images/background.jpg")
        screen.blit(screenImg,(0,0)) 
        
        img= pygame.image.load("Images/apple.jpg")
               
        # #Function to adjust brightness of the image
        # img.fill((bright,bright,bright),special_flags=pygame.BLEND_RGB_ADD)
        newimg=pygame.transform.scale(img,(newWidth,newHeight))
        screen.blit(newimg,(10,10)) 
 
        # time.sleep(1)
        
    except:
        if KeyboardInterrupt:
            pygame.quit()
            phy.close()
            break
        
        
print("Closing")