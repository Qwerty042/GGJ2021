import pygame as pg
import os



class MainGame:
  def __init__(self):
    pg.init()
    self.SCREEN_WIDTH = 1200
    self.SCREEN_HEIGHT = 800
    self.BG_COLOUR = (0, 173, 173)
    self.screen = pg.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
    self.bg_image = pg.image.load(os.path.join("Assets", "temp_island1.png")).convert_alpha()
    self.bg_image = pg.transform.scale(self.bg_image, (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))


  def game_loop(self, events):
    bg_surface = pg.Surface((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
    bg_surface.fill(self.BG_COLOUR)
    bg_surface.blit(self.bg_image, (0,0))
    self.screen.blit(bg_surface, (0,0))
    pg.display.update()
    return


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