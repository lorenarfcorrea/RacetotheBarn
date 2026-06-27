import pygame
from Code.Const import *


class Player:

    #Classe responsável pelos personagens do jogo.

    def __init__(self, sprite_path, x, y, control_keys, flip=False):

        # CARREGA A SPRITE SHEET

        self.sprite_sheet = pygame.image.load(sprite_path).convert_alpha()

        # Cada sprite possui 6 colunas e 4 linhas
        self.frame_width = self.sprite_sheet.get_width() // 6
        self.frame_height = self.sprite_sheet.get_height() // 4


        # CONTROLE DA ANIMAÇÃO

        self.frames = []
        self.current_frame = 0
        self.animation_timer = 0

        # Teclas utilizadas pelo jogador
        self.control_keys = control_keys

        # Inverte o personagem horizontalmente (coelho)
        self.flip = flip

        # Carrega todos os frames da animação
        self.load_frames()

        # Primeiro frame exibido
        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect()


        # POSIÇÃO INICIAL

        self.rect.x = x
        self.ground_y = y
        self.rect.y = self.ground_y


        # FÍSICA DO PULO

        self.velocity_y = 0
        self.gravity = PLAYER_GRAVITY
        self.jump_strength = PLAYER_JUMP_STRENGTH
        self.is_jumping = False

        # Som do pulo
        self.jump_sound = pygame.mixer.Sound("asset/Jump.wav")

    def load_frames(self):

        #Recorta os frames da sprite sheet.


        row = 2

        for col in range(6):

            frame = self.sprite_sheet.subsurface(
                col * self.frame_width,
                row * self.frame_height,
                self.frame_width,
                self.frame_height
            )

            # Ajusta o tamanho do sprite
            frame = pygame.transform.scale(
                frame,
                (FOX_FRAME_WIDTH, FOX_FRAME_HEIGHT)
            )

            # Inverte horizontalmente caso necessário
            if self.flip:
                frame = pygame.transform.flip(frame, True, False)

            self.frames.append(frame)

    def handle_input(self):

        #Verifica se alguma tecla de controle foi pressionada.

        keys = pygame.key.get_pressed()

        for key in self.control_keys:

            if keys[key] and not self.is_jumping:

                self.jump_sound.play()

                self.velocity_y = self.jump_strength
                self.is_jumping = True

    def apply_gravity(self):

        #Aplica a gravidade ao personagem.

        self.velocity_y += self.gravity
        self.rect.y += self.velocity_y

        if self.rect.y >= self.ground_y:

            self.rect.y = self.ground_y
            self.velocity_y = 0
            self.is_jumping = False

    def update_animation(self):

        #Atualiza a animação de corrida.

        self.animation_timer += 1

        if self.animation_timer >= FOX_ANIMATION_SPEED:

            self.animation_timer = 0
            self.current_frame += 1

            if self.current_frame >= len(self.frames):
                self.current_frame = 0

            self.image = self.frames[self.current_frame]

    def update(self):

        #Atualiza todas as ações do personagem.

        self.handle_input()
        self.apply_gravity()
        self.update_animation()

    def draw(self, window):

        #Desenha o personagem na tela.

        window.blit(self.image, self.rect)