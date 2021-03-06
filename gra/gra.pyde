###### I niech stanie się gra #######

import sys
import random

#Colors

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (240 ,255, 0)
PURPLE = (255, 0, 255)
ORANGE = (255, 140, 0)
CHOCOLATE = (123, 63, 0)
PINK = (255, 192, 203)
GREY = (128, 128, 128)

#ZMIENNE

global kosmos, Komandor #przez Komandor rozumiem gracza. 
kosmos = "kosmos.jpg"

#KLASY

class Sprite():
    def __init__(self, image, speed):
        self.image = image
        self.speed = speed
        
class Tlo():
    def wyswietl(self,img):
        img = loadImage(kosmos)
        image(img, width/2, height/2)
        
class Powitanie():
    def wyswietl(self):
        strokeWeight(0)
        fill(252, 237, 10)
        rect(width/2,height/2-10, width/2, 100)
        textSize(50)
        fill(0, 0, 0)
        text("Hello! Press start to begin.", width/2, height/2)

class Ship(Sprite): #baza obiektu statku
    def __init__(self):
        self.image = IMG['ship']
        self.speed = 6
        self.rect = self.image.get_rect(topleft=(375, 540))
        
    def ruchy(self, toLeft): #ruchy obiektu
        if toLeft:
            self.x = self.x + (Ship.right - Ship.left)
        else:
            self.x = self.x + (Ship.left - Ship.right)
        if self.x > width:
            self.x = 0
    
def setup():
    size(1280, 720)
    frameRate(30)
    imageMode(CENTER)
    textAlign(CENTER)
    rectMode(CENTER)
    myFont = createFont("Book Antiqua", 15)
    textFont(myFont)
    pass
    tlo = Tlo()
    tlo.wyswietl(kosmos)
    powitanie = Powitanie()
    powitanie.wyswietl()

def draw():
    pass
