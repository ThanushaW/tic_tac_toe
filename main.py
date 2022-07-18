import random
import keyboard
import time

# keep track of rendering state and valid choices
state = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
valid_choices = state[:]


# welcome screen
def welcome():
    print('*' * 45)
    print('*' * 10 + ' Welcome to tick-tac-toe ' + '*' * 10)
    print('*' * 45)
    print(' ' * 10 + '-Press any key to start-' + ' ' * 10)


# render state to screen / UI
def render():
    global state
    for i in range(3):
        print(('+' + '-' * 7) * 3 + '+')
        print(('|' + ' ' * 7) * 3 + '|')
        for j in range(i * 3, i * 3 + 3):
            print('|' + ' ' * 3 + str(state[j]) + ' ' * 3, end='')
        print('|')
        print(('|' + ' ' * 7) * 3 + '|')
    print(('+' + '-' * 7) * 3 + '+')


# remove selected position from future choices
def remove(choosed):
    global valid_choices
    del valid_choices[valid_choices.index(choosed)]


# computer marking 'X'
def computer():
    global state
    global valid_choices
    print("\n\n\nComputer's choice : ")
    choice = random.randint(0, len(valid_choices) - 1)
    state[state.index(valid_choices[choice])] = 'X'
    remove(valid_choices[choice])


# user marking 'O'
def user():
    global state
    global valid_choices
    while True:
        print('\n\n\nEnter your choice : ', end='')
        position = input()
        if position in valid_choices:
            state[state.index(position)] = 'O'
            remove(position)
            break
        else:
            print(position, 'is not a valid choice')


# check if someone won
def check_win(s):
    global state
    row = state[:3] == [s, s, s] or state[3:6] == [s, s, s] or state[6:] == [s, s, s]
    col = False
    for i in range(3):
        if [state[i], state[i + 3], state[i + 6]] == [s, s, s]:
            col = True
            break
    diag = [state[0], state[4], state[8]] == [s, s, s] or [state[2], state[4], state[6]] == [s, s, s]
    if row or col or diag:
        if s == 'X':
            print('Game Over ! Computer Won !')
            return True
        else:
            print('Congratulations ! You Won !')
            return True
    return False


def game_flow():
    global state
    welcome()
    if keyboard.read_key():
        # initial step : computer always choose 5
        print('\n\n\nComputer chooses first')
        state[4] = 'X'
        remove('5')
        render()
        # until computer win do tic-tac-toe
        while not check_win('X'):
            user()
            render()
            time.sleep(3)
            # user win check
            if check_win('O'):
                break
            computer()
            render()


game_flow()
