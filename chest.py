import pygame as pg
from moviepy.editor import VideoFileClip
import os

class Chest(pg.sprite.Sprite):
  def __init__(self, width, height, pos, screen_width, screen_height, passcode, secret_message, is_ending_chest = False):
    pg.sprite.Sprite.__init__(self)
    self.font = pg.font.SysFont(None, 256)
    self.font.set_bold(True)
    self.open_image = pg.transform.smoothscale(pg.image.load(os.path.join("Assets", "temp_chest_open_1.png")), (width,height)).convert_alpha()
    self.closed_image = pg.transform.smoothscale(pg.image.load(os.path.join("Assets", "temp_chest_closed_1.png")), (width,height)).convert_alpha()
    self.image = self.closed_image
    self.rect = self.image.get_rect()
    self.pos = pos
    self.rect.center = self.pos
    self.screen_width = screen_width
    self.screen_height = screen_height
    self.is_locked = True
    self.is_interacting = False
    self.is_digit_pressed = False
    self.digits = [None, None, None, None]
    self.passcode = passcode
    self.secret_message = secret_message
    self.is_ending_chest = is_ending_chest
    if self.is_ending_chest:
      self.ending_clip = VideoFileClip('Assets/ending_video.mpg')
    else:
      self.ending_clip = None
    self.open_sound = pg.mixer.Sound(os.path.join("Assets", "chest_opening.wav"))
    self.failed_open_sound = pg.mixer.Sound(os.path.join("Assets", "chest_failed_open.wav"))
    self.enter_number_sound = pg.mixer.Sound(os.path.join("Assets", "enter_number.wav"))
    self.open_number_panel_sound = pg.mixer.Sound(os.path.join("Assets", "open_number_panel.wav"))
    self.close_number_panel_sound = pg.mixer.Sound(os.path.join("Assets", "close_number_panel.wav"))

  def interact(self, paper):
    self.is_interacting = not self.is_interacting
    if self.is_interacting:
      if self.is_locked:
        pg.mixer.Channel(1).play(self.open_number_panel_sound)
        self.digits = [None, None, None, None]
      else:
        if self.is_ending_chest:
          self.ending_clip.preview()
          pg.quit()
        else:
          pg.mixer.Channel(1).play(self.open_sound)
          paper.write(self.secret_message)
          paper.appear()
          pass
    else:
      if self.is_locked:
        pg.mixer.Channel(1).play(self.close_number_panel_sound)
        self.image = self.closed_image
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
      else:
        paper.dissapear()

  def _draw_digits(self):
    block_height = 300
    block_width = 180
    block_offset = (50,50)
    block_offset_x_step = ((self.rect.width - 100 - (4 * block_width))//3) + block_width
    self.image
    for digit in self.digits:
      if digit == None:
        digit_str = '-'
      else:
        digit_str = str(digit)
      rendered_digit = self.font.render(digit_str, True, (200,200,200))
      digit_width, digit_height = rendered_digit.get_size()
      rendered_block = pg.Surface((block_width,block_height))
      rendered_block.fill((20,60,80))
      digit_offset = (block_width//2 - digit_width//2 + 5, block_height//2 - digit_height//2)
      rendered_block.blit(rendered_digit, digit_offset)
      self.image.blit(rendered_block, block_offset)
      block_offset = (block_offset[0] + block_offset_x_step, block_offset[1])



  def update(self, paper):
    if self.is_interacting:
      if self.is_locked:
        self.image = pg.Surface((self.screen_width - 200, self.screen_height - 200))
        self.image.fill((79, 83, 97))
        self.rect = self.image.get_rect()
        self.rect.center = (self.screen_width//2, self.screen_height//2)
        
        keys = pg.key.get_pressed()
        if not self.is_digit_pressed:
          if keys[pg.K_0]:
            self.is_digit_pressed = True
            pg.mixer.Channel(1).play(self.enter_number_sound)
            self.digits[self.digits.index(None)] = 0
          elif keys[pg.K_1]:
            self.is_digit_pressed = True
            pg.mixer.Channel(1).play(self.enter_number_sound)
            self.digits[self.digits.index(None)] = 1
          elif keys[pg.K_2]:
            self.is_digit_pressed = True
            pg.mixer.Channel(1).play(self.enter_number_sound)
            self.digits[self.digits.index(None)] = 2
          elif keys[pg.K_3]:
            self.is_digit_pressed = True
            pg.mixer.Channel(1).play(self.enter_number_sound)
            self.digits[self.digits.index(None)] = 3
          elif keys[pg.K_4]:
            self.is_digit_pressed = True
            pg.mixer.Channel(1).play(self.enter_number_sound)
            self.digits[self.digits.index(None)] = 4
          elif keys[pg.K_5]:
            self.is_digit_pressed = True
            pg.mixer.Channel(1).play(self.enter_number_sound)
            self.digits[self.digits.index(None)] = 5
          elif keys[pg.K_6]:
            self.is_digit_pressed = True
            pg.mixer.Channel(1).play(self.enter_number_sound)
            self.digits[self.digits.index(None)] = 6
          elif keys[pg.K_7]:
            self.is_digit_pressed = True
            pg.mixer.Channel(1).play(self.enter_number_sound)
            self.digits[self.digits.index(None)] = 7
          elif keys[pg.K_8]:
            self.is_digit_pressed = True
            pg.mixer.Channel(1).play(self.enter_number_sound)
            self.digits[self.digits.index(None)] = 8
          elif keys[pg.K_9]:
            self.is_digit_pressed = True
            pg.mixer.Channel(1).play(self.enter_number_sound)
            self.digits[self.digits.index(None)] = 9
        elif not (keys[pg.K_0]
                  or keys[pg.K_1]
                  or keys[pg.K_2]
                  or keys[pg.K_3]
                  or keys[pg.K_4]
                  or keys[pg.K_5]
                  or keys[pg.K_6]
                  or keys[pg.K_7]
                  or keys[pg.K_8]
                  or keys[pg.K_9]): self.is_digit_pressed = False

        self._draw_digits()

        if self.digits.count(None) == 0:
          if self.digits == self.passcode:
            self.is_locked = False
            self.image = self.open_image
            self.is_interacting = False
            self.interact(paper)
          else:
            pg.mixer.Channel(1).play(self.failed_open_sound)
            self.image = self.closed_image
            self.is_interacting = False
          self.rect = self.image.get_rect()
          self.rect.center = self.pos
          
      
      
