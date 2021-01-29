import pygame as pg
import os

class Player(pg.sprite.Sprite):
  def __init__(self, width, height, startpos):
    pg.sprite.Sprite.__init__(self)
    self.image = pg.transform.scale(pg.image.load(os.path.join("Assets", "temp_player_1.png")), (width, height)).convert_alpha()
    self.rect = self.image.get_rect()
    self.rect.center = startpos
    self.direction = 0 #zero indicates the player is pointing to the right of screen