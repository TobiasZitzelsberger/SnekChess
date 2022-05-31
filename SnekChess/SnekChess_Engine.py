class GameState:
    def __init__(self):
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
        ]

        self.wK_position = [7, 4]
        self.bK_position = [0, 4]

        self.en_passant_position = [0, 0]

        self.whiteToMove = True
        self.en_passant = False
        self.castling = False
        self.check = False
        self.checkMate = False

        # Saves movable squares of selected piece
        self.moveOptions = [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]
        ]

        self.whiteControlLog = [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [0, 1, 1, 1, 1, 1, 1, 0]
        ]

        self.blackControlLog = [
            [0, 1, 1, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]
        ]

        self.whitePawnLog = [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0]
        ]

        self.blackPawnLog = [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]
        ]

        self.attackerPositions = [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]
        ]

    def check_if_pinned_vertically(self, r, c):
        x = r
        if self.whiteToMove:
            me = "w"
            enemy = "b"
            kingPos = self.wK_position
        else:
            me = "b"
            enemy = "w"
            kingPos = self.bK_position

        if r < kingPos[0]:
            while x < kingPos[0]:
                x += 1
                if not self.board[x][c] == "--" and not self.board[x][c] == me + "K":
                    return False
            x = r
            while x > 0:
                x -= 1
                if self.board[x][c] == enemy + "R" or self.board[x][c] == enemy + "Q":
                    return True
                if not self.board[x][c] == "--":
                    return False
        x = r
        if r > kingPos[0]:
            while x > kingPos[0]:
                x -= 1
                if not self.board[x][c] == "--" and not self.board[x][c] == me + "K":
                    return False
            x = r
            while x < 7:
                x += 1
                if self.board[x][c] == enemy + "R" or self.board[x][c] == enemy + "Q":
                    return True
                if not self.board[x][c] == "--":
                    return False
        return False

    def check_if_pinned_horizontally(self, r, c):
        x = c
        if self.whiteToMove:
            me = "w"
            enemy = "b"
            kingPos = self.wK_position
        else:
            me = "b"
            enemy = "w"
            kingPos = self.bK_position

        if self.whiteToMove and r == kingPos[0]:
            if c < kingPos[1]:
                while x < kingPos[1]:
                    x += 1
                    if not self.board[r][x] == "--" and not self.board[r][x] == me + "K":
                        return False
                x = c
                while x > 0:
                    x -= 1
                    if self.board[r][x] == enemy + "R" or self.board[r][x] == enemy + "Q":
                        return True
                    if not self.board[r][x] == "--":
                        return False
            x = c
            if c > kingPos[1]:
                while x > kingPos[1]:
                    x -= 1
                    if not self.board[r][x] == "--" and not self.board[r][x] == me + "K":
                        return False
                x = c
                while x < 7:
                    x += 1
                    if self.board[r][x] == enemy + "R" or self.board[r][x] == enemy + "Q":
                        return True
                    if not self.board[r][x] == "--":
                        return False
            return False

    def check_if_pinned_diagonally_left_down(self, r, c):
        if self.whiteToMove:
            me = "w"
            enemy = "b"
        else:
            me = "b"
            enemy = "w"
        x = r
        y = c
        x2 = r
        y2 = c
        while x > 0 and y > 0:
            x -= 1
            y -= 1
            if self.board[x][y] == me + "K":
                while x2 < 7 and y2 < 7:
                    x2 += 1
                    y2 += 1
                    if self.board[x2][y2] == enemy + "Q" or self.board[x2][y2] == enemy + "B":
                        return True
                    elif not self.board[x2][y2] == "--":
                        x2 = 8
            elif not self.board[x][y] == "--":
                x = 0
        x = r
        y = c
        x2 = r
        y2 = c
        while x < 7 and y < 7:
            x += 1
            y += 1
            if self.board[x][y] == me + "K":
                while x2 > 0 and y2 > 0:
                    x2 -= 1
                    y2 -= 1
                    if self.board[x2][y2] == enemy + "Q" or self.board[x2][y2] == enemy + "B":
                        return True
                    elif not self.board[x2][y2] == "--":
                        x2 = 0
            elif not self.board[x][y] == "--":
                x = 7

    def check_if_pinned_diagonally_left_up(self, r, c):
        if self.whiteToMove:
            me = "w"
            enemy = "b"
        else:
            me = "b"
            enemy = "w"
        x = r
        y = c
        x2 = r
        y2 = c
        while x < 7 and y > 0:
            x += 1
            y -= 1
            if self.board[x][y] == me + "K":
                while x2 > 0 and y2 < 7:
                    x2 -= 1
                    y2 += 1
                    if self.board[x2][y2] == enemy + "Q" or self.board[x2][y2] == enemy + "B":
                        return True
                    elif not self.board[x2][y2] == "--":
                        x2 = 0
            elif not self.board[x][y] == "--":
                x = 7
        x = r
        y = c
        x2 = r
        y2 = c
        while x > 0 and y < 7:
            x -= 1
            y += 1
            if self.board[x][y] == me + "K":
                while x2 < 7 and y2 > 0:
                    x2 += 1
                    y2 -= 1
                    if self.board[x2][y2] == enemy + "Q" or self.board[x2][y2] == enemy + "B":
                        return True
                    elif not self.board[x2][y2] == "--":
                        x2 = 7
            elif not self.board[x][y] == "--":
                x = 0

    def check_if_pinned_diagonally(self, r, c):
        if self.check_if_pinned_diagonally_left_down(r, c) or self.check_if_pinned_diagonally_left_up(r, c):
            return True
        else:
            return False

    def calculate_move_options(self, r, c, piece):
        selected_piece = piece
        if self.whiteToMove:
            me = 'w'
            enemy = 'b'
        else:
            me = 'b'
            enemy = 'w'
        # Save diagonal movement options for bishop and queen
        if (selected_piece.__contains__("B") or selected_piece.__contains__("Q")) \
                and not self.check_if_pinned_vertically(r, c) and not self.check_if_pinned_horizontally(r, c):
            if not self.check_if_pinned_diagonally_left_up(r, c):
                cTemp = c
                rTemp = r
                while rTemp > 0 and cTemp > 0 and not self.board[rTemp - 1][cTemp - 1].__contains__(me):
                    rTemp -= 1
                    cTemp -= 1
                    self.moveOptions[rTemp][cTemp] = 1
                    if self.board[rTemp][cTemp].__contains__(enemy):
                        cTemp = 0
                        rTemp = 0
                cTemp = c
                rTemp = r
                while rTemp < 7 and cTemp < 7 and not self.board[rTemp + 1][cTemp + 1].__contains__(me):
                    rTemp += 1
                    cTemp += 1
                    self.moveOptions[rTemp][cTemp] = 1
                    if self.board[rTemp][cTemp].__contains__(enemy):
                        cTemp = 7
                        rTemp = 7

            if not self.check_if_pinned_diagonally_left_down(r, c):
                cTemp = c
                rTemp = r
                while rTemp > 0 and cTemp < 7 and not self.board[rTemp - 1][cTemp + 1].count(me):
                    rTemp -= 1
                    cTemp += 1
                    self.moveOptions[rTemp][cTemp] = 1
                    if self.board[rTemp][cTemp].__contains__(enemy):
                        cTemp = 7
                        rTemp = 0
                cTemp = c
                rTemp = r
                while rTemp < 7 and cTemp > 0 and not self.board[rTemp + 1][cTemp - 1].__contains__(me):
                    rTemp += 1
                    cTemp -= 1
                    self.moveOptions[rTemp][cTemp] = 1
                    if self.board[rTemp][cTemp].__contains__(enemy):
                        cTemp = 0
                        rTemp = 7

        # Save horizontal and vertical movement options for queen and rook
        if selected_piece.__contains__("Q") or selected_piece.__contains__("R"):
            if not self.check_if_pinned_horizontally(r, c) and not self.check_if_pinned_diagonally(r, c):
                cTemp = c
                rTemp = r
                while rTemp > 0 and not self.board[rTemp - 1][cTemp].__contains__(me):
                    rTemp -= 1
                    self.moveOptions[rTemp][cTemp] = 1
                    if self.board[rTemp][cTemp].__contains__(enemy):
                        rTemp = 0
                cTemp = c
                rTemp = r
                while rTemp < 7 and not self.board[rTemp + 1][cTemp].count(me):
                    rTemp += 1
                    self.moveOptions[rTemp][cTemp] = 1
                    if self.board[rTemp][cTemp].__contains__(enemy):
                        rTemp = 7

            if not self.check_if_pinned_vertically(r, c) and not self.check_if_pinned_diagonally(r, c):
                cTemp = c
                rTemp = r
                while cTemp > 0 and not self.board[rTemp][cTemp - 1].__contains__(me):
                    cTemp -= 1
                    self.moveOptions[rTemp][cTemp] = 1
                    if self.board[rTemp][cTemp].__contains__(enemy):
                        cTemp = 0
                cTemp = c
                rTemp = r
                while cTemp < 7 and not self.board[rTemp][cTemp + 1].__contains__(me):
                    cTemp += 1
                    self.moveOptions[rTemp][cTemp] = 1
                    if self.board[rTemp][cTemp].__contains__(enemy):
                        cTemp = 7

        # Save movement options for knight
        if selected_piece.__contains__("N") and not self.check_if_pinned_vertically(r, c) \
                and not self.check_if_pinned_horizontally(r, c) and not self.check_if_pinned_diagonally(r, c):
            cTemp = c + 2
            rTemp = r + 1
            if 8 > cTemp > -1 and 8 > rTemp > -1 and not self.board[rTemp][cTemp].__contains__(me):
                self.moveOptions[rTemp][cTemp] = 1
            cTemp = c + 2
            rTemp = r - 1
            if 8 > cTemp > -1 and 8 > rTemp > -1 and not self.board[rTemp][cTemp].__contains__(me):
                self.moveOptions[rTemp][cTemp] = 1
            cTemp = c - 2
            rTemp = r + 1
            if 8 > cTemp > -1 and 8 > rTemp > -1 and not self.board[rTemp][cTemp].__contains__(me):
                self.moveOptions[rTemp][cTemp] = 1
            cTemp = c - 2
            rTemp = r - 1
            if 8 > cTemp > -1 and 8 > rTemp > -1 and not self.board[rTemp][cTemp].__contains__(me):
                self.moveOptions[rTemp][cTemp] = 1
            cTemp = c + 1
            rTemp = r + 2
            if 8 > cTemp > -1 and 8 > rTemp > -1 and not self.board[rTemp][cTemp].__contains__(me):
                self.moveOptions[rTemp][cTemp] = 1
            cTemp = c - 1
            rTemp = r + 2
            if 8 > cTemp > -1 and 8 > rTemp > -1 and not self.board[rTemp][cTemp].__contains__(me):
                self.moveOptions[rTemp][cTemp] = 1
            cTemp = c + 1
            rTemp = r - 2
            if 8 > cTemp > -1 and 8 > rTemp > -1 and not self.board[rTemp][cTemp].__contains__(me):
                self.moveOptions[rTemp][cTemp] = 1
            cTemp = c - 1
            rTemp = r - 2
            if 8 > cTemp > -1 and 8 > rTemp > -1 and not self.board[rTemp][cTemp].__contains__(me):
                self.moveOptions[rTemp][cTemp] = 1

        if not self.whiteToMove:
            # save movement options for black pawn
            if selected_piece == "bp":
                # forward movement
                if r < 7 and self.board[r + 1][c] == "--" and not self.check_if_pinned_diagonally(r, c):
                    self.moveOptions[r + 1][c] = 1
                    if self.blackPawnLog[r][c] == 1 and self.board[r + 2][c] == "--":
                        self.moveOptions[r + 2][c] = 1
                # regular taking
                if not self.check_if_pinned_vertically(r, c) and not self.check_if_pinned_horizontally(r, c):
                    if c - 1 >= 0 and self.board[r + 1][c - 1].__contains__("w"):
                        self.moveOptions[r + 1][c - 1] = 1
                    if c + 1 <= 7 and self.board[r + 1][c + 1].__contains__("w"):
                        self.moveOptions[r + 1][c + 1] = 1
                # en passant
                if not self.check_if_pinned_vertically(r, c):
                    if c - 1 >= 0 and [r, c - 1] == self.en_passant_position and self.en_passant:
                        self.moveOptions[r + 1][c - 1] = 1
                    if c + 1 <= 7 and [r, c + 1] == self.en_passant_position and self.en_passant:
                        self.moveOptions[r + 1][c + 1] = 1

            # Save movement options for black king
            if selected_piece == 'bK':
                self.calculate_control_logs()
                # normal movement
                cTemp = c + 1
                rTemp = r
                if 8 > cTemp > -1 and 8 > rTemp > -1 and not self.board[rTemp][cTemp].__contains__("b"):
                    if self.whiteControlLog[rTemp][cTemp] == 0:
                        self.moveOptions[rTemp][cTemp] = 1
                rTemp = r + 1
                if 8 > cTemp > -1 and 8 > rTemp > -1 and not self.board[rTemp][cTemp].__contains__("b"):
                    if self.whiteControlLog[rTemp][cTemp] == 0:
                        self.moveOptions[rTemp][cTemp] = 1
                rTemp = r - 1
                if 8 > cTemp > -1 and 8 > rTemp > -1 and not self.board[rTemp][cTemp].__contains__("b"):
                    if self.whiteControlLog[rTemp][cTemp] == 0:
                        self.moveOptions[rTemp][cTemp] = 1
                cTemp = c
                if 8 > cTemp > -1 and 8 > rTemp > -1 and not self.board[rTemp][cTemp].__contains__("b"):
                    if self.whiteControlLog[rTemp][cTemp] == 0:
                        self.moveOptions[rTemp][cTemp] = 1
                rTemp = r + 1
                if 8 > cTemp > -1 and 8 > rTemp > -1 and not self.board[rTemp][cTemp].__contains__("b"):
                    if self.whiteControlLog[rTemp][cTemp] == 0:
                        self.moveOptions[rTemp][cTemp] = 1
                cTemp = c - 1
                if 8 > cTemp > -1 and 8 > rTemp > -1 and not self.board[rTemp][cTemp].__contains__("b"):
                    if self.whiteControlLog[rTemp][cTemp] == 0:
                        self.moveOptions[rTemp][cTemp] = 1
                rTemp = r - 1
                if 8 > cTemp > -1 and 8 > rTemp > -1 and not self.board[rTemp][cTemp].__contains__("b"):
                    if self.whiteControlLog[rTemp][cTemp] == 0:
                        self.moveOptions[rTemp][cTemp] = 1
                cTemp = c - 1
                rTemp = r
                if 8 > cTemp > -1 and 8 > rTemp > -1 and not self.board[rTemp][cTemp].__contains__("b"):
                    if self.whiteControlLog[rTemp][cTemp] == 0:
                        self.moveOptions[rTemp][cTemp] = 1
                # castling black king
                if self.board[0][4] == "bK":
                    if self.board[0][3] == "--" and self.board[0][2] == "--" and self.board[0][1] == "--":
                        if self.whiteControlLog[0][3] == 0 and self.whiteControlLog[0][2] == 0 \
                                and self.whiteControlLog[0][1] == 0:
                            if self.board[0][0] == "bR" and self.whiteControlLog[0][0] == 0:
                                self.moveOptions[0][3] = 1
                                self.moveOptions[0][2] = 1
                                self.castling = True
                    if self.board[0][5] == "--" and self.board[0][6] == "--":
                        if self.whiteControlLog[0][5] == 0 and self.whiteControlLog[0][6] == 0:
                            if self.board[0][7] == "bR" and self.whiteControlLog[0][7] == 0:
                                self.moveOptions[0][5] = 1
                                self.moveOptions[0][6] = 1
                                self.castling = True

        # Save movement options for white pawn
        if self.whiteToMove:
            if selected_piece == "wp":
                # forward movement
                if r > 0 and self.board[r - 1][c] == "--" and not self.check_if_pinned_diagonally(r, c):
                    self.moveOptions[r - 1][c] = 1
                    if self.whitePawnLog[r][c] == 1 and self.board[r - 2][c] == "--":
                        self.moveOptions[r - 2][c] = 1
                # regular taking
                if not self.check_if_pinned_vertically(r, c) and not self.check_if_pinned_horizontally(r, c):
                    if c - 1 >= 0 and self.board[r - 1][c - 1].__contains__("b"):
                        self.moveOptions[r - 1][c - 1] = 1
                    if c + 1 <= 7 and self.board[r - 1][c + 1].__contains__("b"):
                        self.moveOptions[r - 1][c + 1] = 1
                # en passant
                if not self.check_if_pinned_vertically(r, c):
                    if c - 1 >= 0 and [r, c - 1] == self.en_passant_position and self.en_passant:
                        self.moveOptions[r - 1][c - 1] = 1
                    if c + 1 <= 7 and [r, c + 1] == self.en_passant_position and self.en_passant:
                        self.moveOptions[r - 1][c + 1] = 1

            # Save movement options for white king
            if selected_piece == 'wK':
                self.calculate_control_logs()
                print("wK")
                print(self.blackControlLog)
                # normal movement
                cTemp = c + 1
                rTemp = r
                if 8 > cTemp > -1 and 8 > rTemp > -1 and not self.board[rTemp][cTemp].__contains__("w"):
                    if self.blackControlLog[rTemp][cTemp] == 0:
                        self.moveOptions[rTemp][cTemp] = 1
                rTemp = r + 1
                if 8 > cTemp > -1 and 8 > rTemp > -1 and not self.board[rTemp][cTemp].__contains__("w"):
                    if self.blackControlLog[rTemp][cTemp] == 0:
                        self.moveOptions[rTemp][cTemp] = 1
                rTemp = r - 1
                if 8 > cTemp > -1 and 8 > rTemp > -1 and not self.board[rTemp][cTemp].__contains__("w"):
                    if self.blackControlLog[rTemp][cTemp] == 0:
                        self.moveOptions[rTemp][cTemp] = 1
                cTemp = c
                if 8 > cTemp > -1 and 8 > rTemp > -1 and not self.board[rTemp][cTemp].__contains__("w"):
                    if self.blackControlLog[rTemp][cTemp] == 0:
                        self.moveOptions[rTemp][cTemp] = 1
                rTemp = r + 1
                if 8 > cTemp > -1 and 8 > rTemp > -1 and not self.board[rTemp][cTemp].__contains__("w"):
                    if self.blackControlLog[rTemp][cTemp] == 0:
                        self.moveOptions[rTemp][cTemp] = 1
                cTemp = c - 1
                if 8 > cTemp > -1 and 8 > rTemp > -1 and not self.board[rTemp][cTemp].__contains__("w"):
                    if self.blackControlLog[rTemp][cTemp] == 0:
                        self.moveOptions[rTemp][cTemp] = 1
                rTemp = r - 1
                if 8 > cTemp > -1 and 8 > rTemp > -1 and not self.board[rTemp][cTemp].__contains__("w"):
                    if self.blackControlLog[rTemp][cTemp] == 0:
                        self.moveOptions[rTemp][cTemp] = 1
                cTemp = c - 1
                rTemp = r
                if 8 > cTemp > -1 and 8 > rTemp > -1 and not self.board[rTemp][cTemp].__contains__("w"):
                    if self.blackControlLog[rTemp][cTemp] == 0:
                        self.moveOptions[rTemp][cTemp] = 1
                # castling
                if self.board[7][4] == "wK":
                    if self.board[7][3] == "--" and self.board[7][2] == "--" and self.board[7][1] == "--":
                        if self.blackControlLog[7][3] == 0 and self.blackControlLog[7][2] == 0 \
                                and self.blackControlLog[7][1] == 0:
                            if self.board[7][0] == "wR" and self.blackControlLog[7][0] == 0:
                                self.moveOptions[7][3] = 1
                                self.moveOptions[7][2] = 1
                                self.castling = True
                    if self.board[7][5] == "--" and self.board[7][6] == "--":
                        if self.blackControlLog[7][5] == 0 and self.blackControlLog[7][6] == 0:
                            if self.board[7][7] == "wR" and self.blackControlLog[7][7] == 0:
                                self.moveOptions[7][5] = 1
                                self.moveOptions[7][6] = 1
                                self.castling = True

    def move_piece(self, r, c, piece_r, piece_c, selected_piece):
        if self.moveOptions[r][c] == 1:
            self.board[r][c] = selected_piece
            if not selected_piece.__contains__("p"):
                self.en_passant = False
            # special pawn-movement
            if selected_piece == "wp":
                self.whitePawnLog[piece_r][piece_c] = 0
                if r == 0:
                    self.board[r][c] = "wQ"
                if self.en_passant and self.board[piece_r][piece_c - 1] == "bp" and c == piece_c - 1:
                    self.board[piece_r][piece_c - 1] = "--"
                    self.en_passant = False
                if self.en_passant and self.board[piece_r][piece_c + 1] == "bp" and c == piece_c + 1:
                    self.board[piece_r][piece_c + 1] = "--"
                    self.en_passant = False
                if piece_r == r + 2 and self.board[r][c+1] == "bp":
                    self.en_passant = True
                    self.en_passant_position = [r, c]
                if piece_r == r + 2 and self.board[r][c-1] == "bp":
                    self.en_passant = True
                    self.en_passant_position = [r, c]

            if selected_piece == "bp":
                self.blackPawnLog[piece_r][piece_c] = 0
                if r == 7:
                    self.board[r][c] = "bQ"
                if self.en_passant and self.board[piece_r][piece_c - 1] == "wp" and c == piece_c - 1:
                    self.board[piece_r][piece_c - 1] = "--"
                    self.en_passant = False
                if self.en_passant and self.board[piece_r][piece_c + 1] == "wp" and c == piece_c + 1:
                    self.board[piece_r][piece_c + 1] = "--"
                    self.en_passant = False
                if piece_r == r - 2 and self.board[r][c + 1] == "wp":
                    self.en_passant = True
                    self.en_passant_position = [r, c]
                if piece_r == r - 2 and self.board[r][c - 1] == "wp":
                    self.en_passant = True
                    self.en_passant_position = [r, c]

            # special king-movement
            if selected_piece == "wK":
                self.wK_position = [r, c]
                if piece_c > c and self.castling:
                    self.board[piece_r][piece_c - 1] = "wR"
                    self.board[r][c] = selected_piece
                    self.board[r][0] = "--"
                if piece_c < c and self.castling:
                    self.board[piece_r][piece_c + 1] = "wR"
                    self.board[r][c] = selected_piece
                    self.board[r][7] = "--"
                self.wK_position = [r, c]
            if selected_piece == "bK":
                self.bK_position = [r, c]
                if piece_c > c and self.castling:
                    self.board[piece_r][piece_c - 1] = "bR"
                    self.board[r][c] = selected_piece
                    self.board[r][0] = "--"
                if piece_c < c and self.castling:
                    self.board[piece_r][piece_c + 1] = "bR"
                    self.board[r][c] = selected_piece
                    self.board[r][7] = "--"
                self.bK_position = [r, c]

            self.board[piece_r][piece_c] = "--"

            # reset control logs
            self.blackControlLog = [
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0]
            ]
            self.whiteControlLog = [
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0]
            ]
            self.check = False
            self.check_for_check()
            if self.whiteToMove:
                self.whiteToMove = False
            else:
                self.whiteToMove = True

    # calculate controlled squares for king movement
    def calculate_control_logs(self):
        if self.whiteToMove:
            me = 'w'
            enemy = 'b'
        else:
            me = 'b'
            enemy = 'w'
        for r in range(8):
            for c in range(8):
                piece = self.board[r][c]
                # bishop and queen
                if piece.__contains__("B") or piece.__contains__("Q"):
                    x = c
                    y = r
                    while y > 0 and x > 0 and not self.board[y - 1][x - 1].__contains__(me):
                        y -= 1
                        x -= 1
                        if piece.__contains__("w"):
                            self.whiteControlLog[y][x] = 1
                        else:
                            self.blackControlLog[y][x] = 1
                        if self.board[y][x].__contains__(enemy) and not self.board[y][x].__contains__("K"):
                            x = 0
                            y = 0
                    x = c
                    y = r
                    while y > 0 and x < 7 and not self.board[y - 1][x + 1].count(me):
                        y -= 1
                        x += 1
                        if piece.__contains__("w"):
                            self.whiteControlLog[y][x] = 1
                        else:
                            self.blackControlLog[y][x] = 1
                        if self.board[y][x].__contains__(enemy) and not self.board[y][x].__contains__("K"):
                            x = 7
                            y = 0
                    x = c
                    y = r
                    while y < 7 and x > 0 and not self.board[y + 1][x - 1].__contains__(me):
                        y += 1
                        x -= 1
                        if piece.__contains__("w"):
                            self.whiteControlLog[y][x] = 1
                        else:
                            self.blackControlLog[y][x] = 1
                        if self.board[y][x].__contains__(enemy) and not self.board[y][x].__contains__("K"):
                            x = 0
                            y = 7
                    x = c
                    y = r
                    while y < 7 and x < 7 and not self.board[y + 1][x + 1].__contains__(me):
                        y += 1
                        x += 1
                        if piece.__contains__("w"):
                            self.whiteControlLog[y][x] = 1
                        else:
                            self.blackControlLog[y][x] = 1
                        if self.board[y][x].__contains__(enemy) and not self.board[y][x].__contains__("K"):
                            x = 7
                            y = 7

                # queen and rook
                if piece.__contains__("Q") or piece.__contains__("R"):
                    x = c
                    y = r
                    while y > 0 and not self.board[y - 1][x].__contains__(me):
                        y -= 1
                        if piece.__contains__("w"):
                            self.whiteControlLog[y][x] = 1
                        else:
                            self.blackControlLog[y][x] = 1
                        if self.board[y][x].__contains__(enemy) and not self.board[y][x].__contains__("K"):
                            y = 0
                    x = c
                    y = r
                    while y < 7 and not self.board[y + 1][x].count(me):
                        y += 1
                        if piece.__contains__("w"):
                            self.whiteControlLog[y][x] = 1
                        else:
                            self.blackControlLog[y][x] = 1
                        if self.board[y][x].__contains__(enemy) and not self.board[y][x].__contains__("K"):
                            y = 7
                    x = c
                    y = r
                    while x > 0 and not self.board[y][x - 1].__contains__(me):
                        x -= 1
                        if piece.__contains__("w"):
                            self.whiteControlLog[y][x] = 1
                        else:
                            self.blackControlLog[y][x] = 1
                        if self.board[y][x].__contains__(enemy) and not self.board[y][x].__contains__("K"):
                            x = 0
                    x = c
                    y = r
                    while x < 7 and not self.board[y][x + 1].__contains__(me):
                        x += 1
                        if piece.__contains__("w"):
                            self.whiteControlLog[y][x] = 1
                        else:
                            self.blackControlLog[y][x] = 1
                        if self.board[y][x].__contains__(enemy) and not self.board[y][x].__contains__("K"):
                            x = 7

                # knight
                if piece.__contains__("N"):
                    x = c + 2
                    y = r + 1
                    if 8 > x > -1 and 8 > y > -1 and not self.board[y][x].__contains__(me):
                        if piece.__contains__("w"):
                            self.whiteControlLog[y][x] = 1
                        else:
                            self.blackControlLog[y][x] = 1
                    x = c + 2
                    y = r - 1
                    if 8 > x > -1 and 8 > y > -1 and not self.board[y][x].__contains__(me):
                        if piece.__contains__("w"):
                            self.whiteControlLog[y][x] = 1
                        else:
                            self.blackControlLog[y][x] = 1
                    x = c - 2
                    y = r + 1
                    if 8 > x > -1 and 8 > y > -1 and not self.board[y][x].__contains__(me):
                        if piece.__contains__("w"):
                            self.whiteControlLog[y][x] = 1
                        else:
                            self.blackControlLog[y][x] = 1
                    x = c - 2
                    y = r - 1
                    if 8 > x > -1 and 8 > y > -1 and not self.board[y][x].__contains__(me):
                        if piece.__contains__("w"):
                            self.whiteControlLog[y][x] = 1
                        else:
                            self.blackControlLog[y][x] = 1
                    x = c + 1
                    y = r + 2
                    if 8 > x > -1 and 8 > y > -1 and not self.board[y][x].__contains__(me):
                        if piece.__contains__("w"):
                            self.whiteControlLog[y][x] = 1
                        else:
                            self.blackControlLog[y][x] = 1
                    x = c - 1
                    y = r + 2
                    if 8 > x > -1 and 8 > y > -1 and not self.board[y][x].__contains__(me):
                        if piece.__contains__("w"):
                            self.whiteControlLog[y][x] = 1
                        else:
                            self.blackControlLog[y][x] = 1
                    x = c + 1
                    y = r - 2
                    if 8 > x > -1 and 8 > y > -1 and not self.board[y][x].__contains__(me):
                        if piece.__contains__("w"):
                            self.whiteControlLog[y][x] = 1
                        else:
                            self.blackControlLog[y][x] = 1
                    x = c - 1
                    y = r - 2
                    if 8 > x > -1 and 8 > y > -1 and not self.board[y][x].__contains__(me):
                        if piece.__contains__("w"):
                            self.whiteControlLog[y][x] = 1
                        else:
                            self.blackControlLog[y][x] = 1

                # black pawn
                if piece == "bp":
                    # regular taking
                    if c - 1 >= 0 and r + 1 <= 7:
                        self.blackControlLog[r + 1][c - 1] = 1
                    if c + 1 <= 7 and r + 1 <= 7:
                        self.blackControlLog[r + 1][c + 1] = 1

                # black king
                if piece == 'bK':
                    # normal movement
                    x = c + 1
                    y = r
                    if 8 > x > -1 and 8 > y > -1 and not self.board[y][x].__contains__("b"):
                        self.blackControlLog[y][x] = 1
                    y = r + 1
                    if 8 > x > -1 and 8 > y > -1 and not self.board[y][x].__contains__("b"):
                        self.blackControlLog[y][x] = 1
                    y = r - 1
                    if 8 > x > -1 and 8 > y > -1 and not self.board[y][x].__contains__("b"):
                        self.blackControlLog[y][x] = 1
                    x = c
                    if 8 > x > -1 and 8 > y > -1 and not self.board[y][x].__contains__("b"):
                        self.blackControlLog[y][x] = 1
                    y = r + 1
                    if 8 > x > -1 and 8 > y > -1 and not self.board[y][x].__contains__("b"):
                        self.blackControlLog[y][x] = 1
                    x = c - 1
                    if 8 > x > -1 and 8 > y > -1 and not self.board[y][x].__contains__("b"):
                        self.blackControlLog[y][x] = 1
                    y = r - 1
                    if 8 > x > -1 and 8 > y > -1 and not self.board[y][x].__contains__("b"):
                        self.blackControlLog[y][x] = 1
                    x = c - 1
                    y = r
                    if 8 > x > -1 and 8 > y > -1 and not self.board[y][x].__contains__("b"):
                        self.blackControlLog[y][x] = 1

                # white pawn
                if piece == "wp":
                    # regular taking
                    if c - 1 >= 0 and r - 1 >= 0:
                        self.whiteControlLog[r - 1][c - 1] = 1
                    if c + 1 <= 7 and r - 1 >= 0:
                        self.whiteControlLog[r - 1][c + 1] = 1

                # white king
                if piece == 'wK':
                    # normal movement
                    x = c + 1
                    y = r
                    if 8 > x > -1 and 8 > y > -1 and not self.board[y][x].__contains__("w"):
                        self.whiteControlLog[y][x] = 1
                    y = r + 1
                    if 8 > x > -1 and 8 > y > -1 and not self.board[y][x].__contains__("w"):
                        self.whiteControlLog[y][x] = 1
                    y = r - 1
                    if 8 > x > -1 and 8 > y > -1 and not self.board[y][x].__contains__("w"):
                        self.whiteControlLog[y][x] = 1
                    x = c
                    if 8 > x > -1 and 8 > y > -1 and not self.board[y][x].__contains__("w"):
                        self.whiteControlLog[y][x] = 1
                    y = r + 1
                    if 8 > x > -1 and 8 > y > -1 and not self.board[y][x].__contains__("w"):
                        self.whiteControlLog[y][x] = 1
                    x = c - 1
                    if 8 > x > -1 and 8 > y > -1 and not self.board[y][x].__contains__("w"):
                        self.whiteControlLog[y][x] = 1
                    y = r - 1
                    if 8 > x > -1 and 8 > y > -1 and not self.board[y][x].__contains__("w"):
                        self.whiteControlLog[y][x] = 1
                    x = c - 1
                    y = r
                    if 8 > x > -1 and 8 > y > -1 and not self.board[y][x].__contains__("w"):
                        self.whiteControlLog[y][x] = 1

    def check_for_check(self):
        self.calculate_control_logs()
        self.attackerPositions = [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]
        ]
        for r in range(8):
            for c in range(8):
                piece = self.board[r][c]
                if piece == "wK" and self.blackControlLog[r][c] == 1:
                    print("check!")
                    self.check = True
                    r_temp = r
                    c_temp = c

                if piece == "bK" and self.whiteControlLog[r][c] == 1:
                    print("check!")
                    self.check = True
        if not self.check:
            self.blackControlLog = [
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0]
            ]
            self.whiteControlLog = [
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0]
            ]
