"""
╔══════════════════════════════════════════════════════════════════╗
║  VALID SUDOKU                                                    ║
║  LeetCode #36  |  Difficulty: Medium  |  Topic: Arrays/HashMap  ║
║  Link: https://leetcode.com/problems/valid-sudoku/              ║
╚══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Given a 9x9 sudoku board, determine if it is valid.
  A board is valid if:
    - Each ROW has digits 1-9 with no repeats
    - Each COLUMN has digits 1-9 with no repeats
    - Each of the nine 3x3 SUB-BOXES has digits 1-9 with no repeats
  Empty cells are marked with '.'. We do NOT need to solve it,
  just check if the current filled numbers are valid.

  Input : board = 9x9 2D list of characters ('1'-'9' or '.')
  Output: True if valid, False otherwise

  Example 1 — basic:
    Input : standard partially filled sudoku board
    Output: True
    Why?  : no row, column, or 3x3 box has duplicate digits

  Example 2 — invalid:
    Input : board where row 0 has two '8's
    Output: False
    Why?  : row 0 has duplicate digit '8'

  Constraints:
    - board.length == 9, board[i].length == 9
    - board[i][j] is a digit '1'-'9' or '.'
    - We only validate, not solve

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Problem odi aada mele namma brain enu think maadabeeku:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  9x9 sudoku board            │
  │  Output ಏನು ಬೇಕು?     →  Valid ಆ ಇಲ್ಲವಾ True/False   │
  │  Constraints ಏನಿದೆ?   →  3 rules: row, col, 3x3 box   │
  │                           ಲ್ಲಿ duplicate ಇರಬಾರದು     │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ನನಗೆ ಗೊತ್ತಿರೋ simple way ಏನು?
  →  ಪ್ರತಿ row, ಪ್ರತಿ col, ಪ್ರತಿ 3x3 box ನ separately
     check ಮಾಡಿ duplicate ಇದ್ಯಾ ಅಂತ ನೋಡೋಣ
  →  ಆದರೆ ಇದು slow ಯಾಕೆ? → Actually O(81) = O(1) since
     board is always 9x9 — fixed size! But 3 passes ಮಾಡಬೇಕು

  ಹಂತ 3 — Better way ಹೇಗೆ ಯೋಚಿಸುವುದು?
  →  "ಒಂದೇ pass ಲ್ಲಿ rows, cols, boxes ಎಲ್ಲ check ಮಾಡಬಹುದಾ?"
  →  YES! ಒಂದು cell (r, c) ನೋಡಿದಾಗ:
     - row r ಗೆ add ಮಾಡು
     - col c ಗೆ add ಮಾಡು
     - box (r//3, c//3) ಗೆ add ಮಾಡು
  →  ಇದರಿಂದ ನಾವು HashMap/HashSet — single pass use ಮಾಡಬಹுದು!

  ಹಂತ 4 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  Duplicate check = HashSet perfect
  →  3x3 box index = (r//3, c//3) — key insight!
  →  Single pass ಲ್ಲಿ 3 HashSets simultaneously check ಮಾಡಬಹுದು

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು:
  →  "I need to check 3 constraints simultaneously — rows, cols, boxes"
  →  "For each cell, I can add to all 3 sets in one pass"
  →  "Key trick: box index is (row//3, col//3) — that maps any
      cell to its 3x3 box"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : HashMap/HashSet — duplicate detection
  Secondary : Matrix/2D — box index trick (r//3, c//3)

  WHY HashSet?
  → Need to detect duplicates in rows, cols, boxes
  → HashSet gives O(1) lookup and insertion
  → Three separate sets for rows, cols, boxes track independently

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  The key observation: for any cell (r, c), it belongs to exactly
  3 groups — row r, column c, and box (r//3, c//3).
  If we can check all 3 in one pass, we are done.

  The journey from brute to optimal:
    Brute thought   →  3 separate loops for rows, cols, boxes
    Problem with it →  Clean but 3 passes, repetitive code
    Better question →  "Can I check all 3 constraints at once?"
    Insight         →  Each cell contributes to row, col, AND box
                       simultaneously — use 3 sets, update all at once
    Optimal         →  Single pass, defaultdict of sets, O(81) = O(1)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Three separate passes — first check all rows, then all cols,
    then all 3x3 boxes. Use a set each time to find duplicates.

  Pseudocode:
    step 1: for each row → check no duplicate digits
    step 2: for each col → check no duplicate digits
    step 3: for each 3x3 box → check no duplicate digits
    step 4: if any check fails → return False, else True

  Time  : O(81) = O(1)  →  Why: board is always fixed 9x9
  Space : O(81) = O(1)  →  Why: sets hold at most 9 elements each

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ?
    → Actually O(1) ಆಗಿರೋದ್ರಿಂದ valid! But 3 passes instead of 1
    → Code repetitive aagatte — single pass cleaner

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 6 — APPROACH 2 — OPTIMAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Single pass through all 81 cells.
    For each non-empty cell, check and insert into 3 sets:
    rows[r], cols[c], boxes[(r//3, c//3)]
    If digit already exists in any set → invalid!

  Key steps:
    1. Create 3 defaultdict(set) — rows, cols, boxes
    2. For each cell (r, c), skip if '.'
    3. digit = board[r][c]
    4. box_key = (r // 3, c // 3)
    5. If digit in rows[r] OR cols[c] OR boxes[box_key] → False
    6. Else add digit to all 3 sets

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ:
    → "ಪ್ರತಿ cell (r,c) ನೋಡಿ, '.' ಅಲ್ಲದಿದ್ರೆ rows[r], cols[c],
       boxes[r//3, c//3] — ಮೂರು sets ಲ್ಲಿ duplicate check ಮಾಡು.
       ಇದ್ರೆ False, ಇಲ್ಲದಿದ್ರೆ add ಮಾಡಿ continue. ಕೊನೆಗೆ True!"

  Time  : O(81) = O(1)  →  Why: fixed 9x9 board, one pass
  Space : O(81) = O(1)  →  Why: sets hold max 9 elements × 27 groups

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 7 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Board row 0: ['5','3','.','.','7','.','.','.','.']

  (r=0, c=0) digit='5'  box=(0,0)  not in any set → add to rows[0], cols[0], boxes[(0,0)]
  (r=0, c=1) digit='3'  box=(0,0)  not in any set → add to rows[0], cols[1], boxes[(0,0)]
  (r=0, c=2) digit='.'  → skip
  (r=0, c=3) digit='.'  → skip
  (r=0, c=4) digit='7'  box=(0,1)  not in any set → add to rows[0], cols[4], boxes[(0,1)]
  ... continues

  Invalid case dry run:
  Board row 0: ['8','3','.','.','7','.','.','.','8']
  (r=0, c=0) digit='8' → not in sets → add '8' to rows[0]
  (r=0, c=8) digit='8' → '8' already in rows[0] → return False ✓

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 8 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ Empty board (all '.')?      →  True — nothing to violate
  ✓ Duplicate in same row?      →  Caught by rows[r] set
  ✓ Duplicate in same col?      →  Caught by cols[c] set
  ✓ Duplicate in same 3x3 box?  →  Caught by boxes[(r//3,c//3)] set
  ✓ Same digit in different row and col but same box? → Caught by box set

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 9 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                Time      Space
  Brute Force   O(1)      O(1)    3 passes
  Optimal       O(1)      O(1)    1 pass  ← use this ✅

  Time yaake O(1)?  → Board always 9x9 = 81 cells fixed
  Space yaake O(1)? → Sets hold max 9×27 = 243 entries, fixed

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 10 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: HashSet — Multi-group Duplicate Detection

  Ee pattern yaavaaga use maadabeeku?
  → Cell belongs to multiple groups simultaneously
  → Need to detect duplicates across all groups in one pass
  → Fixed size grid problems (board games, matrix validation)

  Idee pattern beere problemsalli kaanisatte:
  → Valid Sudoku Solver #37 (extension — actually fill the board)
  → N-Queens (place queens without conflicts)
  → Check if grid is valid magic square

  Next time intaha problem bandre naanu modalu idannu think maadtene:
  → "Cell multiple groups ge belong maadatte → ek pass alli
     ellaa groups simultaneously check maadu using separate sets!"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 11 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "I need to validate a 9x9 sudoku board — check that no digit
      repeats in any row, column, or 3x3 box."

  2. Brute force:
     "I could do 3 separate passes — one for rows, one for cols,
      one for boxes — using sets each time."

  3. Optimize:
     "Since each cell belongs to exactly one row, one col, and one
      box, I can check all 3 constraints in a single pass.
      The key insight is box index = (r//3, c//3)."

  4. Code:
     "I will use defaultdict(set) for rows, cols, and boxes.
      For each non-empty cell, check all 3 sets, then insert."

  5. Complexity:
     "Time and Space are both O(1) since board is always 9x9."

  Mukhya: summane kuutu code bareyabeda!
          r//3, c//3 box index trick — interviewer impressive aagatte!
"""

from collections import defaultdict


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(1) Time | O(1) Space (3 passes)
# ═══════════════════════════════════════════════════════════════════
def is_valid_sudoku_brute(board):
    """Idu modala aaloochane — 3 separate passes"""
    # Check rows
    for r in range(9):
        seen = set()
        for c in range(9):
            if board[r][c] == '.':
                continue
            if board[r][c] in seen:
                return False
            seen.add(board[r][c])

    # Check columns
    for c in range(9):
        seen = set()
        for r in range(9):
            if board[r][c] == '.':
                continue
            if board[r][c] in seen:
                return False
            seen.add(board[r][c])

    # Check 3x3 boxes
    for box_r in range(3):
        for box_c in range(3):
            seen = set()
            for r in range(box_r * 3, box_r * 3 + 3):
                for c in range(box_c * 3, box_c * 3 + 3):
                    if board[r][c] == '.':
                        continue
                    if board[r][c] in seen:
                        return False
                    seen.add(board[r][c])

    return True


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(1) Time | O(1) Space (single pass)
# ═══════════════════════════════════════════════════════════════════
def is_valid_sudoku(board):
    """Idu final answer — single pass, 3 sets simultaneously"""
    rows = defaultdict(set)
    cols = defaultdict(set)
    boxes = defaultdict(set)   # key = (r//3, c//3)

    for r in range(9):
        for c in range(9):
            digit = board[r][c]
            if digit == '.':
                continue

            box_key = (r // 3, c // 3)

            # check all 3 constraints at once
            if (digit in rows[r] or
                digit in cols[c] or
                digit in boxes[box_key]):
                return False

            # add to all 3 sets
            rows[r].add(digit)
            cols[c].add(digit)
            boxes[box_key].add(digit)

    return True


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # Test 1 — Valid board
    valid_board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    assert is_valid_sudoku(valid_board) == True

    # Test 2 — Invalid board (duplicate 8 in row)
    invalid_board = [
        ["8","3",".",".","7",".",".",".","8"],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    assert is_valid_sudoku(invalid_board) == False

    print("All tests passed!")
