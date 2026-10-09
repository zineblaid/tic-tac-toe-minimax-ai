# Tic-Tac-Toe AI with Minimax

## Overview

This project implements a command-line Tic-Tac-Toe game in Python, where a human player competes against an AI opponent using the Minimax algorithm.

The AI evaluates possible future game states recursively to select a move that maximizes its chances of winning while minimizing the human player's chances.

## Features

- Interactive command-line gameplay.
- Human player versus AI opponent.
- Minimax algorithm for decision-making.
- Recursive exploration of possible game states.
- Win, loss, and draw detection.
- Input validation for human moves.
- Board display after each move.

## Technologies

- Python 3
- Minimax algorithm
- Recursion
- Game-tree search

## How to Play

The human player uses `X`, and the AI uses `O`.

The board positions are numbered from 1 to 9:

```text
 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9
```

Enter the number corresponding to an empty cell when prompted. The AI then calculates its move and updates the board.

## How to Run

Make sure Python 3 is installed.

1. Clone this repository.
2. Open a terminal in the project directory.
3. Run the following command:

```bash
python tictactoe_minimax.py
```

No external libraries are required.

## How Minimax Works

The algorithm evaluates possible game outcomes using the following scores:

- `1`: AI wins.
- `-1`: Human player wins.
- `0`: Draw.

The AI explores available moves recursively and chooses the move with the highest score. During the human player's simulated turns, the algorithm assumes that the human chooses the move with the lowest score.

## Project Structure

```text
tic-tac-toe-minimax-ai/
├── tictactoe_minimax.py
├── README.md
└── .gitignore
```

## Learning Objectives

- Understand the Minimax decision-making algorithm.
- Practice recursion and backtracking.
- Explore game-tree search.
- Implement an AI opponent for a two-player game.
- Understand how an AI evaluates possible outcomes.

## Possible Improvements

- Add Alpha-Beta pruning to reduce the number of explored states.
- Implement a graphical user interface.
- Allow the human player to choose their symbol.
- Improve move ordering to explore promising moves first.

## License

Add a license file if you want to specify the terms under which others can use, modify, and distribute this project.
