from multiprocessing import RLock
import random

game = True
game_variable = ["rock", "paper", "spock", "lizard", "scissors"]

def player_choise():
    while True:
        player_input = input(f'Your choice {game_variable}: ')
        player_input.lower()
        if player_input in  game_variable:
            return player_input
        else:
            print("Invalid input:")

def check_continue():
    while True:
        repeat = input("Repeat (Y/N)? ")
        repeat.lower()
        if repeat == "y":
            return True
        elif repeat == "n":
            return False
        else:
            print('Invalid input: "' , repeat, '"')


def win_check(player_input, npc_choise):
    magic_dict = {'scissors': ('paper', 'lizard'),
                  'paper': ('rock', 'spock'),
                  'rock': ('scissors', 'lizard'),
                  'lizard': ('spock', 'paper'),
                  'spock': ('scissors', 'rock')}
    if player_input == npc_choise:
        print("Nobody wins")
        return
    for key, value in magic_dict.items():
        if player_input in key and npc_choise in value:
            print("You win!")
            return
        # else:
    print("You loose!")
    # return


while game:
    player_input = player_choise()
    npc_choise = random.choice(game_variable)
    print(f'Your choice: {player_input}')
    print(f'Computer choice: {npc_choise}')
    win_check(player_input, npc_choise)
    game = check_continue()


