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

class Heart:
  def __init__(self,x,y):
    self.image = pygame.image.load("heart.png")
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y


