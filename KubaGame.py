# Kevin Hayden
# 5/28/2021
# Description: Kuba Game. Utilizes a class for the game and initializes a starting set of marble positions. Players
# attempt to either capture the majority of red marbles or knock off their opponent's so they can no longer make moves.

class KubaGame:
    """Class for the Kuba Game. Game ends when a player wins.  A player wins by pushing off and capturing seven"""
    """neutral red stones or by pushing off all of the opposing stones.  A player who has no legal moves available"""
    """has lost the game."""
    def __init__(self, tuple1, tuple2):  # takes two tuples for each player,each containing player name and marble color
        """Initializes the game board and set-up."""
        self._first_player, self._first_token = tuple1
        self._second_player, self._second_token = tuple2
        self._current_turn = None
        self._previous_turn = None
        self._winner = None
        self._white_count = 8
        self._white_reds_captured = 0
        self._black_count = 8
        self._black_reds_captured = 0
        self._red_count = 13
        self._board = [['W', 'W', 'X', 'X', 'X', 'B', 'B'], ['W', 'W', 'X', 'R', 'X', 'B', 'B'],
                       ['X', 'X', 'R', 'R', 'R', 'X', 'X'], ['X', 'R', 'R', 'R', 'R', 'R', 'X'],
                       ['X', 'X', 'R', 'R', 'R', 'X', 'X'], ['B', 'B', 'X', 'R', 'X', 'W', 'W'],
                       ['B', 'B', 'X', 'X', 'X', 'W', 'W']]

    def get_current_turn(self):
        """Returns the player name whose turn it is.  Returns none if neither player has moved yet."""
        return self._current_turn

    def set_current_turn(self, player_name):
        """Sets current turn."""
        self._current_turn = player_name

    def is_your_turn(self, player_name):
        """Checks to see if it is current player's turn."""
        if self._current_turn is None:
            self.set_current_turn(player_name)
            return True

        if self._current_turn != self._previous_turn:
            return True

        else:
            return False  # Invalid move, not their turn

    def get_winner(self):
        """Returns the name of the winning player.  If game is not over, returns None."""
        return self._winner

    def set_winner(self, player_name):
        """Sets the winner if the game has been won."""
        self._winner = player_name

    def is_winner(self, player_name):
        """Checks to see if player won."""
        if self._white_reds_captured == 7 or self._black_count == 0:
            if self.get_player_token(player_name) == 'W':
                self.set_winner(player_name)  # White won
                return True

        if self._black_reds_captured == 7 or self._white_count == 0:
            if self.get_player_token(player_name) == 'B':
                self.set_winner(player_name)  # Black won
                return True

        else:
            return False  # nobody won yet

    def get_captured(self, player_name):
        """Returns the number of Red Marbles captured by the player.  Returns 0 if none have been captured by player."""
        marble_color = self.get_player_token(player_name)
        if marble_color == 'W':
            return self._white_reds_captured
        if marble_color == 'B':
            return self._black_reds_captured

    def get_marble(self, coordinates):
        """Takes the coordinates of a cell as a tuple and returns the marble that is present at that location.  If no"""
        """marble is present at the coordinate location, return 'X'."""
        row = coordinates[0]
        column = coordinates[1]
        return self._board[row][column]

    def get_marble_count(self):
        """Returns the number of White, Black and Red Marbles on the board, in play as a tuple in that order."""
        return self._white_count, self._black_count, self._red_count

    def get_player_token(self, player_name):
        """Returns player marble color based off player name."""
        if player_name == self._first_player:
            return self._first_token

        if player_name == self._second_player:
            return self._second_token

    def display_board(self):
        """Prints the board."""
        for i in range(0, 7):
            for j in range(0, 7):
                print(self._board[i][j], " ", end='')
            print(' ')

    def make_move(self, player_name, coordinates, direction):
        """To make a move, you need an empty space (or edge of the board) on the side you are pushing away from."""
        x = coordinates[0]
        y = coordinates[1]
        token = self.get_player_token(player_name)
        self._current_turn = player_name

        if self._winner is not None:
            return False  # game already won

        if self.is_your_turn(player_name) is False:
            return False  # not your turn

        else:
            if direction == 'L':
                if self.get_marble((x, y)) is not token:
                    return False  # invalid move, not your marble

                captured_marble = -1

                if y != 6 and self.get_marble((x, y + 1)) != 'X':
                    return False  # invalid move, space pushing from not empty

                elif True or y == 6:
                    for i in range(0, y + 1):
                        if self._board[x][i] == 'X':
                            captured_marble = i

                    if captured_marble == -1 and player_name == self._first_player:  # first player
                        if self._board[x][0] == token:
                            return False  # invalid move, cannot knock your own marble out

                        if self.get_player_token(player_name) == 'W':
                            if self._board[x][0] == 'B':
                                self._black_count -= 1
                            if self._board[x][0] == 'R':
                                self._red_count -= 1
                                self._white_reds_captured += 1

                        if self.get_player_token(player_name) == 'B':
                            if self._board[x][0] == 'W':
                                self._white_count -= 1
                            if self._board[x][0] == 'R':
                                self._red_count -= 1
                                self._black_reds_captured += 1

                    if captured_marble == -1 and player_name == self._second_player:  # second player
                        if self._board[x][0] == token:
                            return False  # invalid move, cannot knock your own marble out

                        if self.get_player_token(player_name) == 'W':
                            if self._board[x][0] == 'B':
                                self._black_count -= 1
                            if self._board[x][0] == 'R':
                                self._red_count -= 1
                                self._white_reds_captured += 1

                        if self.get_player_token(player_name) == 'B':
                            if self._board[x][0] == 'W':
                                self._white_count -= 1
                            if self._board[x][0] == 'R':
                                self._red_count -= 1
                                self._black_reds_captured += 1

                    if captured_marble == -1:  # board arranging begin
                        pushed_marble = 0
                    else:
                        pushed_marble = captured_marble
                    for i in range(pushed_marble, y):
                        self._board[x][i] = self._board[x][i + 1]
                    self._board[x][y] = 'X'  # board arranging end

                    if self.is_winner(player_name) is True:
                        self.set_winner(player_name)  # player won

                    self._previous_turn = player_name  # turn change

                    return True  # move successful

            if direction == 'R':
                if self.get_marble((x, y)) is not token:  # not your marble
                    return False

                captured_marble = -1

                if y != 0 and self.get_marble((x, y - 1)) != 'X':  # invalid move, space pushing from not empty
                    return False

                elif True or y == 0:  # valid move
                    for i in range(y + 1, 7):
                        if self._board[x][i] == 'X':
                            captured_marble = i
                            break
                    if captured_marble == -1 and player_name == self._first_player:
                        if self._board[x][6] == token:
                            return False  # invalid move, cannot push own marble off

                        if self.get_player_token(player_name) == 'W':
                            if self._board[x][6] == 'B':
                                self._black_count -= 1
                            if self._board[x][6] == 'R':
                                self._red_count -= 1
                                self._white_reds_captured += 1

                        if self.get_player_token(player_name) == 'B':
                            if self._board[x][6] == 'W':
                                self._white_count -= 1
                            if self._board[x][6] == 'R':
                                self._red_count -= 1
                                self._black_reds_captured += 1

                    if captured_marble == -1 and player_name == self._second_player:
                        if self._board[x][6] == token:
                            return False  # invalid move, cannot push own marble off

                        if self.get_player_token(player_name) == 'W':
                            if self._board[x][6] == 'B':
                                self._black_count -= 1
                            if self._board[x][6] == 'R':
                                self._red_count -= 1
                                self._white_reds_captured += 1

                        if self.get_player_token(player_name) == 'B':
                            if self._board[x][6] == 'W':
                                self._white_count -= 1
                            if self._board[x][6] == 'R':
                                self._red_count -= 1
                                self._black_reds_captured += 1

                    if captured_marble == -1:  # board arranging begin
                        pushed_marble = 7
                    else:
                        pushed_marble = captured_marble + 1
                    count = pushed_marble - 1
                    for i in range(y + 1, pushed_marble):
                        self._board[x][count] = self._board[x][count - 1]
                        count = count - 1
                    self._board[x][y] = 'X'  # board arranging end

                    if self.is_winner(player_name) is True:
                        self.set_winner(player_name)  # player won

                    self._previous_turn = player_name  # turn change

                    return True  # move successful

            if direction == 'F':
                if self.get_marble((x, y)) is not token:  # not your marble
                    return False

                captured_marble = -1

                if x != 6 and self.get_marble((x + 1, y)) != 'X':  # invalid move, space pushing from not empty
                    return False

                elif True or x == 6:  # valid move
                    for i in range(0, x):
                        if self._board[i][y] == 'X':
                            captured_marble = i

                    if captured_marble == -1 and player_name == self._first_player:
                        if self._board[0][y] == token:
                            return False  # invalid move, cannot push own marble off

                        if self.get_player_token(player_name) == 'W':
                            if self._board[0][y] == 'B':
                                self._black_count -= 1
                            if self._board[0][y] == 'R':
                                self._red_count -= 1
                                self._white_reds_captured += 1

                        if self.get_player_token(player_name) == 'B':
                            if self._board[0][y] == 'W':
                                self._white_count -= 1
                            if self._board[0][y] == 'R':
                                self._red_count -= 1
                                self._black_reds_captured += 1

                    if captured_marble == -1 and player_name == self._second_player:
                        if self._board[0][y] == token:
                            return False  # invalid move, cannot push own marble off

                        if self.get_player_token(player_name) == 'W':
                            if self._board[0][y] == 'B':
                                self._black_count -= 1
                            if self._board[0][y] == 'R':
                                self._red_count -= 1
                                self._white_reds_captured += 1

                        if self.get_player_token(player_name) == 'B':
                            if self._board[0][y] == 'W':
                                self._white_count -= 1
                            if self._board[0][y] == 'R':
                                self._red_count -= 1
                                self._black_reds_captured += 1

                    if captured_marble == -1:  # board arranging begin
                        pushed_marble = 0
                    else:
                        pushed_marble = captured_marble
                    for i in range(pushed_marble, x):
                        self._board[i][y] = self._board[i + 1][y]
                    self._board[x][y] = 'X'  # board arranging end

                    if self.is_winner(player_name) is True:
                        self.set_winner(player_name)  # player won

                    self._previous_turn = player_name  # turn change

                    return True  # move successful

            if direction == 'B':
                if self.get_marble((x, y)) is not token:  # not your marble
                    return False

                captured_marble = -1

                if x != 0 and self.get_marble((x - 1, y)) != 'X':  # invalid move, space pushing from not empty
                    return False

                elif True or x == 0:  # valid move
                    for i in range(x + 1, 7):
                        if self._board[i][y] == 'X':
                            captured_marble = i
                            break
                    if captured_marble == -1 and player_name == self._first_player:  # first player move/capture
                        if self._board[6][y] == token:
                            return False  # invalid move, cannot push own marble off

                        if self.get_player_token(player_name) == 'W':
                            if self._board[6][y] == 'B':
                                self._black_count -= 1
                            if self._board[6][y] == 'R':
                                self._red_count -= 1
                                self._white_reds_captured += 1

                        if self.get_player_token(player_name) == 'B':
                            if self._board[6][y] == 'W':
                                self._white_count -= 1
                            if self._board[6][y] == 'R':
                                self._red_count -= 1
                                self._black_reds_captured += 1

                    if captured_marble == -1 and player_name == self._second_player:  # second player move/capture
                        if self._board[6][y] == token:
                            return False  # invalid move, cannot push own marble off
                        if self.get_player_token(player_name) == 'W':
                            if self._board[6][y] == 'B':
                                self._black_count -= 1
                            if self._board[6][y] == 'R':
                                self._red_count -= 1
                                self._white_reds_captured += 1

                        if self.get_player_token(player_name) == 'B':
                            if self._board[6][y] == 'W':
                                self._white_count -= 1
                            if self._board[6][y] == 'R':
                                self._red_count -= 1
                                self._black_reds_captured += 1

                    if captured_marble == -1:  # board arranging begin
                        pushed_marble = 7
                    else:
                        pushed_marble = captured_marble + 1
                    count = pushed_marble - 1
                    for i in range(x + 1, pushed_marble):
                        self._board[count][y] = self._board[count - 1][y]
                        count = count - 1
                    self._board[x][y] = 'X'  # board arranging end

                    if self.is_winner(player_name) is True:
                        self.set_winner(player_name)  # player won

                    self._previous_turn = player_name  # turn change

                    return True  # move successful


# def main():
    # Initializing
    # game = KubaGame(('PlayerA', 'W'), ('PlayerB', 'B'))  # CORRECT, game is initialized
    # game.display_board()  # CORRECT, Game board is correct

    # Test initial variables
    # print(game.get_marble_count())  # CORRECT, returns (8, 8, 13)
    # print(game.get_captured('PlayerA'))  # CORRECT returns 0
    # print(game.get_current_turn())  # CORRECT, neither player has started, returns None
    # print(game.get_winner())  # CORRECT, returns None
    # print(game.get_marble((5, 5)))  # returns 'W'

    # Test invalid moves
    # print(game.make_move('PlayerA', (5, 5), 'F'))  # CORRECT, return False, invalid move
    # print(game.make_move('PlayerA', (5, 6), 'L'))  # CORRECT, return True, player made move
    # print(game.make_move('PlayerA', (5, 5), 'L'))  # CORRECT, return False, player already went
    # print(game.make_move('PlayerB', (6, 0), 'R'))  # CORRECT, return True, player made move
    # print(game.make_move('PlayerB', (6, 1), 'R'))  # CORRECT, return False, player already went
    # print(game.make_move('PlayerA', (5, 5), 'L'))  # CORRECT, return True
    # print(game.make_move('PlayerB', (6, 1), 'R'))  # CORRECT, return True

    # Testing White Marble moves going Left, before turn logic added
    # print(game.make_move('PlayerA', (5, 6), 'L'))  # CORRECT, return True
    # print(game.make_move('PlayerA', (5, 5), 'L'))
    # print(game.make_move('PlayerA', (5, 4), 'L'))
    # print(game.make_move('PlayerA', (5, 3), 'L'))
    # print(game.make_move('PlayerA', (5, 2), 'L'))
    # game.display_board()
    # print(game.get_marble_count())  # CORRECT, (8, 6, 12), White pushed off two black marbles and one red
    # print(game.get_captured('PlayerA'))  # CORRECT, White captured one Red Marble

    # Testing Black Marble moves going Right, before turn logic added
    # print(game.make_move('PlayerB', (5, 0), 'R'))
    # print(game.make_move('PlayerB', (5, 1), 'R'))
    # print(game.make_move('PlayerB', (5, 2), 'R'))
    # print(game.make_move('PlayerB', (5, 3), 'R'))
    # print(game.make_move('PlayerB', (5, 4), 'R'))
    # game.display_board()
    # print(game.get_marble_count())  # CORRECT, (6, 8, 12), Black pushed off two white marbles and one red
    # print(game.get_captured('PlayerB'))  # CORRECT, Black captured one Red Marble

    # Testing White Marble moves going Forward, before turn logic added
    # print(game.make_move('PlayerA', (6, 5), 'F'))
    # print(game.make_move('PlayerA', (5, 5), 'F'))
    # print(game.make_move('PlayerA', (4, 5), 'F'))
    # print(game.make_move('PlayerA', (3, 5), 'F'))
    # print(game.make_move('PlayerA', (2, 5), 'F'))
    # game.display_board()
    # print(game.get_marble_count())  # CORRECT, (8, 6, 12), White pushed off two black marbles and one red
    # print(game.get_captured('PlayerA'))  # CORRECT, White captured one Red Marble

    # Testing Black Marble moves going Backward, before turn logic added
    # print(game.make_move('PlayerB', (0, 5), 'B'))
    # print(game.make_move('PlayerB', (1, 5), 'B'))
    # print(game.make_move('PlayerB', (2, 5), 'B'))
    # print(game.make_move('PlayerB', (3, 5), 'B'))
    # print(game.make_move('PlayerB', (4, 5), 'B'))
    # game.display_board()
    # print(game.get_marble_count())  # CORRECT, (6, 8, 12), Black pushed off two white marbles and one red
    # print(game.get_captured('PlayerB'))  # CORRECT, Black captured one Red Marble

    # Testing with Gradescope Tests
    # print(game.make_move('PlayerA', (6, 5), 'F'))
    # game.display_board()
    # game.make_move('PlayerB', (0, 5), 'B')
    # game.display_board()
    # game.make_move('PlayerA', (5, 5), 'F')
    # game.display_board()
    # game.make_move('PlayerB', (0, 6), 'L')
    # game.display_board()
    # game.make_move('PlayerA', (4, 5), 'F')
    # game.display_board()
    # game.make_move('PlayerB', (0, 5), 'L')
    # game.display_board()
    # game.make_move('PlayerA', (3, 5), 'F')
    # game.display_board()
    # game.make_move('PlayerB', (6, 1), 'F')
    # game.display_board()
    # game.make_move('PlayerA', (2, 5), 'F')
    # game.display_board()
    # print(game.get_marble_count())

    # Testing further for win conditions
    # game.make_move('PlayerB', (1, 6), 'L')
    # game.make_move('PlayerA', (5, 6), 'L')
    # game.make_move('PlayerB', (1, 5), 'L')
    # game.make_move('PlayerA', (5, 5), 'L')
    # game.make_move('PlayerB', (1, 4), 'L')
    # game.make_move('PlayerA', (5, 4), 'L')
    # game.make_move('PlayerB', (1, 3), 'L')
    # game.make_move('PlayerA', (5, 3), 'L')
    # game.make_move('PlayerB', (1, 2), 'L')
    # game.make_move('PlayerA', (5, 2), 'L')
    # game.make_move('PlayerB', (1, 1), 'L')
    # game.make_move('PlayerA', (5, 1), 'L')
    # game.make_move('PlayerB', (1, 0), 'F')
    # game.make_move('PlayerA', (5, 0), 'B')
    # game.make_move('PlayerB', (4, 1), 'R')
    # game.make_move('PlayerA', (0, 1), 'L')
    # game.make_move('PlayerB', (4, 2), 'R')
    # game.make_move('PlayerA', (6, 0), 'F')
    # game.make_move('PlayerB', (4, 3), 'R')
    # game.make_move('PlayerA', (5, 0), 'F')
    # game.make_move('PlayerB', (4, 4), 'R')
    # game.make_move('PlayerA', (4, 0), 'F')
    # game.make_move('PlayerB', (4, 5), 'R')
    # game.make_move('PlayerA', (3, 0), 'R')
    # game.make_move('PlayerB', (4, 6), 'B')
    # game.make_move('PlayerA', (3, 1), 'R')
    # game.make_move('PlayerB', (5, 6), 'B')
    # game.make_move('PlayerA', (3, 2), 'R')
    # game.make_move('PlayerB', (6, 6), 'F')
    # game.make_move('PlayerA', (3, 3), 'R')
    # game.make_move('PlayerB', (5, 6), 'F')
    # game.make_move('PlayerA', (3, 4), 'R')
    # game.make_move('PlayerB', (0, 3), 'R')
    # game.make_move('PlayerA', (3, 5), 'R')
    # game.make_move('PlayerB', (0, 4), 'R')
    # game.make_move('PlayerA', (3, 6), 'B')
    # game.make_move('PlayerB', (0, 5), 'B')
    # game.make_move('PlayerA', (4, 6), 'B')
    # game.make_move('PlayerB', (0, 6), 'B')
    # game.make_move('PlayerA', (5, 6), 'B')
    # game.make_move('PlayerB', (1, 5), 'B')
    # game.make_move('PlayerA', (0, 0), 'B')
    # game.make_move('PlayerB', (1, 6), 'B')
    # game.make_move('PlayerA', (6, 6), 'F')
    # game.make_move('PlayerB', (2, 6), 'L')
    # game.make_move('PlayerA', (5, 6), 'F')
    # game.make_move('PlayerB', (2, 5), 'L')
    # game.make_move('PlayerA', (4, 6), 'F')
    # game.make_move('PlayerB', (2, 4), 'L')
    # game.make_move('PlayerA', (3, 6), 'F')
    # game.make_move('PlayerB', (2, 3), 'L')
    # game.make_move('PlayerA', (2, 6), 'L')
    # game.make_move('PlayerB', (2, 2), 'B')
    # game.make_move('PlayerA', (1, 0), 'B')
    # game.make_move('PlayerB', (2, 1), 'L')
    # game.make_move('PlayerA', (2, 5), 'L')
    # game.make_move('PlayerB', (2, 0), 'B')
    # game.make_move('PlayerA', (2, 4), 'L')
    # game.make_move('PlayerB', (3, 0), 'B')
    # game.make_move('PlayerA', (2, 3), 'L')
    # game.make_move('PlayerB', (4, 0), 'B')
    # game.make_move('PlayerA', (2, 2), 'B')
    # game.make_move('PlayerB', (5, 0), 'R')
    # game.make_move('PlayerA', (3, 2), 'B')
    # game.make_move('PlayerB', (5, 1), 'F')
    # game.make_move('PlayerA', (4, 2), 'B')
    # game.make_move('PlayerB', (4, 1), 'L')
    # game.make_move('PlayerA', (5, 2), 'B')
    # game.make_move('PlayerB', (4, 0), 'B')
    # game.make_move('PlayerA', (6, 2), 'L')

    # White Wins by Capturing 7 Reds
    # game.make_move('PlayerB', (5, 0), 'R')
    # game.make_move('PlayerA', (6, 1), 'L')  # PlayerA wins, Marble count and captured correct
    # print(game.make_move('PlayerB', (5, 1), 'B'))  # returns False, PlayerA already won

    # Black Wins by Capturing 7 Reds
    # game.make_move('PlayerB', (5, 0), 'B')  # PlayerB wins, Marble count and captured correct
    # print(game.make_move('PlayerA', (6, 1), 'L'))  # returns False, PlayerB already won

    # End Result
    # game.display_board()
    # print(game.get_marble_count())
    # print(game.get_captured('PlayerA'))
    # print(game.get_captured('PlayerB'))

    # All Testing Correct and Complete

# if __name__ == '__main__':
#     main()
