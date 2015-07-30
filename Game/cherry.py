import pygame
from pygame.locals import *
import random

FPS = 60

class Cherry:
  def __init__(self,good,x,y):
    if (good):
      self.image = pygame.image.load("cherry.png")
    else:
      self.image = pygame.image.load("bad_cherry.png")

    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
    self.tele_check = 0
    self.tele_seconds = 99999

    self.x_dir = 7
    self.y_dir = 7

  def move(self,WIDTH,HEIGHT):
    if (self.rect.y <= 0 or self.rect.y >= HEIGHT - self.rect.height):
      self.y_dir *= -1
    if (self.rect.x <= 0 or self.rect.x >= WIDTH - self.rect.width):
      self.x_dir *= -1

    self.rect.move_ip(self.x_dir,self.y_dir)

  def teleport(self,WIDTH,HEIGHT):
    self.move(WIDTH,HEIGHT)

    if (self.tele_check == FPS*self.tele_seconds):
      self.rect.x = random.randint(0,WIDTH-self.rect.width)
      self.rect.y = random.randint(0,HEIGHT-self.rect.height)
      self.tele_check = 0
    else:
      self.tele_check += 1

