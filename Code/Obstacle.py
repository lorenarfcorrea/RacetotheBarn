import pygame


class Obstacle:

    #Classe responsável pelos obstáculos do jogo.


    def __init__(self, image_path, x, y, speed):
        """
        image_path : caminho da imagem do obstáculo.
        x          : posição inicial no eixo X.
        y          : posição fixa no eixo Y.
        speed      : velocidade de deslocamento.
        """

        # Carrega a imagem mantendo transparência
        self.image = pygame.image.load(image_path).convert_alpha()

        # Cria o retângulo de colisão baseado na imagem
        self.rect = self.image.get_rect()

        # Define posição inicial
        self.rect.x = x
        self.rect.y = y

        # Velocidade de movimento
        self.speed = speed

    def update(self):

        #Move o obstáculo continuamente para a esquerda.

        self.rect.x -= self.speed

    def draw(self, window):

        #Desenha o obstáculo na janela do jogo.

        window.blit(self.image, self.rect)