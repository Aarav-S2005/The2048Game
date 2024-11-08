# 2048 Game in Python

This project is a Python-based GUI implementation of the classic 2048 game using the `tkinter` library. The game consists of a 4x4 grid in which players combine numbers to reach the 2048 tile.

## Game Rules

- Use arrow keys to slide the tiles left, right, up, or down.
- Tiles with the same number merge when they touch, creating a new tile with double the number.
- The goal is to reach the 2048 tile. If you succeed, you win the game!
- The game is over when no moves are possible (when the grid is full, and no adjacent tiles have the same number).

## Features

- **Score tracking**: Displays your current score.
- **Game Over and Win Notifications**: Alerts you when you win (by reaching the 2048 tile) or lose (when no moves are possible).
- **Grid Colors**: Each tile value has a unique color to improve readability.
- **Randomized Starting Tiles**: The game starts with two random tiles in the grid.

## How to Play

1. Run the game by executing the Python script.
2. Press `Space` to start a new game.
3. Use the following controls:
   - Arrow keys (`←`, `→`, `↑`, `↓`) to move the tiles in the specified direction.
   - `Esc` to exit the game.

## Installation

1. Make sure you have Python 3 installed on your computer.
2. Install the necessary libraries using the following command:

```bash
  pip install tkinker
  python 2048_game.py
```
