import pygame

class Background:
    def __init__(self, image_path, speed):
        self.image = pygame.image.load(image_path).convert()
        self.speed = speed
        self.x = 0

    def update(self):
        self.x -= self.speed
        if self.x <= -576:
            self.x = 0

    def draw(self, window):
        window.blit(self.image, (self.x, 0))
        window.blit(self.image, (self.x + 576, 0))