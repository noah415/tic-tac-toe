import curses

def print_center(message, screen):
    # Calculate center row
    middle_row = int(25 / 2)

    # Calculate center column, and then adjust starting position based
    # on the length of the message
    half_length_of_message = int(len(message) / 2)
    middle_column = int(75 / 2)
    x_position = middle_column - half_length_of_message

    # Draw the text
    screen.addstr(middle_row, x_position, message)
    screen.refresh()


def draw_board(screen):
    pass


def draw_start(screen, start_selector_num, selector):
    if selector == "KEY_UP":
        start_selector_num += 1
    elif selector == "KEY_DOWN":
        start_selector_num -= 1

    screen.clear()
    print_center("Welcome to Tic Tac Toe", screen)
    if start_selector_num == 0:
        screen.addstr(0,0,"Player vs AI")
        screen.addstr(2,0,"Player vs Player")
        screen.addstr(4,0,"Quit", curses.A_BLINK)
        screen.addstr(4,5,"*")
                
    elif start_selector_num == 1:
        screen.addstr(0,0,"Player vs AI")
        screen.addstr(2,0,"Player vs Player", curses.A_BLINK)
        screen.addstr(2,17,"*")
        screen.addstr(4,0,"Quit")

    elif start_selector_num == 2:
        screen.addstr(0,0,"Player vs AI", curses.A_BLINK)
        screen.addstr(0,13,"*")
        screen.addstr(2,0,"Player vs Player")
        screen.addstr(4,0,"Quit")

    screen.refresh()
    return start_selector_num