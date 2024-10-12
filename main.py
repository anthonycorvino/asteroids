import pygame
from constants import *
from player import Player 
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
   pygame.init()
   screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
   clock = pygame.time.Clock()
   dt = 0 #delta time

   updatable = pygame.sprite.Group()
   drawable = pygame.sprite.Group()
   asteroid = pygame.sprite.Group()

   Asteroid.containers = (asteroid, updatable, drawable)
   Player.containers = (updatable, drawable)
   AsteroidField.containers = (updatable)   

   AsteroidField()
   player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

   while True:
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            return

      screen.fill((0, 0, 0))

      for sprite in updatable:
         sprite.update(dt)
      for sprite in drawable:
         sprite.draw(screen)

      for a in asteroid:
         if player.check_collision(a):
            print("Game over!")
            return

      pygame.display.flip()
      pygame.time.delay(10)
      clock.tick(60)
      dt = clock.tick(60) / 1000


if __name__ == "__main__":
   main()
