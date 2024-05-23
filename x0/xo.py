# Tic-Tac-Toe (XO game) using Minimax algorithm

# Function to display the current state of the game
def display_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Function to check if a player has won
def check_win(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Function to check if the game is a draw
def check_draw(board):
    return all(board[i][j] != " " for i in range(3) for j in range(3))

# Function to find the available moves
def get_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

# Minimax function to determine the best move for the AI player
def minimax(board, depth, maximizing):
    if check_win(board, "X"):
        return 1
    if check_win(board, "O"):
        return -1
    if check_draw(board):
        return 0

    if maximizing:
        best_score = -float('inf')
        for move in get_moves(board):
            i, j = move
            board[i][j] = "X"
            score = minimax(board, depth + 1, False)
            board[i][j] = " "
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for move in get_moves(board):
            i, j = move
            board[i][j] = "O"
            score = minimax(board, depth + 1, True)
            board[i][j] = " "
            best_score = min(best_score, score)
        return best_score

# Function to find the best move for the AI player using the minimax algorithm
def find_best_move(board):
    best_score = -float('inf')
    best_move = None
    for move in get_moves(board):
        i, j = move
        board[i][j] = "X"
        score = minimax(board, 0, False)
        board[i][j] = " "
        if score > best_score:
            best_score = score
            best_move = (i, j)
    return best_move

# Main game loop
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "O"

    while True:
        display_board(board)

        if player == "O":
            i, j = (int(x) for x in input("Enter your move (row and column): ").split())
            if (i, j) not in get_moves(board):
                print("Invalid move. Try again.")
                continue
            board[i][j] = player
        else:
            print("AI is thinking...")
            i, j = find_best_move(board)
            board[i][j] = player

        if check_win(board, player):
            display_board(board)
            print(f"{player} wins!")
            break
        elif check_draw(board):
            display_board(board)
            print("It's a draw!")
            break

        player = "O" if player == "X" else "X"

if __name__ == "__main__":
    play_game()
