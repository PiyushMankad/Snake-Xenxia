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

direction = 'RIGHT'
changeto = direction
score = 0

#function-> game over
def gameover():
    myFont = pygame.font.SysFont('AR Blanca',56)
    GOsurf = myFont.render('Game Over!', True, red)
    GOrect = GOsurf.get_rect()
    GOrect.midtop = (360,20)
    surface.blit(GOsurf,GOrect)
    pygame.display.flip()
    showscore(0)
    time.sleep(5)
    pygame.quit()
    sys.exit()
#function-> show score    
def showscore(choice=1):
    sFont = pygame.font.SysFont('AR Blanca',24)
    ssurf = sFont.render('Score : {0}'.format(score), True, black)
    srect = ssurf.get_rect()
    if choice == 1:
                         srect.midtop = (80,100)
    else:
                         srect.midtop = (360,120)
    surface.blit(ssurf,srect)
    pygame.display.flip()                     
#main logic
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                changeto = 'RIGHT'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                changeto = 'LEFT'
            if event.key == pygame.K_UP or event.key == ord('w'):
                changeto = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                changeto = 'DOWN'
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))
                
  #for not moving in the opposite direction              
    if changeto == 'RIGHT' and not direction == 'LEFT':
        direction ='RIGHT'
    if changeto == 'LEFT' and not direction == 'RIGHT':
        direction ='LEFT'
    if changeto == 'UP' and not direction == 'DOWN':
        direction ='UP'
    if changeto == 'DOWN' and not direction == 'UP':
        direction ='DOWN'
        
    #snake head position   
    if direction == 'RIGHT':
        head[0] += 10
    if direction == 'LEFT':
        head[0] -= 10
    if direction == 'DOWN':
        head[1] += 10
    if direction == 'UP':
        head[1] -= 10
        
    #body addition and deletion
    body.insert(0,list(head))
    if head[0] == food[0] and head[1] == food[1]:
        score +=1
        foodspawn = False
    else:
        body.pop()
     #food is eaten   
    if foodspawn == False:
        food = [random.randrange(1,72)*10,random.randrange(1,48)*10]
    foodspawn = True
    # background color
    surface.fill(white)
    for pos in body:
        pygame.draw.rect(surface, blue, pygame.Rect(pos[0],pos[1],10,10))
        
    pygame.draw.rect(surface, orange, pygame.Rect(food[0],food[1],10,10))
        
    #snake out of bounds
    if head[0] > 710 or head[0] < 0:
        gameover()
    if head[1] > 470 or head[1] < 0:
        gameover()
     #collision with itself   
    for block in body[1:]:
        if head[0] == block[0] and head[1] == block[1]:
            gameover()
    
    pygame.display.flip()#updates the screen
    showscore()                     
    fps.tick(11)# 11 times update in a second

    
    
    
    
    
    
    
