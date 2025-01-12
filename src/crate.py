import pygame

from constants import *

"""
Klasse som inneholder alle variabler og funksjoner som trengs for en boks
"""

class Crate:

    def __init__(self, speed, y):

        self.sprite = CRATE_SPRITE
        self.x, self.y = SCREEN_RES[0], y

        self.hitbox = pygame.Rect(self.x, self.y, CRATE_SIZE, CRATE_SIZE)

        self.destroy_flag = False

        self.speed = speed

    def draw(self, win : pygame.Surface):
        """ Viser boksen på skjermen """

        win.blit(self.sprite, (self.x, self.y))
        
    def update(self):
        
        """ flytter boksen og oppdaterer hitboxen """

        self.x -= self.speed

        self.hitbox = pygame.Rect(self.x, self.y, CRATE_SIZE, CRATE_SIZE)

    def _is_colliding_with_player(self, player_rect, is_sliding):
        
        """ Sjekker om boksen kolliderer med spiller"""

        if self.hitbox.colliderect(player_rect):

            if not is_sliding:
                return True
            else:
                self.destroy_flag = True # Hvis spiller slider vil boksen ødelegge seg selv
        

    



