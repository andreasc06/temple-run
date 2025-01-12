import pygame

from constants import *

""" Klasse som inneholder variabler og funksjoner som stein hindringen krever """

class Rock:

    def __init__(self, speed, y):

        self.sprite = ROCK_SPRITE

        self.x, self.y = SCREEN_RES[0], y

        self.rect = pygame.Rect(self.x, self.y, ROCK_SIZE, ROCK_SIZE)

        self.speed = speed

    def draw(self, win : pygame.Surface):

        win.blit(self.sprite, (self.x, self.y))
        
    def update(self):

        self.x -= self.speed

        self.rect = pygame.Rect(self.x, self.y, ROCK_SIZE, ROCK_SIZE)

    def _is_colliding_with_player(self, player_rect):

        if self.rect.colliderect(player_rect):

            return True