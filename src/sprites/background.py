import pygame

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file: str):
        super().__init__()
        self.image = pygame.image.load(image_file).convert()
        self.rect = self.image.get_rect()