import pygame as pg
import os
import sys
from player import *
from background import *
from island import *

  
class MainGame:
  def __init__(self):
    
    self.SCREEN_WIDTH = 1200
    self.SCREEN_HEIGHT = 800
    self.SCREEN_SIZE = (self.SCREEN_WIDTH, self.SCREEN_HEIGHT)

    pg.init()
    self.screen = pg.display.set_mode(self.SCREEN_SIZE)
    pg.display.set_caption("LOST")

    self.background = Background(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
    self.island = Island(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
    self.player = Player(566//8, 566//8, (200, 200)) # I like me some magic numbers nom nom

    # list of all the sprite objects to be drawn
    # first in list is drawn first so will be underneath evertthing else
    self.sprite_group = pg.sprite.OrderedUpdates([
      self.background,
      self.island,
      self.player
    ])


  def _game_logic(self, events):
    # add dank game logic here
    
    keys=pg.key.get_pressed()
    if keys[pg.K_a]:
      self.player.rotate(1)
    if keys[pg.K_d]:
      self.player.rotate(-1)
    if keys[pg.K_w]:
      self.player.move(1)
    if keys[pg.K_s]:
      self.player.move(-1)
    # call update functions of sprite objects
    for sprite in self.sprite_group:
      sprite.update()
    return


  def _draw(self):
    # drawn in order they are in the sprite group
    # if this becomes a problem later with dynamically adding sprites
    #   we may need to draw individually or something
    #   maybe could have a dynamic nested sprite list perhaps?
    updated_area = self.sprite_group.draw(self.screen)
    pg.display.update(updated_area)


  def run(self):
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
