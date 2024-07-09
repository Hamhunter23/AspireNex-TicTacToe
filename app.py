from flask import Flask, request, jsonify, render_template
import random

app = Flask(__name__)

# Initialize the board
board = [' ' for _ in range(9)]

# Winning combinations
WINNING_COMBOS = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
    [0, 4, 8], [2, 4, 6]  # Diagonals
]

def minimax(board, depth, is_maximizing, alpha, beta):
    scores = {'X': 1, 'O': -1, 'Tie': 0}
    
    winner = check_winner(board)
    if winner:
        return scores[winner]
    
    if is_maximizing:
        best_score = float('-inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, depth + 1, False, alpha, beta)
                board[i] = ' '
                best_score = max(score, best_score)
                alpha = max(alpha, best_score)
                if beta <= alpha:
                    break
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, depth + 1, True, alpha, beta)
                board[i] = ' '
                best_score = min(score, best_score)
                beta = min(beta, best_score)
                if beta <= alpha:
                    break
        return best_score

def best_move(board):
    best_score = float('-inf')
    move = None
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            score = minimax(board, 0, False, float('-inf'), float('inf'))
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    return move

def check_winner(board):
    for combo in WINNING_COMBOS:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != ' ':
            return board[combo[0]]
    
    if ' ' not in board:
        return 'Tie'
    
    return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/move', methods=['POST'])
def make_move():
    global board
    move = int(request.json['move'])
    
    if board[move] != ' ':
        return jsonify({'error': 'Invalid move'}), 400
    
    board[move] = 'O'
    
    winner = check_winner(board)
    if winner:
        return jsonify({'board': board, 'winner': winner, 'winningCombo': get_winning_combo(board)})
    
    ai_move = best_move(board)
    board[ai_move] = 'X'
    
    winner = check_winner(board)
    return jsonify({'board': board, 'winner': winner, 'winningCombo': get_winning_combo(board)})

@app.route('/reset', methods=['POST'])
def reset_game():
    global board
    board = [' ' for _ in range(9)]
    return jsonify({'board': board})

def get_winning_combo(board):
    for combo in WINNING_COMBOS:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != ' ':
            return combo
    return None

if __name__ == '__main__':
    app.run(debug=True)