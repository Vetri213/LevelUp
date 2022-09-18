import pygame, sys
from button import Button

pygame.init()

width, height = (1280, 720)



#SCREEN = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
SCREEN = pygame.display.set_mode((width, height))


pygame.display.set_caption("Menu")

BG = pygame.image.load("Assets/bg.png")
BG = pygame.transform.scale(BG, (width, height))


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("Assets/font.ttf", size)


def play(user_text):
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
                    main_menu(user_text)
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


def options(user_text):
    active = False
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        Progress_BUTTON = Button(image=pygame.image.load("Assets/Options Rect.png"),
                             pos=(640, 250),
                             text_input="Progress", font=get_font(70),
                             base_color="#d7fcd4", hovering_color="White")
        Progress_BUTTON.changeColor(OPTIONS_MOUSE_POS)
        Progress_BUTTON.update(SCREEN)

        Infinite_BUTTON = Button(
            image=pygame.image.load("Assets/Options Rect.png"), pos=(640, 400),
            text_input="Infinite", font=get_font(70), base_color="#d7fcd4",
            hovering_color="White")

        Infinite_BUTTON.changeColor(OPTIONS_MOUSE_POS)
        Infinite_BUTTON.update(SCREEN)

        OPTIONS_BACK = Button(image=None, pos=(640, 600),
                              text_input="BACK", font=get_font(70),
                              base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu(user_text)
                if Progress_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    pass
                    #Set to progress mode and activate text
                if Infinite_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    #Set to infinite and deactivate text
                    pass


        pygame.display.update()


def main_menu(user_text):
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()
        message = ("Welcome "+user_text)
        MENU_TEXT = get_font(75).render(message, True, "#170064")
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
                    play(user_text)
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options(user_text)
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
        pygame.display.update()

def first_page():
    user_text = "Username"
    first = True
    while True:
        SCREEN.blit(BG, (0, 0))

        # basic font for user typed
        base_font = pygame.font.Font(None, 120)

        # create rectangle
        input_rect = pygame.Rect(width/2-250, height/2-150, 500, 100)

        color_active = pygame.Color('lightskyblue3')

        color_passive = pygame.Color('chartreuse4')
        color = color_passive
        pygame.draw.rect(SCREEN, color, input_rect)

        active = False

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("Level Up", True, "#645f00")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        ENTER_BUTTON = Button(image=pygame.image.load("Assets/Options Rect.png"), pos=(640, 400),
            text_input="Enter", font=get_font(75), base_color="#d7fcd4",
            hovering_color="White")

        QUIT_BUTTON = Button(image=pygame.image.load("Assets/Quit Rect.png"),
                             pos=(640, 550),
                             text_input="QUIT", font=get_font(75),
                             base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [ENTER_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ENTER_BUTTON.checkForInput(MENU_MOUSE_POS):
                    main_menu(user_text)
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False

            if event.type == pygame.KEYDOWN:

                # Check for backspace
                if event.key == pygame.K_BACKSPACE:

                    # get text input from 0 to -1 i.e. end.
                    user_text = user_text[:-1]

                # Unicode standard is used for string
                # formation
                elif event.key == pygame.K_RETURN:
                    main_menu(user_text)
                else:
                    if first:
                        user_text = event.unicode
                        first = False
                    else:
                        if len(user_text) > 8:
                            user_text = user_text[0:8]
                        else:
                            user_text += event.unicode

        if active:
            color = color_active
        else:
            color = color_passive

        text_surface = base_font.render(user_text, True, (255, 255, 255))

        SCREEN.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))

        input_rect.w = max(100, text_surface.get_width() + 10)
        pygame.display.flip()

        pygame.display.update()


first_page()