import os
import sys

# Function to display the board
def display_board(board):
    """
    Prints the Tic-Tac-Toe board to the console.
    
    Args:
        board (list): A list of 9 strings representing the board.
    """
    os.system('cls' if os.name == 'nt' else 'clear')  # Clears the console
    print("\n")
    print("  " + board[0] + " | " + board[1] + " | " + board[2])
    print(" ---+---+---")
    print("  " + board[3] + " | " + board[4] + " | " + board[5])
    print(" ---+---+---")
    print("  " + board[6] + " | " + board[7] + " | " + board[8])
    print("\n")

# Function to get and validate player input
def get_player_move(board):
    """
    Prompts the current player for their move (1-9), validates it,
    and returns the chosen position.
    
    Args:
        board (list): The current state of the board.
        
    Returns:
        int: The index of the chosen position (0-8).
    """
    while True:
        try:
            position = int(input("Choose your next position (1-9): "))
            # Check if the input is a number from 1 to 9
            if 1 <= position <= 9:
                # Check if the chosen position is empty
                if board[position - 1] == str(position):
                    return position - 1
                else:
                    print("That position is already taken. Please choose another one.")
            else:
                print("Invalid input. Please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Function to place a marker on the board
def place_marker(board, marker, position):
    """
    Places the player's marker on the board at the given position.
    
    Args:
        board (list): The current state of the board.
        marker (str): The player's marker ('X' or 'O').
        position (int): The index of the position to place the marker.
    """
    board[position] = marker

# Function to check for a win
def check_win(board, marker):
    """
    Checks if the current player has won the game.
    
    Args:
        board (list): The current state of the board.
        marker (str): The player's marker to check for ('X' or 'O').
    
    Returns:
        bool: True if the player has won, False otherwise.
    """
    win_conditions = [
        # Horizontal wins
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        # Vertical wins
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        # Diagonal wins
        [0, 4, 8], [2, 4, 6]
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == marker:
            return True
    return False

# Function to check if the board is full
def is_board_full(board):
    """
    Checks if the board is full, indicating a tie.
    
    Args:
        board (list): The current state of the board.
        
    Returns:
        bool: True if the board is full, False otherwise.
    """
    for x in board:
        if x in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            return False
    return True

# Main game loop function
def play_game():
    """
    Manages the full game of Tic-Tac-Toe, alternating turns and checking
    for a win or a tie.
    """
    # Initialize the board with numbers 1-9
    board = [str(i) for i in range(1, 10)]
    current_player = 'X'
    game_on = True
    winner = None

    while game_on:
        # Display the board
        display_board(board)

        # Get player's move
        print(f"It's Player {current_player}'s turn.")
        position = get_player_move(board)

        # Place the marker on the board
        place_marker(board, current_player, position)

        # Check for a win
        if check_win(board, current_player):
            display_board(board)
            winner = current_player
            game_on = False
        # Check for a tie
        elif is_board_full(board):
            display_board(board)
            game_on = False

        # Switch to the other player
        if game_on:
            current_player = 'O' if current_player == 'X' else 'X'

    # Game over, print the result
    if winner:
        print(f"Congratulations! Player {winner} wins!")
    else:
        print("The game is a tie!")

# Start the game
if __name__ == "__main__":
    play_game()

