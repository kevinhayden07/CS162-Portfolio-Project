class KubaGame:
    def __init__(self, tuple1, tuple2):  # takes two tuples for each player,each containing player name and marble color
        """Initializes the game board and set-up."""
        self._first_player, self._first_token = tuple1
        self._second_player, self._second_token = tuple2
        self._current_turn = None
        self._winner = None
        self._marble_count = (8, 8, 13)  # White, Black, Red in that order
        first_pushed_off = 0
        second_pushed_off = 0
        first_reds_captured = 0
        self.first_captured = []
        self.second_captured = []
        second_reds_captured = 0
        self._board = [['W','W','O','O','O','B','B'],['W','W','O','R','O','B','B'],['O','O','R','R','R','O','O'],['O','R','R','R','R','R','O'],['O','O','R','R','R','O','O'],['B','B','O','R','O','W','W'],['B','B','O','O','O','W','W']]

    def display_board(self):  # ADDED, for testing
        """Prints the board."""
        for i in range(0,7):
            for j in range(0,7):
                print(self._board[i][j], " ",end = '')
            print(' ')

    def get_player_token(self, player_name):  # ADDED, gets token of player
        """"""
        if player_name == self._first_player:
            return self._first_token

        if player_name == self._second_player:
            return self._second_token

    def get_marble(self, coordinates):
        """Takes the coordinates of a cell as a tuple and returns the marble that is present at that location.  If no"""
        """marble is present at the coordinate location, return 'X'."""
        row = coordinates[0]
        column = coordinates[1]
        return self._board[row][column]

    def make_move(self, player_name, coordinates, direction):  # direction is Forward, Backward, Left, Right
        """To make a move, you need an empty space (or edge of the board) on the side you are pushing away from."""
        """A player can not undo a move the opponent just made."""
        x = coordinates[0]
        y = coordinates[1]
        token = self.get_player_token(player_name)

        # False base cases

        if self._winner is not None:  # Invalid Move, game is already over
            return False

        # horizontal moves
        else:
            if direction == 'L':
                if self.get_marble((x, y)) is not token:  # not your marble
                    print("Invalid move")
                    return False

                ss = -1

                if y != 6 and self.get_marble((x, y + 1)) != 'O':  # invalid move, space pushing from not empty
                    print("Invalid move")
                    return False

                # if  # cannot push off own marble
                elif True or y == 6:  # valid move
                    for i in range(0, y + 1):
                        if self._board[x][i] == 'O':
                            ss = i
                    if ss == -1 and player_name == "PlayerA":
                        self.first_captured.append(self._board[x][0])
                    if ss == -1 and player_name == "PlayerB":
                        self.second_captured.append(self._board[x][0])
                    if ss == -1:
                        st = 0
                    else:
                        st = ss
                    for i in range(st, y):
                        self._board[x][i] = self._board[x][i + 1]
                    self._board[x][y] = 'O'
                    # print(self.second_captured)
                    return True

            if direction == 'R':
                if self.get_marble((x, y)) is not token:  # not your marble
                    print("Invalid move")
                    return False

                ss = -1

                if y != 0 and self.get_marble((x, y - 1)) != 'O':  # invalid move, space pushing from not empty
                    print("Invalid move")
                    return False

                # if  # cannot push off own marble
                #
                elif True or y == 0:  # valid move
                    for i in range(y + 1, 7):
                        if self._board[x][i] == 'O':
                            ss = i
                            break
                    if ss == -1 and player_name == "PlayerA":
                        self.first_captured.append(self._board[x][6])
                    if ss == -1 and player_name == "PlayerB":
                        self.second_captured.append(self._board[x][6])
                    if ss == -1:
                        st = 7
                    else:
                        st = ss + 1
                    count = st - 1
                    for i in range(y + 1, st):
                        self._board[x][count] = self._board[x][count - 1]
                        count = count - 1
                    self._board[x][y] = 'O'
                    return True

            if direction == 'F':
                if self.get_marble((x, y)) is not token:  # not your marble
                    print("Invalid move")
                    return False

                ss = -1

                if x != 6 and self.get_marble((x + 1, y)) != 'O':  # invalid move, space pushing from not empty
                    print("Invalid move")
                    return False

                # if  # cannot push off own marble
                #
                elif True or x == 6:  # valid move
                    for i in range(0, x):
                        if self._board[i][y] == 'O':
                            ss = i
                    if ss == -1 and player_name == "PlayerA":
                        self.first_captured.append(self._board[0][y])
                    if ss == -1 and player_name == "PlayerB":
                        self.second_captured.append(self._board[0][y])
                    if ss == -1:
                        st = 0
                    else:
                        st = ss
                    for i in range(st, x):
                        self._board[i][y] = self._board[i + 1][y]
                    self._board[x][y] = 'O'
                    print(self.first_captured)
                    return True

            if direction == 'B':
                if self.get_marble((x, y)) is not token:  # not your marble
                    print("Invalid move")
                    return False

                ss = -1

                if x != 0 and self.get_marble((x - 1, y)) != 'O':  # invalid move, space pushing from not empty
                    print("Invalid move")
                    return False

                # if  # cannot push off own marble
                #
                elif True or x == 0:  # valid move
                    for i in range(x + 1, 7):
                        if self._board[i][y] == 'O':
                            ss = i
                            break
                    if ss == -1 and player_name == "PlayerA":
                        self.first_captured.append(self._board[6][y])
                    if ss == -1 and player_name == "PlayerB":
                        self.second_captured.append(self._board[6][y])
                    if ss == -1:
                        st = 7
                    else:
                        st = ss + 1
                    count = st - 1
                    for i in range(x + 1, st):
                        self._board[count][y] = self._board[count - 1][y]
                        count = count - 1
                    self._board[x][y] = 'O'
                    # print(self.first_captured)
                    return True


def main():
    game = KubaGame(('PlayerA', 'W'), ('PlayerB', 'B'))  # CORRECT, game is initialized
    print("game1")
    game.display_board()  # CORRECT, testing purposes
    game.make_move('PlayerA', (0, 0), 'B')
    game.make_move('PlayerA', (1, 0), 'B')
    game.make_move('PlayerA', (2, 0), 'B')
    game.make_move('PlayerA', (3, 0), 'B')
    game.make_move('PlayerA', (4, 0), 'B')
    print("game2")
    game.display_board()


if __name__ == '__main__':
    main()