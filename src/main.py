import random

class TicTocToe:
    """
    A class to represent the Tic-Tac-Toe game.
    
    Attributes:
    -----------
    board : list[str]
        The game board represented as a list of strings.
    player_turn : str
        The player whose turn it is, either 'X' or 'O'.
    """

    def __init__(self) -> None:
        """Initialize the Tic-Tac-Toe game with an empty board and a random starting player."""
        self.board: list[str] = [' '] * 10
        self.player_turn: str = self.get_random_first_player()

    def get_random_first_player(self) -> str:
        """Randomly select which player ('X' or 'O') goes first.

        Returns:
        --------
        str
            The randomly chosen first player.
        """
        return random.choice(['X', 'O'])

    def show_board(self) -> None:
        """Display the current state of the game board."""
        print('\n')
        print(self.board[1] + '|' + self.board[2] + '|' + self.board[3])
        print('-----')
        print(self.board[4] + '|' + self.board[5] + '|' + self.board[6])
        print('-----')
        print(self.board[7] + '|' + self.board[8] + '|' + self.board[9])
        print('\n')

    def swap_player_turn(self) -> str:
        """Switch the current player to the other player.

        Returns:
        --------
        str
            The new current player after the swap.
        """
        self.player_turn = 'X' if self.player_turn == 'O' else 'O'
        return self.player_turn

    def is_board_filled(self) -> bool:
        """Check if the game board is completely filled.

        Returns:
        --------
        bool
            True if the board is filled, False otherwise.
        """
        return ' ' not in self.board[1:]

    def fix_spot(self, cell: int, player: str) -> None:
        """Mark a spot on the board for a player.

        Parameters:
        -----------
        cell : int
            The position on the board to mark (1-9).
        player : str
            The player making the move ('X' or 'O').
        """
        self.board[cell] = player

    def has_player_won(self, player: str) -> bool:
        """Check if the specified player has won the game.

        Parameters:
        -----------
        player : str
            The player to check ('X' or 'O').

        Returns:
        --------
        bool
            True if the player has won, False otherwise.
        """
        win_combinations: list[list[int]] = [
            [1, 2, 3], [4, 5, 6], [7, 8, 9],  # rows
            [1, 4, 7], [2, 5, 8], [3, 6, 9],  # columns
            [1, 5, 9], [3, 5, 7]  # diagonals
        ]
        for combination in win_combinations:
            if all(self.board[cell] == player for cell in combination):
                return True
        return False

    def start(self) -> None:
        """Begin the Tic-Tac-Toe game loop."""
        while True:
            self.show_board()
            print(f'Player {self.player_turn} turn')
            try:
                cell = int(input('Enter cell number from 1 to 9: '))
            except ValueError:
                print('Invalid input. Please enter a number from 1 to 9.')
                continue

            if self.board[cell] == ' ' and 1 <= cell <= 9:
                self.fix_spot(cell, self.player_turn)

                if self.has_player_won(self.player_turn):
                    self.show_board()
                    print(f'Player {self.player_turn} won!')
                    break
                if self.is_board_filled():
                    print('Draw')
                    break

                self.swap_player_turn()
            else:
                print('Invalid cell number or spot already taken. Try again.')

if __name__ == '__main__':
    game = TicTocToe()
    game.start()
