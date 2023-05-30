import sys
import pygame

from screens.main_screen import MainScreen
from sprites.background import Background

class Main:
    def __init__(self):
        pygame.init()
        self.window = MainScreen()
        self.background = Background('assets/bgdino.png')
        self.background = pygame.transform.scale(self.background, (800, int(800 * 614 / 2214)))
        self.run()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.window.screen.blit(self.background.image, self.background.rect)
            pygame.display.update()

if __name__ == '__main__': Main()