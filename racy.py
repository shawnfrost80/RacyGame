import pygame
import random

pygame.init()

display_width = 1000    
display_height = 800
car_width = 75

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

carimage = pygame.image.load("racecar1.jpg")


gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Racy')
clock = pygame.time.Clock()

def car(x,y):
    gameDisplay.blit(carimage, (x,y))

def box (boxX, boxY, boxW, boxH, color):
    pygame.draw.rect(gameDisplay, color, [boxX, boxY, boxW, boxH])

def gameLoop():
    
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    x_change = 0
    

    box_startx = random.randrange(0, display_width)
    box_starty = -800
    box_height = 100
    box_width = 100
    box_speed = 6

    crash = False

    while not crash:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crash = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5 

            if event.type == pygame.KEYUP:
                x_change = 0

        x += x_change
        gameDisplay.fill(white)

        #box (boxX, boxY, boxW, boxH, color)
        box(box_startx, box_starty, box_width, box_height, red)
        box_starty += box_speed

        if box_starty > display_height:
            box_speed += 1
            box_starty = -100
            box_startx = random.randrange(0, display_width)

        if y < box_starty:
            if x > box_startx and x < box_startx+box_width or x+car_width > box_startx and x+car_width < box_startx+box_width:
                crash = True

        car(x,y)       
        
        if x > display_width-car_width or x < 0:
            crash = True

        pygame.display.update()
        clock.tick(60)

gameLoop()
pygame.quit()
quit()
