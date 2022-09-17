import pygame, sys
from button import Button

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("Assets/bg.png")
BG = pygame.transform.scale(BG, (1280, 720))


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("Assets/font.ttf", size)


def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        PLAY_TEXT = get_font(45).render("SELECT AN EXERCISE", True,
                                        "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(640, 460),
                           text_input="BACK", font=get_font(75),
                           base_color="White", hovering_color="Green")
        PUSH_UPS = Button(image=None, pos=(220, 380),
                           text_input="PUSH UPS", font=get_font(50),
                           base_color="White", hovering_color="Green")
        SIT_UPS = Button(image=None, pos=(660, 380),
                           text_input="SIT UPS", font=get_font(50),
                           base_color="White", hovering_color="Green")
        SQUATS = Button(image=None, pos=(1060, 380),
                           text_input="SQUATS", font=get_font(50),
                           base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        PUSH_UPS.changeColor(PLAY_MOUSE_POS)
        PUSH_UPS.update(SCREEN)

        SIT_UPS.changeColor(PLAY_MOUSE_POS)
        SIT_UPS.update(SCREEN)

        SQUATS.changeColor(PLAY_MOUSE_POS)
        SQUATS.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if PUSH_UPS.checkForInput(PLAY_MOUSE_POS):
                    import pushup
                    pushup.main()
                    pygame.quit()
                    sys.exit()
                if SIT_UPS.checkForInput(PLAY_MOUSE_POS):
                    import situp
                    situp.main()
                    pygame.quit()
                    sys.exit()

                if SQUATS.checkForInput(PLAY_MOUSE_POS):
                    import squat
                    squat.main()
                    pygame.quit()
                    sys.exit()

                ## ONE MORE

        pygame.display.update()


def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True,
                                           "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460),
                              text_input="BACK", font=get_font(75),
                              base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#006400")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("Assets/Play Rect.png"),
                             pos=(640, 250),
                             text_input="PLAY", font=get_font(75),
                             base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(
            image=pygame.image.load("Assets/Options Rect.png"), pos=(640, 400),
            text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4",
            hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("Assets/Quit Rect.png"),
                             pos=(640, 550),
                             text_input="QUIT", font=get_font(75),
                             base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()


        pygame.display.update()


main_menu()
