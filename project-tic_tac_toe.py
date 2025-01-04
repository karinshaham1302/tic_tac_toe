import random


def print_board(board: dict[int, str]) -> None:
    """
    Prints the Tic Tac Toe board
    """
    print()
    print(f" {board[1]} | {board[2]} | {board[3]} ")
    print("---+---+---")
    print(f" {board[4]} | {board[5]} | {board[6]} ")
    print("---+---+---")
    print(f" {board[7]} | {board[8]} | {board[9]} ")
    print()


def check_winner(board: dict[int, str], player: str) -> bool:
    """
    Checks if a player has won the game
    """
    win_conditions = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],
        [1, 4, 7], [2, 5, 8], [3, 6, 9],
        [1, 5, 9], [3, 5, 7]
    ]

    return any(board[c[0]] == board[c[1]] == board[c[2]] == player for c in win_conditions)


def is_full(board: dict[int, str]) -> bool:
    """
    Checks if the board is full
    """
    return all(value != ' ' for value in board.values())


def random_move(board: dict[int, str]) -> int:
    """
    Chooses a random valid move for the computer
    """
    available_positions = [pos for pos, value in board.items() if value == ' ']
    return random.choice(available_positions)


def player_move(board: dict[int, str], current_player: str) -> int:
    """
    Handles a player's move with input validation
    """
    while True:
        try:
            move = int(input(f"Player {current_player}, choose a position (1-9): "))
            if move not in range(1, 10):
                print("Choose a number between 1 and 9")
            elif board[move] != ' ':
                print("This position is already taken. Try again")
            else:
                return move
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 9")


def tic_tac_toe() -> None:
    """
    Main function to run the Tic-Tac-Toe game
    """
    print("Welcome to Tic-Tac-Toe!")
    print("Players take turns marking a square with 'X' or 'O'")
    print("The winner is the first player to line up three marks in a row, column, or diagonal")
    print()

    while True:
        board: dict[int, str] = {i: ' ' for i in range(1, 10)}
        current_player: str = 'X'

        while True:
            print_board(board)

            if current_player == 'O':
                move: int = random_move(board)
                print(f"Computer chooses position: {move}")
            else:
                move: int = player_move(board, current_player)

            board[move] = current_player

            if check_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break

            if is_full(board):
                print_board(board)
                print("It's a tie!")
                break

            current_player = 'O' if current_player == 'X' else 'X'

        play_again: str = input("Do you want to play again? (Y/N): ").upper()
        if play_again != 'Y':
            print("Thanks for playing! Goodbye")
            break


if __name__ == "__main__":
    tic_tac_toe()
