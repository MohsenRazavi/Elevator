import os
import platform


def clear_screen():
    os_ = platform.system()
    if os_ == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


def get_user_choice(options):
    for o in range(len(options)):
        print(f"{o + 1}- {options[o]}")

    while True:
        choice = input('choose option: ')
        try:
            choice = int(choice)
        except ValueError:
            print('invalid input ! try again.')
        else:
            if 1 <= choice <= len(options):
                return choice
            print('invalid input ! try again.')


def get_boolean_user_input(question, true_tuple, false_tuple):
    while True:
        choice = input(question)
        if choice not in ('', 'y', 'n'):
            print('invalid input ! try again.')
        else:
            if choice in true_tuple:
                return True
            elif choice in false_tuple:
                return False


def get_integer_user_input(question, default):
    while True:
        user_input = input(question)
        try:
            user_input = int(user_input)
            break
        except ValueError:
            if user_input == '':
                user_input = default
                print(f'Set as default ({default})')
                break
            print('invalid input ! try again.')
    return user_input


def get_bounded_integer_user_input(question, bound):
    while True:
        user_input = input(question)
        try:
            user_input = int(user_input)
            if user_input in bound:
                return user_input
            print('invalid input ! try again.')
        except ValueError:
            if user_input == '':
                print('invalid input ! try again.')

