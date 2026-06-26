import pygame

from Code.Const import *

class Player:

    def __init__(self):

        self.sprite_sheet = pygame.image.load("asset/Fox_Run.png").convert_alpha()
        self.jump_sound = pygame.mixer.Sound("asset/Jump.wav")

        self.frame_width = self.sprite_sheet.get_width() // 6
        self.frame_height = self.sprite_sheet.get_height() // 4

        self.frames = []
        self.current_frame = 0
        self.animation_timer = 0

        self.load_frames()

        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect()

        self.rect.x = PLAYER_START_X
        self.ground_y = PLAYER_GROUND_Y
        self.rect.y = self.ground_y

        self.velocity_y = 0
        self.gravity = PLAYER_GRAVITY
        self.jump_strength = PLAYER_JUMP_STRENGTH
        self.is_jumping = False

    def load_frames(self):

        row = 2

        for col in range(6):
            frame = self.sprite_sheet.subsurface(
                col * self.frame_width,
                row * self.frame_height,
                self.frame_width,
                self.frame_height
            )

            frame = pygame.transform.scale(frame, (FOX_FRAME_WIDTH, FOX_FRAME_HEIGHT))
            self.frames.append(frame)

    def handle_input(self):

        keys = pygame.key.get_pressed()

        if (keys[pygame.K_UP] or keys[pygame.K_SPACE]) and not self.is_jumping:
            self.jump_sound.play()
            self.velocity_y = self.jump_strength
            self.is_jumping = True

    def apply_gravity(self):

        self.velocity_y += self.gravity
        self.rect.y += self.velocity_y

        if self.rect.y >= self.ground_y:
            self.rect.y = self.ground_y
            self.velocity_y = 0
            self.is_jumping = False

    def update_animation(self):

        self.animation_timer += 1

        if self.animation_timer >= FOX_ANIMATION_SPEED:
            self.animation_timer = 0
            self.current_frame += 1

            if self.current_frame >= len(self.frames):
                self.current_frame = 0

            self.image = self.frames[self.current_frame]

    def update(self):

        self.handle_input()
        self.apply_gravity()
        self.update_animation()

    def draw(self, window):

        window.blit(self.image, self.rect)