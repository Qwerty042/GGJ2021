import pygame as pg
import math
import os

class Player(pg.sprite.Sprite):
  def __init__(self, width, height, startpos):
    pg.sprite.Sprite.__init__(self)
    self.original_image = pg.transform.smoothscale(pg.image.load(os.path.join("Assets", "temp_player_2.png")), (width, height)).convert_alpha()
    self.image = self.original_image.copy()
    self.rect = self.image.get_rect()
    self.rect.center = startpos
    self.direction = 0                           # zero indicates the player is pointing to the right of screen
    self.pos_x, self.pos_y = self.rect.center    # have to use a seperate position variable because rect only uses integers

  def update(self):
    self.image = self.rot_center(self.original_image,self.direction)

  def rot_center(self, image, angle):
    """rotate an image while keeping its center and size"""
    orig_rect = image.get_rect()
    rot_image = pg.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image

  def rotate(self, angle):
    self.direction += angle
    if self.direction >= 360:
      self.direction = 0
    if self.direction < 0:
      self.direction = 360

  def move(self, distance, island_mask):
    next_pos_x = self.pos_x + distance*math.cos(math.radians(self.direction))
    next_pos_y = self.pos_y - distance*math.sin(math.radians(self.direction))
    
    if island_mask.get_at((int(next_pos_x), int(next_pos_y))): # check if new pos is within the island
      self.pos_x = next_pos_x
      self.pos_y = next_pos_y

    self.rect.center = (self.pos_x, self.pos_y)