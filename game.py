import pygame as pg



class MainGame:
  def __init__(self):
    pg.init()
    self.SCREEN_WIDTH = 1200
    self.SCREEN_HEIGHT = 800
    self.screen = pg.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))


  def game_loop(self, events):
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