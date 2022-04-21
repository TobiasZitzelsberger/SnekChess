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
        self.whiteToMove = True
        self.en_passant = False
        self.castling = False
        self.check = False
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

    def calculate_move_options(self, r, c, piece):
        selected_piece = piece
        if self.whiteToMove:
            me = 'w'
            enemy = 'b'
        else:
            me = 'b'
            enemy = 'w'
        # Save diagonal movement options for bishop and queen
        if selected_piece.__contains__("B") or selected_piece.__contains__("Q"):
            x = c
            y = r
            while y > 0 and x > 0 and not self.board[y - 1][x - 1].__contains__(me):
                y -= 1
                x -= 1
                self.moveOptions[y][x] = 1
                if self.board[y][x].__contains__(enemy):
                    x = 0
                    y = 0
            x = c
            y = r
            while y > 0 and x < 7 and not self.board[y - 1][x + 1].count(me):
                y -= 1
                x += 1
                self.moveOptions[y][x] = 1
                if self.board[y][x].__contains__(enemy):
                    x = 7
                    y = 0
            x = c
            y = r
            while y < 7 and x > 0 and not self.board[y + 1][x - 1].__contains__(me):
                y += 1
                x -= 1
                self.moveOptions[y][x] = 1
                if self.board[y][x].__contains__(enemy):
                    x = 0
                    y = 7
            x = c
            y = r
            while y < 7 and x < 7 and not self.board[y + 1][x + 1].__contains__(me):
                y += 1
                x += 1
                self.moveOptions[y][x] = 1
                if self.board[y][x].__contains__(enemy):
                    x = 7
                    y = 7

        # Save horizontal movement options for queen and rook
        if selected_piece.__contains__("Q") or selected_piece.__contains__("R"):
            x = c
            y = r
            while y > 0 and not self.board[y - 1][x].__contains__(me):
                y -= 1
                self.moveOptions[y][x] = 1
                if self.board[y][x].__contains__(enemy):
                    y = 0
            x = c
            y = r
            while y < 7 and not self.board[y + 1][x].count(me):
                y += 1
                self.moveOptions[y][x] = 1
                if self.board[y][x].__contains__(enemy):
                    y = 7
            x = c
            y = r
            while x > 0 and not self.board[y][x - 1].__contains__(me):
                x -= 1
                self.moveOptions[y][x] = 1
                if self.board[y][x].__contains__(enemy):
                    x = 0
            x = c
            y = r
            while x < 7 and not self.board[y][x + 1].__contains__(me):
                x += 1
                self.moveOptions[y][x] = 1
                if self.board[y][x].__contains__(enemy):
                    x = 7

        # Save movement options for knight
        if selected_piece.__contains__("N"):
            x = c + 2
            y = r + 1
            if 8 > x > -1 and 8 > y > -1 and not self.board[y][x].__contains__(me):
                self.moveOptions[y][x] = 1
            x = c + 2
            y = r - 1
            if 8 > x > -1 and 8 > y > -1 and not self.board[y][x].__contains__(me):
                self.moveOptions[y][x] = 1
            x = c - 2
            y = r + 1
            if 8 > x > -1 and 8 > y > -1 and not self.board[y][x].__contains__(me):
                self.moveOptions[y][x] = 1
            x = c - 2
            y = r - 1
            if 8 > x > -1 and 8 > y > -1 and not self.board[y][x].__contains__(me):
                self.moveOptions[y][x] = 1
            x = c + 1
            y = r + 2
            if 8 > x > -1 and 8 > y > -1 and not self.board[y][x].__contains__(me):
                self.moveOptions[y][x] = 1
            x = c - 1
            y = r + 2
            if 8 > x > -1 and 8 > y > -1 and not self.board[y][x].__contains__(me):
                self.moveOptions[y][x] = 1
            x = c + 1
            y = r - 2
            if 8 > x > -1 and 8 > y > -1 and not self.board[y][x].__contains__(me):
                self.moveOptions[y][x] = 1
            x = c - 1
            y = r - 2
            if 8 > x > -1 and 8 > y > -1 and not self.board[y][x].__contains__(me):
                self.moveOptions[y][x] = 1

        if not self.whiteToMove:
            # save movement options for black pawn
            if selected_piece == "bp":
                # forward movement
                if r < 7 and self.board[r + 1][c] == "--":
                    self.moveOptions[r + 1][c] = 1
                    if self.blackPawnLog[r][c] == 1 and self.board[r + 2][c] == "--":
                        self.moveOptions[r + 2][c] = 1
                # regular taking
                if c - 1 > 0 and self.board[r + 1][c - 1].__contains__("w"):
                    self.moveOptions[r + 1][c - 1] = 1
                if c + 1 < 7 and self.board[r + 1][c + 1].__contains__("w"):
                    self.moveOptions[r + 1][c + 1] = 1
                # en passant
                if c - 1 > 0 and self.board[r][c - 1] == "wp" and self.board[r + 1][c - 1] == "--":
                    self.moveOptions[r + 1][c - 1] = 1
                    self.en_passant = True
                if c + 1 < 7 and self.board[r][c + 1] == "wp" and self.board[r + 1][c - 1] == "--":
                    self.moveOptions[r + 1][c + 1] = 1
                    self.en_passant = True

            # Save movement options for black king
            if selected_piece == 'bK':
                self.calculate_control_logs()
                # normal movement
                x = c + 1
                y = r
                if 8 > x > -1 and 8 > y > -1 and not self.board[y][x].__contains__("b"):
                    if self.whiteControlLog[y][x] == 0:
                        self.moveOptions[y][x] = 1
                y = r + 1
                if 8 > x > -1 and 8 > y > -1 and not self.board[y][x].__contains__("b"):
                    if self.whiteControlLog[y][x] == 0:
                        self.moveOptions[y][x] = 1
                y = r - 1
                if 8 > x > -1 and 8 > y > -1 and not self.board[y][x].__contains__("b"):
                    if self.whiteControlLog[y][x] == 0:
                        self.moveOptions[y][x] = 1
                x = c
                if 8 > x > -1 and 8 > y > -1 and not self.board[y][x].__contains__("b"):
                    if self.whiteControlLog[y][x] == 0:
                        self.moveOptions[y][x] = 1
                y = r + 1
                if 8 > x > -1 and 8 > y > -1 and not self.board[y][x].__contains__("b"):
                    if self.whiteControlLog[y][x] == 0:
                        self.moveOptions[y][x] = 1
                x = c - 1
                if 8 > x > -1 and 8 > y > -1 and not self.board[y][x].__contains__("b"):
                    if self.whiteControlLog[y][x] == 0:
                        self.moveOptions[y][x] = 1
                y = r - 1
                if 8 > x > -1 and 8 > y > -1 and not self.board[y][x].__contains__("b"):
                    if self.whiteControlLog[y][x] == 0:
                        self.moveOptions[y][x] = 1
                x = c - 1
                y = r
                if 8 > x > -1 and 8 > y > -1 and not self.board[y][x].__contains__("b"):
                    if self.whiteControlLog[y][x] == 0:
                        self.moveOptions[y][x] = 1
                # castling black king
                if self.board[0][4] == "bK":
                    if self.board[0][3] == "--" and self.board[0][2] == "--" and self.board[0][1] == "--":
                        if self.whiteControlLog[0][3] == 0 and self.whiteControlLog[0][2] == 0 and self.whiteControlLog[0][1] == 0:
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
                if r > 0 and self.board[r - 1][c] == "--":
                    self.moveOptions[r - 1][c] = 1
                    if self.whitePawnLog[r][c] == 1 and self.board[r - 2][c] == "--":
                        self.moveOptions[r - 2][c] = 1
                # regular taking
                if c - 1 > 0 and self.board[r - 1][c - 1].__contains__("b"):
                    self.moveOptions[r - 1][c - 1] = 1
                if c + 1 < 7 and self.board[r - 1][c + 1].__contains__("b"):
                    self.moveOptions[r - 1][c + 1] = 1
                # en passant
                if c - 1 > 0 and self.board[r][c - 1] == "bp" and self.board[r - 1][c - 1] == "--":
                    self.moveOptions[r - 1][c - 1] = 1
                    self.en_passant = True
                if c + 1 < 7 and self.board[r][c + 1] == "bp" and self.board[r - 1][c - 1] == "--":
                    self.moveOptions[r - 1][c + 1] = 1
                    self.en_passant = True

            # Save movement options for white king
            if selected_piece == 'wK':
                self.calculate_control_logs()
                print("wK")
                print(self.blackControlLog)
                # normal movement
                x = c + 1
                y = r
                if 8 > x > -1 and 8 > y > -1 and not self.board[y][x].__contains__("w"):
                    if self.blackControlLog[y][x] == 0:
                        self.moveOptions[y][x] = 1
                y = r + 1
                if 8 > x > -1 and 8 > y > -1 and not self.board[y][x].__contains__("w"):
                    if self.blackControlLog[y][x] == 0:
                        self.moveOptions[y][x] = 1
                y = r - 1
                if 8 > x > -1 and 8 > y > -1 and not self.board[y][x].__contains__("w"):
                    if self.blackControlLog[y][x] == 0:
                        self.moveOptions[y][x] = 1
                x = c
                if 8 > x > -1 and 8 > y > -1 and not self.board[y][x].__contains__("w"):
                    if self.blackControlLog[y][x] == 0:
                        self.moveOptions[y][x] = 1
                y = r + 1
                if 8 > x > -1 and 8 > y > -1 and not self.board[y][x].__contains__("w"):
                    if self.blackControlLog[y][x] == 0:
                        self.moveOptions[y][x] = 1
                x = c - 1
                if 8 > x > -1 and 8 > y > -1 and not self.board[y][x].__contains__("w"):
                    if self.blackControlLog[y][x] == 0:
                        self.moveOptions[y][x] = 1
                y = r - 1
                if 8 > x > -1 and 8 > y > -1 and not self.board[y][x].__contains__("w"):
                    if self.blackControlLog[y][x] == 0:
                        self.moveOptions[y][x] = 1
                x = c - 1
                y = r
                if 8 > x > -1 and 8 > y > -1 and not self.board[y][x].__contains__("w"):
                    if self.blackControlLog[y][x] == 0:
                        self.moveOptions[y][x] = 1
                # castling
                if self.board[7][4] == "wK":
                    if self.board[7][3] == "--" and self.board[7][2] == "--" and self.board[7][1] == "--":
                        if self.blackControlLog[7][3] == 0 and self.blackControlLog[7][2] == 0 and self.blackControlLog[7][1] == 0:
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

    def move_piece(self, r, c, selected_r, selected_c, selected_piece):
        if self.moveOptions[r][c] == 1:
            self.board[r][c] = selected_piece
            # special pawn-movement
            if selected_piece == "wp":
                self.whitePawnLog[selected_r][selected_c] = 0
                if r == 0:
                    self.board[r][c] = "wQ"
                if self.en_passant:
                    if c == selected_c - 1:
                        self.board[selected_r][selected_c - 1] = "--"
                    if c == selected_c + 1:
                        self.board[selected_r][selected_c + 1] = "--"
            if selected_piece == "bp":
                self.blackPawnLog[selected_r][selected_c] = 0
                if r == 7:
                    self.board[r][c] = "bQ"
                if self.en_passant:
                    if c == selected_c - 1:
                        self.board[selected_r][selected_c - 1] = "--"
                    if c == selected_c + 1:
                        self.board[selected_r][selected_c + 1] = "--"
            # special king-movement
            if selected_piece == "wK":
                if selected_c > c and self.castling:
                    self.board[selected_r][selected_c - 1] = "wR"
                    self.board[r][c] = selected_piece
                    self.board[r][0] = "--"
                if selected_c < c and self.castling:
                    self.board[selected_r][selected_c + 1] = "wR"
                    self.board[r][c] = selected_piece
                    self.board[r][7] = "--"
            if selected_piece == "bK":
                if selected_c > c and self.castling:
                    self.board[selected_r][selected_c - 1] = "bR"
                    self.board[r][c] = selected_piece
                    self.board[r][0] = "--"
                if selected_c < c and self.castling:
                    self.board[selected_r][selected_c + 1] = "bR"
                    self.board[r][c] = selected_piece
                    self.board[r][7] = "--"

            self.board[selected_r][selected_c] = "--"

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
                        if self.board[y][x].__contains__(enemy):
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
                        if self.board[y][x].__contains__(enemy):
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
                        if self.board[y][x].__contains__(enemy):
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
                        if self.board[y][x].__contains__(enemy):
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
                        if self.board[y][x].__contains__(enemy):
                            y = 0
                    x = c
                    y = r
                    while y < 7 and not self.board[y + 1][x].count(me):
                        y += 1
                        if piece.__contains__("w"):
                            self.whiteControlLog[y][x] = 1
                        else:
                            self.blackControlLog[y][x] = 1
                        if self.board[y][x].__contains__(enemy):
                            y = 7
                    x = c
                    y = r
                    while x > 0 and not self.board[y][x - 1].__contains__(me):
                        x -= 1
                        if piece.__contains__("w"):
                            self.whiteControlLog[y][x] = 1
                        else:
                            self.blackControlLog[y][x] = 1
                        if self.board[y][x].__contains__(enemy):
                            x = 0
                    x = c
                    y = r
                    while x < 7 and not self.board[y][x + 1].__contains__(me):
                        x += 1
                        if piece.__contains__("w"):
                            self.whiteControlLog[y][x] = 1
                        else:
                            self.blackControlLog[y][x] = 1
                        if self.board[y][x].__contains__(enemy):
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
                    if c - 1 > 0 and r + 1 < 7:
                        self.blackControlLog[r + 1][c - 1] = 1
                    if c + 1 < 7 and r + 1 < 7:
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
                    if c - 1 > 0 and r - 1 > 0:
                        self.whiteControlLog[r - 1][c - 1] = 1
                    if c + 1 < 7 and r - 1 > 0:
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
        for r in range(8):
            for c in range(8):
                piece = self.board[r][c]
                if piece == "wK" and self.blackControlLog[r][c] == 1:
                    print("check!")
                    self.check = True
                if piece == "bK" and self.whiteControlLog[r][c] == 1:
                    print("check!")
                    self.check = True

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
