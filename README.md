# Number Guessing Game

An interactive number guessing game with multiple difficulty levels, intelligent hints, and performance tracking.

## Features
- 5 difficulty levels (Easy, Medium, Hard, Expert, Custom)
- Intelligent hint system (way too low/high, too low/high, a bit low/high)
- Performance evaluation and optimal strategy comparison
- Game statistics tracking
- Guess history display
- Time tracking per game

## How to Play
1. Choose your difficulty level
2. The computer thinks of a random number
3. Make your guess
4. Follow the hints to narrow down the number
5. Try to guess in as few attempts as possible!

## Difficulty Levels
- **Easy:** 1-50
- **Medium:** 1-100
- **Hard:** 1-500
- **Expert:** 1-1000
- **Custom:** Choose your own range

## Example Gameplay
```
🎯 I'm thinking of a number between 1 and 100
Enter your guess: 50
📈 Too low! Go higher!
Enter your guess: 75
📉 A bit high! Try lower!
Enter your guess: 68
🎉 CONGRATULATIONS! YOU WON! 🎉
🏆 You guessed it in 3 attempts!
```

## How to Use
1. Clone the repository
2. Run: `python guessing_game.py`
3. Follow the on-screen instructions

## Requirements
- Python 3.x

## Technologies
- Python
- `random` module
- `time` module
