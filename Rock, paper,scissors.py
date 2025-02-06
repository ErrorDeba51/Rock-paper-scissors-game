import random
import time
import threading

variable = None


def get_player_input():

    global variable
    variable = input(
        "Enter rock, paper, scissors (or press 'q' to quit the game): ").lower()


def computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])


def winner_select(player, computer):
    if player == computer:
        return 'Tie'
    elif (player == 'rock' and computer == 'scissors') or \
         (player == 'scissors' and computer == 'paper') or \
         (player == 'paper' and computer == 'rock'):
        return 'Player'
    else:
        return 'Computer'


def start_game():
    print('Welcome to Rock, Paper, Scissors GAME')
    name = input("Hey player, enter your name here: ")
    print(f"Welcome {name.title()}!\n")
    mode = input(
        "Two modes available:\n1. In 30 seconds, score the highest.\n2. First to score 100 points wins.\nSelect mode (1/2): ")
    print("Invalid input. Please enter 1 or 2.\n")
    if mode not in ["1", "2"]:
        print("Invalid input. Please enter 1 or 2.\n")
        return start_game()

    if mode == "1":
        print("In 30sec who will do highest will win the game!\n")
        print("loading...")
        time.sleep(5)

        print("Game started!\n")

        player_score = 0
        computer_score = 0
        # ===
        start_time = time.time()
        while time.time() - start_time < 30:
            global variable
            variable = None
            input_thread = threading.Thread(target=get_player_input)
            input_thread.start()
            input_thread.join(timeout=10)

            if variable is None:
                print("\nNo input detected. Time's up!\n")
                return start_game()
            player = variable
            if player in ['q', 'quit']:
                break
            elif player in ['p', 'paper']:
                player = 'paper'
            elif player in ['s', 'scissors']:
                player = 'scissors'
            elif player in ['r', 'rock']:
                player = 'rock'
            else:
                print('Invalid choice. Please enter rock, paper, or scissors.')
                continue

            computer = computer_choice()

            print(f"\n{name.title()} choose: {player}")
            print(f"Computer choose: {computer}")

            result = winner_select(player, computer)
            if result == 'Player':
                player_score += 10
                print(f"{name.title()} wins this round!")
            elif result == 'Computer':
                computer_score += 10
                print("Computer wins this round!")
            else:
                print("It's a tie!")

            print(f"\n{name.title()} Score: {
                  player_score} | Computer Score: {computer_score}")
            print("---" * 10)

        if player_score > computer_score:
            print(f"\nCongratulations {name.title()}! You won the game!")
        elif player_score < computer_score:
            print("\nComputer wins the game! Better luck next time!")
        else:
            print("It's a tie!")
        print("Thanks for playing!")

    # ======================================================================================================================================
    elif mode == "2":
        print("First to score 100 points will win the game!\n")

        player_score = 0
        computer_score = 0

        while player_score < 100 and computer_score < 100:
            player = input(
                "Enter rock, paper, scissors (or press 'q' to quit the game): ").lower()

            if player in ['q', 'quit']:
                break
            elif player in ['p', 'paper']:
                player = 'paper'
            elif player in ['s', 'scissors']:
                player = 'scissors'
            elif player in ['r', 'rock']:
                player = 'rock'
            else:
                print('Invalid choice. Please enter rock, paper, or scissors.')
                continue

            computer = computer_choice()

            print(f"\n{name.title()} choose: {player}")
            print(f"Computer choose: {computer}")

            result = winner_select(player, computer)
            if result == 'Player':
                player_score += 10
                print(f"{name.title()} wins this round!")
            elif result == 'Computer':
                computer_score += 10
                print("Computer wins this round!")
            else:
                print("It's a tie!")

            print(f"\n{name.title()} Score: {
                  player_score} | Computer Score: {computer_score}")
            print("---" * 10)

        if player_score >= 100:
            print(f"\nCongratulations {name.title()}! You won the game!")
        elif computer_score >= 100:
            print("\nComputer wins the game! Better luck next time!")
        print("Thanks for playing!")


start_game()
