import pygame as pg
import os

class Scroll(pg.sprite.Sprite):
  def __init__(self, width, height, pos):
    pg.sprite.Sprite.__init__(self)
    self.image = pg.transform.smoothscale(pg.image.load(os.path.join("Assets", "temp_scroll_1.png")), (width, height)).convert_alpha()
    self.rect = self.image.get_rect()
    self.rect.center = pos
    self.is_interacting = False

  def interact(self):
    self.is_interacting = not self.is_interacting