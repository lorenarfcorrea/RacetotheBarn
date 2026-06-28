import pygame

from Code.Const import *
from Code.Menu import Menu
from Code.Level import Level


class Game:

    #Classe principal do jogo.

    def __init__(self):
        # Cria a janela do jogo usando as medidas definidas em Const.py
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption("Race to the Barn")

        icon = pygame.image.load("asset/icon.png")
        pygame.display.set_icon(icon)

        # Fontes usadas na tela final
        self.font = pygame.font.Font("asset/PressStart2P-Regular.ttf", 18)
        self.instruction_font = pygame.font.Font("asset/PressStart2P-Regular.ttf", 9)

    def run(self):

       #Loop principal do jogo.

        while True:
            menu = Menu(self.window)
            option = menu.run()

            # Fecha o jogo caso o jogador escolha EXIT
            if option == "EXIT":
                pygame.quit()
                quit()

            # Define o modo de jogo e quais personagens começam ativos
            if option == "1 PLAYER":
                game_mode = "single"
                active_players = ["fox"]

            elif option == "2P COOPERATIVE":
                game_mode = "coop"
                active_players = ["fox", "hare"]

            elif option == "2P COMPETITIVE":
                game_mode = "competitive"
                active_players = ["fox", "hare"]

            # Executa o Level 1
            result_level_1, active_players, score_level_1 = Level(
                self.window,
                1,
                game_mode,
                active_players
            ).run()

            # Se perder no Level 1, mostra Game Over e volta ao menu
            if result_level_1 == "GAME_OVER":
                pygame.mixer.music.stop()
                self.end_screen("GAME OVER", score_level_1)
                continue

            # Executa o Level 2 usando apenas os jogadores que sobreviveram ao Level 1
            result_level_2, active_players, score_level_2 = Level(
                self.window,
                2,
                game_mode,
                active_players
            ).run()

            # Soma os scores dos dois níveis separadamente para cada player
            total_score = {
                "fox": score_level_1["fox"] + score_level_2["fox"],
                "hare": score_level_1["hare"] + score_level_2["hare"]
            }

            # Para a música do level antes da tela final
            pygame.mixer.music.stop()

            # Exibe a tela final
            if result_level_2 == "GAME_OVER":
                self.end_screen("GAME OVER", total_score)
            else:
                self.end_screen("YOU WIN!", total_score)

    def end_screen(self, message, score):


       # Tela final do jogo.

        while True:
            self.window.fill(COLOR_BLACK)

            # Define textos e cores de acordo com o resultado
            if message == "GAME OVER":
                title_text = "GAME OVER"
                subtitle_text = "THE STORM WON!"
                title_color = COLOR_RED
            else:
                title_text = "YOU WIN!"
                subtitle_text = "YOU REACHED THE BARN!"
                title_color = COLOR_YELLOW

            # Título principal
            title = self.font.render(title_text, True, title_color)
            title_rect = title.get_rect(center=(WIN_WIDTH / 2, 90))
            self.window.blit(title, title_rect)

            # Subtítulo
            subtitle = self.instruction_font.render(
                subtitle_text,
                True,
                COLOR_WHITE
            )
            subtitle_rect = subtitle.get_rect(center=(WIN_WIDTH / 2, 130))
            self.window.blit(subtitle, subtitle_rect)

            # Score do Player 1
            p1_score_text = self.instruction_font.render(
                f"P1 SCORE: {score['fox']}",
                True,
                COLOR_YELLOW
            )
            p1_rect = p1_score_text.get_rect(center=(WIN_WIDTH / 2, 165))
            self.window.blit(p1_score_text, p1_rect)

            # Score do Player 2
            p2_score_text = self.instruction_font.render(
                f"P2 SCORE: {score['hare']}",
                True,
                COLOR_YELLOW
            )
            p2_rect = p2_score_text.get_rect(center=(WIN_WIDTH / 2, 185))
            self.window.blit(p2_score_text, p2_rect)

            # Instrução para voltar ao menu
            instruction = self.instruction_font.render(
                "Press ENTER to return to Menu",
                True,
                COLOR_WHITE
            )
            instruction_rect = instruction.get_rect(center=(WIN_WIDTH / 2, 225))
            self.window.blit(instruction, instruction_rect)

            pygame.display.flip()

            # Eventos da tela final
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    raise SystemExit

                # ENTER volta ao menu
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return