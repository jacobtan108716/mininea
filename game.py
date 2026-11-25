#generates the window for the game, the screen the window is currently on (in game, menu etc)

import pygame
import settings

fps_clock = pygame.time.Clock()
game_window = pygame.display.set_mode((settings.window_w, settings.window_h))
pygame.display.set_caption("Mazecrawler")


running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    game_window.fill(settings.floor_colour)

    pygame.display.flip() #draws absolutely EVERYTHING i have done in this frame. always do it last.
    #all the stuff i just changed e.g players moving, is now actually drawn in

    fps_clock.tick(settings.fps) #60