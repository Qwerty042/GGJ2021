import pygame as pg
import os

class Chest(pg.sprite.Sprite):
  def __init__(self, width, height, pos):
    pg.sprite.Sprite.__init__(self)
    self.open_image = pg.transform.smoothscale(pg.image.load(os.path.join("Assets", "temp_chest_open_1.png")), (width,height)).convert_alpha()
    self.closed_image = pg.transform.smoothscale(pg.image.load(os.path.join("Assets", "temp_chest_closed_1.png")), (width,height)).convert_alpha()
    self.image = self.closed_image
    self.rect = self.image.get_rect()
    self.rect.center = pos
    self.closed = True

  def interact(self):
    self.closed = not self.closed
    if self.closed: self.image = self.closed_image
    else: self.image = self.open_image

    