ex_fen = "r1b1k1nr/pp1pbp2/nqp1p3/1P4pp/2P1P3/B2B3N/P2P1PPP/RN1QK2R w KQkq - 1 8"

#mat2FEN
def matrix_to_fen(matrix):
    fen_rows = []
    
    for row in matrix:
        fen_row = ""
        empty_count = 0
        for square in row:
            if square is None:
                # Count consecutive empty squares
                empty_count += 1
            else:
                # Append empty count if any, then the piece
                if empty_count > 0:
                    fen_row += str(empty_count)
                    empty_count = 0
                fen_row += square
        
        # Append remaining empty count if the row ends with empty squares
        if empty_count > 0:
            fen_row += str(empty_count)
        
        fen_rows.append(fen_row)
    
    # Join the rows with '/' to form the board part of the FEN
    board_fen = "/".join(fen_rows)
    
    # Additional FEN fields (assuming standard starting position)
    side_to_move = "w"       # White to move
    castling = "KQkq"        # All castling rights available
    en_passant = "-"         # No en passant target square
    halfmove_clock = "0"     # Halfmove clock
    fullmove_number = "1"    # Fullmove number
    
    # Combine all parts to form the final FEN string
    fen = f"{board_fen} {side_to_move} {castling} {en_passant} {halfmove_clock} {fullmove_number}"
    
    return fen

# Example matrix representing a simple board position
example_matrix = [
    ["r", "n", "b", "q", "k", "b", "n", "r"],
    ["p", "p", "p", "p", "p", "p", "p", "p"],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    ["P", "P", "P", "P", "P", "P", "P", "P"],
    ["R", "N", "B", "Q", "K", "B", "N", "R"]
]

# Convert the matrix to FEN
fen1 = matrix_to_fen(example_matrix)
# print(fen1)  # Output should be the FEN string for the starting position


#FEN2mat
def fen_to_matrix(fen):
    # Split the FEN string at spaces to get the board part only
    board_fen = fen.split()[0]
    
    # Initialize an empty 8x8 matrix
    matrix = []
    
    # Process each row in the FEN board part
    for fen_row in board_fen.split('/'):
        row = []
        for char in fen_row:
            if char.isdigit():
                # For digits, add that many empty squares (None) to the row
                row.extend([None] * int(char))
            else:
                # For piece symbols, add the symbol directly to the row
                row.append(char)
        matrix.append(row)
    
    return matrix

# Example FEN string for the standard starting position
# fen2 = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
# fen2 = ex_fen

# Convert FEN to 8x8 matrix
matrix2 = fen_to_matrix(ex_fen)
gen_fen = matrix_to_fen(matrix2)

print(ex_fen == gen_fen)
print(gen_fen)
print(ex_fen)


# for row in matrix2:
#     print(row)
