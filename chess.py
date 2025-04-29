# Converts a board position (e.g., 'a1') into an index tuple (e.g., (0, 0)).
def position_to_index(pos):
    return ord(pos[0].lower()) - ord('a'), int(pos[1]) - 1

# Converts an index tuple (e.g., (0, 0)) back into a board position (e.g., 'A1').
def index_to_position(index):
    return chr(index[0] + ord('a')).upper() + str(index[1] + 1)

# Checks if the given position is valid on a chessboard (a1 to h8).
def is_valid_position(position):
    return len(position) == 2 and 'a' <= position[0].lower() <= 'h' and '1' <= position[1] <= '8'

# Checks if the given black piece type is valid (pawn, knight, bishop, rook, queen, king).
def is_valid_piece(piece_type):
    valid_pieces = {"pawn", "knight", "bishop", "rook", "queen", "king"}
    return piece_type.lower() in valid_pieces

# Returns all possible moves for a white knight from the given position, considering the board boundaries.
def get_knight_moves(position):
    row, col = position_to_index(position)
    knight_moves = [(2, 1), (2, -1), (-2, 1), (-2, -1),
                    (1, 2), (1, -2), (-1, 2), (-1, -2)]
    moves = []
    for dx, dy in knight_moves:
        new_row, new_col = row + dx, col + dy
        if 0 <= new_row < 8 and 0 <= new_col < 8:
            moves.append((new_row, new_col))
    return moves

# Returns all possible moves for a white rook from the given position, considering the board boundaries and obstacles.
def get_rook_moves(position, all_pieces):
    row, col = position_to_index(position)
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    moves = []
    for dx, dy in directions:
        new_row, new_col = row, col
        while True:
            new_row += dx
            new_col += dy
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                new_position = (new_row, new_col)
                if new_position in all_pieces:
                    moves.append(new_position)
                    break
                else:
                    moves.append(new_position)
            else:
                break
    return moves

# Main function to handle the input and output of the chess piece capture checking program.
def main():
    white_piece = None
    black_pieces = []
    black_king_count = 0
    black_pawn_count = 0

    # Loop to get the white piece input from the user.
    while not white_piece:
        input_str = input("Enter white piece and position (e.g., knight a5): ").strip().lower()
        parts = input_str.split()
        if len(parts) != 2:
            print("Error: Invalid input format")
            continue
        piece_type, position = parts
        if piece_type not in ["knight", "rook"] or not is_valid_position(position):
            print("Error: Invalid piece type or position")
            continue
        white_piece = (piece_type.capitalize(), position)
        print(f"White piece {piece_type.capitalize()} added at {position.upper()}")

    # Loop to get the black pieces input from the user.
    while len(black_pieces) < 16:
        input_str = input("Enter black piece and position (e.g., pawn d4) or 'done' to finish: ").strip().lower()
        if input_str == "done":
            if len(black_pieces) < 1:
                print("Error: You must add at least one black piece before finishing.")
                continue
            break
        parts = input_str.split()
        if len(parts) != 2:
            print("Error: Invalid input format")
            continue
        piece_type, position = parts
        if not is_valid_piece(piece_type) or not is_valid_position(position):
            print("Error: Invalid piece type or position")
            continue
        if position == white_piece[1]:
            print("Error: Position already occupied by the white piece")
            continue
        if any(pos == position for _, pos in black_pieces):
            print("Error: Position already occupied by another black piece")
            continue
        if piece_type == "king" and black_king_count >= 1:
            print("Error: Only one black king is allowed")
            continue
        if piece_type == "pawn" and black_pawn_count >= 8:
            print("Error: Only up to eight black pawns are allowed")
            continue
        if piece_type == "king":
            black_king_count += 1
        if piece_type == "pawn":
            black_pawn_count += 1
        black_pieces.append((piece_type.capitalize(), position))
        print(f"Black piece {piece_type.capitalize()} added at {position.upper()}")

    # Create a set of all black pieces' positions.
    all_black_positions = {position_to_index(pos) for _, pos in black_pieces}

    # Determine the possible moves for the white piece.
    white_moves = []
    if white_piece[0].lower() == "knight":
        white_moves = get_knight_moves(white_piece[1])
    elif white_piece[0].lower() == "rook":
        white_moves = get_rook_moves(white_piece[1], all_black_positions)

    # Determine which black pieces can be captured.
    captures = [piece for piece in black_pieces if position_to_index(piece[1]) in white_moves]

    # Output the result.
    if captures:
        print("The white piece can capture the following black pieces:")
        for piece_type, position in captures:
            print(f"{piece_type} at {position.upper()}")
    else:
        print("The white piece cannot capture any black pieces.")

if __name__ == "__main__":
    main()

# Assumptions made:
# 1 Coordinates will always be valid chessboard coordinates (a1 to h8) (letter - y axis, number x axis)
# 2 The white piece can only be a knight or a rook
# 3 There will be at least one black piece and at most 16 black pieces
# 4 The black pieces can be of any valid type: pawn, knight, bishop, rook, queen, and king
# 5 A black piece cannot be placed on the same position as the white piece
# 6 A black piece cannot be placed on the same position as another black piece
# 7 Only one black king is allowed
# 8 Only up to eight black pawns are allowed
# 9 The user will input either "done" or a valid piece and position in various formats.
# 10 The white rook can capture only one black piece in case black pieces are on the same capture line and blocking the way for white piece
