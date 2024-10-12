import sys
import pygame
from constants import *
from player import Player 
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from score import Score

def main():
   pygame.init()
   screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
   clock = pygame.time.Clock()

   updatable = pygame.sprite.Group()
   drawable = pygame.sprite.Group()
   asteroid = pygame.sprite.Group()
   shots = pygame.sprite.Group()

   Asteroid.containers = (asteroid, updatable, drawable)
   Player.containers = (updatable, drawable)
   AsteroidField.containers = (updatable)   
   Shot.containers = (shots, updatable, drawable)
   AsteroidField()

   player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
   dt = 0 #delta time
   score = Score()

   while True:
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            return

      for sprite in updatable:
         sprite.update(dt)
      
      for a in asteroid:
         if player.check_collision(a):
            print("Game over!")
            sys.exit()

         for shot in shots:
            if a.check_collision(shot):
               a.split(shot, score)
      
      screen.fill("black")
      score.draw(screen)

      for sprite in drawable:
         sprite.draw(screen)
      
      pygame.display.flip()
      dt = clock.tick(60) / 1000


if __name__ == "__main__":
   main()
