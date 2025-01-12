from constants import *

from src.crate import Crate
from src.rock import Rock

"""
Rekke funksjoner som returner dataen som kreves for ferdiglagde samlinger av hindringer

funksjonene returnerer: liste med bokser, liste med steiner
"""

def single_crate():

    # Lager en enkel boks på bakken
    

    crates = [Crate(15, SCREEN_RES[1] - 50 - (1 * CRATE_SIZE))]
    
    rocks = []

    return crates, rocks


def rock_wall():

    # Lager en stein vegg med bokser i midten

    crates = [Crate(15, SCREEN_RES[1] -   50 - (3 * CRATE_SIZE)),
                Crate(15,SCREEN_RES[1] -   50 - (4 * CRATE_SIZE)),
               Crate(15,SCREEN_RES[1] -   50 - (5 * CRATE_SIZE))]


    rocks = [Rock(15, SCREEN_RES[1] -  50 - ROCK_SIZE), 
            Rock(15, SCREEN_RES[1] -   50 - 2 * ROCK_SIZE),
            Rock(15, SCREEN_RES[1] -   50 - 6 * ROCK_SIZE),
            Rock(15, SCREEN_RES[1] -   50 - 7 * ROCK_SIZE),
            Rock(15, SCREEN_RES[1] -   50 - 8 * ROCK_SIZE)]

    return crates, rocks

def crate_slide():

    # Lager en stein vegg med bokser i nederst

    crates = [Crate(15, SCREEN_RES[1] -  50 -  (1 * CRATE_SIZE)),
              Crate(15, SCREEN_RES[1] -   50 - (2 * CRATE_SIZE))]
    
    rocks = [ 
            Rock(15, SCREEN_RES[1] -   50 - 3 * ROCK_SIZE),
            Rock(15, SCREEN_RES[1] -   50 - 4 * ROCK_SIZE),
            Rock(15, SCREEN_RES[1] -   50 - 5 * ROCK_SIZE),
            Rock(15, SCREEN_RES[1] -   50 - 6 * ROCK_SIZE),
            Rock(15, SCREEN_RES[1] -   50 - 7 * ROCK_SIZE),
            Rock(15, SCREEN_RES[1] -   50 - 8 * ROCK_SIZE)]
    
    return crates, rocks

