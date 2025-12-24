import random
import time

def display_welcome():
    """Display welcome message and game rules"""
    print("\n" + "="*60)
    print("🎮 WELCOME TO THE NUMBER GUESSING GAME! 🎮")
    print("="*60)
    print("\nHow to play:")
    print("1. I'll think of a number within your chosen range")
    print("2. You try to guess it")
    print("3. I'll give you hints (higher/lower)")
    print("4. Try to guess in as few attempts as possible!")
    print("\n" + "="*60)

def get_difficulty():
    """Let user choose difficulty level"""
    print("\n🎯 Choose difficulty level:")
    print("1. Easy (1-50)")
    print("2. Medium (1-100)")
    print("3. Hard (1-500)")
    print("4. Expert (1-1000)")
    print("5. Custom range")
    
    while True:
        try:
            choice = int(input("\nEnter your choice (1-5): "))
            
            if choice == 1:
                return 1, 50, "Easy"
            elif choice == 2:
                return 1, 100, "Medium"
            elif choice == 3:
                return 1, 500, "Hard"
            elif choice == 4:
                return 1, 1000, "Expert"
            elif choice == 5:
                min_num = int(input("Enter minimum number: "))
                max_num = int(input("Enter maximum number: "))
                if min_num >= max_num:
                    print("Maximum must be greater than minimum!")
                    continue
                return min_num, max_num, "Custom"
            else:
                print("Invalid choice! Please enter 1-5.")
        except ValueError:
            print("Please enter a valid number!")

def play_game(min_num, max_num, difficulty):
    """Main game logic"""
    
    # Generate random number
    secret_number = random.randint(min_num, max_num)
    attempts = 0
    start_time = time.time()
    guess_history = []
    
    print(f"\n🎲 Difficulty: {difficulty}")
    print(f"🎯 I'm thinking of a number between {min_num} and {max_num}")
    print("Let's see how many tries it takes you!\n")
    
    # Calculate optimal attempts
    optimal_attempts = len(bin(max_num - min_num)) - 2
    
    while True:
        try:
            # Get user guess
            guess = int(input(f"Enter your guess ({min_num}-{max_num}): "))
            
            # Validate guess range
            if guess < min_num or guess > max_num:
                print(f"⚠️ Please guess between {min_num} and {max_num}!")
                continue
            
            attempts += 1
            guess_history.append(guess)
            
            # Check guess
            if guess < secret_number:
                difference = secret_number - guess
                if difference > 50:
                    print("📈 Way too low! Go much higher!")
                elif difference > 20:
                    print("📈 Too low! Go higher!")
                else:
                    print("📈 A bit low! Try higher!")
                    
            elif guess > secret_number:
                difference = guess - secret_number
                if difference > 50:
                    print("📉 Way too high! Go much lower!")
                elif difference > 20:
                    print("📉 Too high! Go lower!")
                else:
                    print("📉 A bit high! Try lower!")
            else:
                # Correct guess!
                end_time = time.time()
                time_taken = round(end_time - start_time, 2)
                
                print("\n" + "="*60)
                print("🎉 CONGRATULATIONS! YOU WON! 🎉")
                print("="*60)
                print(f"\n🎯 The number was: {secret_number}")
                print(f"🏆 You guessed it in {attempts} attempts!")
                print(f"⏱️ Time taken: {time_taken} seconds")
                
                # Performance feedback
                if attempts <= optimal_attempts:
                    print(f"🌟 OUTSTANDING! You used optimal strategy!")
                elif attempts <= optimal_attempts + 3:
                    print(f"👏 GREAT JOB! Very efficient!")
                elif attempts <= optimal_attempts + 7:
                    print(f"👍 GOOD! Nice guessing!")
                else:
                    print(f"💪 Keep practicing to improve your strategy!")
                
                print(f"\n📊 Your guess history: {guess_history}")
                print("="*60)
                
                return attempts, time_taken
                
        except ValueError:
            print("❌ Invalid input! Please enter a number.")
        except KeyboardInterrupt:
            print("\n\n👋 Game interrupted. Thanks for playing!")
            return None, None

def display_statistics(games_played, total_attempts, best_attempts, total_time):
    """Display player statistics"""
    if games_played == 0:
        return
    
    avg_attempts = total_attempts / games_played
    avg_time = total_time / games_played
    
    print("\n" + "="*60)
    print("📊 YOUR STATISTICS")
    print("="*60)
    print(f"🎮 Games played: {games_played}")
    print(f"🏆 Best performance: {best_attempts} attempts")
    print(f"📈 Average attempts: {avg_attempts:.1f}")
    print(f"⏱️ Average time per game: {avg_time:.1f} seconds")
    print("="*60)

def main():
    """Main function to run the game"""
    
    display_welcome()
    
    # Game statistics
    games_played = 0
    total_attempts = 0
    best_attempts = float('inf')
    total_time = 0
    
    while True:
        # Get difficulty
        min_num, max_num, difficulty = get_difficulty()
        
        # Play game
        attempts, time_taken = play_game(min_num, max_num, difficulty)
        
        if attempts is not None:
            # Update statistics
            games_played += 1
            total_attempts += attempts
            total_time += time_taken
            best_attempts = min(best_attempts, attempts)
        
        # Ask to play again
        print("\n" + "="*60)
        play_again = input("🎮 Play again? (y/n): ").lower()
        
        if play_again != 'y':
            display_statistics(games_played, total_attempts, best_attempts, total_time)
            print("\n👋 Thanks for playing! See you next time!")
            print("="*60)
            break

if __name__ == "__main__":
    main()
