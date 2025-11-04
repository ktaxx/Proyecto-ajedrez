
# FEN String Syntactic Analyzer – Final Project

**Course:** Programming Languages  
**University:** EAFIT University  
**Lecturer:** Alexander Narváez Berrío  
**Date:** November 3rd 2025  

## Authors

- Catalina Zuluaga Echavarria
- Jeronimo Gutierrez Gutierrez
---

## Project Description
- Reads the FEN text.
- Checks if it’s written correctly.
- Converts it into a digital board.
- Draws the board using chess symbols.
- Shows whose turn it is and other details.
- If you make a mistake in the FEN, it tells you exactly where you went wrong.

---

## Programming Language

- **Python 3**

The project was implemented in Python because it allows fast prototyping, clear string handling, and easy printing of Unicode characters in the console.

---

## Minimum Requirements

To run this project, you need:

- **Python 3.8 or higher** installed.
- An operating system capable of running Python:
  - Windows, macOS, or any modern Linux distribution.
- A terminal / console that supports **Unicode** so that the chess symbols are displayed correctly (♜♞♝♛♚, etc.).

No additional external libraries are required; the project uses only Python’s standard library.

---

## How to Run

1. **Clone or download** this repository:

  ```bash
   git clone https://github.com/YOUR_USERNAME/analizador-fen-lengprog.git
   cd analizador-fen-lengprog
  ```

2. **Run** the main script with Python:

   ```text
   python analizador_fen_proyecto_final.py
   ```

3. When prompted, **enter a valid FEN string**.
   For example, the standard initial position:

   ```text
   rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1
   ```
---
4. If the FEN string is valid, you will see:

   * The chessboard drawn on the console using Unicode pieces.
   * The side to move (White or Black).
   * Castling availability.
   * En passant target square.
   * Halfmove clock.
   * Fullmove counter.

5. If the FEN string is invalid, the program will print:

   ```text
   Invalid FEN string
   ```

   and an additional message indicating the specific error detected by the parser.


```
