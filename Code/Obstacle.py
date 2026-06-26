import pygame


class Obstacle:

    def __init__(self, image_path, x, y, speed):
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def update(self):
        self.rect.x -= self.speed

    def draw(self, window):
        window.blit(self.image, self.rect)