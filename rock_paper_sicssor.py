import random

def show_welcome():
    print("🎮" + "="*40 + "🎮")
    print("    WELCOME TO ROCK PAPER SCISSORS!")
    print("🎮" + "="*40 + "🎮")
    print("Rules:")
    print("🪨 Rock beats Scissors")
    print("✂️  Scissors beats Paper") 
    print("📄 Paper beats Rock")
    print("-"*44)

def get_user_choice():
    print("\nChoose your weapon:")
    print("1. 🪨 Rock")
    print("2. 📄 Paper") 
    print("3. ✂️  Scissors")
    
    while True:
        choice = input("Enter your choice (1-3): ")
        if choice == "1":
            return "rock"
        elif choice == "2":
            return "paper"
        elif choice == "3":
            return "scissors"
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def get_emoji(choice):
    if choice == "rock":
        return "🪨"
    elif choice == "paper":
        return "📄"
    elif choice == "scissors":
        return "✂️"

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "user"
    else:
        return "computer"

def display_result(user_choice, computer_choice, winner):
    print("\n" + "="*30)
    print("ROUND RESULT")
    print("="*30)
    print(f"You chose:     {get_emoji(user_choice)} {user_choice.title()}")
    print(f"Computer chose: {get_emoji(computer_choice)} {computer_choice.title()}")
    print("-"*30)
    
    if winner == "tie":
        print("🤝 It's a TIE!")
    elif winner == "user":
        print(" YOU WIN!")
    else:
        print("💻 COMPUTER WINS!")

def display_score(user_score, computer_score):
    print("\n" + "🏆" + "="*20 + "🏆")
    print("      SCOREBOARD")
    print("🏆" + "="*20 + "🏆")
    print(f"You: {user_score}")
    print(f"Computer: {computer_score}")
    print("-"*24)

def get_number_of_games():
    while True:
        try:
            games = int(input("How many games do you want to play? "))
            if games > 0:
                return games
            else:
                print("Please enter a number greater than 0.")
        except ValueError:
            print("Please enter a valid number.")

def play_again():
    while True:
        choice = input("Do you want to play another set of games? (y/n): ").lower()
        if choice in ['y', 'yes']:
            return True
        elif choice in ['n', 'no']:
            return False
        else:
            print("Please enter 'y' for yes or 'n' for no.")

def main():
    show_welcome()
    
    total_user_score = 0
    total_computer_score = 0
    total_rounds_played = 0
    
    while True:
        # Get number of games for this set
        num_games = get_number_of_games()
        print(f"\n🎯 Starting a set of {num_games} games!")
        
        # Reset scores for this set
        user_score = 0
        computer_score = 0
        
        # Play the specified number of games
        for round_number in range(1, num_games + 1):
            print(f"\n🎯 GAME {round_number} of {num_games}")
            print("-" * 20)
            
            # Get choices
            user_choice = get_user_choice()
            computer_choice = get_computer_choice()
            
            # Determine winner
            winner = determine_winner(user_choice, computer_choice)
            
            # Update scores
            if winner == "user":
                user_score += 1
                total_user_score += 1
            elif winner == "computer":
                computer_score += 1
                total_computer_score += 1
            
            total_rounds_played += 1
            
            # Display results
            display_result(user_choice, computer_choice, winner)
            display_score(user_score, computer_score)
        
        # Show set results
        print("\n" + "🎊" + "="*30 + "🎊")
        print(f"       SET OF {num_games} GAMES COMPLETE!")
        print("🎊" + "="*30 + "🎊")
        print(f"This Set - You: {user_score} | Computer: {computer_score}")
        
        if user_score > computer_score:
            print("🏆 YOU WON THIS SET! 🏆")
        elif computer_score > user_score:
            print("💻 Computer won this set!")
        else:
            print("🤝 This set was a tie!")
        
        print(f"\nOverall - You: {total_user_score} | Computer: {total_computer_score}")
        print(f"Total Games Played: {total_rounds_played}")
        
        # Check if user wants to play another set
        if not play_again():
            break
    
    # Final overall results
    print("\n" + "🎊" + "="*35 + "🎊")
    print("         FINAL OVERALL RESULTS")
    print("🎊" + "="*35 + "🎊")
    print(f"Total Games Played: {total_rounds_played}")
    print(f"Your Total Score: {total_user_score}")
    print(f"Computer Total Score: {total_computer_score}")
    
    if total_user_score > total_computer_score:
        print("🏆 CONGRATULATIONS! YOU ARE THE OVERALL CHAMPION! 🏆")
    elif total_computer_score > total_user_score:
        print("💻 Computer wins overall! Better luck next time!")
    else:
        print("🤝 Overall it's a perfect tie! Amazing game!")
    
    print("\nThanks for playing Rock Paper Scissors! 🎮")

# Run the game
if __name__ == "__main__":
    main()