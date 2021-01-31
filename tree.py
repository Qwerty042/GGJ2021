import pygame as pg
import os

class Tree(pg.sprite.Sprite):
  def __init__(self, width, height, pos):
    pg.sprite.Sprite.__init__(self)
    self.image = pg.transform.smoothscale(pg.image.load(os.path.join("Assets", "temp_tree_1.png")), (width, height)).convert_alpha()
    self.rect = self.image.get_rect()
    self.mask_image = pg.transform.smoothscale(pg.image.load(os.path.join("Assets", "temp_tree_mask_1.png")), (width, height)).convert_alpha()
    self.rect.center = pos