import pygame

from Code.Const import *
from Code.Menu import Menu
from Code.Level import Level


class Game:

    def __init__(self):
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption("Race to the Barn")
        self.font = pygame.font.SysFont("Race to the Barn", 32, bold=True)

    def run(self):
        while True:
            menu = Menu(self.window)
            option = menu.run()

            if option == "EXIT":
                pygame.quit()
                quit()

            result_level_1 = Level(self.window, 1).run()

            if result_level_1 == "GAME_OVER":
                pygame.mixer.music.stop()
                self.end_screen("GAME OVER")
                continue

            result_level_2 = Level(self.window, 2).run()

            if result_level_2 == "GAME_OVER":
                pygame.mixer.music.stop()
                self.end_screen("GAME OVER")
            else:
                pygame.mixer.music.stop()
                self.end_screen("YOU WIN!")

    def end_screen(self, message):
        while True:
            self.window.fill(COLOR_BLACK)

            text = self.font.render(message, True, COLOR_YELLOW)
            self.window.blit(text, text.get_rect(center=(WIN_WIDTH / 2, 130)))

            instruction = pygame.font.SysFont("Race to the Barn", 20).render("Press ENTER to return to Menu",True,COLOR_WHITE)
            self.window.blit(instruction, instruction.get_rect(center=(WIN_WIDTH / 2, 190)))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return