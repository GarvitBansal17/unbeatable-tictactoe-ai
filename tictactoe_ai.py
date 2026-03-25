import math

# --- 1. Game State Setup ---
# The board is a simple list of 9 spaces. 
# Indices 0-2 are the top row, 3-5 middle, 6-8 bottom.
board = [' ' for _ in range(9)]

def print_board(board):
    """Prints the current state of the board in the terminal."""
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

# --- 2. Game Logic ---
def check_winner(board, player):
    """Checks if the specified player ('X' or 'O') has won."""
    # Winning combinations: rows, columns, diagonals
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Columns
        [0, 4, 8], [2, 4, 6]             # Diagonals
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def check_draw(board):
    """Checks if the board is full (a draw)."""
    return ' ' not in board

# --- 3. The Core AI (Minimax Algorithm) ---
def minimax(board, depth, is_maximizing):
    """
    The Minimax algorithm. It plays out every possible future game state.
    Returns +1 if AI wins, -1 if Human wins, 0 for a draw.
    """
    # Base cases: Check if the game has ended in this hypothetical future
    if check_winner(board, 'O'): # AI wins
        return 1
    elif check_winner(board, 'X'): # Human wins
        return -1
    elif check_draw(board): # Draw
        return 0

    if is_maximizing:
        # AI's turn (trying to maximize the score)
        best_score = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O' # Try the move
                score = minimax(board, depth + 1, False) # Let the human respond
                board[i] = ' ' # Undo the move
                best_score = max(score, best_score)
        return best_score
    else:
        # Human's turn (AI assumes human will minimize the AI's score)
        best_score = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X' # Try the move
                score = minimax(board, depth + 1, True) # Let the AI respond
                board[i] = ' ' # Undo the move
                best_score = min(score, best_score)
        return best_score

def get_best_move(board):
    """Loops through all available moves and uses minimax to pick the best one."""
    best_score = -math.inf
    best_move = -1
    
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O' # Try the move
            score = minimax(board, 0, False) # Run minimax
            board[i] = ' ' # Undo the move
            
            # If this move leads to a better outcome, save it
            if score > best_score:
                best_score = score
                best_move = i
                
    return best_move

# --- 4. Main Application Loop ---
def main():
    print("="*40)
    print("🤖 UNBEATABLE TIC-TAC-TOE AI 🤖")
    print("You are 'X'. The AI is 'O'.")
    print("Positions are numbered 0-8 from top-left to bottom-right.")
    print("="*40)
    
    print_board(['0', '1', '2', '3', '4', '5', '6', '7', '8']) # Show position guide
    
    while True:
        # Human Turn
        try:
            move = int(input("Enter your move (0-8): "))
            if board[move] != ' ':
                print("That space is already taken! Try again.")
                continue
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number between 0 and 8.")
            continue
            
        board[move] = 'X'
        
        # Check if Human won (impossible, but required for logic) or drew
        if check_winner(board, 'X'):
            print_board(board)
            print("You win! (Wait, that's impossible...)")
            break
        elif check_draw(board):
            print_board(board)
            print("It's a draw! Well played.")
            break
            
        # AI Turn
        print("\nAI is calculating its move...")
        ai_move = get_best_move(board)
        board[ai_move] = 'O'
        print_board(board)
        
        # Check if AI won or drew
        if check_winner(board, 'O'):
            print("The AI wins! Better luck next time.")
            break
        elif check_draw(board):
            print("It's a draw! Well played.")
            break

if __name__ == "__main__":
    main()