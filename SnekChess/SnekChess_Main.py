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
                    piece = gs.board[r][c]
                    print(piece)
                    if piece != "--":
                        if (piece.__contains__("b") and not gs.whiteToMove) or (piece.__contains__("w")
                                                                                and gs.whiteToMove):
                            piece_is_selected = True
                            selected_c = c
                            selected_r = r
                            selected_piece = piece
                            # Save movement options
                            gs.calculate_move_options(r, c, piece)
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
                    # Movement
                    gs.move_piece(r, c, selected_r, selected_c, selected_piece)
                    # Cancel movement by clicking on un-highlighted square
                    piece_is_selected = False
                    gs.moveOptions = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                                      [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                                      [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
                    gs.castling = False
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
    draw_board(screen, gs.board, gs.moveOptions)


if __name__ == "__main__":
    main()
