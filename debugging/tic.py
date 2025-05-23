#!/usr/bin/python3

def print_board(board):
    print()  # Add space for better readability
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:  # Only print separator after first two rows
            print("-" * 9)
    print()  # Add space after board

def check_winner(board):
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    current_player = "X"
    
    while True:
        print_board(board)
        
        # Get player move with input validation
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {current_player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {current_player}: "))
            
            if not (0 <= row <= 2 and 0 <= col <= 2):
                print("Invalid coordinates! Row and column must be between 0 and 2.")
                continue
                
        except ValueError:
            print("Invalid input! Please enter numbers only.")
            continue
            
        # Make move if space is available
        if board[row][col] == " ":
            board[row][col] = current_player
            
            # Check for win
            if check_winner(board):
                print_board(board)
                print(f"Player {current_player} wins!")
                break
                
            # Check for draw
            if is_board_full(board):
                print_board(board)
                print("It's a draw!")
                break
                
            # Switch player
            current_player = "O" if current_player == "X" else "X"
        else:
            print("That spot is already taken! Try again.")

if __name__ == "__main__":
    tic_tac_toe()
