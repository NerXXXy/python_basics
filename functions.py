import random

def greeting(name):
    print(f'Hello, {name}!')

greeting('Volodymyr')


def number_game(secret_number, stop_chars):
    user_input = ''
    while user_input != stop_chars:
        user_input = input('Guess the number from 1 to 100: ')
        if user_input == secret_number:
            print('Bingo , you won!')
        else:
            print(f'Your number is {user_input}. Try again')

# number_game(str(99), 'Stop')


def random_number_game():
    random_number = str(random.randint(0, 101))
    print(random_number)
    user_input = ''
    while user_input != random_number:
        user_input = input('Enter your number from 1 to 100: ')
        if user_input == random_number:
            print('Bingo! You won')
        else:
            print(f'Your number is {user_input}. Try again')


# random_number_game()


def return_function(a: int, b: int) -> int:    # we expect int in input of function and we need to return (-> int) from function
    return a + b , a * b


c, d = return_function(3, 5)
print(c, d)
