import pygame as pg
import os

class Paper(pg.sprite.Sprite):
  def __init__(self, width, height, pos):
    pg.sprite.Sprite.__init__(self)
    self.font = pg.font.SysFont(None, 48)
    self.image = pg.Surface((width - 8, height - 8))
    self.image.fill((0,0,0))
    self.inner = pg.Surface((width - 16, height - 16))
    self.inner.fill((255,255,255))
    self.rect = self.image.get_rect()
    self.rect.topleft = (pos[0] + 4, pos[1] + 4)
    self.image.blit(self.inner, (4,4))
    self.image.set_alpha(0)
    self.text = None

  def _clear_paper(self):
    self.image.fill((0,0,0))
    self.image.blit(self.inner, (4,4))

  def appear(self):
    self.image.set_alpha(255)

  def dissapear(self):
    self.image.set_alpha(0)

  def write(self, text):
    self.text = text
    self._clear_paper()
    rendered_text = self.font.render(self.text, True, (0,0,0))
    #text_rect = rendered_text.get_rect()
    self.image.blit(rendered_text, (10,10))
    