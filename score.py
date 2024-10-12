from constants import *
import pygame

class Score:
   def __init__(self, score=0):
      self.position = pygame.Vector2(SCORE_POSITION, SCORE_POSITION)
      self.score = score
      self.font = pygame.font.Font(None, 36)
      self.color = SCORE_COLOR
   
   def draw(self, screen):
      text = self.font.render(f"Score: {self.score}", True, self.color)
      screen.blit(text, self.position)
   
   def increase(self, amount):
      self.score += amount 
