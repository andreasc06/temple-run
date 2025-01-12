import pygame

"""
Konstanter som brukes gjennom hele spillet
Gjør det my enklere å lese koden

"""

BLACK = (0, 0, 0)

SCREEN_RES = (1280, 720)

TARGET_FPS = 60


# Player 

PLAYER_SIZE = 150
PLAYER_HITBOX = 75
PLAYER_HITBOX_OFFSET = (PLAYER_SIZE - PLAYER_HITBOX) // 2

PLAYER_WANTED_X_POS = 30
PLAYER_WANTED_Y_POS = SCREEN_RES[1] - PLAYER_SIZE

PLAYER_SLIDE_OFFSET = 50
PLAYER_SLIDE_COOLDOWN = 100
SLIDING_FORCE = 7

SLIDE_DURATION = 1000

ANIMATION_SPEED = 10
JUMP_FORCE = 30
TERMINAL_VELOCITY = 15

# Obstacles

CRATE_SIZE = 100

ROCK_SIZE = 100

BLADE_SIZE = 200
BLADE_HITBOX = 150
ROTATION_SPEED = 5

CRATE_SPRITE = pygame.transform.scale(pygame.image.load("res/crate.png"), (CRATE_SIZE, CRATE_SIZE))
ROCK_SPRITE = pygame.transform.scale(pygame.image.load("res/rock.png"), (ROCK_SIZE, ROCK_SIZE))