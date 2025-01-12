import pygame

from constants import *

"""

Lager en bakgrunn og bakke som beveger seg uendelig

"""

class Background():
    def __init__(self, bg_sprite, bg_speed, g_sprite, g_speed):

        self.bg_image = pygame.image.load(bg_sprite)
        self.bg_image = pygame.transform.scale(self.bg_image, SCREEN_RES)

        self.bg_speed = bg_speed

        self.bg_x1 = 0    # første bilde starter på x=0
        self.bg_x2 = SCREEN_RES[0]  # andre bilde starter på x=1280


        self.g_image = pygame.image.load(g_sprite)
        self.g_image = pygame.transform.scale(self.g_image, (1300, 50))  # Ensure it's the correct size
        self.g_speed = g_speed
        self.g_x1 = 0   # første bilde starter på x=0
        self.g_x2 = SCREEN_RES[0] # andre bilde starter på x=1280

    def draw(self, screen):
        """ viser bakken og bakgrunnen  """

        screen.blit(self.bg_image, (self.bg_x1, 0))
        screen.blit(self.bg_image, (self.bg_x2, 0))

        screen.blit(self.g_image, (self.g_x1, SCREEN_RES[1] - 50))
        screen.blit(self.g_image, (self.g_x2, SCREEN_RES[1] - 50))

    def update(self):
        """ Beveger bakgrunnen og bakken """

        #Beveger begge bildene til venstre
        self.bg_x1 -= self.bg_speed
        self.bg_x2 -= self.bg_speed

        # flytter bilde tilbake når den har gått av skjermen
        if self.bg_x1 <= -SCREEN_RES[0]:
            self.bg_x1 = SCREEN_RES[0]
        if self.bg_x2 <= -SCREEN_RES[0]:
            self.bg_x2 = SCREEN_RES[0]

        # Gjør det samme bare med bakken
        self.g_x1 -= self.g_speed
        self.g_x2 -= self.g_speed

        if self.g_x1 <= -SCREEN_RES[0]:
            self.g_x1 = SCREEN_RES[0]
        if self.g_x2 <= -SCREEN_RES[0]:
            self.g_x2 = SCREEN_RES[0]
