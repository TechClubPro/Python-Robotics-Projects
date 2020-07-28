"""
Program to Rotate an image in a direction of a Gesture sensed through
two IR proximity sensors

IR Proximity Sensor1 is connected at IO pin 1 
IR Proximity Sensor2 is connected at IO pin 2 



IO Pin 1 is configured to Digital Input, to read Digital values from sensor
IO Pin 2 is configured to Digital Input, to read Digital values from sensor



"""
import phygital_v2 as phy
from time import sleep as s
import pygame
import rotateImage as rotator
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

img=pygame.image.load("Images/arrow.png")
newimg=pygame.transform.scale(img,(400,400))
        
screen.blit(newimg,(60,60))

phy.pinMode(1,"dinput")
phy.pinMode(2,"dinput")
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
            
        
        data1=phy.dRead(1)
        data2=phy.dRead(2)
        if data1 == 1:
            
            while data2==0:
                print("In While")
                data2=phy.dRead(2)
            screenImg = pygame.image.load("Images/background.jpg")
            screen.blit(screenImg,(0,0)) 
        
            img= pygame.image.load("Images/arrow.png")
               
       
            newimg=pygame.transform.scale(newimg,(400,400))
        
            for i in range (10,360,10):
                # print("in For")
                pygame.display.update()
                rotator.blitRotate(screen,newimg,(280,300),-i)
                print("in For")
                s(0.1)
            
        elif data2==1:
            while data1==0:
                data1=phy.dRead(1)
            screenImg = pygame.image.load("Images/background.jpg")
            screen.blit(screenImg,(0,0)) 
        
            img= pygame.image.load("Images/arrow.png")
               
       
            newimg=pygame.transform.scale(img,(400,400))
        
            for i in range (10,360,10):
                pygame.display.update()
                rotator.blitRotate(screen,newimg,(280,300),i)
                s(0.1)
        
        
        
    except:
        if KeyboardInterrupt:
            pygame.quit()
            phy.close()
            break
        
        
print("Closing")
