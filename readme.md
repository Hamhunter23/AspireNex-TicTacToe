# Tic-Tac-Toe AI

## Description

This project is an implementation of a Tic-Tac-Toe game with an unbeatable AI opponent using the Minimax algorithm with alpha-beta pruning. The game is built using Python with Flask for the backend and HTML/JavaScript for the frontend, creating an interactive and visually appealing web-based game.

## Features

- Web-based Tic-Tac-Toe game
- Unbeatable AI opponent using Minimax algorithm with alpha-beta pruning
- Responsive design for various screen sizes
- Animated moves and winning combinations
- Easy-to-use interface with a reset button

## Technology Stack

- Backend: Python, Flask
- Frontend: HTML, CSS, JavaScript
- Animation: Anime.js library

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/Hamhunter23/AspireNex-TicTacToe.git
   cd tic-tac-toe-ai
   ```

2. Install the required Python packages:
   ```
   pip install flask
   ```

3. Run the Flask application:
   ```
   python app.py
   ```

4. Open a web browser and navigate to `http://localhost:5000` to play the game.

## How to Play

1. The game board is a 3x3 grid.
2. You play as 'O', and the AI plays as 'X'.
3. Click on an empty cell to make your move.
4. The AI will automatically make its move after you.
5. The first player to get three of their symbols in a row (horizontally, vertically, or diagonally) wins.
6. If all cells are filled and no player has won, the game is a tie.
7. Click the "Reset Game" button to start a new game at any time.

## Code Structure

- `app.py`: Contains the Flask application and the game logic, including the Minimax algorithm.
- `index.html`: The HTML file for the game's frontend, including styles and JavaScript.

### Key Functions

- `minimax(board, depth, is_maximizing, alpha, beta)`: Implements the Minimax algorithm with alpha-beta pruning for the AI's decision-making.
- `best_move(board)`: Determines the best move for the AI using the Minimax algorithm.
- `check_winner(board)`: Checks if there's a winner or a tie.
- `make_move()`: Handles player moves and triggers the AI's response.
- `reset_game()`: Resets the game board.

## AI Algorithm

The AI uses the Minimax algorithm with alpha-beta pruning to determine the best move. This makes the AI unbeatable - it will always win or force a tie. The algorithm works by:

1. Simulating all possible game states.
2. Evaluating each end state (win, lose, or tie).
3. Choosing the move that leads to the best outcome for the AI, assuming the player also plays optimally.

Alpha-beta pruning is used to optimize the algorithm by eliminating branches that don't need to be evaluated.

## Frontend Design

The frontend is designed with a clean and intuitive interface. It features:

- A 3x3 grid for the game board.
- Animated moves using the Anime.js library.
- A message display for game status and results.
- A reset button to start a new game.
- Responsive design for various screen sizes.
- Visual highlighting of the winning combination.

## Future Improvements

- Add difficulty levels by adjusting the AI's decision-making process.
- Implement a scoreboard to track wins, losses, and ties.
- Add sound effects for moves and game results.
- Create a two-player mode for local multiplayer.
- Optimize the AI algorithm for faster performance on larger board sizes.

## Contributing

Contributions to improve the game or fix bugs are welcome. Please feel free to submit a pull request or open an issue to discuss potential changes/additions.

## License

[MIT License](LICENSE)

## Acknowledgements

- Flask: https://flask.palletsprojects.com/
- Anime.js: https://animejs.com/

Enjoy playing Tic-Tac-Toe against the unbeatable AI!
