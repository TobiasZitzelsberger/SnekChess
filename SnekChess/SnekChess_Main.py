import math

import pygame as p
from SnekChess import SnekChess_Engine

WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 20
IMAGES = {}


# Initialize  a global directory of images.
def load_images():
    pieces = ['wp', 'wR', 'wN', 'wB', 'wQ', 'wK', 'bp', 'bR', 'bN', 'bB', 'bQ', 'bK']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))


# The main driver: user input, updating, graphics etc.
def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    p.display.set_caption("SnekChess")
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = SnekChess_Engine.GameState()

    piece_is_selected = False
    selected_c = 0
    selected_r = 0
    selected_piece = "--"

    load_images()
    running = True
    draw_game_state(screen, gs)
    clock.tick(MAX_FPS)
    p.display.flip()
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
        clock.tick(MAX_FPS)

        if not piece_is_selected:
            for selectPiece in p.event.get():
                if selectPiece.type == p.MOUSEBUTTONUP:
                    mouse_x, mouse_y = p.mouse.get_pos()
                    c = math.ceil(mouse_x / 64) - 1
                    r = math.ceil(mouse_y / 64) - 1
                    print(r)
                    print(c)
                    piece = gs.board[r][c]
                    print(piece)
                    print(gs.moveLogClear)
                    if piece != "--" and piece.__contains__("w"):
                        piece_is_selected = True
                        selected_c = c
                        selected_r = r
                        selected_piece = piece
                        # Highlight movement options for pawn
                        if selected_piece == "wp":
                            if gs.board[r-1][c] == "--":
                                gs.moveLog[r-1][c] = 1
                            if c-1 > 0 and gs.board[r-1][c-1].__contains__("b"):
                                gs.moveLog[r-1][c-1] = 1
                            if c+1 < 7 and gs.board[r-1][c+1].__contains__("b"):
                                gs.moveLog[r-1][c+1] = 1
                        # Highlight diagonal movement options for bishop and queen
                        if selected_piece == "wB" or selected_piece == "wQ":
                            x = c
                            y = r
                            while y > 0 and x > 0 and not gs.board[y-1][x-1].__contains__("w"):
                                y -= 1
                                x -= 1
                                gs.moveLog[y][x] = 1
                                if gs.board[y][x].__contains__("b"):
                                    x = 0
                                    y = 0

                            x = c
                            y = r
                            while y > 0 and x < 7 and not gs.board[y-1][x+1].count("w"):
                                y -= 1
                                x += 1
                                gs.moveLog[y][x] = 1
                                if gs.board[y][x].__contains__("b"):
                                    x = 7
                                    y = 0

                            x = c
                            y = r
                            while y < 7 and x > 0 and not gs.board[y + 1][x - 1].__contains__("w"):
                                y += 1
                                x -= 1
                                gs.moveLog[y][x] = 1
                                if gs.board[y][x].__contains__("b"):
                                    x = 0
                                    y = 7

                            x = c
                            y = r
                            while y < 7 and x < 7 and not gs.board[y + 1][x + 1].__contains__("w"):
                                y += 1
                                x += 1
                                gs.moveLog[y][x] = 1
                                if gs.board[y][x].__contains__("b"):
                                    x = 7
                                    y = 7

                        # Highlight horizontal movement options for queen and rook
                        if selected_piece == "wQ" or selected_piece == "wR":
                            x = c
                            y = r
                            while y > 0 and not gs.board[y - 1][x].__contains__("w"):
                                y -= 1
                                gs.moveLog[y][x] = 1
                                if gs.board[y][x].__contains__("b"):
                                    y = 0

                            x = c
                            y = r
                            while y < 7 and not gs.board[y + 1][x].count("w"):
                                y += 1
                                gs.moveLog[y][x] = 1
                                if gs.board[y][x].__contains__("b"):
                                    y = 7

                            x = c
                            y = r
                            while x > 0 and not gs.board[y][x - 1].__contains__("w"):
                                x -= 1
                                gs.moveLog[y][x] = 1
                                if gs.board[y][x].__contains__("b"):
                                    x = 0

                            x = c
                            y = r
                            while x < 7 and not gs.board[y][x + 1].__contains__("w"):
                                x += 1
                                gs.moveLog[y][x] = 1
                                if gs.board[y][x].__contains__("b"):
                                    x = 7
                        draw_game_state(screen, gs)
                        # Highlight selected piece
                        colors_move_log = [p.Color("blue"), p.Color("darkblue")]
                        color_move_log = colors_move_log[((r + c) % 2)]
                        p.draw.rect(screen, color_move_log, p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                        screen.blit(IMAGES[selected_piece], p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                        p.display.flip()

        if piece_is_selected:
            for movePiece in p.event.get():
                if movePiece.type == p.MOUSEBUTTONUP:
                    mouse_x, mouse_y = p.mouse.get_pos()
                    c = math.ceil(mouse_x / 64) - 1
                    r = math.ceil(mouse_y / 64) - 1
                    # Cancel movement by clicking on the selected piece
                    if c == selected_c and r == selected_r:
                        piece_is_selected = False
                        gs.moveLog = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                                      [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                                      [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
                        draw_game_state(screen, gs)
                        p.display.flip()
                    # Movement
                    if gs.moveLog[r][c] == 1:
                        gs.board[selected_r][selected_c] = "--"
                        gs.board[r][c] = selected_piece
                        if r == 0 and selected_piece == "wp":
                            gs.board[r][c] = "wQ"
                        piece_is_selected = False
                        gs.moveLog = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                                      [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                                      [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
                        draw_game_state(screen, gs)
                        p.display.flip()


# Draws the squares and pieces on the board
def draw_board(screen, board, move_log):
    colors = [p.Color("white"), p.Color("darkgrey")]
    colors_move_log = [p.Color("blue"), p.Color("darkblue")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r + c) % 2)]
            p.draw.rect(screen, color, p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))
            if move_log[r][c] == 1:
                color_move_log = colors_move_log[((r + c) % 2)]
                p.draw.rect(screen, color_move_log, p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))
            piece = board[r][c]
            if piece != "--":
                screen.blit(IMAGES[piece], p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))


# Responsible for graphics in current game state
def draw_game_state(screen, gs):
    colors = [p.Color("white"), p.Color("darkgrey")]
    colors_move_log = [p.Color("blue"), p.Color("darkblue")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r + c) % 2)]
            p.draw.rect(screen, color, p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))
            if gs.moveLog[r][c] == 1:
                color_move_log = colors_move_log[((r + c) % 2)]
                p.draw.rect(screen, color_move_log, p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))
            piece = gs.board[r][c]
            if piece != "--":
                screen.blit(IMAGES[piece], p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))


if __name__ == "__main__":
    main()
