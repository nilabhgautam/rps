#!/usr/bin/env python3
"""
Text-Based Games Collection
==========================

This program offers two classic games:

1. Number Guessing Game:
   - Computer picks a random number between 1-100
   - Player guesses until they find it
   - Hints provided after each guess
   - Tracks number of attempts

2. Rock, Paper, Scissors:
   - Player vs Computer
   - Standard rules: Rock beats Scissors, Scissors beats Paper, Paper beats Rock
   - Score tracking for both players
   - Type 'exit' anytime to quit

How to Play:
- Run the program and choose a game from the menu
- Follow the on-screen instructions
- Type 'exit' anytime to return to main menu or quit

Author: Chef Assistant
Version: 1.0
"""

import random
import sys


class GameStats:
    """Class to track game statistics"""
    
    def __init__(self):
        self.number_game_best_score = float('inf')
        self.rps_player_wins = 0
        self.rps_computer_wins = 0
        self.games_played = 0
    
    def update_number_game(self, attempts):
        """Update number guessing game stats"""
        if attempts < self.number_game_best_score:
            self.number_game_best_score = attempts
        self.games_played += 1
    
    def update_rps_game(self, player_wins, computer_wins):
        """Update rock paper scissors stats"""
        self.rps_player_wins += player_wins
        self.rps_computer_wins += computer_wins
        self.games_played += 1
    
    def display_stats(self):
        """Display current game statistics"""
        print("\n" + "="*40)
        print("           GAME STATISTICS")
        print("="*40)
        print(f"Total games played: {self.games_played}")
        
        if self.number_game_best_score != float('inf'):
            print(f"Number Game best score: {self.number_game_best_score} attempts")
        
        if self.rps_player_wins > 0 or self.rps_computer_wins > 0:
            total_rps_rounds = self.rps_player_wins + self.rps_computer_wins
            win_rate = (self.rps_player_wins / total_rps_rounds * 100) if total_rps_rounds > 0 else 0
            print(f"RPS Player wins: {self.rps_player_wins}")
            print(f"RPS Computer wins: {self.rps_computer_wins}")
            print(f"RPS Win rate: {win_rate:.1f}%")
        
        print("="*40)


def get_user_input(prompt, valid_options=None):
    """
    Get user input with validation
    
    Args:
        prompt (str): The prompt to display to user
        valid_options (list): List of valid options (optional)
    
    Returns:
        str: User input (lowercase and stripped)
    """
    while True:
        user_input = input(prompt).strip().lower()
        
        if user_input == 'exit':
            return 'exit'
        
        if valid_options is None:
            return user_input
        
        if user_input in valid_options:
            return user_input
        
        print(f"Invalid input. Please choose from: {', '.join(valid_options)}")


def number_guessing_game():
    """
    Number Guessing Game Implementation
    
    Returns:
        int: Number of attempts taken to guess correctly
    """
    print("\n" + "="*50)
    print("           NUMBER GUESSING GAME")
    print("="*50)
    print("I'm thinking of a number between 1 and 100!")
    print("Try to guess it. I'll give you hints after each guess.")
    print("Type 'exit' anytime to return to main menu.\n")
    
    # Generate random number
    secret_number = random.randint(1, 100)
    attempts = 0
    
    while True:
        # Get user guess
        guess_input = get_user_input("Enter your guess (1-100): ")
        
        if guess_input == 'exit':
            print("Returning to main menu...")
            return None
        
        # Validate numeric input
        try:
            guess = int(guess_input)
        except ValueError:
            print("Please enter a valid number!")
            continue
        
        # Validate range
        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100!")
            continue
        
        attempts += 1
        
        # Check guess
        if guess == secret_number:
            print(f"\n🎉 Congratulations! You guessed it!")
            print(f"The number was {secret_number}")
            print(f"It took you {attempts} attempts.")
            
            # Provide feedback based on performance
            if attempts <= 5:
                print("Excellent! You're a guessing master! 🏆")
            elif attempts <= 10:
                print("Great job! That's pretty good! 👍")
            elif attempts <= 15:
                print("Not bad! You got there in the end! 😊")
            else:
                print("You made it! Practice makes perfect! 💪")
            
            return attempts
        
        elif guess < secret_number:
            print(f"Too low! Try a higher number. (Attempt {attempts})")
        else:
            print(f"Too high! Try a lower number. (Attempt {attempts})")


def rock_paper_scissors_game():
    """
    Rock Paper Scissors Game Implementation
    
    Returns:
        tuple: (player_wins, computer_wins)
    """
    print("\n" + "="*50)
    print("         ROCK, PAPER, SCISSORS")
    print("="*50)
    print("Let's play Rock, Paper, Scissors!")
    print("Rules: Rock beats Scissors, Scissors beats Paper, Paper beats Rock")
    print("Type 'exit' anytime to return to main menu.\n")
    
    choices = ['rock', 'paper', 'scissors']
    player_score = 0
    computer_score = 0
    round_number = 1
    
    while True:
        print(f"\n--- Round {round_number} ---")
        print(f"Score - You: {player_score} | Computer: {computer_score}")
        
        # Get player choice
        player_choice = get_user_input(
            "Choose Rock, Paper, or Scissors: ", 
            choices
        )
        
        if player_choice == 'exit':
            break
        
        # Computer makes random choice
        computer_choice = random.choice(choices)
        
        print(f"\nYou chose: {player_choice.title()}")
        print(f"Computer chose: {computer_choice.title()}")
        
        # Determine winner
        if player_choice == computer_choice:
            print("It's a tie! 🤝")
        elif (
            (player_choice == 'rock' and computer_choice == 'scissors') or
            (player_choice == 'paper' and computer_choice == 'rock') or
            (player_choice == 'scissors' and computer_choice == 'paper')
        ):
            print("You win this round! 🎉")
            player_score += 1
        else:
            print("Computer wins this round! 🤖")
            computer_score += 1
        
        round_number += 1
        
        # Ask if player wants to continue
        continue_game = get_user_input(
            "\nPlay another round? (yes/no): ", 
            ['yes', 'y', 'no', 'n']
        )
        
        if continue_game == 'exit' or continue_game in ['no', 'n']:
            break
    
    # Display final results
    print(f"\n--- Final Score ---")
    print(f"You: {player_score} | Computer: {computer_score}")
    
    if player_score > computer_score:
        print("🏆 You won overall! Great job!")
    elif computer_score > player_score:
        print("🤖 Computer won overall! Better luck next time!")
    else:
        print("🤝 It's a tie overall! Well played!")
    
    return player_score, computer_score


def display_main_menu():
    """Display the main menu"""
    print("\n" + "="*50)
    print("           WELCOME TO GAME COLLECTION")
    print("="*50)
    print("Choose a game to play:")
    print("1. Number Guessing Game")
    print("2. Rock, Paper, Scissors")
    print("3. View Statistics")
    print("4. Exit")
    print("="*50)


def main():
    """Main game loop"""
    print("🎮 Welcome to the Text-Based Games Collection! 🎮")
    
    # Initialize game statistics
    stats = GameStats()
    
    while True:
        display_main_menu()
        
        choice = get_user_input("Enter your choice (1-4): ", ['1', '2', '3', '4'])
        
        if choice == 'exit' or choice == '4':
            print("\n👋 Thanks for playing! Goodbye!")
            stats.display_stats()
            sys.exit(0)
        
        elif choice == '1':
            attempts = number_guessing_game()
            if attempts is not None:
                stats.update_number_game(attempts)
        
        elif choice == '2':
            player_wins, computer_wins = rock_paper_scissors_game()
            if player_wins > 0 or computer_wins > 0:
                stats.update_rps_game(player_wins, computer_wins)
        
        elif choice == '3':
            stats.display_stats()
        
        # Pause before returning to menu
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Game interrupted. Thanks for playing!")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ An unexpected error occurred: {e}")
        print("Please restart the program.")
        sys.exit(1)
