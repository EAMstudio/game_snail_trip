import pygame
import sys
from ball1 import Ball
from ball_vertically import ball_v
from random import randint
from button import Button  # Отрисовка кнопок в меню
from pygame.locals import *  # это добавляет обработку клавиш

#########################################################

sprite_appear_time = 2000  # Интервал появления спрайтов милисекунд
W, H = 1000, 570  # Соотношения рабочего окна, пикселей
FPS = 60
game_score = 0  # Начальный опыт
game_score_max_level = 100
game_score_plus = 7
game_score_minus = -2
game_score_max_minus = -3
damage_1 = -100
damage_2 = -100
is_jump = False
jump_count = 10
VERSION_of_program = 1  # Весия програмым
multiplier_hard_easy = 1
multiplier_speed = 1

#########################################################
pygame.display.set_icon(pygame.image.load("images/snail.png")) # Иконка программы
pygame.init()
pygame.time.set_timer(pygame.USEREVENT, sprite_appear_time)  # Таймер который каждые 2 секунды создает событие (
# создание спрайтов)
f = pygame.font.SysFont('arial', 30)  # Шрифт опыта

SCREEN = pygame.display.set_mode((W, H))  # Устанавливаем рабочую область
pygame.display.set_caption("EAM1studio: Snail Trip")

#########################################################

# Music
pygame.mixer.pre_init(44100, -16, 1, 512)  # Преинициализация чтобы звук эффекты раньше подгрузились и не отставали
sound_menu = pygame.mixer.Sound('musics/vyibor-nujnogo-deystviya.ogg')
sound_collideBalls = pygame.mixer.Sound('musics/zvonkiy-schelchok.ogg')
sound_usui = pygame.mixer.Sound('musics/usui.ogg')
pygame.mixer.music.load('musics/July_level_two_compresed.mp3')
pygame.mixer.music.play(loops=-1, start=54)
is_music_play = True  # ToDo Сделать ВКЛ
#########################################################

# Подгружаем фон, героя
bg = pygame.image.load('images/background.jpg').convert()
bg_first_first = pygame.image.load('images/background_first_first.jpg').convert()  # Сразу подгруизм фон для уровней
bg_first_two = pygame.image.load('images/background_first_two.jpg').convert()
bg_third_one = pygame.image.load('images/background_third_one.jpg').convert()
bg_third_two = pygame.image.load('images/background_third_two.jpg').convert()
bg_fourth = pygame.image.load('images/background_fourth.jpg').convert()

score = pygame.image.load('images/score_fon.png').convert_alpha()
snail = pygame.image.load('images/snail.png').convert_alpha()
# Change size of hero
snail = pygame.transform.scale(snail, (snail.get_width() // 3, snail.get_height() // 3))
snail_to_left = pygame.transform.flip(snail, 1, 0)
snail_to_right = snail
# Start position of hero and general position
t_rect = snail.get_rect(centerx=W // 4, bottom=H // 1.2)

clock = pygame.time.Clock()

#########################################################
# Меню и разговорные окна

BG_menu = pygame.image.load("assets/Background.png")


# Загружаем шрифт
# ToDo нужно проверить работает ли на другом компьютере. Подгружает ли шрифт
def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)


def play(time_screen_update=0):
    SCREEN.blit(bg_first_first, (0, 0))
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        # Кнопка назад
        PLAY_BACK = Button(image=None, pos=(W - 340, H - 100),
                           text_input="MENU", font=get_font(35), base_color="BLACK", hovering_color="Green")
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        # Кнопка игра
        PLAY_game = Button(image=None, pos=(W - 550, H - 100),
                           text_input="GAME", font=get_font(35), base_color="BLACK", hovering_color="Green")
        PLAY_game.changeColor(PLAY_MOUSE_POS)
        PLAY_game.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    sound_menu.play()
                    main_menu()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_game.checkForInput(PLAY_MOUSE_POS):
                    sound_usui.play()
                    july_game(is_jump, jump_count)
            time_screen_update += 1  # Ввели переменную которая считает циклы, чтобы с гэпом показать второй скрин
            if time_screen_update == 40:
                SCREEN.blit(bg_first_two, (0, 0))

        pygame.display.update()


def play_two(time_screen_update=0):
    SCREEN.blit(bg_third_one, (0, 0))
    global game_score_two_level  # Ввел глобальный переменную, чтобы при повторе уровня очки обнулялись
    game_score_two_level = 0
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        # Кнопка назад
        PLAY_BACK = Button(image=None, pos=(W - 150, H - 100),
                           text_input="MENU", font=get_font(35), base_color="Black", hovering_color="Green")
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        # Кнопка игра
        PLAY_game = Button(image=None, pos=(W - 350, H - 100),
                           text_input="GAME", font=get_font(35), base_color="Black", hovering_color="Green")
        PLAY_game.changeColor(PLAY_MOUSE_POS)
        PLAY_game.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    sound_menu.play()
                    main_menu()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_game.checkForInput(PLAY_MOUSE_POS):
                    sound_usui.play()
                    game_level_two()
            time_screen_update += 1  # Ввели переменную которая считает циклы, чтобы с гэпом показать второй скрин
            if time_screen_update == 40:
                SCREEN.blit(bg_third_two, (0, 0))

        pygame.display.update()


def play_tree(time_screen_update=0):
    # global game_score_two_level
    # game_score_two_level = 1000  # костыль,т.к.игра продолжает играть и есть вероятность что опыт будет <0 и new def

    SCREEN.blit(bg_fourth, (0, 0))
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        # Кнопка назад
        PLAY_BACK = Button(image=None, pos=(W - 350, H - 100),
                           text_input="MENU", font=get_font(35), base_color="Black", hovering_color="Green")
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        # Кнопка игра
        PLAY_about = Button(image=None, pos=(W - 600, H - 100),
                            text_input="ABOUT", font=get_font(35), base_color="Black", hovering_color="Green")
        PLAY_about.changeColor(PLAY_MOUSE_POS)
        PLAY_about.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    sound_menu.play()
                    main_menu()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_about.checkForInput(PLAY_MOUSE_POS):
                    sound_usui.play()
                    about()

        pygame.display.update()


def options():
    global game_score_max_level
    global multiplier_hard_easy
    global multiplier_speed
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        # Заглавная надпись
        OPTIONS_TEXT = get_font(45).render("OPTIONS", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(W // 2, H // 5))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        # Кнопка назад в меню
        OPTIONS_BACK = Button(image=None, pos=(W // 2, H - 100),
                              text_input="BACK", font=get_font(45), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        # Кнопка Первого уровня
        OPTIONS_july_game = Button(image=None, pos=(W // 2, H // 3),
                                   text_input="FIRST GAME", font=get_font(30), base_color="Gray",
                                   hovering_color="Green")

        OPTIONS_july_game.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_july_game.update(SCREEN)

        # Кнопка Второго уровня
        OPTIONS_game_two = Button(image=None, pos=(W // 2, H // 3 + 50),
                                  text_input="SECOND GAME", font=get_font(30), base_color="Gray",
                                  hovering_color="Green")

        OPTIONS_game_two.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_game_two.update(SCREEN)

        # Кнопка Отключить музыку
        OPTIONS_music_off = Button(image=None, pos=(W // 2, H // 3 + 100),
                                   text_input="MUSIC OFF", font=get_font(30), base_color="Black",
                                   hovering_color="Green")

        OPTIONS_music_off.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_music_off.update(SCREEN)

        # Кнопка Уровень Изи
        OPTIONS_easy = Button(image=None, pos=(W // 2, H // 3 + 150),
                                   text_input="EASY KATKA", font=get_font(30), base_color="Black",
                                   hovering_color="Green")
        OPTIONS_easy.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_easy.update(SCREEN)
        # Кнопка Уровень Изи
        OPTIONS_hard = Button(image=None, pos=(W // 2, H // 3 + 200),
                                   text_input="HARD KATKA", font=get_font(30), base_color="Black",
                                   hovering_color="Green")

        OPTIONS_hard.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_hard.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    sound_menu.play()
                    main_menu()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_july_game.checkForInput(OPTIONS_MOUSE_POS):
                    sound_usui.play()
                    july_game(is_jump, jump_count)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_game_two.checkForInput(OPTIONS_MOUSE_POS):
                    sound_usui.play()
                    game_level_two()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_music_off.checkForInput(OPTIONS_MOUSE_POS):
                    sound_menu.play()
                    pygame.mixer.music.pause()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_easy.checkForInput(OPTIONS_MOUSE_POS):
                    sound_menu.play()
                    game_score_max_level = 1
                    multiplier_hard_easy = 1
                    multiplier_speed = 1
                    main_menu()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_hard.checkForInput(OPTIONS_MOUSE_POS):
                    sound_menu.play()
                    game_score_max_level = 2000
                    multiplier_hard_easy = 10
                    multiplier_speed = 2
                    main_menu()

        pygame.display.update()


def about():
    while True:
        about_MOUSE_POS = pygame.mouse.get_pos()

        BG_about = pygame.image.load("images/background_about.jpg").convert()
        SCREEN.blit(BG_about, (0, 0))

        about_BACK = Button(image=None, pos=(W // 2, H - 100),
                            text_input="BACK", font=get_font(35), base_color="Black", hovering_color="Green")

        about_BACK.changeColor(about_MOUSE_POS)
        about_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if about_BACK.checkForInput(about_MOUSE_POS):
                    sound_menu.play()
                    main_menu()

        pygame.display.update()


def eam():
    while True:

        BG_about = pygame.image.load("images/background_eam.jpg").convert()
        SCREEN.blit(BG_about, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                sound_menu.play()
                main_menu()

        pygame.display.update()


def game_over():
    while True:
        game_over_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        game_over_TEXT = get_font(45).render("GAME OVER", True, "Black")
        game_over_RECT = game_over_TEXT.get_rect(centerx=W // 2, bottom=H // 4)
        SCREEN.blit(game_over_TEXT, game_over_RECT)

        game_over_TEXT = get_font(25).render("Please don't let the snail die!", True, "Black")
        game_over_RECT = game_over_TEXT.get_rect(centerx=W // 2, bottom=H // 3)
        SCREEN.blit(game_over_TEXT, game_over_RECT)

        game_over_BACK = Button(image=None, pos=(W // 2, int(H // 1.3)),
                                text_input="MENU", font=get_font(75), base_color="Black", hovering_color="Green")

        game_over_BACK.changeColor(game_over_MOUSE_POS)
        game_over_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if game_over_BACK.checkForInput(game_over_MOUSE_POS):
                    sound_menu.play()
                    main_menu()
        global game_score
        game_score = 0
        pygame.display.update()


def main_menu():
    while True:
        SCREEN.blit(BG_menu, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(50).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(centerx=W // 2, bottom=H // 4)

        # Подгружаем рамки для текста
        image_play = pygame.image.load("assets/Play Rect.png")
        image_options = pygame.image.load("assets/Options Rect.png")
        image_quit = pygame.image.load("assets/Quit Rect.png")

        # Масштабируем рамки
        image_play = pygame.transform.scale(image_play, (int(image_play.get_width() // 1.4),
                                                         int(image_play.get_height() // 1.4)))
        image_options = pygame.transform.scale(image_options, (int(image_options.get_width() // 1.4),
                                                               int(image_options.get_height() // 1.4)))
        image_quit = pygame.transform.scale(image_quit, (int(image_quit.get_width() // 1.4),
                                                         int(image_quit.get_height() // 1.4)))
        image_about = image_quit

        # Настраиваем текст
        PLAY_BUTTON = Button(image=image_play, pos=(W // 2, 200), text_input="PLAY",
                             font=get_font(35), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=image_options, pos=(W // 2, 300), text_input="OPTIONS",
                                font=get_font(35), base_color="#d7fcd4", hovering_color="White")
        ABOUT_BUTTON = Button(image=image_about, pos=(W // 2, 400), text_input="ABOUT",
                              font=get_font(35), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=image_quit, pos=(W // 2, 500), text_input="QUIT",
                             font=get_font(35), base_color="#d7fcd4", hovering_color="White")
        VERSION_BUTTON = Button(image=None, pos=(W - 50, H - 10), text_input=f"v_{VERSION_of_program}",
                                font=get_font(15), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, ABOUT_BUTTON, QUIT_BUTTON, VERSION_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    sound_menu.play()
                    play()  # Сначала инициализируем разговорное окно, после функцию july_game()
                    # july_game(is_jump, jump_count)
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    sound_menu.play()
                    options()
                if ABOUT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    sound_menu.play()
                    about()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
                if VERSION_BUTTON.checkForInput(MENU_MOUSE_POS):
                    sound_menu.play()
                    eam()

        pygame.display.update()


#########################################################
# Первый уровень

balls_data = ({'path': 'ball_snowduck.png', 'score': game_score_plus},
              {'path': 'ball_stick1.png', 'score': game_score_minus},
              {'path': 'ball_stick2.png', 'score': game_score_max_minus})
# поочередно загружаем каждую иконку
balls_surf = [pygame.image.load('images/' + data['path']).convert_alpha() for data in balls_data]

balls = pygame.sprite.Group()




def createBall(group):
    a_randint = H * 0.6
    b_randint = H // 1.2
    indx = randint(0, len(balls_surf) - 1)
    y = randint(a_randint, b_randint)
    speed = randint(12, 14*multiplier_speed)

    return Ball(y, speed, balls_surf[indx], balls_data[indx]['score'], group)


createBall(balls)
speed = 10


def collideBalls():
    global game_score
    for ball in balls:
        # при касании спрайт исчезает, добовляется очки
        if t_rect.collidepoint(ball.rect.midleft):
            sound_collideBalls.play()  # звук столкновения
            game_score += ball.score*multiplier_hard_easy
            ball.kill()


# Функция самой игры
def july_game(is_jump, jump_count):
    while True:
        keys = pygame.key.get_pressed()
        # Кнопка выхода
        game_july_MOUSE_POS = pygame.mouse.get_pos()
        game_july_BACK = Button(image=None, pos=(W - 100, H - 20),
                                text_input="MENU", font=get_font(35), base_color="Black", hovering_color="Green")
        game_july_BACK.changeColor(game_july_MOUSE_POS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if game_score < 0:
                game_over()
            if game_score >= game_score_max_level:
                play_two()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if game_july_BACK.checkForInput(game_july_MOUSE_POS):
                    main_menu()
            # Генерация спрайтов каждые 2 секунды, за счет таймера событий вначале
            elif event.type == pygame.USEREVENT:
                createBall(balls)

        # Если мы не в прыжке и нажимаем Пробел
        if not is_jump:
            if keys[pygame.K_SPACE]:
                is_jump = True
        else:
            if jump_count >= -10:
                # замедляем изменение координаты
                t_rect.y -= (jump_count * abs(jump_count)) * 0.5
                jump_count -= 0.5
            else:
                jump_count = 10
                is_jump = False

        # ФОН и СПРАЙТЫ
        SCREEN.blit(bg, (0, 0))  # Отрисовка фона
        balls.draw(SCREEN)  # Отрисовка спрайтов
        # ОПЫТ
        SCREEN.blit(score, (5, 5))  # Отрисовка поля опыта с отступом от начала координат
        sc_text = f.render(str(game_score), 1, (94, 138, 14))  # Формирование текста опыта
        SCREEN.blit(sc_text, (25, 15))  # Отрисовка опыта
        # Герой
        SCREEN.blit(snail, t_rect)
        game_july_BACK.update(SCREEN)  # Отрисовка кнопки
        pygame.display.update()

        clock.tick(FPS)

        collideBalls()  # Столкновения
        balls.update(W)


################################################################

balls_v_data = ({'path': 'branch1.png', 'score': game_score_minus},
                {'path': 'branch2.png', 'score': game_score_minus-2},
                {'path': 'branch3.png', 'score': game_score_max_minus},
                {'path': 'blueberries.png', 'score': 8})
balls_v_surf = [pygame.image.load('images/' + data['path']).convert_alpha() for data in balls_v_data]


def createBall_v(group):
    indx = randint(0, len(balls_v_surf) - 1)
    x = randint(20, W - 20)
    speed = randint(1, 4)

    return ball_v(x, speed, balls_v_surf[indx], balls_v_data[indx]['score'], group)


balls_v = pygame.sprite.Group()
createBall_v(balls_v)
speed = 10


def collideBalls_v():
    global game_score_two_level
    for ball in balls_v:
        # при касании спрайт исчезает, добовляется очки
        if t_rect.collidepoint(ball.rect.midleft) or t_rect.collidepoint(ball.rect.midright):
            sound_collideBalls.play()  # звук столкновения
            game_score_two_level += ball.score
            ball.kill()


game_score_two_level = 0


def game_level_two():
    # global game_level_two_BACK
    speed = 20
    global snail
    while True:

        keys = pygame.key.get_pressed()  # Нажатия клавиатуры
        game_level_two_MOUSE_POS = pygame.mouse.get_pos()
        # Движок
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if game_score_two_level < -1:
                play_two()
            if game_score_two_level >= game_score_max_level:
                play_tree()
            # Кнопка выхода
            if event.type == pygame.MOUSEBUTTONDOWN:
                if game_level_two_BACK.checkForInput(game_level_two_MOUSE_POS):
                    main_menu()
            # Генерация спрайтов каждые 2 секунды, за счет таймера событий вначале
            elif event.type == pygame.USEREVENT:
                createBall_v(balls_v)

        # Движение улитки
        if keys[pygame.K_LEFT]:
            t_rect.x -= speed
            snail = snail_to_left
            if t_rect.x < 0:
                t_rect.x = 0
        elif keys[pygame.K_RIGHT]:
            t_rect.x += speed
            snail = snail_to_right
            if t_rect.x > W - t_rect.width:
                t_rect.x = W - t_rect.width

        # Фон спрайты
        BG_game_level_two = pygame.image.load("images/background_two.jpg").convert()
        SCREEN.blit(BG_game_level_two, (0, 0))
        balls_v.draw(SCREEN)  # Отрисовка спрайтов

        # Кнопка выхода
        game_level_two_BACK = Button(image=None, pos=(W - 100, H - 20),
                                     text_input="MENU", font=get_font(35), base_color="Black", hovering_color="Green")
        game_level_two_BACK.changeColor(game_level_two_MOUSE_POS)
        game_level_two_BACK.update(SCREEN)

        # ОПЫТ
        SCREEN.blit(score, (5, 5))  # Отрисовка поля опыта с отступом от начала координат
        sc_text = f.render(str(game_score_two_level), 1, (94, 138, 14))  # Формирование текста опыта
        SCREEN.blit(sc_text, (25, 15))  # Отрисовка опыта

        # Герой-улитка
        SCREEN.blit(snail, t_rect)
        pygame.display.update()

        collideBalls_v()  # Столкновения
        balls_v.update(H)

        clock.tick(FPS)
        pygame.display.update()  # Обновление экрана


main_menu()

