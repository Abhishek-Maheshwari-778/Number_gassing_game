import random
import csv
import time
from colorama import Fore, Style

# Load or create user profiles
def load_user_profiles():
    try:
        with open('user_profiles.csv', mode='r') as file:
            reader = csv.reader(file)
            profiles = {row[0]: row[1:] for row in reader}
        return profiles
    except FileNotFoundError:
        return {}

# Save user profiles
def save_user_profiles(profiles):
    with open('user_profiles.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        for user, data in profiles.items():
            writer.writerow([user] + data)

# Game intro
def game_intro():
    print(Fore.CYAN + "\nWelcome to the Number Guessing Game!")
    print("Your goal is to guess the number within the given attempts.")
    print("Choose from Single Player, 2-Player, or Time Attack modes. Good luck!\n" + Style.RESET_ALL)

# Select difficulty level
def select_difficulty():
    print(Fore.YELLOW + "\nSelect a difficulty level:" + Style.RESET_ALL)
    print(Fore.CYAN + "1. Easy (1-50, 10 attempts)\n2. Medium (1-100, 8 attempts)\n3. Hard (1-200, 6 attempts)" + Style.RESET_ALL)
    choice = input("Choose difficulty (1-3): ")

    if choice == '1':
        return 1, 50, 10  # Easy difficulty
    elif choice == '2':
        return 1, 100, 8  # Medium difficulty
    elif choice == '3':
        return 1, 200, 6  # Hard difficulty
    else:
        print(Fore.RED + "Invalid choice. Defaulting to Easy mode." + Style.RESET_ALL)
        return 1, 50, 10  # Default to Easy

# Provide hints to the player
def give_hint(number, guess):
    if guess < number:
        return "Hint: Try a higher number!"
    elif guess > number:
        return "Hint: Try a lower number!"

# Calculate score based on remaining attempts
def calculate_score(attempts_left, max_attempts):
    return attempts_left * (100 // max_attempts)

# Single-player game
def play_single_player_game():
    profiles = load_user_profiles()
    username = input(Fore.MAGENTA + "Enter your username: " + Style.RESET_ALL)
    if username not in profiles:
        profiles[username] = ['0', '0', '0']  # [Total Attempts, Games Played, Wins]

    low, high, attempts_left = select_difficulty()
    number = random.randint(low, high)
    max_attempts = attempts_left

    print(Fore.GREEN + f"\nGuess the number between {low} and {high}." + Style.RESET_ALL)
    print(Fore.YELLOW + f"You have {attempts_left} attempts. Good luck!" + Style.RESET_ALL)

    while attempts_left > 0:
        try:
            guess = int(input(Fore.CYAN + "Enter your guess: " + Style.RESET_ALL))
        except ValueError:
            print(Fore.RED + "Invalid input! Please enter a number." + Style.RESET_ALL)
            continue
        attempts_left -= 1

        if guess == number:
            print(Fore.GREEN + "Congratulations! You've guessed the correct number!" + Style.RESET_ALL)
            score = calculate_score(attempts_left, max_attempts)
            print(Fore.CYAN + f"Your score: {score}\n" + Style.RESET_ALL)
            profiles[username][0] = str(int(profiles[username][0]) + max_attempts - attempts_left)
            profiles[username][1] = str(int(profiles[username][1]) + 1)
            profiles[username][2] = str(int(profiles[username][2]) + 1)
            save_user_profiles(profiles)
            break
        else:
            if attempts_left > 0:
                print(Fore.RED + "Incorrect! " + give_hint(number, guess) + Style.RESET_ALL)
                print(Fore.YELLOW + f"Attempts left: {attempts_left}\n" + Style.RESET_ALL)
            else:
                print(Fore.RED + "Game Over! You've run out of attempts." + Style.RESET_ALL)
                print(Fore.CYAN + f"The correct number was {number}." + Style.RESET_ALL)
                profiles[username][0] = str(int(profiles[username][0]) + max_attempts)
                profiles[username][1] = str(int(profiles[username][1]) + 1)
                save_user_profiles(profiles)

# 2-Player game
def play_two_player_game():
    profiles = load_user_profiles()
    player1 = input(Fore.MAGENTA + "Enter Player 1 username: " + Style.RESET_ALL)
    player2 = input(Fore.MAGENTA + "Enter Player 2 username: " + Style.RESET_ALL)
    
    if player1 not in profiles:
        profiles[player1] = ['0', '0', '0']
    if player2 not in profiles:
        profiles[player2] = ['0', '0', '0']

    low, high, attempts_left = select_difficulty()
    number = random.randint(low, high)
    max_attempts = attempts_left

    print(Fore.GREEN + f"\nThe number to guess is between {low} and {high}. Good luck!" + Style.RESET_ALL)
    
    for player in [player1, player2] * (max_attempts // 2):
        print(Fore.CYAN + f"\n{player}'s turn:" + Style.RESET_ALL)
        try:
            guess = int(input(Fore.CYAN + "Enter your guess: " + Style.RESET_ALL))
        except ValueError:
            print(Fore.RED + "Invalid input! Please enter a number." + Style.RESET_ALL)
            continue
        attempts_left -= 1
        
        if guess == number:
            print(Fore.GREEN + f"Congratulations {player}! You guessed the correct number!" + Style.RESET_ALL)
            profiles[player][0] = str(int(profiles[player][0]) + (max_attempts - attempts_left))
            profiles[player][1] = str(int(profiles[player][1]) + 1)
            profiles[player][2] = str(int(profiles[player][2]) + 1)
            save_user_profiles(profiles)
            break
        else:
            print(Fore.RED + "Incorrect! " + give_hint(number, guess) + Style.RESET_ALL)
            if attempts_left == 0:
                print(Fore.RED + "Game Over! No one guessed the number." + Style.RESET_ALL)
                break
            print(Fore.YELLOW + f"Attempts left: {attempts_left}\n" + Style.RESET_ALL)

# Time Attack mode
def play_time_attack():
    profiles = load_user_profiles()
    username = input(Fore.MAGENTA + "Enter your username: " + Style.RESET_ALL)
    if username not in profiles:
        profiles[username] = ['0', '0', '0']

    low, high, attempts_left = select_difficulty()
    number = random.randint(low, high)
    max_attempts = attempts_left
    time_limit = 30  # 60-second time limit
    start_time = time.time()

    print(Fore.GREEN + f"\nGuess the number between {low} and {high}. You have {time_limit} seconds to succeed!" + Style.RESET_ALL)

    while attempts_left > 0:
        elapsed_time = time.time() - start_time
        remaining_time = time_limit - elapsed_time

        # Check if time is up
        if remaining_time <= 0:
            print(Fore.RED + "Time's up! You ran out of time." + Style.RESET_ALL)
            break

        print(Fore.YELLOW + f"\nTime remaining: {remaining_time:.2f} seconds" + Style.RESET_ALL)
        try:
            guess = int(input(Fore.CYAN + "Enter your guess: " + Style.RESET_ALL))
        except ValueError:
            print(Fore.RED + "Invalid input! Please enter a number." + Style.RESET_ALL)
            continue
        
        attempts_left -= 1

        if guess == number:
            elapsed_time = time.time() - start_time  # Final time for score
            print(Fore.GREEN + f"Congratulations! You've guessed the correct number in {elapsed_time:.2f} seconds!" + Style.RESET_ALL)
            score = calculate_score(attempts_left, max_attempts)
            print(Fore.CYAN + f"Your score: {score}\n" + Style.RESET_ALL)
            profiles[username][0] = str(int(profiles[username][0]) + (max_attempts - attempts_left))
            profiles[username][1] = str(int(profiles[username][1]) + 1)
            profiles[username][2] = str(int(profiles[username][2]) + 1)
            save_user_profiles(profiles)
            break
        else:
            print(Fore.RED + "Incorrect! " + give_hint(number, guess) + Style.RESET_ALL)
            if attempts_left > 0:
                print(Fore.YELLOW + f"Attempts left: {attempts_left}" + Style.RESET_ALL)
            else:
                print(Fore.RED + "Game Over! You've run out of attempts." + Style.RESET_ALL)

        # Final check on remaining time before next attempt
        if remaining_time <= 10:
            print(Fore.RED + "Hurry up! Only a few seconds left!" + Style.RESET_ALL)

    if attempts_left == 0 or remaining_time <= 0:
        print(Fore.CYAN + f"The correct number was {number}." + Style.RESET_ALL)

# Leaderboard display
def show_leaderboard():
    profiles = load_user_profiles()
    leaderboard = sorted(profiles.items(), key=lambda x: int(x[1][2]), reverse=True)
    print(Fore.GREEN + "\n--- Leaderboard ---" + Style.RESET_ALL)
    for idx, (user, stats) in enumerate(leaderboard[:10], 1):
        print(f"{idx}. {user} - Wins: {stats[2]}, Attempts: {stats[0]}, Games Played: {stats[1]}")

# Main game loop
def main():
    game_intro()
    while True:
        print(Fore.YELLOW + "\nSelect a game mode:" + Style.RESET_ALL)
        print(Fore.CYAN + "1. Single Player\n2. 2-Player\n3. Time Attack\n4. Leaderboard\n5. Quit" + Style.RESET_ALL)
        choice = input("Choose a mode (1-5): ")

        if choice == '1':
            play_single_player_game()
        elif choice == '2':
            play_two_player_game()
        elif choice == '3':
            play_time_attack()
        elif choice == '4':
            show_leaderboard()
        elif choice == '5':
            print(Fore.MAGENTA + "Thank you for playing! Goodbye!" + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Invalid choice. Please select again." + Style.RESET_ALL)

if __name__ == "__main__":
    main()
