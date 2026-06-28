from pygame import pygame

from Menu import Menu
from code.Const import WIN_WIDTH, WIN_HEIGHT


class Game:

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):

        while True:
            menu = Menu(self.window)
            menu.run()
            pass

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                pygame.quit()  # Close Window
                quit()  # end pygame
