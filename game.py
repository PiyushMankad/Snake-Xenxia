import pygame,sys,time,random


errors = pygame.init()
if errors[1]>0:
    print("Had {0} initializing errors".format(errors[1]))
    sys.exit()
else :
    print("Success")

surface = pygame.display.set_mode((720,480))
pygame.display.set_caption("Snake Xenxia")


#colours
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 225, 255)
blue = pygame.Color(0,255,255)
orange = pygame.Color(255,165,0)
red = pygame.Color(255,60,0)

#controller
fps = pygame.time.Clock()

#variables
head = [100,100]
body = [[100,100], [90,100], [80,100]]

food = [random.randrange(1,72)*10,random.randrange(1,48)*10]
foodspawn = True

direction = 'right'
changeto = direction

#function-> game over
def gameover():
    myFont = pygame.font.SysFont('AR Blanca',56)
    GOsurf = myFont.render('Game Over!', True, red)
    GOrect = GOsurf.get_rect()
    GOrect.midtop = (360,20)
    surface.blit(GOsurf,GOrect)
    pygame.display.flip()
    
gameover()
time.sleep(3)    
    
