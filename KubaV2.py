class KubaGame:
    """Class for the Kuba Game. Game ends when a player wins.  A player wins by pushing off and capturing seven"""
    """neutral red stones or by pushing off all of the opposing stones.  A player who has no legal moves available"""
    """has lost the game."""
    def __init__(self, tuple1, tuple2):  # takes two tuples for each player,each containing player name and marble color
        """Initializes the game board and set-up."""
        self._first_player, self._first_token = tuple1
        self._second_player, self._second_token = tuple2
        self._current_player = None
        self._current_turn = None
        self._winner = None
        self._white_count = 8  # White, Black, Red in that order
        self._white_reds_captured = 0
        self._black_count = 8
        self._black_reds_captured = 0
        self._red_count = 13
        self._board = [['W', 'W', 'X', 'X', 'X', 'B', 'B'], ['W', 'W', 'X', 'R', 'X', 'B', 'B'],
                       ['X', 'X', 'R', 'R', 'R', 'X', 'X'], ['X', 'R', 'R', 'R', 'R', 'R', 'X'],
                       ['X', 'X', 'R', 'R', 'R', 'X', 'X'], ['B', 'B', 'X', 'R', 'X', 'W', 'W'],
                       ['B', 'B', 'X', 'X', 'X', 'W', 'W']]

    def get_current_turn(self):  # anyone can start
        """Returns the player name whose turn it is.  Returns none if neither player has moved yet."""
        return self._current_turn

    def set_current_turn(self, player_name):
        """"""
        self._current_turn(player_name)

    def get_winner(self):
        """Returns the name of the winning player.  If game is not over, returns None."""
        return self._winner

    def set_winner(self, player_name):  # ADDED, sets winner
        """Sets the winner if the game has been won."""
        self._winner = player_name

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

    def get_marble_count(self):  # returns number of white, black and red marbles as tuple in this order, important
        """Returns the number of White, Black and Red Marbles on the board, in play as a tuple in that order."""
        return self._white_count, self._black_count, self._red_count

    def get_player_token(self, player_name):  # ADDED, gets token of player
        """"""
        if player_name == self._first_player:
            return self._first_token

        if player_name == self._second_player:
            return self._second_token

    def display_board(self):  # ADDED, for testing
        """Prints the board."""
        for i in range(0, 7):
            for j in range(0, 7):
                print(self._board[i][j], " ", end='')
            print(' ')

    def make_move(self, player_name, coordinates, direction):  # direction is Forward, Backward, Left, Right
        """To make a move, you need an empty space (or edge of the board) on the side you are pushing away from."""
        """A player can not undo a move the opponent just made."""
        x = coordinates[0]
        y = coordinates[1]
        token = self.get_player_token(player_name)

        if self._winner is not None:  # Invalid Move, game is already over
            return False

        if self._current_turn is None:  # Checks to see if this is new game starting
            self._current_turn = player_name

        if self._current_turn is not player_name:  # Possibly Invalid Move, not their turn
            return False

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
                            removed = i
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
                    if captured_marble == -1:
                        pushed_marble = 0
                    else:
                        pushed_marble = captured_marble
                    for i in range(pushed_marble, y):
                        self._board[x][i] = self._board[x][i + 1]
                    self._board[x][y] = 'X'
                    #  set current turn
                    return True

            if direction == 'R':
                if self.get_marble((x, y)) is not token:  # not your marble
                    print("Invalid move")
                    return False

                captured_marble = -1

                if y != 0 and self.get_marble((x, y - 1)) != 'X':  # invalid move, space pushing from not empty
                    print("Invalid move")
                    return False

                # if  # cannot push off own marble
                #
                elif True or y == 0:  # valid move
                    for i in range(y + 1, 7):
                        if self._board[x][i] == 'X':
                            captured_marble = i
                            break
                    if captured_marble == -1 and player_name == self._first_player:
                        if self._board[x][6] == token:
                            print("Invalid move: takes your own piece out.")
                            return False
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
                            print("Invalid move: takes your own piece out.")
                            return False
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
                    if captured_marble == -1:
                        pushed_marble = 7
                    else:
                        pushed_marble = captured_marble + 1
                    count = pushed_marble - 1
                    for i in range(y + 1, pushed_marble):
                        self._board[x][count] = self._board[x][count - 1]
                        count = count - 1
                    self._board[x][y] = 'X'
                    return True

            if direction == 'F':
                if self.get_marble((x, y)) is not token:  # not your marble
                    print("Invalid move")
                    return False

                captured_marble = -1

                if x != 6 and self.get_marble((x + 1, y)) != 'X':  # invalid move, space pushing from not empty
                    print("Invalid move")
                    return False

                # if  # cannot push off own marble
                #
                elif True or x == 6:  # valid move
                    for i in range(0, x):
                        if self._board[i][y] == 'X':
                            captured_marble = i
                    if captured_marble == -1 and player_name == self._first_player:
                        if self._board[0][y] == token:
                            print("Invalid move: takes your own piece out.")
                            return False
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
                            print("Invalid move: takes your own piece out.")
                            return False
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
                    if captured_marble == -1:
                        pushed_marble = 0
                    else:
                        pushed_marble = captured_marble
                    for i in range(pushed_marble, x):
                        self._board[i][y] = self._board[i + 1][y]
                    self._board[x][y] = 'X'
                    # print(self.first_captured)
                    return True

            if direction == 'B':
                if self.get_marble((x, y)) is not token:  # not your marble
                    print("Invalid move")
                    return False

                captured_marble = -1

                if x != 0 and self.get_marble((x - 1, y)) != 'X':  # invalid move, space pushing from not empty
                    print("Invalid move")
                    return False

                # if  # cannot push off own marble
                #
                elif True or x == 0:  # valid move
                    for i in range(x + 1, 7):
                        if self._board[i][y] == 'X':
                            captured_marble = i
                            break
                    if captured_marble == -1 and player_name == self._first_player:
                        if self._board[6][y] == token:
                            print("Invalid move: takes your own piece out.")
                            return False
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
                    if captured_marble == -1 and player_name == self._second_player:
                        if self._board[6][y] == token:
                            print("Invalid move: takes your own piece out.")
                            return False
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
                    if captured_marble == -1:
                        pushed_marble = 7
                    else:
                        pushed_marble = captured_marble + 1
                    count = pushed_marble - 1
                    for i in range(x + 1, pushed_marble):
                        self._board[count][y] = self._board[count - 1][y]
                        count = count - 1
                    self._board[x][y] = 'X'
                    # print(self.first_captured)
                    return True

        # NOTE
        # coordinates should be a tuple for board location
        # if opponent marble is pushed off it is removed from board
        # if red marble is pushed off it is considered captured by the player who made the move

        # RETURN TRUE
        #   if move is successful

        # RETURN FALSE
        #   if the move is being made after the game has been won CHECK (in first base case of make_move)
        #   if it's not the player's turn  CHECK
        #   if the coordinates provided are not valid
        #   if a marble in the coordinates cannot be moved in the direction specified
        #   if it is not the player's marble  CHECK (in each 'if direction' statements)
        #   if any other invalid condition return


def main():
    game = KubaGame(('PlayerA', 'W'), ('PlayerB', 'B'))  # CORRECT, game is initialized
    game.display_board()  # CORRECT, testing purposes
    print(game.get_marble_count())  # CORRECT returns (8,8,13), prints (8, 8, 13)
    print(game.get_captured('PlayerA'))  # WRONG, returns None, not 0
    print(game.get_current_turn())  # CORRECT, neither player has started, returns None
    print(game.get_winner())  # CORRECT, returns None
    print(game.make_move('PlayerA', (5, 5), 'F'))  # CORRECT, return False
    print(game.make_move('PlayerA', (5, 6), 'L'))  # CORRECT, return True
    print(game.get_marble((5, 5)))  # returns 'W'
    game.display_board()  # CORRECT


if __name__ == '__main__':
    main()
