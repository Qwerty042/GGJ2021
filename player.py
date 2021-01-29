import pygame as pg
import os

class Player(pg.sprite.Sprite):
  def __init__(self, width, height):
    pg.sprite.Sprite.__init__(self)
    self.image = pg.transform.scale(pg.image.load(os.path.join("Assets", "temp_player_1.png")), (width, height)).convert_alpha()
    self.rect = self.image.get_rect()