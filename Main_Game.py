import random
import button
import pygame
# import sys
import time
from pygame.locals import (
    # RLEACCEL,
    # K_UP,
    # K_DOWN,
    # K_LEFT,
    # K_RIGHT,
    # K_ESCAPE,
    # KEYDOWN,
    MOUSEBUTTONDOWN,

    QUIT,
)

pygame.init()

# create display window
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 600
pygame.font.init()
# load the background image
background = pygame.image.load("Start_Menu_Images/main_menu_bg.jpeg")
# resizing the background image to fit the screen
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Return to Tekoon: Deluge')

# load button images
start_img = pygame.image.load('Start_Menu_Images/start_b.png').convert_alpha()
# leaderboard_button = pygame.image.load('leaderboard_button.png').convert_alpha()


title_img = pygame.image.load('Start_Menu_Images/title_text.png')
title_text = pygame.transform.scale(title_img, (500, 150))
# create button instances
start_button = button.Button(240, 350, start_img, 0.2)
# leaderboard_button = button.Button(230, 400, leaderboard_button, 0.3)
FPS = 30  # frames per second setting
fpsClock = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
font = pygame.font.Font(None, 22)
font2 = pygame.font.SysFont("Raleway", 32, bold=True, italic=False)
font3 = pygame.font.Font(None, 18)
font4 = pygame.font.SysFont("Raleway", 54, bold=True, italic=False)
user_data_file = open("Text Files/User_Data.txt", "r")

'''
line_output = user_data_file.readline()
while line_output != "":
    line_output = line_output.rstrip()
    print(line_output)
    line_output = user_data_file.readline()
'''


def main_menu():
    # game loop

    run = True
    while run:
        screen.fill((202, 228, 241))
        screen.blit(background, (0, 0))
        screen.blit(title_text, (50, 100))

        if start_button.draw(screen):
            user_data_check(600, 600)
        # if leaderboard_button.draw(screen):
        #    leaderboard()
        # event handler
        for event in pygame.event.get():
            # quit game
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()


# Parameters: image 1 and image 2 are the image paths for the backgrounds,
# objective_img is the image for the objective
# jellib start x and start y are the starting coordinates for the jellib
# trigger x is the trigger point in background 2 when the story begins
# story_name is the part of the story.
# If part = 0, old man will be blitted in second image
# if part =1, old man will be in first image, else not
def navig_to_story(scrn_w, scrn_h, image_1, image_2, objective_img,
                   jellib_start_x, jellib_start_y, trigger_x, story_name):
    # Part 1: Nav to Old man
    # Part 2: Nav to Demon
    # Part 3: Nav to Labyrinth
    # Part 4: Nav to Sphinx
    # Maybe?? Part 5: Story End Scene

    background1 = pygame.image.load(image_1)
    background2 = pygame.image.load(image_2)
    background1 = pygame.transform.scale(background1, (scrn_w, scrn_h))
    background2 = pygame.transform.scale(background2, (scrn_w, scrn_h))
    background_name = 0
    background_file = background1
    pygame.display.set_caption('Return to Tekoon: Deluge')
    WHITE = (255, 255, 255)
    jellib = pygame.image.load('Level_0/Jellib.png')
    jellib = pygame.transform.scale(jellib, (50, 50))

    jellibx = jellib_start_x
    jelliby = jellib_start_y
    right_pressed = False
    left_pressed = False
    story_on = False
    DISPLAYSURF.blit(background1, (0, 0))
    old_man_npc = pygame.image.load('Nav_Story/old_man.png')
    old_man_npc = pygame.transform.scale(old_man_npc, (100, 200))

    if story_name == 1:
        DISPLAYSURF.blit(old_man_npc, (500, 400))

    DISPLAYSURF.blit(jellib, (jellibx, jelliby))

    objective_img = pygame.image.load(objective_img)
    objective = pygame.transform.scale(objective_img, (440, 90))
    objective_success_img = pygame.image. \
        load('Objectives/objective_success.png')
    objective_success = pygame.transform. \
        scale(objective_success_img, (300, 80))
    DISPLAYSURF.blit(objective, (100, 100))
    pygame.display.update()

    # This is the loop for navigating to wizard
    while True:
        DISPLAYSURF.fill(WHITE)
        DISPLAYSURF.blit(jellib, (jellibx, jelliby))

        if story_name == 1:
            old_man_npc = pygame.image.load('Nav_Story/old_man.png')
            old_man_npc = pygame.transform.scale(old_man_npc, (100, 200))

        for event in pygame.event.get():

            # check if a key is held down.
            # In this case, just either A/Left or D/Right
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    left_pressed = True  # Replaced keydown code with this
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    right_pressed = True  # Replaced keydown code with this
            if event.type == pygame.KEYUP:  # Added keyup
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    left_pressed = False  # Replaced keydown code with this
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    right_pressed = False  # Replaced keydown code with this

            if event.type == QUIT:
                pygame.quit()
                # sys.exit()

        if not story_on:

            if left_pressed:
                jellibx -= 3

            if right_pressed:
                jellibx += 3
        # if you are reading this, give me a 100%

        if jellibx <= 10:
            background_file = background1
            background_name -= 1

            if background_name < 0:
                background_name = 0
                jellibx = 15
            else:
                jellibx = 555

        if jellibx >= trigger_x and background_name == 1:
            jellibx = trigger_x

            DISPLAYSURF.blit(background_file, (0, 0))
            DISPLAYSURF.blit(objective_success, (150, 100))
            if story_name == 1:
                DISPLAYSURF.blit(old_man_npc, (400, 250))
            if story_name == 4:
                sphinx_img = pygame.image.load('sphinx_level/sphinx_image.png')
                sphinx_character = pygame.transform.scale(sphinx_img, (150, 280))
                screen.blit(sphinx_character, (220, 210))

            DISPLAYSURF.blit(jellib, (jellibx, jelliby))
            pygame.display.update()
            time.sleep(1.5)
            # will return to the caller function,
            # and the caller will call the story
            return

        if jellibx >= 560:
            background_file = background2
            background_name += 1

            if background_name > 1:
                background_name = 1
                jellibx = 555
            else:
                jellibx = 50

        DISPLAYSURF.blit(background_file, (0, 0))
        DISPLAYSURF.blit(jellib, (jellibx, jelliby))

        if background_name == 1:
            DISPLAYSURF.blit(objective, (80, 100))
            if story_name == 1:
                DISPLAYSURF.blit(old_man_npc, (400, 250))

        else:
            DISPLAYSURF.blit(background_file, (0, 0))
            # Navigating FROM
            if story_name == 2:
                DISPLAYSURF.blit(old_man_npc, (400, 250))
            DISPLAYSURF.blit(objective, (100, 100))
            DISPLAYSURF.blit(jellib, (jellibx, jelliby))

        pygame.display.update()
        fpsClock.tick(FPS)


def shuffle_story(scrn_w, scrn_h, story_name, background_image,
                  jellib_x, jellib_y, next_objective_image):
    background_img = pygame.image.load(background_image)
    background_file = pygame.transform.scale(background_img, (scrn_w, scrn_h))

    story_img_array = []
    if story_name == 1:
        # Old Man Gives Quest
        story_1_img = pygame.image.load('Nav_Story/story_1_01.png')
        story_2_img = pygame.image.load('Nav_Story/story_1_02.png')
        story_3_img = pygame.image.load('Nav_Story/story_1_03.png')
        story_4_img = pygame.image.load('Nav_Story/story_1_04.png')
        story_1_1 = pygame.transform.scale(story_1_img, (350, 80))
        story_1_2 = pygame.transform.scale(story_2_img, (350, 80))
        story_1_3 = pygame.transform.scale(story_3_img, (350, 80))
        story_1_4 = pygame.transform.scale(story_4_img, (350, 80))
        story_img_array = [story_1_1, story_1_2, story_1_3, story_1_4]

    elif story_name == 2:
        # Recovering from Demon
        story_1_img = pygame.image.load('Story_2/story_02_1.png')
        story_2_img = pygame.image.load('Story_2/story_02_2.png')
        story_3_img = pygame.image.load('Story_2/story_02_3.png')
        story_2_1 = pygame.transform.scale(story_1_img, (420, 100))
        story_2_2 = pygame.transform.scale(story_2_img, (420, 100))
        story_2_3 = pygame.transform.scale(story_3_img, (420, 100))
        story_img_array = [story_2_1, story_2_2, story_2_3]

    elif story_name == 3:
        # Recovering from Labyrinth
        story_1_img = pygame.image.load('Story_3/story_03_1.png')
        story_2_img = pygame.image.load('Story_3/story_03_2.png')
        story_3_img = pygame.image.load('Story_3/story_03_3.png')
        story_3_1 = pygame.transform.scale(story_1_img, (420, 100))
        story_3_2 = pygame.transform.scale(story_2_img, (420, 100))
        story_3_3 = pygame.transform.scale(story_3_img, (420, 100))
        story_img_array = [story_3_1, story_3_2, story_3_3]

    story_arrow = pygame.image.load("Nav_Story/arrow.png")
    story_arrow = pygame.transform.scale(story_arrow, (80, 50))
    story_arrow_rect = story_arrow.get_rect(topleft=(440, 120))

    story_length = len(story_img_array)
    active_story = story_img_array[0]
    story_part = 0

    jellib = pygame.image.load('Level_0/Jellib.png')
    jellib = pygame.transform.scale(jellib, (50, 50))

    jellibx = jellib_x
    jelliby = jellib_y

    DISPLAYSURF.blit(background, (0, 0))
    old_man_npc = pygame.image.load('Nav_Story/old_man.png')
    old_man_npc = pygame.transform.scale(old_man_npc, (100, 200))

    DISPLAYSURF.blit(background_file, (0, 0))
    DISPLAYSURF.blit(jellib, (jellibx, jelliby))

    if story_name == 1:
        DISPLAYSURF.blit(old_man_npc, (400, 250))
        DISPLAYSURF.blit(active_story, (100, 100))
    else:
        DISPLAYSURF.blit(active_story, (20, 100))

    DISPLAYSURF.blit(story_arrow, story_arrow_rect)
    time.sleep(1)
    pygame.display.update()

    # This is the LOOP for the wizard giving the quest, you click on story
    in_story_mode = True
    while in_story_mode:

        for event in pygame.event.get():

            if event.type == QUIT:

                pygame.quit()

            elif event.type == MOUSEBUTTONDOWN:

                if story_arrow_rect.collidepoint(event.pos):
                    story_part += 1

                    if story_part >= story_length:

                        DISPLAYSURF.blit(background_file, (0, 0))
                        if story_name == 1:
                            DISPLAYSURF.blit(old_man_npc, (400, 250))
                        DISPLAYSURF.blit(jellib, (jellibx, jelliby))
                        objective_2_1_img = pygame.image. \
                            load(next_objective_image)
                        objective_2_1 = pygame.transform. \
                            scale(objective_2_1_img, (440, 90))
                        DISPLAYSURF.blit(objective_2_1, (100, 100))
                        pygame.display.update()
                        time.sleep(1)
                        return

                    DISPLAYSURF.blit(background_file, (0, 0))
                    DISPLAYSURF.blit(jellib, (jellibx, jelliby))

                    if story_name == 1:
                        DISPLAYSURF.blit(old_man_npc, (400, 250))
                        DISPLAYSURF.blit(story_img_array[story_part], (100, 100))
                    else:
                        DISPLAYSURF.blit(story_img_array[story_part], (20, 100))

                    pygame.display.update()
                    time.sleep(2)
                    DISPLAYSURF.blit(story_arrow, story_arrow_rect)
                    pygame.display.update()


'''
# runs when leaderboard is pressed
def leaderboard():
    print("Leaderboard")
'''


# The function replace_line was made by Kevin Browne @ https://portfoliocourses.com
# Replace the line at line_number in the file with the provided filename with
# the text in the string text
def replace_line(filename, line_number, text):
    # Open the file and read all the lines from the file into a list 'lines'
    with open(filename) as file:
        lines = file.readlines()

    # if the line number is in the file, we can replace it successfully
    if (line_number <= len(lines)):

        # Replace the associated line in the list with the replacement text
        # (followed by a newline \n to end the line), we need to use line_number - 1
        # as the index because lists are zero-indexed in Python.
        lines[line_number - 1] = text + "\n"

        # Open the file in 'writing mode' using the 2nd argument "w", this means
        # that the file will be made blank, and any new text we write to the file
        # will become the new file contents.
        with open(filename, "w") as file:

            # Loop through the list of lines, write each of them to the file
            for line in lines:
                file.write(line)

    # otherwise if the line number is past the length of the file, we can't
    # replace the line so output an error message instead
    else:

        # Output the line number that was requested to be replaced and the number
        # of lines the file actually has to inform the user
        print("Line", line_number, "not in file.")
        print("File has", len(lines), "lines.")


def textbox_maker():
    font = pygame.font.Font(None, 32)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREY = (128, 128, 128)
    current_color = GREY
    # Set up the input box
    input_box = pygame.Rect(280, 180, 40, 40)
    text = ''
    is_active = False
    max_characters = 1

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    is_active = True
                    current_color = WHITE
                else:
                    is_active = False
                    current_color = GREY
            if event.type == pygame.KEYDOWN:
                if is_active:
                    if event.key == pygame.K_RETURN:
                        return text
                    elif event.key == pygame.K_BACKSPACE:
                        text = ''

                    elif len(text) < max_characters:
                        if event.unicode != '':
                            text += event.unicode
                        else:
                            text = ''

            pygame.draw.rect(screen, current_color, input_box, 2)
            print(text)
            text_surface = font.render(text, True, WHITE)
            screen.blit(text_surface, (input_box.x + 5, input_box.y + 5))
            pygame.display.update()


def user_data_check(scrn_w, scrn_h):


    print("Start")
    counter = 0
    open("Text Files/User_Data.txt")
    user_data_file = open("Text Files/User_Data.txt", "r")

    line_output = user_data_file.readline()
    while line_output != "":
        line_output = line_output.rstrip()
        screen.blit(background, (0, 0))
        screen.blit(title_text, (50, 100))
        pygame.display.update()

        if line_output == "GameInProgress:True":
            last_comp_level = user_data_file.readline().rstrip()
            print(last_comp_level)

            new_game_img = pygame.image.load("Start_Menu_Images/new_game_btn.png")
            new_game_img = pygame.transform.scale(new_game_img, (180, 80))
            new_game_rect = new_game_img.get_rect(topleft=(200, 290))

            resume_game_img = pygame.image.load("Start_Menu_Images/resume_game_btn.png")
            resume_game_img = pygame.transform.scale(resume_game_img, (180, 80))
            resume_game_rect = new_game_img.get_rect(topleft=(200, 350))

            screen.fill((202, 228, 241))
            screen.blit(background, (0, 0))
            screen.blit(title_text, (50, 100))
            DISPLAYSURF.blit(new_game_img, new_game_rect)
            DISPLAYSURF.blit(resume_game_img, resume_game_rect)
            pygame.display.update()

            # This is the LOOP for the wizard giving the quest, you click on story
            game_resume_standby = True
            while game_resume_standby:

                for event in pygame.event.get():

                    if event.type == QUIT:

                        pygame.quit()

                    # If resume game button is clicked
                    elif event.type == MOUSEBUTTONDOWN:

                        if resume_game_rect.collidepoint(event.pos):

                            if last_comp_level == "Last Completed Level:0":
                                print("You completed the pre-game parts.")
                                print("Resuming at Level 1")
                                user_data_file.close()
                                whack_a_demon(scrn_w, scrn_h)
                            elif str(last_comp_level) == "Last Completed Level:1":
                                print("Your Last Level Was 1:")
                                print("Resuming at Level 2")
                                user_data_file.close()
                                labyrinth(scrn_w, scrn_h)
                            elif last_comp_level == "Last Completed Level:2":
                                print("Your Last Level Was 2:")
                                print("Resuming at Level 3")
                                user_data_file.close()
                                sphinx(scrn_w, scrn_h)
                            elif last_comp_level == "Last Completed Level:3":
                                print("Your Last Level Was 3:")
                                print("Resuming at End Game Sequence")
                                user_data_file.close()
                                end_sequence(scrn_w, scrn_h)
                            else:
                                print("You had not completed the pre-game sequence")
                                print("Resuming at Pre Game Sequence")
                                user_data_file.close()
                                start_sequence(scrn_w, scrn_h)

                        elif new_game_rect.collidepoint(event.pos):
                            print("Will continue a new game")
                            replace_line("Text Files/User_Data.txt", 1, "GameInProgress:True")
                            user_data_file.close()
                            start_sequence(scrn_w, scrn_h)

        else:
            print("Will continue a new game")
            replace_line("Text Files/User_Data.txt", 1, "GameInProgress:True")
            user_data_file.close()
            start_sequence(scrn_w, scrn_h)

    '''
    while line_read != "":  # validates for an empty string
        counter += 1
        line_read = user_data_file.readline()
        print(line_read)
        user_data_file.close()
        break
    '''

    username = None
    gameID = None
    game_finish_time = None
    level_1_score = None
    level_2_score = None
    level_3_score = None
    total_score = None
    user_data = [[username, gameID, game_finish_time, total_score], [level_1_score, level_2_score, level_3_score]]
    # to calculate total score, a for loop runs through the second array in the record to add to total


def start_sequence(scrn_w, scrn_h):
    background_imgs_raw = [pygame.image.load("Beginning_Cutscene/start_bg_1.png"),
                           pygame.image.load("Beginning_Cutscene/start_bg_2.png"),
                           pygame.image.load("Beginning_Cutscene/start_bg_3.png"),
                           pygame.image.load("Beginning_Cutscene/start_bg_4.png"),
                           pygame.image.load("Beginning_Cutscene/start_bg_5.png"),
                           pygame.image.load("Beginning_Cutscene/start_bg_6.png")]
    background_imgs = []
    for background_image in background_imgs_raw:
        background_imgs.append(pygame.transform.scale(background_image, (scrn_w, scrn_h)))

    story_imgs_raw = [pygame.image.load("Beginning_Cutscene/start_seq_1.png"),
                      pygame.image.load("Beginning_Cutscene/start_seq_2.png"),
                      pygame.image.load("Beginning_Cutscene/start_seq_3.png"),
                      pygame.image.load("Beginning_Cutscene/start_seq_4.png"),
                      pygame.image.load("Beginning_Cutscene/start_seq_5.png"),
                      pygame.image.load("Beginning_Cutscene/start_seq_6.png"),
                      pygame.image.load("Beginning_Cutscene/start_seq_7.png"),
                      pygame.image.load("Beginning_Cutscene/start_seq_8.png")]
    story_imgs = []
    for story_image in story_imgs_raw:
        story_imgs.append(pygame.transform.scale(story_image, (420, 100)))

    # The actual story

    DISPLAYSURF.blit(background_imgs[0], (0, 0))
    DISPLAYSURF.blit(story_imgs[0], (100, 100))
    pygame.display.update()
    time.sleep(6)

    DISPLAYSURF.blit(background_imgs[1], (0, 0))
    DISPLAYSURF.blit(story_imgs[1], (100, 100))
    pygame.display.update()
    time.sleep(6)

    DISPLAYSURF.blit(background_imgs[2], (0, 0))
    DISPLAYSURF.blit(story_imgs[2], (100, 100))
    pygame.display.update()
    time.sleep(6)

    DISPLAYSURF.blit(background_imgs[3], (0, 0))
    DISPLAYSURF.blit(story_imgs[3], (100, 100))
    pygame.display.update()
    time.sleep(6)

    DISPLAYSURF.blit(background_imgs[4], (0, 0))
    DISPLAYSURF.blit(story_imgs[4], (100, 100))
    pygame.display.update()
    time.sleep(6)

    DISPLAYSURF.blit(background_imgs[5], (0, 0))
    DISPLAYSURF.blit(story_imgs[5], (100, 100))
    pygame.display.update()
    time.sleep(6)

    DISPLAYSURF.blit(background_imgs[5], (0, 0))
    DISPLAYSURF.blit(story_imgs[6], (100, 100))
    pygame.display.update()
    time.sleep(6)

    DISPLAYSURF.blit(background_imgs[5], (0, 0))
    DISPLAYSURF.blit(story_imgs[7], (100, 100))
    pygame.display.update()
    time.sleep(6)

    pre_game(scrn_w, scrn_h)


def pre_game(scrn_w, scrn_h):
    # Have the "Flood Sequence here"

    navig_to_story(scrn_w, scrn_h, "Level_0/background_1.jpg",
                   "Level_0/background_2.jpg",
                   'Objectives/objective_01_nav_wiz.png',
                   300, 450, 300, 1)

    shuffle_story(600, 600, 1, "Level_0/background_2.jpg", 300,
                  450, 'Objectives/objective_2_1_nav_to_demon.png')
    open("Text Files/User_Data.txt", "r")
    replace_line("Text Files/User_Data.txt", 2, "Last Completed Level:0")
    user_data_file.close()
    whack_a_demon(scrn_w, scrn_h)


def whack_a_demon(scrn_w, scrn_h):
    navig_to_story(scrn_w, scrn_h, "Level_0/background_2.jpg",
                   "whack_a_demon/whack_a_demon_meadow.png",
                   'Objectives/objective_2_1_nav_to_demon.png',
                   300, 450, 300, 2)

    background_img = pygame.image. \
        load("whack_a_demon/whack_a_demon_meadow.png")
    background_file = pygame.transform.scale(background_img, (scrn_w, scrn_h))
    DISPLAYSURF.blit(background_file, (0, 0))

    demon = pygame.image.load('whack_a_demon/little_demon_heads.png')
    ghost_demon = pygame.image.load('whack_a_demon/ghost_demon.png')
    demon = pygame.transform.scale(demon, (100, 100))
    ghost_demon = pygame.transform.scale(ghost_demon, (100, 100))

    demon_rect_1 = demon.get_rect(topleft=(460, 400))
    demon_rect_2 = demon.get_rect(topleft=(230, 340))
    demon_rect_3 = demon.get_rect(topleft=(65, 220))
    ghost_demon_rect_1 = demon.get_rect(topleft=(460, 400))
    ghost_demon_rect_2 = demon.get_rect(topleft=(230, 340))
    ghost_demon_rect_3 = demon.get_rect(topleft=(65, 220))
    real_demon_array = [demon_rect_1, demon_rect_2, demon_rect_3]
    ghost_demon_array = [ghost_demon_rect_1, ghost_demon_rect_2, ghost_demon_rect_3]
    DISPLAYSURF.blit(demon, demon_rect_1)
    DISPLAYSURF.blit(demon, demon_rect_2)
    DISPLAYSURF.blit(demon, demon_rect_3)

    objective_2_2_img = pygame.image. \
        load('Objectives/objective_2_2_demonhorde.png')
    objective_2_2 = pygame.transform.scale(objective_2_2_img, (440, 90))

    objective_success_img = pygame.image.load('Objectives/objective_success.png')
    objective_success = pygame.transform.scale(objective_success_img, (300, 80))

    for i in range(3):
        DISPLAYSURF.blit(demon, real_demon_array[i])
    pygame.display.update()
    time.sleep(1.5)
    DISPLAYSURF.blit(background_file, (0, 0))
    DISPLAYSURF.blit(objective_2_2, (100, 100))
    pygame.display.update()
    score = 0
    lives = 3
    font = pygame.font.Font(None, 36)

    remaining_turns = 12
    while remaining_turns > 0:

        print(f"Score: {score}")
        print(f"Lives: {lives}")
        demon_position = random.randint(1, 3)
        real_or_fake_demon = random.randint(1, 2)

        DISPLAYSURF.blit(background_file, (0, 0))
        if real_or_fake_demon == 1:
            demon_array = real_demon_array
            DISPLAYSURF.blit(demon, demon_array[demon_position - 1])
        else:
            demon_array = ghost_demon_array
            DISPLAYSURF.blit(ghost_demon, demon_array[demon_position - 1])

        DISPLAYSURF.blit(objective_2_2, (100, 100))

        remaining_turns_text = font.render(f"Remaining Turns: {remaining_turns}", True, (255, 255, 255))
        remaining_turns_rect = remaining_turns_text.get_rect(topleft=(320, 30))
        screen.blit(remaining_turns_text, remaining_turns_rect)

        lives_text = font.render(f"Lives: {lives}", True, (255, 255, 255))
        lives_rect = lives_text.get_rect(topleft=(20, 30))
        screen.blit(lives_text, lives_rect)

        pygame.display.update()
        # appear_time = random.randint(1, 3)
        # start time of each cycle must be immediately before the while loop
        start_time = pygame.time.get_ticks()
        print(f"Remaining Turns: {remaining_turns}")

        cycle_on = True
        while cycle_on:
            elapsed_time = 0

            clock = pygame.time.Clock()
            if lives == 0:


                lives_text = font.render(f"The Jellib was consumed by the Demons", True, (255, 0, 0))
                lives_rect = lives_text.get_rect(topleft=(20, 30))
                screen.blit(lives_text, lives_rect)

                lives_text = font.render(f"Game Over", True, (255, 0, 0))
                lives_rect = lives_text.get_rect(topleft=(20, 30))
                screen.blit(lives_text, lives_rect)

                print("You died")
                time.sleep(50)
                # Blit all real demons
                # Endgame code
                # Then break
            end_time = pygame.time.get_ticks()
            print(f"Start time: {start_time}")
            print(f"End time: {end_time}")
            elapsed_time = (pygame.time.get_ticks() - start_time) // 1000
            print(f"elapsed time: {elapsed_time}")
            # check if 2 seconds have elapsed without the
            if elapsed_time >= 2:

                # If it was a real demon, missing it leads to lower score
                if real_or_fake_demon == 1:
                    lives -= 1
                    score -= 25

                # else, youre supposed to avoid it. So do nothing

                remaining_turns -= 1
                cycle_on = False

            # clock.tick(appear_time)  # used to control the frame rate
            clock.tick(2)
            for event in pygame.event.get():  # checks for events such as key presses and program quitting
                if event.type == pygame.QUIT:
                    # Will have:"Are you sure you want to quit? code"
                    quit()

                # If a demon is clicked
                elif event.type == MOUSEBUTTONDOWN:

                    if demon_array[demon_position - 1].collidepoint(event.pos):
                        if real_or_fake_demon == 1:

                            # Measures the quarter-second intervals
                            elapsed_time = (pygame.time.get_ticks() - start_time) // 250
                            score_bonus = 2000 - elapsed_time
                            score_bonus = (round(score_bonus, -1)) / 10
                            score += score_bonus

                            remaining_turns -= 1
                        else:
                            lives -= 1
                            score -= 25
                            remaining_turns -= 1
                        cycle_on = False
                        # Calculate the elapsed time in seconds

    print("Won")
    endgame_text = font.render(f"Final Score: {score}", True, (255, 255, 255))
    endgame_rect = endgame_text.get_rect(topleft=(400, 30))
    screen.blit(background_file, (0, 0))

    screen.blit(endgame_text, endgame_rect)
    screen.blit(objective_success, (100, 0))
    pygame.display.update()
    time.sleep(2)

    # file modification code
    open("Text Files/User_Data.txt", "r")
    replace_line("Text Files/User_Data.txt", 2, "Last Completed Level:1")
    replace_line("Text Files/User_Data.txt", 3, f"Level 1 Score:{score}")
    user_data_file.close()
    shuffle_story(600, 600, 2, "whack_a_demon/whack_a_demon_meadow.png", 300,
                  450, 'Objectives/objective_3_1_nav_to_labyrinth.png')
    labyrinth(scrn_w, scrn_h)


def labyrinth(scrn_w, scrn_h):
    navig_to_story(scrn_w, scrn_h, "whack_a_demon/whack_a_demon_meadow.png",
                   "Maze/demon_to_labyrinth_bg.png",
                   'Objectives/objective_3_1_nav_to_labyrinth.png',
                   300, 450, 300, 3)

    # global Wall, walls, level

    # create a class for the player (provides functionality for moving the character)
    class Player(object):
        # initializes the position and dimensions of self (player character)
        def __init__(self):

            self.image = pygame.image.load("Level_0/Jellib.png")
            self.image = pygame.transform.scale(self.image, (28, 28))
            self.rect = self.image.get_rect(topleft=(100, 110))

        # updates position
        def move(self, dx, dy):
            # moves each axis separately. checks for collisions both times.
            if dx != 0:
                self.move_single_axis(dx, 0)
            if dy != 0:
                self.move_single_axis(0, dy)

        # updates player position based on dx and dy values
        def move_single_axis(self, dx, dy):
            # updates players x and y coordinates
            self.rect.x += dx
            self.rect.y += dy

            # if you collide with a wall, code makes sure that player rectangle does not overlap the wall
            for wall in walls:
                if self.rect.colliderect(wall.rect):
                    if dx > 0:
                        self.rect.right = wall.rect.left
                    if dx < 0:
                        self.rect.left = wall.rect.right
                    if dy > 0:
                        self.rect.bottom = wall.rect.top
                    if dy < 0:
                        self.rect.top = wall.rect.bottom

    # rect(left, top, width, height) creates a rectangle area. For example, 16 is the height and width of walls
    class Wall(object):
        def __init__(self, pos):
            walls.append(self)
            self.rect = pygame.Rect(pos[0], pos[1], 16, 16)

    # initialize pygame
    # pygame.init()

    # set up the display
    pygame.display.set_caption("Return to Tekoon: Deluge")
    screen = pygame.display.set_mode((600, 600))
    clock = pygame.time.Clock()
    walls = []  # list is created to hold the walls
    player = Player()  # creates the player
    # maze layout (W represents the wall, E is the end square)
    level = [
        "WWWWWW  WWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
        "W                                   W",
        "W                                   W",
        "W   WWWW       WWW  WWW             W",
        "W   W           WW  WW              W",
        "W   W    WW   WWWW        WWWWWW    W",
        "W   W     W  WWWWW         WWW      W",
        "W   W     W   WWW          WW      WW",
        "W   WWW   W     W   WWWWWWWW     WWWW",
        "W     W   W     W  WW     W         W",
        "WW    WWWWWWW   W  W      W         W",
        "W W             WWWW    WWWWWWWWWWWWW",
        "W                                  WW",
        "W                                   W",
        "W   W   WWWWWWWW       W   WWWWWW   W",
        "W   W     W WWWW       W   WWWW     W",
        "W   W     W    WWWWWW  WWWWWW      WW",
        "W         W       W       W        WW",
        "W         WW              W         W",
        "WWWWWWW   W             WWWWWW   WWWW",
        "WW    WW          WWW         WWWWWWW",
        "W      W            W               W",
        "W     WWWWW      WWWWWWWWW          W",
        "W     W   W        W               WW",
        "W         WW       W                W",
        "W WWWW     WW      W    WWWWWW     WW",
        "W              W  WWWW   W    WWWWWWW",
        "W               W        W          W",
        "WWW WWWW     WWWW         WWW       W",
        "W               W                   W",
        "W E             W                   W",
        "WW WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    ]

    # parsing the level layout string, initializing the walls and the end rectangle
    def maze_maker():
        x = 0
        y = 90
        for row in level:
            for col in row:
                if col == "W":
                    Wall((x, y))
                if col == "E":
                    end_rect = pygame.Rect(x, y, 16, 16)
                x += 16
            y += 16
            x = 0
        return end_rect

    end_rect = maze_maker()
    running = True
    start_time = pygame.time.get_ticks()  # start time of the game
    font = pygame.font.Font(None, 36)  # font object for displayed messages
    game_over = False
    elapsed_time = 1
    while running:
        clock.tick(60)  # used to control the frame rate

        for e in pygame.event.get():  # checks for events such as key presses and program quitting
            if e.type == pygame.QUIT:
                running = False
            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                running = False
        # drawing the maze (walls, background, player and end color)
        screen.fill((85, 55, 20))
        background = pygame.image.load("Maze/maze_bg.jpeg")
        scrn_w = 600
        scrn_h = 600
        background = pygame.transform.scale(background, (scrn_w, scrn_h))
        screen.blit(background, (0, 0))

        for wall in walls:
            pygame.draw.rect(screen, (25, 200, 0), wall.rect)

        pygame.draw.rect(screen, (255, 0, 0), end_rect)
        screen.blit(player.image, (player.rect.x, player.rect.y))
        objective_img = pygame.image.load('Objectives/objective_3_2_labyrinth.png')
        objective = pygame.transform.scale(objective_img, (440, 90))
        objective_success_img = pygame.image.load('Objectives/objective_success.png')
        objective_success = pygame.transform.scale(objective_success_img, (300, 80))
        objective_failed_img = pygame.image.load('Objectives/objective_failed.png')
        objective_failed = pygame.transform.scale(objective_failed_img, (300, 80))
        screen.blit(objective, (30, 0))
        pygame.display.update()

        game_won = False
        if game_over and not game_won:

            # display message
            time_up_text = font.render("The Jellib died of exhaustion", True, (255, 255, 255))
            time_up_rect = time_up_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
            screen.blit(background, (0, 0))
            end_rect = maze_maker()
            for wall in walls:
                pygame.draw.rect(screen, (25, 200, 0), wall.rect)
            screen.blit(time_up_text, time_up_rect)
            screen.blit(objective_failed, (150, 0))
            pygame.display.update()
            time.sleep(500)

        else:
            print(elapsed_time)
            # move the player if keys w, a, s, or d is pressed
            key = pygame.key.get_pressed()
            if key[pygame.K_a] or key[pygame.K_LEFT]:
                player.move(-1, 0)
            if key[pygame.K_d] or key[pygame.K_RIGHT]:
                player.move(1, 0)
            if key[pygame.K_w] or key[pygame.K_UP]:
                player.move(0, -1)
            if key[pygame.K_s] or key[pygame.K_DOWN]:
                player.move(0, 1)

            # checks if player square collides with end square (if so, end the game)
            if player.rect.colliderect(end_rect) and elapsed_time <= 60:
                print("Won")

                game_over = True
                # display message
                score = (60 - elapsed_time) * 10
                endgame_text = font.render(f"Final Score: {score}", True, (255, 255, 255))
                endgame_rect = endgame_text.get_rect(topleft=(400, 30))
                screen.blit(background, (0, 0))
                end_rect = maze_maker()
                for wall in walls:
                    pygame.draw.rect(screen, (25, 200, 0), wall.rect)
                screen.blit(endgame_text, endgame_rect)
                screen.blit(objective_success, (100, 0))
                pygame.display.update()
                time.sleep(2)

                # file modification code
                open("Text Files/User_Data.txt", "r")
                replace_line("Text Files/User_Data.txt", 2, "Last Completed Level:2")
                replace_line("Text Files/User_Data.txt", 4, f"Level 2 Score:{score}")
                user_data_file.close()
                shuffle_story(600, 600, 3, "sphinx_level/maze_to_sphinx_bg.png", 300,
                              450, 'Objectives/objective_4_1_nav_to_sphinx.png')

                sphinx(scrn_w, scrn_h)

            else:
                game_won = False

            # Calculate the elapsed time in seconds
            elapsed_time = (pygame.time.get_ticks() - start_time) // 1000

            # check if one minute has elapesd
            if elapsed_time >= 60 and not game_won:
                game_over = True
                game_won = False

            # display elapsed time
            remaining_time = 60 - elapsed_time
            white = (255, 255, 255)
            red = (255, 0, 0)
            if remaining_time > 15:
                time_text = font.render(f"Time: {remaining_time}s", True, white)
            else:
                time_text = font.render(f"Time: {remaining_time}s", True, red)
            screen.blit(time_text, (screen.get_width() - time_text.get_width() - 10, 10))

        # updates the display
        pygame.display.flip()
    pygame.quit()


def sphinx(scrn_w, scrn_h):
    navig_to_story(scrn_w, scrn_h, "sphinx_level/maze_to_sphinx_bg.png",
                   "sphinx_level/sphinx_bg.png",
                   'Objectives/objective_4_1_nav_to_sphinx.png',
                   300, 450, 300, 4)

    background = pygame.image.load("sphinx_level/sphinx_bg.png")
    background = pygame.transform.scale(background, (scrn_w, scrn_h))
    sphinx_img = pygame.image.load('sphinx_level/sphinx_image.png')
    sphinx_character = pygame.transform.scale(sphinx_img, (150, 280))
    jellib = pygame.image.load('Level_0/Jellib.png')
    jellib = pygame.transform.scale(jellib, (50, 50))
    objective_img = pygame.image.load('Objectives/objective_4_2_sphinx.png')
    objective = pygame.transform.scale(objective_img, (440, 120))
    objective_success_img = pygame.image.load('Objectives/objective_success.png')
    objective_success = pygame.transform.scale(objective_success_img, (300, 80))
    objective_failed_img = pygame.image.load('Objectives/objective_failed.png')
    objective_failed = pygame.transform.scale(objective_failed_img, (300, 80))

    # Word Game
    def instructions():

        sphinx_instructions_file = open("sphinx_level/Sphinx_Instructions.txt", "r")
        line_output = sphinx_instructions_file.readline()
        while line_output != "":
            line_output = line_output.rstrip()
            instructions_text = font.render(f"{line_output}", True, (0, 0, 0))
            instructions_rect = instructions_text.get_rect(topleft=(50, 30))
            DISPLAYSURF.blit(background, (0, 0))
            DISPLAYSURF.blit(sphinx_character, (220, 210))
            DISPLAYSURF.blit(instructions_text, instructions_rect)
            DISPLAYSURF.blit(jellib, (300, 450))
            pygame.display.update()
            time.sleep(3)
            line_output = sphinx_instructions_file.readline()

    def get_word():
        master_list = ['AXIOM', 'PROBE', 'THORN', 'FOYER', 'LONER', 'OXIDE', 'PIOUS', 'APPLE', 'QUIET',
                       'PROOF', 'NORTH', 'DEPTH', 'FIERY', 'WORDS', 'FIGHT', 'FALLS', 'RATED', 'BATED',
                       'GORGE', 'MOUSE', 'PHONE', 'ISSUE', 'TRUTH', "ARENA", "LUCKY"]
        shuffled_masterlist = random.sample(master_list, len(master_list))
        chosen_word = shuffled_masterlist[0:1]

        return chosen_word

    def liststring(chosen_word):
        word_given_as_list = chosen_word

        main_word_as_string = str(word_given_as_list)
        letter_list = list(main_word_as_string)

        for i in range(2):
            del (letter_list[0])

        for i in range(2):
            del (letter_list[len(letter_list) - 1])

        return letter_list

    def guessed_asterisks(list_of_letters):
        hidden_word = ["_"] * len(list_of_letters)

        return hidden_word

    def exit_program():
        exit()

    insult_array = []
    sphinx_insults_file = open("sphinx_level/Sphinx_Insults.txt", "r")
    line_output = sphinx_insults_file.readline()
    while line_output != "":
        line_output = line_output.rstrip()
        insult_array.append(line_output)
        # print(line_output)
        line_output = sphinx_insults_file.readline()

    instructions()
    start_message = "Ready? Let's begin..I have not consumed Jellib in many millennia."
    instructions_text = font.render(f"{start_message}", True, (0, 0, 0))
    instructions_rect = instructions_text.get_rect(topleft=(50, 30))
    DISPLAYSURF.blit(background, (0, 0))
    DISPLAYSURF.blit(instructions_text, instructions_rect)
    DISPLAYSURF.blit(sphinx_character, (220, 210))
    DISPLAYSURF.blit(jellib, (300, 450))
    pygame.display.update()
    time.sleep(2.5)
    word_obtained = get_word()
    list_of_letters = liststring(word_obtained)
    word_to_be_guessed = guessed_asterisks(list_of_letters)
    number_of_attempts = 10
    replacing_asterisk = int(len(word_to_be_guessed))
    letters_guessed_by_user = []
    DISPLAYSURF.blit(background, (0, 0))
    DISPLAYSURF.blit(sphinx_character, (220, 210))
    screen.blit(objective, (100, 0))
    DISPLAYSURF.blit(jellib, (300, 450))
    print(word_to_be_guessed)
    user_given_letter = textbox_maker()
    pygame.display.update()
    user_given_letter = user_given_letter.upper()

    entire_game = True
    while entire_game:

        word_guessing_game = True
        while word_guessing_game:

            while "_" in word_to_be_guessed:
                print(f"Remaining Attempts: {number_of_attempts}")

                # Technically your last attempt will read as no more attempts remaining (after)
                if number_of_attempts > -1:

                    remaining_attempts = f"Remaining Attempts:{number_of_attempts}"
                    remaining_attempts_text = font.render(f"{remaining_attempts}", True, (0, 0, 0))
                    remaining_attempts_rect = instructions_text.get_rect(topleft=(400, 130))
                    DISPLAYSURF.blit(background, (0, 0))
                    DISPLAYSURF.blit(objective, (100, 0))
                    DISPLAYSURF.blit(remaining_attempts_text, remaining_attempts_rect)

                    if user_given_letter in list_of_letters:

                        if user_given_letter not in letters_guessed_by_user:
                            print(user_given_letter, "is a correct guess!")

                            if "_" not in word_to_be_guessed:
                                score = 500 - (number_of_attempts * 100)
                                print("Hmph..I was looking forward to a meal today..You may pass..for now \n"" ")

                                game_won_phrase_1 = "Hmph..I was looking forward to a meal today..You may pass..for now "
                                game_won_phrase_1_text = font3.render(f"{game_won_phrase_1}", True, (0, 0, 0))
                                game_won_phrase_1_rect = game_won_phrase_1_text.get_rect(topleft=(30, 160))

                                DISPLAYSURF.blit(background, (0, 0))
                                DISPLAYSURF.blit(objective, (100, 0))
                                DISPLAYSURF.blit(jellib, (300, 450))
                                DISPLAYSURF.blit(sphinx_character, (220, 210))
                                DISPLAYSURF.blit(game_won_phrase_1_text, game_won_phrase_1_rect)
                                pygame.display.update()
                                time.sleep(4)

                                open("Text Files/User_Data.txt", "r")
                                replace_line("Text Files/User_Data.txt", 2, "Last Completed Level:3")
                                replace_line("Text Files/User_Data.txt", 5, f"Level 3 Score:{score}")
                                user_data_file.close()
                                entire_game = False
                                end_sequence(scrn_w, scrn_h)

                            correct_answer_phrase = f"{user_given_letter} is a correct guess!"
                            correct_answer_text = font.render(f"{correct_answer_phrase}", True, (0, 0, 0))
                            correct_answer_rect = correct_answer_text.get_rect(topleft=(30, 130))
                            DISPLAYSURF.blit(correct_answer_text, correct_answer_rect)

                            letters_guessed_by_user.append(user_given_letter)

                            for i in range(replacing_asterisk):
                                if list_of_letters[i] == user_given_letter:
                                    del (word_to_be_guessed[i])
                                    word_to_be_guessed.insert(i, user_given_letter)

                            print(word_to_be_guessed)
                            print()

                            number_of_attempts -= 1

                        elif user_given_letter in letters_guessed_by_user:

                            repeat_correct_answer_phrase = f"You fool..You already guessed{user_given_letter} as a correct guess!"
                            repeat_correct_answer_text = font.render(f"{repeat_correct_answer_phrase}", True, (0, 0, 0))
                            repeat_correct_answer_rect = repeat_correct_answer_text.get_rect(topleft=(30, 130))
                            DISPLAYSURF.blit(repeat_correct_answer_text, repeat_correct_answer_rect)

                    elif user_given_letter not in list_of_letters:
                        if user_given_letter not in letters_guessed_by_user:

                            incorrect_answer_phrase = f"{user_given_letter} is an incorrect guess!"
                            incorrect_answer_text = font.render(f"{incorrect_answer_phrase}", True, (0, 0, 0))
                            incorrect_answer_rect = incorrect_answer_text.get_rect(topleft=(30, 130))
                            DISPLAYSURF.blit(incorrect_answer_text, incorrect_answer_rect)

                            random_insult = insult_array[random.randint(0, 3)]
                            random_insult_text = font3.render(f"{random_insult}", True, (0, 0, 0))
                            random_insult_rect = random_insult_text.get_rect(topleft=(20, 160))
                            DISPLAYSURF.blit(random_insult_text, random_insult_rect)

                            letters_guessed_by_user.append(user_given_letter)

                            number_of_attempts -= 1

                        elif user_given_letter in letters_guessed_by_user:

                            repeat_incorrect_answer_phrase = f"You fool..You already guessed{user_given_letter} as an incorrect guess!"
                            repeat_incorrect_answer_text = font.render(f"{repeat_incorrect_answer_phrase}", True,
                                                                       (0, 0, 0))
                            repeat_incorrect_answer_rect = repeat_incorrect_answer_text.get_rect(topleft=(20, 130))
                            DISPLAYSURF.blit(repeat_incorrect_answer_text, repeat_incorrect_answer_rect)
                    # Converts the array to a string
                    word_to_be_guessed_string = ""
                    for word in word_to_be_guessed:
                        if word == "_":
                            word = " _ "
                        word_to_be_guessed_string += word
                        print(word_to_be_guessed_string)
                    word_to_be_guessed_text = font2.render(f"{word_to_be_guessed_string}", True, (255, 255, 255))
                    word_to_be_guessed_rect = word_to_be_guessed_text.get_rect(topleft=(220, 500))
                    DISPLAYSURF.blit(word_to_be_guessed_text, word_to_be_guessed_rect)

                    DISPLAYSURF.blit(sphinx_character, (220, 210))
                    DISPLAYSURF.blit(jellib, (300, 450))
                    #user_given_letter = textbox_maker()
                    pygame.display.update()

                    DISPLAYSURF.blit(background, (0, 0))
                    DISPLAYSURF.blit(sphinx_character, (220, 210))
                    screen.blit(objective, (100, 0))
                    DISPLAYSURF.blit(jellib, (300, 450))
                    print(word_to_be_guessed)
                    user_given_letter = textbox_maker()
                    pygame.display.update()
                    user_given_letter = user_given_letter.upper()

                    # user_given_letter = textbox_maker()
                    # user_given_letter = input("Continue to input letters. Be careful about what you input: ")

                    print()

                elif number_of_attempts <= 0:
                    break

            word_guessing_game = False

        if "_" in word_to_be_guessed:
            failed_word = str(list_of_letters)

            print("Thanks for playing, young Jellib..."
                  "\nIt will be entertaining to hear your screams of pain as you are digested")
            print(f"By the way, the failed word was {failed_word}")
            entire_game = False

            game_lost_phrase_1 = "Thanks for playing, young Jellib..."
            game_lost_phrase_1_text = font.render(f"{game_lost_phrase_1}", True, (0, 0, 0))
            game_lost_phrase_1_rect = game_lost_phrase_1_text.get_rect(topleft=(30, 160))

            game_lost_phrase_2 = "It will be entertaining to hear your screams of pain as you are digested"
            game_lost_phrase_2_text = font3.render(f"{game_lost_phrase_2}", True, (0, 0, 0))
            game_lost_phrase_2_rect = game_lost_phrase_2_text.get_rect(topleft=(20, 160))

            game_lost_phrase_3 = f"By the way, the failed word was {failed_word}"
            game_lost_phrase_3_text = font3.render(f"{game_lost_phrase_3}", True, (0, 0, 0))
            game_lost_phrase_3_rect = game_lost_phrase_3_text.get_rect(topleft=(20, 160))

            game_lost_phrase_texts = [game_lost_phrase_1_text, game_lost_phrase_2_text, game_lost_phrase_3_text]
            game_lost_phrase_rects = [game_lost_phrase_1_rect, game_lost_phrase_2_rect, game_lost_phrase_3_rect]

            for i in range(3):
                DISPLAYSURF.blit(background, (0, 0))
                DISPLAYSURF.blit(objective, (100, 0))
                DISPLAYSURF.blit(sphinx_character, (220, 210))
                DISPLAYSURF.blit(game_lost_phrase_texts[i], game_lost_phrase_rects[i])
                pygame.display.update()
                time.sleep(2)




# End cutscene plus credits
def end_sequence(scrn_w, scrn_h):
    background_imgs_raw = [pygame.image.load("End_Sequence/score_bg.png"),
                           pygame.image.load("End_Sequence/end_sequence_bg.png"),
                           pygame.image.load("End_Sequence/end_credits_bg.png")]
    background_imgs = []
    for background_image in background_imgs_raw:
        background_imgs.append(pygame.transform.scale(background_image, (scrn_w, scrn_h)))

    story_imgs_raw = [pygame.image.load("End_Sequence/end_sequence_story_1.png"),
                      pygame.image.load("End_Sequence/end_sequence_story_2.png"),
                      pygame.image.load("End_Sequence/end_sequence_story_3.png")]
    story_imgs = []
    for story_image in story_imgs_raw:
        story_imgs.append(pygame.transform.scale(story_image, (420, 100)))

    user_data_content = user_data_file.readlines()

    total_scores = []
    for i in range(3):
        total_scores.append(int(user_data_content[2 + i][14:]))

    final_score = 0
    for score in total_scores:
        final_score += score
    replace_line("Text Files/User_Data.txt", 6, f"Total Score:{final_score} ")

    level_1_score_text = font4.render(f"Level 1: {total_scores[0]}", True, (173, 216, 230))
    level_1_score_rect = level_1_score_text.get_rect(topleft=(150, 250))
    level_2_score_text = font4.render(f"Level 2: {total_scores[1]}", True, (173, 216, 230))
    level_2_score_rect = level_2_score_text.get_rect(topleft=(150, 300))
    level_3_score_text = font4.render(f"Level 3: {total_scores[2]}", True, (173, 216, 230))
    level_3_score_rect = level_3_score_text.get_rect(topleft=(150, 350))
    total_score_text = font4.render(f"Total Score: {final_score}", True, (173, 216, 230))
    total_score_rect = total_score_text.get_rect(topleft=(150, 400))

    DISPLAYSURF.blit(background_imgs[0], (0, 0))
    DISPLAYSURF.blit(level_1_score_text, level_1_score_rect)
    DISPLAYSURF.blit(level_2_score_text, level_2_score_rect)
    DISPLAYSURF.blit(level_3_score_text, level_3_score_rect)
    DISPLAYSURF.blit(total_score_text, total_score_rect)
    pygame.display.update()
    time.sleep(6)

    # The actual scene
    DISPLAYSURF.blit(background_imgs[1], (0, 0))
    DISPLAYSURF.blit(story_imgs[0], (100, 100))
    pygame.display.update()
    time.sleep(6)

    DISPLAYSURF.blit(background_imgs[1], (0, 0))
    DISPLAYSURF.blit(story_imgs[1], (100, 100))
    pygame.display.update()
    time.sleep(6)

    DISPLAYSURF.blit(background_imgs[1], (0, 0))
    DISPLAYSURF.blit(story_imgs[2], (100, 100))
    pygame.display.update()
    time.sleep(6)

    DISPLAYSURF.blit(background_imgs[2], (0, 0))
    pygame.display.update()
    time.sleep(8)

    open("Text Files/User_Data.txt", "r")
    replace_line("Text Files/User_Data.txt", 1, "GameInProgress:False")
    replace_line("Text Files/User_Data.txt", 2, "Last Completed Level:--")
    replace_line("Text Files/User_Data.txt", 3, "Level 1 Score: ")
    replace_line("Text Files/User_Data.txt", 4, "Level 2 Score: ")
    replace_line("Text Files/User_Data.txt", 5, "Level 3 Score: ")
    replace_line("Text Files/User_Data.txt", 6, "Total Score: ")

    # GameComplete is a part of a new feature that will be released
    # , which allows user to compare their 3 best scores.
    # If a game complete, the data will be downloaded to another file
    # For now, this variable is reset.
    replace_line("Text Files/User_Data.txt", 7, "GameComplete:False ")

    user_data_file.close()

    main_menu()


main_menu()
pygame.quit()
