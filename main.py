import random
import pygame
pygame.init()


from src.structs import *
from src.player import Player
from src.bg import Background
from constants import *

class Game:
    def __init__(self):

        """ Gjør klar variabler og klasser som spillet skal bruke """

        self.screen = pygame.display.set_mode(SCREEN_RES, pygame.SCALED | pygame.DOUBLEBUF)
        pygame.display.set_caption("Temple Run")

        self.frame = 0
        self.obstacle_interval = START_OBSTACLE_INTERVAL
        self.clock = pygame.time.Clock()

        self.font = pygame.font.SysFont("Arial", 30)
        self.font_2 = pygame.font.SysFont("Arial", 60)

        self.player = Player()
        self.bg = Background("res/bg2.png", 1, "res/g.png", 15)


        pygame.mixer.music.load("sfx/music.mp3")
        pygame.mixer.music.play()


        self.crates, self.rocks = single_crate() # Første hinring er alltid en vanlig boks

    def handle_events(self):

        """ Sjekker tastene spilleren trykker på, og kaller funksjoner basert på hvilke knapp som blir trykket."""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.player.jump()
                elif event.key == pygame.K_DOWN:
                    self.player.slide()
                elif event.key == pygame.K_SPACE and self.player.is_dead:
                    self.reset_game()

    def reset_game(self):

        """ Nullstiller variabler for å starte spille på nytt"""

        pygame.mixer.music.play()
        self.frame = 1
        self.obstacle_interval = START_OBSTACLE_INTERVAL
        self.player = Player()
        self.crates, self.rocks = single_crate()

    def draw_text(self):

        """ Viser tekst """

        if self.player.is_dead:

            pygame.mixer.music.stop()


            dead_text = self.font_2.render("YOU DIED", True, "white")
            score_text = self.font_2.render(f"SCORE: {self.frame}", True, "white")
            retry_text = self.font.render("PRESS SPACE TO RETRY", True, "white")
            self.screen.blit(dead_text, (400, 200))
            self.screen.blit(score_text, (400, 300))
            self.screen.blit(retry_text, (400, 400))
        else:
            # Tegner kun score oppi hjørne dersom spilleren lever
            score_text = self.font.render(f"SCORE: {self.frame}", True, "white")
            self.screen.blit(score_text, (0, 0))

    def update_and_draw_obstacles(self):

        """ Går gjennom vær hindring og oppdaterer og tegner den """

        for crate in self.crates[:]: # Går gjennom hver boks i boks listen
            if not self.player.is_dead:
                # Oppdaterer og tegner dersom spilleren lever
                crate.update()
                crate.draw(self.screen)
            if crate.x < -CRATE_SIZE or crate.destroy_flag:
                # fjerner boksen fra listen dersom den er av skjermen eller har blitt markert til å ødelegger (dersom spiller slidet inn i den)
                self.crates.remove(crate)
            elif crate._is_colliding_with_player(self.player.hitbox, self.player.is_sliding):
                self.player.die()

        for rock in self.rocks[:]:  # Går gjennom hver boks i boks listen
            if not self.player.is_dead:
                # Oppdaterer og tegner dersom spilleren lever
                rock.update()
                rock.draw(self.screen)
            if rock.x < -ROCK_SIZE:
                # fjerner steinen fra listen dersom den er av skjermen
                self.rocks.remove(rock)
            elif rock._is_colliding_with_player(self.player.hitbox):
                self.player.die()

    def spawn_obstacles(self):

        """ Kommer med en ny hindring hvis det har gått langt nok tid siden den forrige """

        if self.frame % (self.obstacle_interval * TARGET_FPS) == 0: # Sjekker om det har gått en viss antall sekunder ved modulo operasjon

            new_obs = random.choice([single_crate(), rock_wall(), crate_slide()]) # Velger en tilfeldig hindring
            # Legger til hindringene i listene
            self.crates.extend(new_obs[0])
            self.rocks.extend(new_obs[1])

    def run(self):

        #self.frame = 4000


        while True:

            if not self.player.is_dead:
                self.frame += 1 # Antall frames men brukes også som score


            # Sjekker om frame er hel tusetall (eks. 2000) 
            # Sjekker om frame er mindre enn start intervallet * 1000 (så tidsintervallet ikke blir mindre en 1 sekund)
            if self.frame % 1000 == 0 and self.frame < (START_OBSTACLE_INTERVAL * 1000): 

                # Reduserer tids intervallet mellom hver hindring med 1 sekund
                self.obstacle_interval -= 1

            self.handle_events() # Spiller input

            if not self.player.is_dead:
                # oppdaterer hvis spilleren lever

                self.bg.update()
                self.player.update()
                self.spawn_obstacles()
            else:
                self.player.handle_gravity() # Kun for å få spilleren til å falle nedover dersom død så han ikke ligger død mitt i lufta

            self.screen.fill(BLACK)
            
            if not self.player.is_dead:
                # Tegner bakgrunnen hvis spilleren lever
                self.bg.draw(self.screen)
                
            self.update_and_draw_obstacles() # oppdaterer og tegner hver hindring

            self.draw_text() # tegner score osv

            self.player.draw(self.screen) # tegner silleren på skjermen

            pygame.display.update()
            self.clock.tick(TARGET_FPS)

if __name__ == "__main__":
    game = Game()
    game.run()
