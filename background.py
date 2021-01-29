import pygame as pg
import os

class Background(pg.sprite.Sprite):
  def __init__(self, width, height):
    pg.sprite.Sprite.__init__(self)
    self.image = pg.Surface((width, height))
    self.image.fill((0, 173, 173))
    self.rect = self.image.get_rect()