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
    # self.mask = pg.mask.from_surface(self.image)
    self.direction = 0                           # zero indicates the player is pointing to the right of screen
    self.pos_x, self.pos_y = self.rect.center    # have to use a seperate position variable because rect only uses integers
    self.walking_sound = pg.mixer.Sound(os.path.join("Assets", "walking.wav")) 
    
  def update(self):
    self.image = self.rot_center(self.original_image,self.direction)
    # self.mask = pg.mask.from_surface(self.image)

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

  def move(self, distance, island_mask, chests):
    if not pg.mixer.Channel(3).get_busy():
      pg.mixer.Channel(3).play(self.walking_sound)
    next_pos_x = self.pos_x + distance*math.cos(math.radians(self.direction))
    next_pos_y = self.pos_y - distance*math.sin(math.radians(self.direction))
      
    player_radius = max(self.rect.width, self.rect.height)
    
    for chest in chests:
      chest_mask = pg.mask.from_surface(chest.image)
      scaled_chest_mask = chest_mask.scale((chest.rect.width + player_radius, chest.rect.height + player_radius))
      scaled_chest_mask_size = scaled_chest_mask.get_size()
      scaled_chest_mask_pos = (chest.rect.centerx - scaled_chest_mask_size[0]//2, chest.rect.centery - scaled_chest_mask_size[1]//2)
      island_mask.erase(scaled_chest_mask, scaled_chest_mask_pos)

    if island_mask.get_at((int(next_pos_x), int(next_pos_y))): # new pos is inside island
      self.pos_x = next_pos_x
      self.pos_y = next_pos_y
    # else:
    #   points = island_mask.outline()
    #   min_dist = 1000
    #   min_dist_point = (0,0)
    #   for (x,y) in points:
    #     dist = abs(math.sqrt((x - next_pos_x)**2 + (y - next_pos_y)**2))
    #     # print("dist:" + str(dist) + " pos:" + str((x,y)) + " player:" + str((next_pos_x, next_pos_y)))
    #     if min_dist < dist:
    #       min_dist = dist
    #       min_dist_point = (x,y)
    #   self.pos_x, self.pos_y = min_dist_point

    # else: # new pos is outside island idk why but this code is broken
    #   offset = (int(next_pos_x - self.rect.width), int(next_pos_y - self.rect.height)) # find top left corner of player
    #   overlap = island_mask.overlap_mask(self.mask, offset)
    #   overlap_outline = overlap.outline()
    #   min_dist = 1000
    #   min_dist_pos = (0,0)
    #   for pos in overlap_outline:
    #     dist = abs(math.sqrt((pos[0] - next_pos_x)**2 + (pos[1] - next_pos_y)**2))
    #     if min_dist < dist:
    #       min_dist = dist
    #       min_dist_pos = pos
    #   self.pos_x, self.pos_y = min_dist_pos
        

    
    self.rect.center = (self.pos_x, self.pos_y)
