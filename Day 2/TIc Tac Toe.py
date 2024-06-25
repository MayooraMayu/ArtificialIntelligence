def print_board(board):
    print("-------------")
    for row in board:
        print("|", row[0], "|", row[1], "|", row[2], "|")
        print("-------------")

def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True

    return False

def tic_tac_toe():
    board = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']]

    player = 'X'
    print_board(board)

    for _ in range(9):  # Maximum 9 moves
        print(f"Player {player}'s turn.")
        valid_move = False
        while not valid_move:
            try:
                move = int(input("Enter your move (1-9): ")) - 1
                row = move // 3
                col = move % 3

                if board[row][col] == ' ':
                    board[row][col] = player
                    valid_move = True
                else:
                    print("That cell is already taken. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Please enter a number between 1 and 9.")

        print_board(board)

        if check_winner(board, player):
            print(f"Player {player} wins!")
            return

        player = 'O' if player == 'X' else 'X'

    print("It's a draw!")

# Run the game
if __name__ == "__main__":
    tic_tac_toe()
