from constants import *
from circleshape import CircleShape
import pygame
from shot import Shot


class Player(CircleShape):
   def __init__(self, x, y):
      self.x = x
      self.y = y
      self.rotation = 0
      super().__init__(self.x, self.y, PLAYER_RADIUS)
      self.timer = 0.0

   def triangle(self):
    forward = pygame.Vector2(0, 1).rotate(self.rotation)
    right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
    a = self.position + forward * self.radius
    b = self.position - forward * self.radius - right
    c = self.position - forward * self.radius + right
    return [a, b, c]
   
   def draw(self, screen):
      pygame.draw.polygon(screen, ("black"), self.triangle(), 2)
   
   def update(self, dt):
      keys = pygame.key.get_pressed()

      if keys[pygame.K_a]:
         self.rotate(-dt)
      if keys[pygame.K_d]:
         self.rotate(dt)
      if keys[pygame.K_w]:
         self.move(dt)
      if keys[pygame.K_s]:
         self.move(-dt)
      if keys[pygame.K_SPACE]:
         # limit the rate of fire
         timer = PLAYER_SHOOT_RATE 
         if self.timer <= 0:
            self.shoot()
            self.timer = timer

      self.timer -= dt
   
   def rotate(self, dt):
      self.rotation += PLAYER_TURN_SPEED * dt

   def move(self, dt):
      forward = pygame.Vector2(0, 1).rotate(self.rotation)
      self.position += forward * PLAYER_SPEED * dt

   def shoot(self):
      shot = Shot(self.position.x, self.position.y, self.radius)
      shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
