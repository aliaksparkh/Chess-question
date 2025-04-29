# ♟️ A Chess Question

<div align="center">
  <img src="https://files.herculeschess.com/file/herculeschess/2023/02/Knight-Movement-1024x1024.png" alt="Knight Movement" width="250"/>
  <img src="https://files.herculeschess.com/file/herculeschess/2023/02/Roook-Movement-1024x1022.png" alt="Rook Movement" width="250"/>
</div>

## 📝 Description

**A Python-based tool to determine which black pieces on a chessboard can be captured by a white knight or rook.**

This program simulates basic chess mechanics and helps evaluate potential captures based on standard chess rules.

---

## 🚀 Usage

To get started, run the script [**chess.py**](https://github.com/aliaksparkh/Chess-question/blob/main/chess.py). You'll be prompted to enter:

1. The position and type of the white piece (knight or rook).
2. The positions and types of black pieces (minimum 1, maximum 16).

The script will then output which black pieces are capturable by the white piece.

---

## ✅ Assumptions

- **Coordinate System:** Uses standard algebraic notation (`a1` to `h8`) — files as letters (Y-axis), ranks as numbers (X-axis).
- **White Piece:** Only one white piece — either a knight or a rook.
- **Black Pieces:** 
  - Between 1 and 16 total.
  - Can include pawns, knights, bishops, rooks, queens, and one king.
  - A maximum of 8 pawns is allowed.
- **Positioning Rules:**
  - No overlapping pieces.
  - Black pieces cannot occupy the same square as each other or the white piece.
- **Rook Movement:** 
  - The rook can only capture one black piece per direction due to line-of-sight blocking.
- **Input Handling:** 
  - Accepts flexible formats for entering pieces and coordinates.
  - Type `'done'` to finish adding black pieces.

---

## 💡 Example Interaction

```bash
$ cd chess
$ python chess.py
Enter white piece and position (e.g., knight a5): knight a4
White piece Knight added at A4

Enter black piece and position (e.g., pawn d4) or 'done' to finish: pawn c3
Black piece Pawn added at C3

Enter black piece and position (e.g., queen c5) or 'done' to finish: queen c5
Black piece Queen added at C5

Enter black piece and position (e.g., pawn d4) or 'done' to finish: done
The white piece can capture the following black pieces:
- Pawn at C3
- Queen at C5




