import pygame as pg
from moviepy.editor import VideoFileClip
import os
import sys
from player import *
from background import *
from island import *
from paper import *
from chest import *
from scroll import *

  
class MainGame:
  def __init__(self):
    
    self.SCREEN_WIDTH = 1200
    self.SCREEN_HEIGHT = 800
    self.SCREEN_SIZE = (self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
    chest_secret_messages = [
      "Nice.",
      "tinyurl.com/aliensarerealandtheyarehere",
      "Nice.",
      "Password: check the game description for the password",
      "https://pastebin.com/mLGDVsMc",
      "YOU WIN!",
    ]

    scroll_messages = [
      "4, 8, 15, 16, 23, 42",
      "The code to the south chest is the year Gabriel Cramer was born.",
      "Press E to interact with objects... oh wait you just have."
    ]

    pg.init()
    pg.font.init()
    self.screen = pg.display.set_mode(self.SCREEN_SIZE)
    pg.display.set_caption("LOST")

    self.bg_music = pg.mixer.Sound(os.path.join("Assets", "The_Islands_Mystery.wav"))

    self.background = Background(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
    self.island = Island(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
    self.player = Player(566//8, 566//8, (200, 200)) # I like me some magic numbers nom nom
    self.paper = Paper(self.SCREEN_WIDTH, 120, (0, self.SCREEN_HEIGHT - 120))
    self.chest_1 = Chest(642//8, 683//8, (288, 138), self.SCREEN_WIDTH, self.SCREEN_HEIGHT, [6,9,6,9], chest_secret_messages[0])
    self.chest_2 = Chest(642//8, 683//8, (907, 125), self.SCREEN_WIDTH, self.SCREEN_HEIGHT, [5,5,1,6], chest_secret_messages[1])
    self.chest_3 = Chest(642//8, 683//8, (200, 570), self.SCREEN_WIDTH, self.SCREEN_HEIGHT, [6,9,6,9], chest_secret_messages[2])
    self.chest_4 = Chest(642//8, 683//8, (1035, 572), self.SCREEN_WIDTH, self.SCREEN_HEIGHT, [9,8,5,7], chest_secret_messages[3])
    self.chest_5 = Chest(642//8, 683//8, (557, 585), self.SCREEN_WIDTH, self.SCREEN_HEIGHT, [1,7,0,4], chest_secret_messages[4])
    self.chest_6 = Chest(642//8, 683//8, (550, 329), self.SCREEN_WIDTH, self.SCREEN_HEIGHT, [6,0,7,9], chest_secret_messages[5], is_ending_chest = True)
    self.scroll_1 = Scroll(395//8, 404//8, (120, 305), scroll_messages[0])
    self.scroll_2 = Scroll(395//8, 404//8, (633, 129), scroll_messages[1])
    self.scroll_3 = Scroll(395//8, 404//8, (900, 415), scroll_messages[2])

    self.chests = [self.chest_1, self.chest_2, self.chest_3, self.chest_4, self.chest_5, self.chest_6]
    self.scrolls = [self.scroll_1, self.scroll_2, self.scroll_3]
    # list of all the sprite objects to be drawn
    # first in list is drawn first so will be underneath evertthing else
    self.main_sprite_group = pg.sprite.OrderedUpdates([
      self.background,
      self.island,
      *self.scrolls,
      self.player
    ])

    self.chests_sprite_group = pg.sprite.OrderedUpdates(self.chests)
    self.overlay_sprite_group = pg.sprite.OrderedUpdates(self.paper)


  def _game_logic(self, events):
    # add dank game logic here
    
    interacting = False
    for chest in self.chests:
      if chest.is_interacting:
        interacting = True
        break
    if not interacting:
      for scroll in self.scrolls:
        if scroll.is_interacting:
          interacting = True
          break

    keys=pg.key.get_pressed()
    if not interacting:
      if keys[pg.K_a]:
        self.player.rotate(1)
      if keys[pg.K_d]:
        self.player.rotate(-1)
      if keys[pg.K_w]:
        self.player.move(1, self.island.mask, self.chests)
      if keys[pg.K_s]:
        self.player.move(-1, self.island.mask, self.chests)

    for event in events:
      if (event.type == pg.KEYDOWN) and (event.key == pg.K_e):
        for chest in self.chests:
          if not chest.is_interacting:
            player_to_chest_dist = abs(math.sqrt((self.player.rect.centerx - chest.rect.centerx)**2 + (self.player.rect.centery - chest.rect.centery)**2))
            if player_to_chest_dist < 110:
              chest.interact(self.paper)
          else:
            chest.interact(self.paper)
        
        for scroll in self.scrolls:
          if not scroll.is_interacting:
            player_to_scroll_dist = abs(math.sqrt((self.player.rect.centerx - scroll.rect.centerx)**2 + (self.player.rect.centery - scroll.rect.centery)**2))
            if player_to_scroll_dist < 80:
              scroll.interact(self.paper)
          else:
            scroll.interact(self.paper)



    # call update functions of sprite objects in sprite group
    self.main_sprite_group.update()
    for chest in self.chests:
      chest.update(self.paper)


  def _draw(self):
    # drawn in order they are in the sprite group
    # if this becomes a problem later with dynamically adding sprites
    #   we may need to draw individually or something
    #   maybe could have a dynamic nested sprite list perhaps?
    updated_area = self.main_sprite_group.draw(self.screen)
    updated_area += self.chests_sprite_group.draw(self.screen)
    updated_area += self.overlay_sprite_group.draw(self.screen)
    for chest in self.chests:
      if chest.is_interacting:
        self.screen.blit(chest.image, chest.rect.topleft)
        break

    pg.display.update(updated_area)


        


  def run(self):
    
    pg.mixer.Channel(0).play(self.bg_music, -1)
    
    while True:
      # pg.event.get() clears event queue once called so need to save
      #   the list of events so that they can be used but other objects etc
      events = pg.event.get()

      self._game_logic(events)
      self._draw()

      # So you can actually exit the game
      for event in events:
        if (event.type == pg.QUIT):
          pg.quit()




def main():
  icon = pg.image.load('Assets/L.png')
  pg.display.set_icon(icon)
  pg.display.set_caption("LOST")
  clip = VideoFileClip('Assets/intro_video.mpg')
  clip.preview()
  main_game = MainGame()
  main_game.run()


if __name__ == "__main__": main()
