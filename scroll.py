import pygame as pg
import os

class Scroll(pg.sprite.Sprite):
  def __init__(self, width, height, pos, message):
    pg.sprite.Sprite.__init__(self)
    self.image = pg.transform.smoothscale(pg.image.load(os.path.join("Assets", "temp_scroll_1.png")), (width, height)).convert_alpha()
    self.rect = self.image.get_rect()
    self.rect.center = pos
    self.is_interacting = False
    self.message = message
    self.open_sound = pg.mixer.Sound(os.path.join("Assets", "scroll.wav"))

  def interact(self, paper):
    self.is_interacting = not self.is_interacting
    if self.is_interacting:
      pg.mixer.Channel(1).play(self.open_sound)
      paper.write(self.message)
      paper.appear()
    else:
      paper.dissapear()
