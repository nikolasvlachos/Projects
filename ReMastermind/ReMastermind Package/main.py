# \_________________________________________________________________________/#

# Name : ReMastermind
# Date : January 18th, 2023
# Developers : Sakib Uddin, Nikolas Vlachos, Abdu-R-Raheem
# Description : ReMastermind is a revamped version of the original
#               game "Mastermind". This program simulates the game Mastermind
#               but with the additional feature of pygame. The user
#               has access to new features such as buying and using
#               power-ups, and completing challenges to earn in-game
#               cash. This program utilizes classes to store the leaderboard
#               data and player's inventory. Lists were also used to
#               store the player's guesses and were used to break down
#               important information such as the leaderboard and challenges,
#               into smaller parts like indices of a list. Recursion was also
#               used to efficiently display the leaderboard stats. The main
#               screen is all run by a while loop in the "main" function.

# \_________________________________________________________________________/#


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# ~ Libraries and Classes~ #
import random
import time
import pygame
from Button import *
from Leaderboard import *
from Player import *


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# Setting up pygame window
pygame.init ()
screen = pygame.display.set_mode ((800, 800))
pygame.display.set_caption ("ReMastermind")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GOLD = (255, 215, 0)
SILVER = (192, 192, 192)
BRONZE = (205, 127, 50)
GREEN = (0, 255, 0)

# Fonts
font15 = pygame.font.Font ("ARCADEGAMER.TTF", 15)
font20 = pygame.font.Font ("ARCADEGAMER.TTF", 20)
font30 = pygame.font.Font ("ARCADEGAMER.TTF", 30)
font50 = pygame.font.Font ("ARCADEGAMER.TTF", 50)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# ~ Functions ~ #


# Calculates the minutes and seconds from the total seconds
def seconds_to_minutes (seconds):
    minutes = seconds // 60
    minutes = int (minutes)
    remaining_seconds = seconds % 60
    remaining_seconds = round (remaining_seconds, 1)

    return (minutes, remaining_seconds)


# Calculates the player's score, depending on the difficulty when they win
def calculate_score (game_mode, guess_count):
    total_score = 0

    if (game_mode == "Easy"):
        total_score = (1000 * (11 - guess_count))
        if (guess_count == 11):
            total_score = 1000

    if (game_mode == "Medium"):
        total_score = (1500 * (11 - guess_count))
        if (guess_count == 11):
            total_score = 1500

    if (game_mode == "Hard"):
        total_score = (2250 * (11 - guess_count))

        if (guess_count == 11):
            total_score = 2250

    return total_score


# Reveals one character and its placement
def powerup_1 (answer):
    answer_char = []
    reveal = random.randint (0, 3)

    for i in answer:
        answer_char.append (i)

    rev_char = answer_char[reveal]
    placement = ["_", "_", "_", "_"]
    placement.pop (reveal)
    placement.insert (reveal, rev_char)
    result = " ".join (placement)

    return result


# Reveals two characters and their placements
def powerup_2 (answer):
    answer_char = []

    reveal1 = random.randint (0, 3)
    reveal2 = random.randint (0, 3)

    while (reveal2 == reveal1):
        reveal2 = random.randint (0, 3)

    for i in answer:
        answer_char.append (i)

    rev_char1 = answer_char[reveal1]
    rev_char2 = answer_char[reveal2]
    placement = ["_", "_", "_", "_"]
    placement.pop (reveal1)
    placement.insert (reveal1, rev_char1)
    placement.pop (reveal2)
    placement.insert (reveal2, rev_char2)
    result = " ".join (placement)

    return result


# Reveals one character without its placement
def powerup_3 (answer):
    answer_char = []

    reveal = random.randint (0, 3)

    for i in answer:
        answer_char.append (i)

    rev_char = answer_char[reveal]

    return rev_char


# Reveals all four characters without their placements
def powerup_4 (answer):
    answer_char = []
    reveal1 = random.randint (0, 3)
    reveal2 = random.randint (0, 3)

    while (reveal2 == reveal1):
        reveal2 = random.randint (0, 3)

    reveal3 = random.randint (0, 3)

    while ((reveal3 == reveal2) or (reveal3 == reveal1)):
        reveal3 = random.randint (0, 3)

    reveal4 = random.randint (0, 3)

    while ((reveal4 == reveal3) or (reveal4 == reveal2) or
           (reveal4 == reveal1)):
        reveal4 = random.randint (0, 3)

    for i in answer:
        answer_char.append (i)

    rev_char1 = answer_char[reveal1]
    rev_char2 = answer_char[reveal2]
    rev_char3 = answer_char[reveal3]
    rev_char4 = answer_char[reveal4]

    result = rev_char1 + ", " + rev_char2 + ", " + rev_char3 + ", " + rev_char4

    return result


# Removes a power-up from the player's inventory once they use it
def remove_from_inventory (list, powerup_used):
    pos = list.index (powerup_used)
    list.pop (pos)

    return list


# Draws text onto the screen
def draw_text (text, font, text_col, x, y):
    img = font.render (text, True, text_col)
    screen.blit (img, (x, y))


# Recursively prints the leaderboard of high scores
def recursive_stat_print (list, x, y, num):
    if (len (list) == 1):
        current = list[0]
        stat = f"{num:<2}.{current[0]:<18} {current[2]}"

        if (num == 1):
            draw_text (stat, font20, GOLD, x, y)

        elif (num == 2):
            draw_text (stat, font20, WHITE, x, y)

        elif (num == 3):
            draw_text (stat, font20, BRONZE, x, y)

        else:
            draw_text (stat, font20, SILVER, x, y)

        return (list[0])

    else:
        current = list[0]
        stat = f"{num:<2}.{current[0]:<18} {current[2]}"

        if (num == 1):
            draw_text (stat, font20, GOLD, x, y)

        elif (num == 2):
            draw_text (stat, font20, WHITE, x, y)

        elif (num == 3):
            draw_text (stat, font20, BRONZE, x, y)

        else:
            draw_text (stat, font20, SILVER, x, y)

        return recursive_stat_print (list[1:], x, y + 52, num + 1)


# Generates the combination for the player to guess
def generate_code (inputted_mode):
    generated_code = ""

    for i in range (4):
        current_symbol = random.randint (1, inputted_mode)

        if (current_symbol == 1):
            generated_code += "@"

        elif (current_symbol == 2):
            generated_code += "!"

        elif (current_symbol == 3):
            generated_code += "#"

        elif (current_symbol == 4):
            generated_code += "$"

        elif (current_symbol == 5):
            generated_code += "%"

        elif (current_symbol == 6):
            generated_code += "&"

        elif (current_symbol == 7):
            generated_code += "/"

        elif (current_symbol == 8):
            generated_code += "?"

    # ----------ANSWER---------- #
    print (generated_code)
    return generated_code
    # ----------ANSWER---------- #


# Checks to symbols in the correct and incorrect spots
def assess_guess (code_array, guess_array):
    # Checks correct placement
    red_peg_counter = 0
    code_xs = ["", "", "", ""]
    guess_xs = ["", "", "", ""]

    for red_assess in range (0, 4):
        if (code_array[red_assess] == guess_array[red_assess]):
            red_peg_counter += 1
            code_xs[red_assess] = "X"
            guess_xs[red_assess] = "X"

    # Checks incorrect placement
    white_peg_counter = 0

    for white_assess in range (0, 4):
        for check_code_for_white in range (0, 4):
            if ((guess_xs[white_assess] != "X") and
                    (code_xs[check_code_for_white] != "X")):
                if (guess_array[white_assess] ==
                        code_array[check_code_for_white]):
                    white_peg_counter += 1
                    guess_xs[white_assess] = "X"
                    code_xs[check_code_for_white] = "X"

    peg_results = [red_peg_counter, white_peg_counter]

    return peg_results


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

def main ():
    # ~ Variable initialization ~ #

    # Variables for pygame screen control
    run = True
    challenges = False
    rules = False
    user = False
    store = False
    rankings = False
    start = False
    easy_state = False
    medium_state = False
    hard_state = False
    insufficient = False
    powerup_state = False
    game_start = False
    game_end = False
    name = False
    win_screen = False
    to_win = False
    to_lose = False

    # Variables to indicate power-up usage
    select_power_1 = False
    select_power_2 = False
    select_power_3 = False
    select_power_4 = False
    select_power_5 = False
    powerup_5 = False

    # Variables to indicate how many extra features the user unlocks depending
    # on mode selection
    med_extra = False
    hard_extra = False

    # Fonts
    font15 = pygame.font.Font ("ARCADEGAMER.TTF", 15)
    font20 = pygame.font.Font ("ARCADEGAMER.TTF", 20)
    font30 = pygame.font.Font ("ARCADEGAMER.TTF", 30)
    font50 = pygame.font.Font ("ARCADEGAMER.TTF", 50)

    # Number of power-ups of user
    powerup1_quantity = 0
    powerup2_quantity = 0
    powerup3_quantity = 0
    powerup4_quantity = 0
    powerup5_quantity = 0

    # (x, y) coordinates to draw text when game is running
    guess_y_pos = 125
    guess_x_pos = 90
    guess_y_inc = 65
    circle_y_inc = 65

    # Variables to store user input mid game
    player_guess = [[" ", " ", " ", " "], [" ", " ", " ", " "],
                    [" ", " ", " ", " "], [" ", " ", " ", " "],
                    [" ", " ", " ", " "], [" ", " ", " ", " "],
                    [" ", " ", " ", " "], [" ", " ", " ", " "],
                    [" ", " ", " ", " "], [" ", " ", " ", " "]]

    total_pegs = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0],
                  [0, 0], [0, 0], [0, 0]]
    current_line = 0
    guess_index = -1
    game_end_timer = 0

    generated_code = ""

    # Colours
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GOLD = (255, 215, 0)
    SILVER = (192, 192, 192)
    BRONZE = (205, 127, 50)
    GREEN = (0, 255, 0)

    # Sound effects
    mouse_click = pygame.mixer.Sound ("mouse_click.mp3")
    exit_sound = pygame.mixer.Sound ("exit_sound.mp3")
    money_sound = pygame.mixer.Sound ("money_sound.mp3")
    broke_sound = pygame.mixer.Sound ("broke_sound.mp3")
    tada_sound = pygame.mixer.Sound ("tada_sound.mp3")
    keyboard_click = pygame.mixer.Sound ("keyboard_click.mp3")
    powerup_sound = pygame.mixer.Sound ("powerup_sound.mp3")
    win_sound = pygame.mixer.Sound ("win_sound.mp3")
    lose_sound = pygame.mixer.Sound ("lose_sound.mp3")
    ding_sound = pygame.mixer.Sound ("ding_sound.mp3")
    wrong_sound = pygame.mixer.Sound ("wrong_sound.mp3")

    # Images/Buttons
    background = pygame.image.load ("bg.png")
    background = pygame.transform.scale (background, (800, 800))

    board_img = pygame.image.load ("board_10.png")
    board_10 = pygame.transform.scale (board_img, (800, 800))

    board_power_img = pygame.image.load ("board_11.png")
    board_11 = pygame.transform.scale (board_power_img, (800, 800))

    input_box = pygame.Surface ((650, 70))
    input_box.fill ((0, 0, 0))
    input_rect = input_box.get_rect ()
    input_rect.center = (400, 410)

    easy_img = pygame.image.load ("easy.png")
    easy_button = Button (210, -3, easy_img, 1.70)

    medium_img = pygame.image.load ("medium.png")
    medium_button = Button (220, 330, medium_img, 1.75)

    hard_img = pygame.image.load ("hard.png")
    hard_button = Button (220, 635, hard_img, 1.74)

    brick_img = pygame.image.load ("brick.png")
    brick_img = pygame.transform.scale (brick_img, (800, 800))

    winner_img = pygame.image.load ("winner.png")
    winner_img = pygame.transform.scale (winner_img, (800, 800))

    loser_img = pygame.image.load ("loser.png")
    loser_img = pygame.transform.scale (loser_img, (800, 800))

    start_img = pygame.image.load ("start.png")
    start_button = Button (210, 200, start_img, 1.50)

    rules_img = pygame.image.load ("rules.png").convert_alpha ()
    rules_button = Button (20, 390, rules_img, 0.9)

    leaderboard_img = pygame.image.load ("leaderboard.png").convert_alpha ()

    close_img = pygame.image.load ("close.png").convert_alpha ()
    close_button = Button (740, -3, close_img, 0.2)

    selection_img = pygame.image.load \
        ("powerup_selection.png").convert_alpha ()

    guide_img = pygame.image.load ("guide.png").convert_alpha ()

    user_info = pygame.image.load ("user_info.png").convert_alpha ()

    store_menu = pygame.image.load ("store_menu.png").convert_alpha ()

    purchase_button_img = pygame.image.load ("purchase_button.png").\
        convert_alpha ()

    enter_name_img = pygame.image.load ("enter_name.png").convert_alpha ()

    submit_img = pygame.image.load ("submit_button.png")
    submit_button = Button (670, 390, submit_img, 0.3)

    store_img = pygame.image.load ("store.png").convert_alpha ()
    store_button = Button (420, 390, store_img, 0.93)

    user_img = pygame.image.load ("user.png").convert_alpha ()
    user_button = Button (20, 569, user_img, 0.92)

    rankings_img = pygame.image.load ("rankings.png").convert_alpha ()
    rankings_button = Button (420, 570, rankings_img, 0.94)

    exclamation_mark = pygame.image.load ("!.png")
    exclamation_button = Button (574, 48, exclamation_mark, 0.8)

    at = pygame.image.load ("@.png")
    at_button = Button (674, 48, at, 0.8)

    ampersand = pygame.image.load ("&.png")
    ampersand_button = Button (574, 148, ampersand, 0.8)

    percent = pygame.image.load ("%.png")
    percent_button = Button (674, 148, percent, 0.8)

    dollar = pygame.image.load ("$.png")
    dollar_button = Button (574, 248, dollar, 0.8)

    hashtag = pygame.image.load ("#.png")
    hashtag_button = Button (674, 248, hashtag, 0.9)

    slash = pygame.image.load ("slash.png")
    slash_button = Button (574, 348, slash, 0.8)

    question_mark = pygame.image.load ("question.png")
    question_button = Button (674, 348, question_mark, 0.8)

    enter_img = pygame.image.load ("enter.png")
    enter_button = Button (586, 470, enter_img, 0.8)

    delete_img = pygame.image.load ("delete.png")
    delete_button = Button (600, 620, delete_img, 0.8)

    continue_img = pygame.image.load ("continue.png")
    continue_button = Button (670, 690, continue_img, 0.3)

    winscreen_continue_img = pygame.image.load ("name_button.png")
    winscreen_button = Button (550, 390, winscreen_continue_img, 0.3)

    game_win_button = Button (50, 390, winscreen_continue_img, 0.3)

    challenges_img = pygame.image.load ("challenges.png")

    purchase_button1 = Button (57, 150, purchase_button_img, 0.35)
    purchase_button2 = Button (57, 260, purchase_button_img, 0.35)
    purchase_button3 = Button (57, 360, purchase_button_img, 0.35)
    purchase_button4 = Button (57, 480, purchase_button_img, 0.35)
    purchase_button5 = Button (57, 590, purchase_button_img, 0.35)

    use_button1 = Button (57, 150, purchase_button_img, 0.35)
    use_button2 = Button (57, 260, purchase_button_img, 0.35)
    use_button3 = Button (57, 360, purchase_button_img, 0.35)
    use_button4 = Button (57, 480, purchase_button_img, 0.35)
    use_button5 = Button (57, 590, purchase_button_img, 0.35)

    # Variables pre-set for user to change in-game
    winstreak = 0
    max_guesses = 10
    win = ""
    leaderboard_name = ""
    mode = ""

    # Class instance
    player = Player ()

    # Inputs leaderboard text file to store players' scores
    leaderboard_file_name = "leaderboard.txt"
    leaderboard = Leaderboard (leaderboard_file_name)

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #


    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    # ~ Main Code ~ #

    while (run):

        # If player clicks on the "RULES" button
        if (rules == True):
            screen.blit (brick_img, (0, 0))
            screen.blit (guide_img, (0, 0))

            # Exit screen
            if (close_button.draw (screen)):
                exit_sound.play ()
                rules = False

        # If player clicks on the "USER" button
        elif (user == True):
            screen.blit (user_info, (0, 0))
            sentence_components = []

            # Breaks the challenge sentences into smaller parts
            # Allows long sentences to be drawn without going over the border
            for challenge in player.selected_challenges:

                words_index_list = []
                temp_slash_list = []

                # Finds all slash positions of the sentence and stores in list
                for i in range (len (challenge)):
                    if (challenge[i] == "/"):
                        temp_slash_list.append (i)

                # Calculates the words in-between each slash and stores in a
                # list
                for j in range (0, len (temp_slash_list)):

                    if (j == 0):
                        slash_position_1 = challenge[:temp_slash_list[j]]
                        words_index_list.append (slash_position_1)

                        if (len (temp_slash_list) == 1):
                            slash_position_2 = challenge[temp_slash_list
                                                         [j] + 1:]
                            words_index_list.append (slash_position_2)

                    elif (j == (len (temp_slash_list) - 1)):
                        slash_position_1 = challenge[temp_slash_list[j - 1] +
                                                     1:temp_slash_list[j]]
                        slash_position_2 = challenge[temp_slash_list[j] + 1:]
                        words_index_list.append (slash_position_1)
                        words_index_list.append (slash_position_2)

                    else:
                        slash_position_1 = challenge[temp_slash_list[j - 1] +
                                                     1:temp_slash_list[j]]
                        words_index_list.append (slash_position_1)

                # Stores list of sentence components into a final list
                sentence_components.append (words_index_list)
                current_x = 200

                # Draws the different sentences into the screen
                for words in sentence_components:
                    for i in range (len (words)):
                        draw_text (words[i], font20, WHITE, 40, current_x)
                        current_x += 25
                    current_x += 50

            # Draws players information onto the screen
            draw_text (str (player.balance), font30, WHITE, 610, 700)
            draw_text (str (winstreak), font30, WHITE, 200, 700)

            draw_text (str (powerup1_quantity), font20, WHITE, 725, 225)
            draw_text (str (powerup2_quantity), font20, WHITE, 725, 305)
            draw_text (str (powerup3_quantity), font20, WHITE, 725, 395)
            draw_text (str (powerup4_quantity), font20, WHITE, 725, 495)
            draw_text (str (powerup5_quantity), font20, WHITE, 725, 570)

            # Exit screen
            if (close_button.draw (screen)):
                exit_sound.play ()
                user = False
        # If player clicks on the "RANKINGS" button
        elif (rankings == True):
            screen.blit (leaderboard_img, (0, 0))
            screen.blit (leaderboard_img, (0, 0))
            current_stats = leaderboard.get_stats ()

            if (len (current_stats) == 0):
                draw_text ("NO NAMES", font50, WHITE, 200, 350)

            else:
                recursive_stat_print (current_stats, 120, 170, 1)

            # Exit screen
            if (close_button.draw (screen)):
                exit_sound.play ()
                rankings = False

        # If player clicks on the "START" button
        elif (start == True):
            screen.blit (brick_img, (0, 0))

            # Easy Mode
            if (easy_button.draw (screen)):
                mouse_click.play ()
                easy_state = True
                medium_state = False
                hard_state = False

            # Medium Mode
            if (medium_button.draw (screen)):
                mouse_click.play ()
                medium_state = True
                easy_state = False
                hard_state = False

            # Hard Mode
            if (hard_button.draw (screen)):
                mouse_click.play ()
                hard_state = True
                easy_state = False
                medium_state = False

            # Exit screen
            if (close_button.draw (screen)):
                exit_sound.play ()
                start = False
                easy_state = False
                medium_state = False
                hard_state = False
                powerup_state = False

            # Easy screen
            if (easy_state == True):
                begin_time = time.time ()
                mode = "Easy"

                if (len (player.inventory) > 0):
                    # Use power-up screen
                    screen.blit (selection_img, (0, 0))
                    draw_text (str (powerup1_quantity), font30, WHITE, 650, 170)
                    draw_text (str (powerup2_quantity), font30, WHITE, 650, 270)
                    draw_text (str (powerup3_quantity), font30, WHITE, 650, 370)
                    draw_text (str (powerup4_quantity), font30, WHITE, 650, 490)
                    draw_text (str (powerup5_quantity), font30, WHITE, 650, 600)

                    if (continue_button.draw (screen)):
                        game_start = True
                        easy_state = False
                        medium_state = False
                        hard_state = False
                        start = False

                        generated_code = generate_code (6)

                        for i in range (len (generated_code)):
                            array_code.append (generated_code[i])

                    # Use power-up 1
                    if (use_button1.draw (screen)):
                        if (powerup1_quantity > 0):
                            powerup_sound.play ()
                            powerup1_quantity -= 1
                            remove_from_inventory (
                                player.inventory, "Reveal 1 character "
                                                 "and its placement")

                            select_power_1 = True
                            game_start = True
                            easy_state = False
                            medium_state = False
                            hard_state = False
                            start = False

                            generated_code = generate_code (6)

                            for i in range (len (generated_code)):
                                array_code.append (generated_code[i])

                            hint_p1 = powerup_1 (generated_code)

                            char_pos = []
                            reveal = ""

                            for i in hint_p1:
                                if (i != " "):
                                    char_pos.append (i)

                            for i in char_pos:
                                if (i != "_"):
                                    reveal = i

                            circle_spot = char_pos.index (reveal)

                            hint_p1 = "HINT: " + str (hint_p1)

                        else:
                            powerup_state = True
                            # Bool to indicate if user is still in power-up
                            # screen

                    # Use power-up 2
                    if (use_button2.draw (screen)):
                        powerup_sound.play ()

                        if (powerup2_quantity > 0):
                            powerup2_quantity -= 1
                            remove_from_inventory (
                                player.inventory, "Reveal 2 characters and "
                                                 "their placements")

                            select_power_2 = True
                            game_start = True
                            easy_state = False
                            medium_state = False
                            hard_state = False
                            start = False

                            generated_code = generate_code (6)

                            for i in range (len (generated_code)):
                                array_code.append (generated_code[i])

                            hint_p2 = powerup_2 (generated_code)

                            char_pos = []
                            both_char = []
                            reveal1 = ""
                            reveal2 = ""

                            for i in hint_p2:
                                if (i != " "):
                                    char_pos.append (i)

                            for i in char_pos:
                                if (i != "_"):
                                    both_char.append (i)

                            for i in char_pos:
                                if (both_char[0] == i):
                                    reveal1 = i
                                if (both_char[1] == i):
                                    reveal2 = i
                                    while (reveal2 == reveal1):
                                        reveal2 = i

                            circle_spot1 = char_pos.index (reveal1)
                            circle_spot2 = char_pos.index (reveal2)

                            hint_p2 = "HINT: " + str (hint_p2)
                        else:
                            powerup_state = True

                    # Use power-up 3
                    if (use_button3.draw (screen)):
                        if (powerup3_quantity > 0):
                            powerup_sound.play ()
                            powerup3_quantity -= 1
                            remove_from_inventory (player.inventory,
                                                  "Reveal 1 character without"
                                                  " its placement")

                            select_power_3 = True
                            game_start = True
                            easy_state = False
                            medium_state = False
                            hard_state = False
                            start = False

                            generated_code = generate_code (6)

                            for i in range (len (generated_code)):
                                array_code.append (generated_code[i])

                            hint_p3 = powerup_3 (generated_code)
                            hint_p3 = "HINT: " + str (hint_p3)
                        else:
                            powerup_state = True

                    # Use power-up 4
                    if (use_button4.draw (screen)):
                        if (powerup4_quantity > 0):
                            powerup_sound.play ()
                            powerup4_quantity -= 1
                            remove_from_inventory (player.inventory,
                                                  "Reveal all 4 characters "
                                                  "without their placements")

                            select_power_4 = True
                            game_start = True
                            easy_state = False
                            medium_state = False
                            hard_state = False
                            start = False

                            generated_code = generate_code (6)

                            for i in range (len (generated_code)):
                                array_code.append (generated_code[i])

                            hint_p4 = powerup_4 (generated_code)
                            hint_p4 = "HINT: " + str (hint_p4)
                        else:
                            powerup_state = True

                    # Use power-up 5
                    if (use_button5.draw (screen)):
                        if (powerup5_quantity > 0):
                            powerup_sound.play ()
                            powerup5_quantity -= 1
                            remove_from_inventory (player.inventory,
                                                  "Get an extra guess")

                            select_power_5 = True

                            # Sets player guess stats to 11
                            player_guess = [[" ", " ", " ", " "],
                                            [" ", " ", " ", " "],
                                            [" ", " ", " ", " "],
                                            [" ", " ", " ", " "],
                                            [" ", " ", " ", " "],
                                            [" ", " ", " ", " "],
                                            [" ", " ", " ", " "],
                                            [" ", " ", " ", " "],
                                            [" ", " ", " ", " "],
                                            [" ", " ", " ", " "],
                                            [" ", " ", " ", " "]]
                            total_pegs = [[0, 0], [0, 0], [0, 0], [0, 0],
                                          [0, 0], [0, 0], [0, 0], [0, 0],
                                          [0, 0], [0, 0], [0, 0]]
                            max_guesses = 11

                            game_start = True
                            easy_state = False
                            medium_state = False
                            hard_state = False
                            start = False

                            generated_code = generate_code (6)

                            for i in range (len (generated_code)):
                                array_code.append (generated_code[i])
                        else:
                            powerup_state = True

                    # Exit screen
                    if (close_button.draw (screen)):
                        exit_sound.play ()
                        easy_state = False
                        start = False
                        powerup_state = False
                else:
                    game_start = True
                    easy_state = False
                    medium_state = False
                    hard_state = False
                    start = False
                    generated_code = generate_code (6)

                    for i in range (len (generated_code)):
                        array_code.append (generated_code[i])

            # Medium screen
            elif (medium_state == True):
                begin_time = time.time ()
                med_extra = True
                mode = "Medium"

                # Same design as easy screen but different generated code
                if (len (player.inventory) > 0):
                    screen.blit (selection_img, (0, 0))
                    draw_text (str (powerup1_quantity), font30, WHITE, 650, 170)
                    draw_text (str (powerup2_quantity), font30, WHITE, 650, 270)
                    draw_text (str (powerup3_quantity), font30, WHITE, 650, 370)
                    draw_text (str (powerup4_quantity), font30, WHITE, 650, 490)
                    draw_text (str (powerup5_quantity), font30, WHITE, 650, 600)

                    if (continue_button.draw (screen)):
                        game_start = True
                        easy_state = False
                        medium_state = False
                        hard_state = False
                        start = False

                        generated_code = generate_code (7)

                        for i in range (len (generated_code)):
                            array_code.append (generated_code[i])

                    if (use_button1.draw (screen)):
                        if (powerup1_quantity > 0):
                            powerup_sound.play ()
                            powerup1_quantity -= 1
                            remove_from_inventory (player.inventory,
                                                  "Reveal 1 character and its"
                                                  " placement")

                            select_power_1 = True
                            game_start = True
                            easy_state = False
                            medium_state = False
                            hard_state = False
                            start = False

                            generated_code = generate_code (7)

                            for i in range (len (generated_code)):
                                array_code.append (generated_code[i])

                            hint_p1 = powerup_1 (generated_code)

                            char_pos = []
                            reveal = ""

                            for i in hint_p1:
                                if (i != " "):
                                    char_pos.append (i)

                            for i in char_pos:
                                if (i != "_"):
                                    reveal = i

                            circle_spot = char_pos.index (reveal)

                            hint_p1 = "HINT: " + str (hint_p1)
                        else:
                            powerup_state = True

                    if (use_button2.draw (screen)):
                        if (powerup2_quantity > 0):
                            powerup_sound.play ()
                            powerup2_quantity -= 1
                            remove_from_inventory (player.inventory,
                                                  "Reveal 2 characters and "
                                                  "their placements")

                            select_power_2 = True
                            game_start = True
                            easy_state = False
                            medium_state = False
                            hard_state = False
                            start = False

                            generated_code = generate_code (7)

                            for i in range (len (generated_code)):
                                array_code.append (generated_code[i])

                            hint_p2 = powerup_2 (generated_code)

                            char_pos = []
                            both_char = []
                            reveal1 = ""
                            reveal2 = ""

                            for i in hint_p2:
                                if (i != " "):
                                    char_pos.append (i)

                            for i in char_pos:
                                if (i != "_"):
                                    both_char.append (i)

                            for i in char_pos:
                                if (both_char[0] == i):
                                    reveal1 = i
                                if (both_char[1] == i):
                                    reveal2 = i
                                    while (reveal2 == reveal1):
                                        reveal2 = i

                            circle_spot1 = char_pos.index (reveal1)
                            circle_spot2 = char_pos.index (reveal2)

                            hint_p2 = "HINT: " + str (hint_p2)
                        else:
                            powerup_state = True

                    if (use_button3.draw (screen)):
                        if (powerup3_quantity > 0):
                            powerup_sound.play ()
                            powerup3_quantity -= 1
                            remove_from_inventory (player.inventory,
                                                  "Reveal 1 character without "
                                                  "its placement")

                            select_power_3 = True
                            game_start = True
                            easy_state = False
                            medium_state = False
                            hard_state = False
                            start = False

                            generated_code = generate_code (7)

                            for i in range (len (generated_code)):
                                array_code.append (generated_code[i])

                            hint_p3 = powerup_3 (generated_code)
                            hint_p3 = "HINT: " + str (hint_p3)
                        else:
                            powerup_state = True

                    if (use_button4.draw (screen)):
                        powerup_sound.play ()

                        if (powerup4_quantity > 0):
                            powerup4_quantity -= 1
                            remove_from_inventory (player.inventory,
                                                  "Reveal all 4 characters "
                                                  "without their placements")

                            select_power_4 = True
                            game_start = True
                            easy_state = False
                            medium_state = False
                            hard_state = False
                            start = False

                            generated_code = generate_code (7)

                            for i in range (len (generated_code)):
                                array_code.append (generated_code[i])

                            hint_p4 = powerup_4 (generated_code)
                            hint_p4 = "HINT: " + str (hint_p4)
                        else:
                            powerup_state = True

                    if (use_button5.draw (screen)):
                        powerup_sound.play ()

                        if (powerup5_quantity > 0):
                            powerup5_quantity -= 1
                            remove_from_inventory (player.inventory,
                                                  "Get an extra guess")

                            select_power_5 = True

                            player_guess = [[" ", " ", " ", " "],
                                            [" ", " ", " ", " "],
                                            [" ", " ", " ", " "],
                                            [" ", " ", " ", " "],
                                            [" ", " ", " ", " "],
                                            [" ", " ", " ", " "],
                                            [" ", " ", " ", " "],
                                            [" ", " ", " ", " "],
                                            [" ", " ", " ", " "],
                                            [" ", " ", " ", " "],
                                            [" ", " ", " ", " "]]
                            total_pegs = [[0, 0], [0, 0], [0, 0], [0, 0],
                                          [0, 0], [0, 0], [0, 0], [0, 0],
                                          [0, 0], [0, 0], [0, 0]]
                            max_guesses = 11

                            game_start = True
                            easy_state = False
                            medium_state = False
                            hard_state = False
                            start = False

                            generated_code = generate_code (7)

                            for i in range (len (generated_code)):
                                array_code.append (generated_code[i])
                        else:
                            powerup_state = True

                    # Exit screen
                    if (close_button.draw (screen)):
                        exit_sound.play ()
                        medium_state = False
                        start = False
                        powerup_state = False

                else:
                    game_start = True
                    easy_state = False
                    medium_state = False
                    hard_state = False
                    start = False

                    generated_code = generate_code (7)

                    for i in range (len (generated_code)):
                        array_code.append (generated_code[i])

            # Hard screen
            elif (hard_state == True):
                begin_time = time.time ()
                hard_extra = True
                mode = "Hard"

                if (len (player.inventory) > 0):
                    screen.blit (selection_img, (0, 0))
                    draw_text (str (powerup1_quantity), font30, WHITE, 650, 170)
                    draw_text (str (powerup2_quantity), font30, WHITE, 650, 270)
                    draw_text (str (powerup3_quantity), font30, WHITE, 650, 370)
                    draw_text (str (powerup4_quantity), font30, WHITE, 650, 490)
                    draw_text (str (powerup5_quantity), font30, WHITE, 650, 600)

                    if (continue_button.draw (screen)):
                        game_start = True
                        easy_state = False
                        medium_state = False
                        hard_state = False
                        start = False

                        generated_code = generate_code (8)

                        for i in range (len (generated_code)):
                            array_code.append (generated_code[i])

                    if (use_button1.draw (screen)):
                        if (powerup1_quantity > 0):
                            powerup_sound.play ()
                            powerup1_quantity -= 1
                            remove_from_inventory (player.inventory,
                                                  "Reveal 1 character and its"
                                                  " placement")

                            select_power_1 = True
                            game_start = True
                            easy_state = False
                            medium_state = False
                            hard_state = False
                            start = False

                            generated_code = generate_code (8)

                            for i in range (len (generated_code)):
                                array_code.append (generated_code[i])

                            hint_p1 = powerup_1 (generated_code)

                            char_pos = []
                            reveal = ""

                            for i in hint_p1:
                                if (i != " "):
                                    char_pos.append (i)

                            for i in char_pos:
                                if (i != "_"):
                                    reveal = i

                            circle_spot = char_pos.index (reveal)

                            hint_p1 = "HINT: " + str (hint_p1)
                        else:
                            powerup_state = True

                    if (use_button2.draw (screen)):
                        if (powerup2_quantity > 0):
                            powerup_sound.play ()
                            powerup2_quantity -= 1
                            remove_from_inventory (player.inventory,
                                                  "Reveal 2 characters and "
                                                  "their placements")

                            select_power_2 = True
                            game_start = True
                            easy_state = False
                            medium_state = False
                            hard_state = False
                            start = False

                            generated_code = generate_code (8)

                            for i in range (len (generated_code)):
                                array_code.append (generated_code[i])

                            hint_p2 = powerup_2 (generated_code)

                            char_pos = []
                            both_char = []
                            reveal1 = ""
                            reveal2 = ""

                            for i in hint_p2:
                                if (i != " "):
                                    char_pos.append (i)

                            for i in char_pos:
                                if (i != "_"):
                                    both_char.append (i)

                            for i in char_pos:
                                if (both_char[0] == i):
                                    reveal1 = i
                                if (both_char[1] == i):
                                    reveal2 = i
                                    while (reveal2 == reveal1):
                                        reveal2 = i

                            circle_spot1 = char_pos.index (reveal1)
                            circle_spot2 = char_pos.index (reveal2)

                            hint_p2 = "HINT: " + str (hint_p2)
                        else:
                            powerup_state = True

                    if (use_button3.draw (screen)):
                        if (powerup3_quantity > 0):
                            powerup_sound.play ()
                            powerup3_quantity -= 1
                            remove_from_inventory (player.inventory,
                                                  "Reveal 1 character without "
                                                  "its placement")

                            select_power_3 = True
                            game_start = True
                            easy_state = False
                            medium_state = False
                            hard_state = False
                            start = False

                            generated_code = generate_code (8)

                            for i in range (len (generated_code)):
                                array_code.append (generated_code[i])

                            hint_p3 = powerup_3 (generated_code)
                            hint_p3 = "HINT: " + str (hint_p3)
                        else:
                            powerup_state = True

                    if (use_button4.draw (screen)):
                        if (powerup4_quantity > 0):
                            powerup_sound.play ()
                            powerup4_quantity -= 1
                            remove_from_inventory (player.inventory,
                                                  "Reveal all 4 characters "
                                                  "without their placements")

                            select_power_4 = True
                            game_start = True
                            easy_state = False
                            medium_state = False
                            hard_state = False
                            start = False

                            generated_code = generate_code (8)

                            for i in range (len (generated_code)):
                                array_code.append (generated_code[i])

                            hint_p4 = powerup_4 (generated_code)
                            hint_p4 = "HINT: " + str (hint_p4)
                        else:
                            powerup_state = True

                    if (use_button5.draw (screen)):
                        if (powerup5_quantity > 0):
                            powerup_sound.play ()
                            powerup5_quantity -= 1
                            remove_from_inventory (player.inventory,
                                                  "Get an extra guess")

                            select_power_5 = True

                            player_guess = [[" ", " ", " ", " "],
                                            [" ", " ", " ", " "],
                                            [" ", " ", " ", " "],
                                            [" ", " ", " ", " "],
                                            [" ", " ", " ", " "],
                                            [" ", " ", " ", " "],
                                            [" ", " ", " ", " "],
                                            [" ", " ", " ", " "],
                                            [" ", " ", " ", " "],
                                            [" ", " ", " ", " "],
                                            [" ", " ", " ", " "]]
                            total_pegs = [[0, 0], [0, 0], [0, 0], [0, 0],
                                          [0, 0], [0, 0], [0, 0], [0, 0],
                                          [0, 0], [0, 0], [0, 0]]
                            max_guesses = 11

                            game_start = True
                            easy_state = False
                            medium_state = False
                            hard_state = False
                            start = False

                            generated_code = generate_code (8)

                            for i in range (len (generated_code)):
                                array_code.append (generated_code[i])
                        else:
                            powerup_state = True

                    # Exit screen
                    if (close_button.draw (screen)):
                        exit_sound.play ()
                        hard_state = False
                        start = False
                        powerup_state = False

                else:
                    game_start = True
                    easy_state = False
                    medium_state = False
                    hard_state = False
                    start = False

                    generated_code = generate_code (8)

                    for i in range (len (generated_code)):
                        array_code.append (generated_code[i])

            if (powerup_state == True):
                draw_text ("Power-up Unavailable!", font20, WHITE, 25, 700)

        # Game boards appears
        elif (game_start == True):

            # Power-up 5 (extra guess) is activated
            # Game board with 11 guesses appears
            if (select_power_5):
                guess_y_pos = 95
                guess_y_inc = 64.5
                circle_y = 105
                circle_y_inc = 64.5

                screen.blit (board_11, (0, 0))
            # Game board with 10 guesses appears
            else:
                circle_y = 137
                guess_y_pos = 125
                screen.blit (board_10, (0, 0))

            # In-game timer
            start_time = time.time () - begin_time
            draw_text (str (round (start_time, 1)), font20, WHITE, 390, 40)

            # Activates power-up #1 (Reveal 1 character and its placement)
            if (select_power_1 == True):
                draw_text (hint_p1, font15, WHITE, 570, 730)
                if (circle_spot == 0):
                    draw_text (reveal, font20, WHITE, 55, 40)
                elif (circle_spot == 1):
                    draw_text (reveal, font20, WHITE, 138, 40)
                elif (circle_spot == 2):
                    draw_text (reveal, font20, WHITE, 221, 40)
                elif (circle_spot == 3):
                    draw_text (reveal, font20, WHITE, 304, 40)

            # Activates power-up #2 (Reveal 2 characters and their placements)
            if (select_power_2 == True):
                draw_text (hint_p2, font15, WHITE, 570, 730)
                if (circle_spot1 == 0):
                    draw_text (reveal1, font20, WHITE, 55, 40)
                elif (circle_spot1 == 1):
                    draw_text (reveal1, font20, WHITE, 138, 40)
                elif (circle_spot1 == 2):
                    draw_text (reveal1, font20, WHITE, 221, 40)
                elif (circle_spot1 == 3):
                    draw_text (reveal1, font20, WHITE, 304, 40)
                if (circle_spot2 == 0):
                    draw_text (reveal2, font20, WHITE, 55, 40)
                elif (circle_spot2 == 1):
                    draw_text (reveal2, font20, WHITE, 138, 40)
                elif (circle_spot2 == 2):
                    draw_text (reveal2, font20, WHITE, 221, 40)
                elif (circle_spot2 == 3):
                    draw_text (reveal2, font20, WHITE, 304, 40)

            # Activates power-up #3 (Reveal 1 character without its placement)
            if (select_power_3 == True):
                draw_text (hint_p3, font15, WHITE, 570, 730)

            # Activates power-up #4 (Reveal all 4 characters without their
            # placements)
            if (select_power_4 == True):
                draw_text (hint_p4, font15, WHITE, 570, 730)

            # Writes player guesses in black circles
            for set in player_guess:
                guess_x_pos = 90

                for value in set:
                    draw_text (value, font20, GOLD, guess_x_pos, guess_y_pos)
                    guess_x_pos += 70

                guess_y_pos += guess_y_inc

            # Draws green or yellow circle when a guess is entered
            for set in total_pegs:
                circle_x = 365

                for i in range (2):
                    current_peg = set[i]

                    for j in range (0, int (current_peg)):
                        if (i == 0):
                            pygame.draw.circle (screen,
                                               GREEN, (circle_x, circle_y), 14)
                            circle_x += 42
                        if (i == 1):
                            pygame.draw.circle (screen,
                                               GOLD, (circle_x, circle_y), 14)
                            circle_x += 42

                circle_y += circle_y_inc

            # Writes the correct code in the grey circles once the game ends.
            if (game_end == True):
                final_x_pos = 55

                for i in generated_code:
                    draw_text (i, font20, WHITE, final_x_pos, 40)
                    final_x_pos += 83

            # Allows user to see board for two seconds once they complete
            # win or lose
            if (((time.time () - game_end_timer) > 0.1) and
                    (game_end_timer != 0)):

                pygame.time.delay (2000)

                game_start = True
                game_end = True

                # User wins and they gain money for winning or completing
                # challenges
                if (to_win):
                    win = True
                    win_screen = True
                    winstreak += 1

                    if (mode == "Easy"):
                        player.add_balance (100)

                    elif (mode == "Medium"):
                        player.add_balance (300)

                    elif (mode == "Hard"):
                        player.add_balance (500)

                    if (player.challenges[0] in player.selected_challenges):
                        if (current_line <= 5):
                            player.add_balance (player.rewards[0])

                    if (player.challenges[1] in player.selected_challenges):
                        if (current_line <= 7):
                            player.add_balance (player.rewards[1])

                    if (player.challenges[2] in player.selected_challenges):
                        if (current_line <= 9):
                            player.add_balance (player.rewards[2])

                    if (player.challenges[3] in player.selected_challenges):
                        if (winstreak % 2 == 0):
                            player.add_balance (player.rewards[3])

                    if (player.challenges[4] in player.selected_challenges):
                        if (winstreak % 3 == 0):
                            player.add_balance (player.rewards[4])

                    if (player.challenges[5] in player.selected_challenges):
                        if (start_time <= 60):
                            player.add_balance (player.rewards[5])

                    if (player.challenges[6] in player.selected_challenges):
                        if (start_time <= 120):
                            player.add_balance (player.rewards[6])

                    if (player.challenges[7] in player.selected_challenges):
                        if (start_time <= 180):
                            player.add_balance (player.rewards[7])

                # User loses
                if (to_lose):
                    win = False
                    win_screen = False
                    winstreak = 0

            # Displays character buttons for easy by default
            if ((exclamation_button.draw (screen)) and (guess_index < 3)):
                    keyboard_click.play ()
                    guess_index += 1
                    player_guess[current_line][guess_index] = "!"

            if ((at_button.draw (screen)) and (guess_index < 3)):
                keyboard_click.play ()
                guess_index += 1
                player_guess[current_line][guess_index] = "@"

            if ((ampersand_button.draw (screen)) and (guess_index < 3)):
                keyboard_click.play ()
                guess_index += 1
                player_guess[current_line][guess_index] = "&"

            if ((hashtag_button.draw (screen)) and (guess_index < 3)):
                keyboard_click.play ()
                guess_index += 1
                player_guess[current_line][guess_index] = "#"

            if ((percent_button.draw (screen)) and (guess_index < 3)):
                keyboard_click.play ()
                guess_index += 1
                player_guess[current_line][guess_index] = "%"

            if ((dollar_button.draw (screen)) and (guess_index < 3)):
                keyboard_click.play ()
                guess_index += 1
                player_guess[current_line][guess_index] = "$"

            # Unlocks and displays additional character buttons for medium
            if ((med_extra) and (not hard_extra)):
                if ((slash_button.draw (screen)) and (guess_index < 3)):
                    keyboard_click.play ()
                    guess_index += 1
                    player_guess[current_line][guess_index] = "/"

            # Unlocks and displays characters buttons for hard
            elif (hard_extra):
                if ((slash_button.draw (screen)) and (guess_index < 3)):
                    keyboard_click.play ()
                    guess_index += 1
                    player_guess[current_line][guess_index] = "/"

                if ((question_button.draw (screen)) and (guess_index < 3)):
                    keyboard_click.play ()
                    guess_index += 1
                    player_guess[current_line][guess_index] = "?"

            # Backspace button
            if (delete_button.draw (screen)):
                keyboard_click.play ()

                if (guess_index > 3):
                    guess_index = 2

                player_guess[current_line][guess_index] = " "
                guess_index -= 1

                if (guess_index == -2):
                    guess_index = -1

            # Enter button to enter score
            if ((enter_button.draw (screen)) and (guess_index == 3)):
                keyboard_click.play ()
                guess_index = -1
                peg_results = assess_guess (array_code,
                                           player_guess[current_line])
                total_pegs[current_line] = peg_results
                current_line += 1

                # Sets variables once game is completed and time is recorded
                if ((current_line == max_guesses) or (peg_results[0] == 4)):
                    game_end_timer = time.time ()
                    easy_state = False
                    medium_state = False
                    hard_state = False
                    start = False
                    powerup_state = False
                    store = False
                    to_win = True
                    game_start = True
                    game_end = True

                # Plays sound once user wins
                if (peg_results[0] == 4):
                    win = True
                    ding_sound.play ()

                # Sets variables once player looses game and plays sound
                elif ((current_line == max_guesses) and
                      (not peg_results[0] == 4)):
                    wrong_sound.play ()

                    easy_state = False
                    medium_state = False
                    hard_state = False
                    start = False
                    powerup_state = False
                    store = False
                    to_lose = True
                    win = True

            # Displays winner screen
            if (win_screen == True):
                screen.blit (winner_img, (0, 0))
                draw_text (generated_code, font30, WHITE, 310, 275)
                draw_text (str (calculate_score (mode, current_line)),
                          font30, WHITE, 340, 445)

                if (game_end_timer != 0):
                    win_sound.play ()
                    new_min, new_sec = seconds_to_minutes (start_time)
                    game_end_timer = 0

                draw_text (str (new_min) + " Minutes", font20, WHITE, 290, 610)
                draw_text (str (new_sec) + "  Seconds", font20, WHITE, 290, 650)

                if (winscreen_button.draw (screen)):
                    win = ""
                    name = True

                # Displays screen to enter name to leaderboard
                if (name == True):
                    screen.blit (enter_name_img, (0, 0))
                    screen.blit (input_box, input_rect)
                    input_text = font30.render (leaderboard_name, True, WHITE)
                    input_text_rect = input_text.get_rect ()
                    input_text_rect.center = input_rect.center
                    screen.blit (input_text, input_text_rect)

                    # Obtains player name and score for leaderboard
                    if (event.type == pygame.K_RETURN):
                        leaderboard_score = str (calculate_score (mode,
                                                                current_line))
                        leaderboard.set_score (leaderboard_name,
                                              leaderboard_score)
                        name = False
                        challenges = True

                    # Displays challenges screen and tells user how much money
                    # they made from winning and completing challenges
                    if (challenges == True):
                        starting_y = 220
                        spacing_inc = 50
                        balance_sum = 0
                        screen.blit (challenges_img, (0, 0))

                        if (mode == "Easy"):
                            draw_text ("Victory Bonus: +100", font20,
                                      WHITE, 60, starting_y)
                            balance_sum += 100
                        elif (mode == "Medium"):
                            draw_text ("Victory Bonus: +300", font20,
                                      WHITE, 60, starting_y)
                            balance_sum += 300
                        elif (mode == "Hard"):
                            draw_text ("Victory Bonus: +500", font20,
                                      WHITE, 60, starting_y)
                            balance_sum += 500

                        if (player.challenges[0] in
                                player.selected_challenges):
                            if (current_line <= 5):
                                draw_text ("<= 5 Guesses: +300", font20,
                                          WHITE, 60, starting_y + spacing_inc)
                                starting_y += spacing_inc
                                balance_sum += 300

                        if (player.challenges[1] in
                                player.selected_challenges):
                            if (current_line <= 7):
                                draw_text ("<= 7 Guesses: +150", font20,
                                          WHITE, 60, starting_y + spacing_inc)
                                starting_y += spacing_inc
                                balance_sum += 150

                        if (player.challenges[2] in
                                player.selected_challenges):
                            if (current_line <= 9):
                                draw_text ("<= 9 Guesses: +50", font20,
                                          WHITE, 60, starting_y + spacing_inc)
                                starting_y += spacing_inc
                                balance_sum += 50

                        if (player.challenges[3] in
                                player.selected_challenges):
                            if (winstreak % 2 == 0):
                                draw_text ("2 Game Streak: +100", font20,
                                          WHITE, 60, starting_y + spacing_inc)
                                starting_y += spacing_inc
                                balance_sum += 100

                        if (player.challenges[4] in
                        player.selected_challenges):
                            if (winstreak % 3 == 0):
                                draw_text ("3 Game Streak: +200", font20,
                                          WHITE, 60, starting_y + spacing_inc)
                                starting_y += spacing_inc
                                balance_sum += 200

                        if (player.challenges [5] in
                                player.selected_challenges):
                            if (start_time <= 60):
                                draw_text ("Under 1 Minute: +400", font20,
                                          WHITE, 60, starting_y + spacing_inc)
                                starting_y += spacing_inc
                                balance_sum += 400

                        if (player.challenges [6] in
                                player.selected_challenges):
                            if (start_time <= 120):
                                draw_text ("Under 2 Minutes: +250", font20,
                                          WHITE, 60, starting_y + spacing_inc)
                                starting_y += spacing_inc
                                balance_sum += 250

                        if (player.challenges [7] in
                                player.selected_challenges):
                            if (start_time <= 180):
                                draw_text ("Under 3 Minutes: +100", font20,
                                          WHITE, 60, starting_y + spacing_inc)
                                starting_y += spacing_inc
                                balance_sum += 100

                        draw_text ("-----------------------", font20, WHITE,
                                  60, starting_y + spacing_inc)
                        starting_y += spacing_inc

                        draw_text (("Balance Earned: +" + str (balance_sum)),
                                  font20, WHITE, 60, starting_y + spacing_inc)
                        starting_y += spacing_inc

                        draw_text (("Total Balance: +" +
                                   str (player.show_balance ())), font20, WHITE,
                                  60, starting_y + spacing_inc)

                        # Exit screen
                        if (close_button.draw (screen)):
                            exit_sound.play ()
                            easy_state = False
                            med_extra = False
                            hard_extra = False
                            medium_state = False
                            hard_state = False
                            start = False
                            powerup_state = False
                            game_start = False
                            store = False
                            name = False
                            challenges = False

            # Displays screen if player loses game
            elif (win == False):
                if (game_end_timer != 0):
                    lose_sound.play ()
                    game_end_timer = 0
                screen.blit (loser_img, (0, 0))
                draw_text (generated_code, font30, WHITE, 280, 405)

                # Exit button
                if (close_button.draw (screen)):
                    exit_sound.play ()
                    easy_state = False
                    med_extra = False
                    hard_extra = False
                    medium_state = False
                    hard_state = False
                    start = False
                    powerup_state = False
                    game_start = False
                    store = False
                    name = False
                    challenges = False

        # Displays store
        elif (store == True):
            screen.blit (store_menu, (0, 0))
            draw_text (str (player.balance), font30, WHITE, 220, 710)

            # Player purchases power-ups
            if (purchase_button1.draw (screen)):
                if (player.balance >= player.powerup_prices[0]):
                    player.subtract_balance (player.powerup_prices[0])
                    player.add_inventory (0)
                    insufficient = True
                    money_sound.play ()
                    phrase = "Purchased: Power-up 1"
                    powerup1_quantity += 1

                else:
                    insufficient = True
                    broke_sound.play ()
                    phrase = "Insufficient Funds"

            if (purchase_button2.draw (screen)):
                if (player.balance >= player.powerup_prices[1]):
                    player.subtract_balance (player.powerup_prices[1])
                    player.add_inventory (1)
                    insufficient = True
                    money_sound.play ()
                    phrase = "Purchased: Power-up 2"
                    powerup2_quantity += 1

                else:
                    insufficient = True
                    broke_sound.play ()
                    phrase = "Insufficient Funds"

            if (purchase_button3.draw (screen)):
                if (player.balance >= player.powerup_prices[2]):
                    player.subtract_balance (player.powerup_prices[2])
                    player.add_inventory (2)
                    insufficient = True
                    money_sound.play ()
                    phrase = "Purchased: Power-up 3"
                    powerup3_quantity += 1

                else:
                    insufficient = True
                    broke_sound.play ()
                    phrase = "Insufficient Funds"

            if (purchase_button4.draw (screen)):
                if (player.balance >= player.powerup_prices[3]):
                    player.subtract_balance (player.powerup_prices[3])
                    player.add_inventory (3)
                    insufficient = True
                    money_sound.play ()
                    phrase = "Purchased: Power-up 4"
                    powerup4_quantity += 1

                else:
                    insufficient = True
                    broke_sound.play ()
                    phrase = "Insufficient Funds"

            if (purchase_button5.draw (screen)):
                if (player.balance >= player.powerup_prices[4]):
                    player.subtract_balance (player.powerup_prices[4])
                    player.add_inventory (4)
                    insufficient = True
                    money_sound.play ()
                    phrase = "Purchased: Power-up 5"
                    powerup5_quantity += 1

                else:
                    insufficient = True
                    broke_sound.play ()
                    phrase = "Insufficient Funds"

            # Exit button
            if (close_button.draw (screen)):
                exit_sound.play ()
                store = False
                insufficient = False

            if (insufficient == True):
                draw_text (phrase, font15, WHITE, 400, 700)

        else:
            # Sets variables at main screen
            game_start = False
            med_extra = False
            hard_extra = False
            medium_state = False
            hard_state = False

            select_power_1 = False
            select_power_2 = False
            select_power_3 = False
            select_power_4 = False
            select_power_5 = False

            to_win = False
            to_lose = False

            game_end = False
            win_screen = False
            name = False
            challenges = False

            player_guess = [[" ", " ", " ", " "], [" ", " ", " ", " "],
                            [" ", " ", " ", " "], [" ", " ", " ", " "],
                            [" ", " ", " ", " "], [" ", " ", " ", " "],
                            [" ", " ", " ", " "], [" ", " ", " ", " "],
                            [" ", " ", " ", " "], [" ", " ", " ", " "]]

            guess_index = -1
            guess_x_pos = 90
            guess_y_pos = 125

            starting_y = 0
            spacing_inc = 0

            balance_sum = 0

            circle_y_inc = 64.25

            win = ""
            game_end_timer = 0

            current_line = 0
            array_code = []
            generated_code = ""
            total_pegs = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0],
                          [0, 0], [0, 0], [0, 0], [0, 0]]
            max_guesses = 10

            screen.blit (background, (0, 0))

            # Buttons on the main screen
            if (start_button.draw (screen)):
                mouse_click.play ()
                start = True
            if (rules_button.draw (screen)):
                mouse_click.play ()
                rules = True
            if (store_button.draw (screen)):
                mouse_click.play ()
                store = True
            if (user_button.draw (screen)):
                mouse_click.play ()
                user = True
            if (rankings_button.draw (screen)):
                mouse_click.play ()
                tada_sound.play ()
                rankings = True

        for event in pygame.event.get ():
            # Closes window
            if (event.type == pygame.QUIT):
                run = False

            # Allows user to enter name for leaderboard
            elif (event.type == pygame.KEYDOWN):
                if (name == True):
                    if (event.unicode.isprintable ()):
                        if (len (leaderboard_name) <= 15):
                            leaderboard_name += event.unicode
                            keyboard_click.play ()

                    # Allows backspace to work when entering name
                    elif (event.key == pygame.K_BACKSPACE):
                        leaderboard_name = leaderboard_name[:-1]

                    # Sets leaderboard name and score when input is entered
                    elif (event.key == pygame.K_RETURN):
                        leaderboard_score = str (calculate_score
                                                (mode, current_line))
                        leaderboard.set_score (leaderboard_name,
                                              leaderboard_score)
                        leaderboard_name = ""
                        challenges = True

        pygame.display.update ()

    pygame.quit ()

main ()