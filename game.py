import pygame as pg
import os
import sys
from player import *
from background import *
from island import *
from paper import *
from chest import *

  
class MainGame:
  def __init__(self):
    
    self.SCREEN_WIDTH = 1200
    self.SCREEN_HEIGHT = 800
    self.SCREEN_SIZE = (self.SCREEN_WIDTH, self.SCREEN_HEIGHT)

    pg.init()
    pg.font.init()
    self.screen = pg.display.set_mode(self.SCREEN_SIZE)
    pg.display.set_caption("LOST")

    self.bg_music = pg.mixer.Sound(os.path.join("Assets", "The_Islands_Mystery.wav"))

    self.background = Background(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
    self.island = Island(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
    self.player = Player(566//8, 566//8, (200, 200)) # I like me some magic numbers nom nom
    self.paper = Paper(self.SCREEN_WIDTH, 120, (0, self.SCREEN_HEIGHT - 120))
    self.chest_1 = Chest(642//8, 683//8, (288, 138), self.SCREEN_WIDTH, self.SCREEN_HEIGHT, [1,1,1,9])
    self.chest_2 = Chest(642//8, 683//8, (907, 125), self.SCREEN_WIDTH, self.SCREEN_HEIGHT, [2,2,2,9])
    self.chest_3 = Chest(642//8, 683//8, (200, 660), self.SCREEN_WIDTH, self.SCREEN_HEIGHT, [3,3,3,9])
    self.chest_4 = Chest(642//8, 683//8, (1025, 648), self.SCREEN_WIDTH, self.SCREEN_HEIGHT, [4,4,4,9])
    self.chest_5 = Chest(642//8, 683//8, (557, 585), self.SCREEN_WIDTH, self.SCREEN_HEIGHT, [5,5,5,9])
    self.chest_6 = Chest(642//8, 683//8, (550, 379), self.SCREEN_WIDTH, self.SCREEN_HEIGHT, [6,6,6,9])

    self.chests = [self.chest_1, self.chest_2, self.chest_3, self.chest_4, self.chest_5, self.chest_6]
    # list of all the sprite objects to be drawn
    # first in list is drawn first so will be underneath evertthing else
    self.sprite_group = pg.sprite.OrderedUpdates([
      self.background,
      self.island,
      self.player,
      *self.chests,
      self.paper
    ])


  def _game_logic(self, events):
    # add dank game logic here
    
    interacting = False
    for chest in self.chests:
      if chest.is_interacting:
        interacting = True
        break

    keys=pg.key.get_pressed()
    if not interacting:
      if keys[pg.K_a]:
        self.player.rotate(1)
      if keys[pg.K_d]:
        self.player.rotate(-1)
      if keys[pg.K_w]:
        self.player.move(1, self.island.mask, self.chest_1)
      if keys[pg.K_s]:
        self.player.move(-1, self.island.mask, self.chest_1)
    # if keys[pg.K_e]:

    for event in events:
      if (event.type == pg.KEYDOWN) and (event.key == pg.K_e):
        for chest in self.chests:
          if not chest.is_interacting:
            player_to_chest_dist = abs(math.sqrt((self.player.rect.centerx - chest.rect.centerx)**2 + (self.player.rect.centery - chest.rect.centery)**2))
            if player_to_chest_dist < 100:
              chest.interact()
          else:
            chest.interact()


    # call update functions of sprite objects in sprite group
    self.sprite_group.update()


  def _draw(self):
    # drawn in order they are in the sprite group
    # if this becomes a problem later with dynamically adding sprites
    #   we may need to draw individually or something
    #   maybe could have a dynamic nested sprite list perhaps?
    updated_area = self.sprite_group.draw(self.screen)
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
        if (event.type == pg.QUIT) or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
          sys.exit()




def main():
  main_game = MainGame()
  main_game.run()


if __name__ == "__main__": main()
