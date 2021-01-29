import pygame as pg
import os
from player import *
from background import *



class MainGame:
  def __init__(self):
    pg.init()
    self.SCREEN_WIDTH = 1200
    self.SCREEN_HEIGHT = 800

    self.screen = pg.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
    pg.display.set_caption("LOST")

    bg_image = pg.transform.scale(pg.image.load(os.path.join("Assets", "temp_island1.png")).convert_alpha(), (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
    self.background = pg.Surface((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
    self.background.fill((0, 173, 173))
    self.background.blit(bg_image, (0,0))
    
    


  def game_loop(self, events):

    self.screen.blit(self.background, (0,0))
    pg.display.update()


  def run(self):
    while True:
      events = pg.event.get()
      
      self.game_loop(events)

      # so you can actually get out of the game
      for event in events:
        if (event.type == pg.QUIT) or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
          exit()

      
  

def main():
  main_game = MainGame()
  main_game.run()

if __name__ == "__main__": main()