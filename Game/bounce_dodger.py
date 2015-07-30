import pygame
from pygame.locals import *
import sys
import time
import random
from cherry import *

WIDTH = 800
HEIGHT = 600
P_SIDE = 50
P_SPEED = 5
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
CYAN = (0,255,255)
FPS = 60
score = 0

def drawText(text, font, surface, x, y):
  textobj = font.render(text, 1, BLACK)
  textrect = textobj.get_rect()
  textrect.topleft = (x, y)
  surface.blit(textobj, textrect)

def wait4Key():
    while True:
      for event in pygame.event.get():
        if event.type == KEYDOWN:
          pygame.quit()
          sys.exit()

pygame.init()
clock = pygame.time.Clock()
font = pygame.font.SysFont("Comic Sans MS", 36)


screen = pygame.display.set_mode((WIDTH,HEIGHT),DOUBLEBUF)
pygame.display.set_caption("Bounce Dodger")

player = pygame.Rect(0,00,P_SIDE,P_SIDE)
red_cherry = Cherry(True,750,550)

evils = []
for i in range (30):
  validplace = False
  while(not validplace):
    cher = Cherry(False,random.randint(0,WIDTH),random.randint(0,HEIGHT))
    for c in evils:
      if (cher.colliderect(c)):
        validplace = False
        break
      validplace = True
      
    if (validplace):
      evils.append(cher)
    else:
      del cher


''' HW: Make a second cherry and have it
teleport every second '''

move_r = move_l = move_u = move_d = False
while (True):

  # check for user input
  for event in pygame.event.get():
    if (event.type == KEYDOWN):
      if (event.key == K_ESCAPE):
        pygame.quit()
        sys.exit()
      if (event.key == K_RIGHT):
        move_r = True
      if (event.key == K_DOWN):
        move_d = True
      if (event.key == K_UP):
        move_u = True
      if (event.key == K_LEFT):
        move_l = True
      if (event.key == ord('s')):
        P_SPEED = 10
    ''' HW: MAKE IT MOVE UP AND LEFT AS WELL '''
    if (event.type == KEYUP):
      if (event.key == K_RIGHT):
        move_r = False
      if (event.key == K_DOWN):
        move_d = False
      if (event.key == K_UP):
        move_u = False
      if (event.key == K_LEFT):
        move_l = False

  # update things based on input
  if (move_r and player.x < WIDTH - P_SIDE):
    player.move_ip(P_SPEED,0)
  if (move_d and player.y < HEIGHT - P_SIDE):
    player.move_ip(0,P_SPEED)
  if (move_l and player.x > 0):
    player.move_ip(-1*P_SPEED,0)
  if (move_u and player.y > 0):
    player.move_ip(0,-1*P_SPEED)
  ''' HW: MAKE IT MOVE UP AND LEFT AS WELL '''
  
  #red_cherry.teleport(WIDTH,HEIGHT)
  #redCherry2.teleport(WIDTH,HEIGHT)
  #evil_cherry.teleport(WIDTH,HEIGHT)

  if (player.colliderect(red_cherry.rect)):
    score += 500000
  for i in evils:
    if (player.colliderect(i)):
        score -=100

  if (score <= -100):
    lose_str = "You lose! Press any key to exit"
    drawText(lose_str,font,screen,WIDTH/4,HEIGHT/2)
    pygame.display.update()
    wait4Key()

  if (score >= 1000):
    win_str = "You win! Press any key to exit"
    drawText(win_str,font,screen,WIDTH/4,HEIGHT/2)
    pygame.display.update()
    wait4Key()

  # draw
  screen.fill(WHITE)
  pygame.draw.rect(screen, CYAN, player)
  screen.blit(red_cherry.image,red_cherry.rect)
  for temp in evils:
    screen.blit(temp.image,temp.rect)

  #score_str = "Score: " + str(score)
  #drawText(score_str, font, screen, 10, 10)

  pygame.display.update()

  clock.tick(FPS)


pygame.quit()
sys.exit()
