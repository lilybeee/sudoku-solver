# Sudoku Solver using SAT (pycosat)

## Overview

This project implements a Sudoku solver by modeling the puzzle as a **Boolean Satisfiability (SAT)** problem. Instead of using traditional backtracking, the Sudoku grid is converted into **Conjunctive Normal Form (CNF)** and solved using the `pycosat` SAT solver.

The goal of this project was to understand how constraint-based problems can be formally represented and solved efficiently using SAT techniques.

---

## Approach

Each Sudoku cell is represented using Boolean variables of the form:

x(r, c, v) → True if cell (r, c) contains value v

Since SAT solvers require integer variables, each (row, column, value) combination is mapped to a unique integer ID using:

ID = (row * 9 + col) * 9 + value

This creates a total of **729 variables (9 × 9 × 9)** representing all possible assignments.

---

## CNF Encoding

The Sudoku constraints are encoded into CNF using the following six groups:

1. **Each cell contains at least one value**  
   Every cell must have at least one digit from 1 to 9.

2. **Each cell contains at most one value**  
   No cell can contain more than one digit (enforced using pairwise constraints).

3. **Each row contains every digit exactly once**  
   Each number appears exactly once in every row.

4. **Each column contains every digit exactly once**  
   Each number appears exactly once in every column.

5. **Each 3×3 subgrid contains every digit exactly once**  
   Ensures consistency within each smaller block.

6. **Pre-filled cells (input clues)**  
   Given values are added as unit clauses to restrict the solution space.

---

## Implementation Details

- For each puzzle, a fresh CNF clause set is created.
- All six constraint groups are encoded into a list of clauses.
- The CNF is passed to `pycosat.solve()`.
- If a solution exists, the satisfying assignment is decoded back into a valid Sudoku grid.
- If no solution exists, the program outputs: **"No solution found"**.

The solver supports processing **multiple puzzles in a single file**, handling each independently.

---

## Input Format

- The script is run as:
python sudoku_solver.py input.txt

- Each line in the input file represents one puzzle (81 characters).
- Digits `1–9` represent filled cells.
- `.` represents empty cells.

---

## Output Format

- Output is written to `output.txt` in the same directory.
- Each line contains the solved puzzle (81 digits).
- The order of solutions matches the input order.
- If a puzzle is unsolvable, the output will be:

---

## Example

Input: .94...13..............76..2.8..1.....32.........2...6.....5.4.......8..7..63.4..8.
Output: <81-digit valid Sudoku solution>

---

## Key Learnings

- Learned how to model real-world problems as **Constraint Satisfaction Problems (CSP)**
- Understood how to convert constraints into **Boolean logic (CNF)**
- Gained hands-on experience with **SAT solvers**
- Explored how formal problem modeling can be more efficient than brute-force approaches

---

## Tech Stack

- Python  
- pycosat  

---

## How to Run

1. Install dependency: pip install pycosat
2. Run the solver: python sudoku_solver.py input.txt

---

## Notes

- Handles multiple puzzles efficiently
- Ensures correctness across rows, columns, and subgrids
- Designed to work with automated evaluation systems
