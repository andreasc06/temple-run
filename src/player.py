from constants import *

import pygame


class Player:
    def __init__(self):
        
        # Importerer bildene for de forskjellige animasjonene til spilleren
        self.running_sprites = [
            pygame.transform.scale(pygame.image.load(f"res/character/run/Run__00{i}.png"), (PLAYER_SIZE-20, PLAYER_SIZE))
            for i in range(10)
        ]
        self.jumping_sprites = [
            pygame.transform.scale(pygame.image.load(f"res/character/jump/Jump__00{i}.png"), (PLAYER_SIZE-20, PLAYER_SIZE))
            for i in range(10)
        ]
        self.sliding_sprites = [
            pygame.transform.scale(pygame.image.load(f"res/character/slide/Slide__00{i}.png"), (PLAYER_SIZE-20, PLAYER_SIZE-20))
            for i in range(10)
        ]
        self.dead_sprite = pygame.transform.scale(pygame.image.load("res/character/dead.png"), (PLAYER_SIZE, PLAYER_SIZE))

        self.current_sprite = self.running_sprites[0] # Variabel som holder på bilde som skal bli vist på skjermen
 
        # Tilstander spilleren kan være i
        self.is_running = True
        self.is_jumping = False
        self.is_sliding = False
        self.is_dead = False

        # Variabler til animasjonene
        self.running_animation_frame = 0
        self.jumping_animation_frame = 0
        self.sliding_animation_frame = 0

        # Logikk for sliding
        self.slide_cooldown = PLAYER_SLIDE_COOLDOWN
        self.sliding_start_time = None

        # Posisjoner til spilleren
        self.x, self.y = 0, PLAYER_WANTED_Y_POS -50
        self.ground_y = PLAYER_WANTED_Y_POS - 50

        # Gravitasjon
        self.upward_force = 0
        self.downward_force = 1

        # Hitbox
        self.hitbox = pygame.Rect(self.x, self.y, PLAYER_HITBOX, PLAYER_HITBOX)

    def draw(self, win : pygame.display):

        """ Viser spilleren på skjermen """

        # en offset hvis spilleren slider fordi bilde er en annen størrelse
        offset = 20 if self.current_sprite in self.sliding_sprites else 0 

        win.blit(self.current_sprite, (self.x + offset, self.y + offset))

        # Viser sliding baren på skjermen
        if not self.is_dead:
            pygame.draw.rect(win, "red", (10, 50, self.slide_cooldown, 20))

    def handle_gravity(self):

        """ Funksjonen håndterer gravitasjonen og hopping til spilleren """
        
        # Drar spilleren nedover med økende tempo dersom y verdien er lavere enn bakken
        if self.y < self.ground_y: 
            self.y += self.downward_force
            if self.downward_force < TERMINAL_VELOCITY: # Maks fart så det ser mer naturlig ut
                self.downward_force += 1
        else:
            self.downward_force = 1


        # Drar spilleren oppover dersom spiller har hoppet (upward_force blir satt til 10)
        if self.upward_force > 0:

            self.y -= self.upward_force
            self.upward_force -= 1  

    def handle_animation(self):

        """ Håndterer animasjon til spilleren"""

        # Løping
        if self.is_running:

            self.running_animation_frame += 1

            if self.running_animation_frame == 10: # Når den har kommet til siste frame starter den på første igjen
                self.running_animation_frame = 0

            self.current_sprite = self.running_sprites[self.running_animation_frame]

        # Hopping
        if self.is_jumping:


            if self.jumping_animation_frame < 8: # Øker med en frame så lenge den ikke er på siste
                self.jumping_animation_frame += 1

            self.current_sprite = self.jumping_sprites[self.jumping_animation_frame]

        # Sliding
        if self.is_sliding:

            self.sliding_animation_frame += 1

            if self.sliding_animation_frame == 10: # Når den har kommet til siste frame starter den på første igjen
                self.sliding_animation_frame = 0

            self.current_sprite = self.sliding_sprites[self.sliding_animation_frame]

    def handle_sliding_time(self):

        """ Håndterer hvor lenge spilleren har slidet (slider maks i 1 sekund) """

        time = pygame.time.get_ticks() # funksjonen returnerer antall ms det har gått siden pygame startet

        if time - self.sliding_start_time > SLIDE_DURATION: # sjekker om det har gått 1000 ms

            self.is_sliding = False


    def update(self):

        """ Hoved funksjon for oppdatering av spilleren """
        
        self.is_running = True if not self.is_jumping else False
        self.is_jumping = True if self.y != self.ground_y else False

        self.handle_gravity()
        self.handle_animation()

        if self.slide_cooldown < PLAYER_SLIDE_COOLDOWN and not self.is_sliding: # Øker cooldown til spilleren dersom den ikke er full
            self.slide_cooldown += 0.5

        if self.is_sliding:
            self.slide_cooldown -= 1 # Minker cooldownen når spilleren slider
            self.handle_sliding_time()
            self.x += SLIDING_FORCE # Drar spiller fremover slik at det ser ut som spillern øker farten
            if self.slide_cooldown <= 0:
                self.is_sliding = False # Avbryter sliding dersom cooldownen er 0 eller mindre


        elif self.x > PLAYER_WANTED_X_POS and not self.is_jumping:
            self.x -= SLIDING_FORCE  # Drar spilleren tilbake igjen etter slidingen


        self.hitbox = pygame.Rect(
            self.x + PLAYER_HITBOX_OFFSET, 
            self.y + PLAYER_HITBOX_OFFSET, 
            PLAYER_HITBOX, 
            PLAYER_HITBOX
        )


    def jump(self):

        """ Kalles når spiller trykker på PIL tast opp"""

        if self.y == self.ground_y and not self.is_dead:

            self.upward_force = JUMP_FORCE
            self.is_jumping = True

    def slide(self):

        """ Kalles når spiller trykker på PIL tast ned"""

        if (self.is_running or self.is_jumping) and not self.is_dead:

            self.is_sliding = True
            self.sliding_start_time = pygame.time.get_ticks() # funksjonen returnerer antall ms det har gått siden pygame startet

    def die(self):

        """ Kalles når spilleren dør """

        self.current_sprite = self.dead_sprite
        self.is_dead = True
















