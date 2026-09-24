"""
╔══════════════════════════════════════════════════════════════════╗
║  SEARCH A 2D MATRIX II                                           ║
║  LeetCode #240  |  Difficulty: Medium  |  Topic: Binary Search  ║
║  Link: https://leetcode.com/problems/search-a-2d-matrix-ii/     ║
║  Source: Striver A2Z + NeetCode 150                              ║
╚══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Given an m×n matrix where:
    - Each ROW is sorted left to right
    - Each COLUMN is sorted top to bottom
  (Unlike #74 — rows do NOT necessarily connect!)
  Search for a target and return True/False.

  Input : matrix = m×n 2D list, target = integer
  Output: True if target exists, False otherwise

  Example 1 — basic:
    Input : matrix = [[1,4,7,11,15],
                      [2,5,8,12,19],
                      [3,6,9,16,22],
                      [10,13,14,17,24],
                      [18,21,23,26,30]], target=5
    Output: True
    Why?  : 5 is at row 1, col 1

  Example 2 — not found:
    Input : same matrix, target=20
    Output: False
    Why?  : 20 is not in the matrix

  Constraints:
    - m == matrix.length, n == matrix[i].length
    - 1 <= n, m <= 300
    - -10^9 <= matrix[i][j] <= 10^9
    - Each row sorted ascending, each column sorted ascending

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Problem odi aada mele namma brain enu think maadabeeku:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  m×n matrix + target         │
  │  Output ಏನು ಬೇಕು?     →  target exists? True/False    │
  │  Constraints ಏನಿದೆ?   →  rows sorted, cols sorted     │
  │                           but rows DON'T connect!       │
  │                           (#74 ಗಿಂತ different!)        │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ನನಗೆ ಗೊತ್ತಿರೋ simple way ಏನು?
  →  Every cell check → O(m×n)
  →  Or binary search each row → O(m log n)
  →  ಆದರೆ O(m+n) solution ಇದೆ! Better think maadu.

  ಹಂತ 3 — Better way ಹೇಗೆ ಯೋಚಿಸುವುದು?
  →  "#74 ಲ್ಲಿ 1D binary search ಮಾಡಿದ್ವಿ — here rows don't connect"
  →  Key insight: TOP-RIGHT corner ಇಂದ start ಮಾಡಿದ್ರೆ?
     matrix[0][n-1] = top-right
     → If > target: eliminate entire column (go left)
     → If < target: eliminate entire row (go down)
     → Each step eliminates a full row OR column!
  →  ಇದರಿಂದ ನಾವು Staircase Search use ಮಾಡಬಹуದು — O(m+n)!

  ಹಂತ 4 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  Top-right is a "saddle point":
     → Largest in its row (row sorted left→right)
     → Smallest in its column (col sorted top→bottom)
  →  This gives us two elimination directions!
  →  Bottom-left also works same way

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು:
  →  "Unlike #74, can't do 1D binary search — rows don't connect"
  →  "Start from top-right corner — it's a saddle point"
  →  "Greater than target → go left. Less → go down. O(m+n)"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Staircase Search (Top-Right Corner)
  Secondary : Binary Search per row O(m log n)

  WHY Staircase Search?
  → Top-right element is max of its row, min of its column
  → If current > target → can eliminate entire column (go left)
  → If current < target → can eliminate entire row (go down)
  → O(m+n) — at most m+n steps total!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  The top-right element has a special property:
  - It is the LARGEST in its row (row sorted left→right)
  - It is the SMALLEST in its column (col sorted top→bottom)

  This means we can always eliminate an entire row OR column:
  - matrix[r][c] == target → found!
  - matrix[r][c] > target → this col is too big for this row
    → nothing below can help → c-- (go left)
  - matrix[r][c] < target → this row is too small for this col
    → nothing to the left can help → r++ (go down)

  We traverse at most m+n steps before going out of bounds!

  The journey from brute to optimal:
    Brute thought   →  Check every cell → O(m×n)
    Better          →  Binary search each row → O(m log n)
    Better question →  "Is there a smarter starting point?"
    Insight         →  Top-right is a saddle point → staircase!
    Optimal         →  O(m+n) staircase search

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea: Check every cell.

  Time  : O(m × n)  →  visit every cell
  Space : O(1)

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ?
    → Doesn't use sorted property at all — wasteful!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚶 SECTION 6 — APPROACH 2 — BETTER (Binary Search per row)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea: Binary search on each row independently.

  Time  : O(m log n)
  Space : O(1)

  ಇನ್ನೂ better ಮಾಡಬಹudaa?
    → YES! O(m+n) staircase search uses column property too!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 7 — APPROACH 3 — OPTIMAL (Staircase Search)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Start from top-right corner (row=0, col=n-1).
    Compare with target and eliminate row or column each step.

  Key steps:
    1. r=0, c=n-1 (top-right corner)
    2. While r < m and c >= 0:
       a. if matrix[r][c] == target → return True
       b. if matrix[r][c] > target → c-- (go left)
       c. if matrix[r][c] < target → r++ (go down)
    3. return False

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ:
    → "Top-right corner ಇಂದ start maadu (row=0, col=n-1).
       Current > target → left go (c--) — entire col eliminate.
       Current < target → down go (r++) — entire row eliminate.
       Current == target → True return maadu.
       Out of bounds iddre False. At most m+n steps!"

  Time  : O(m + n)  →  Why: at most m down + n left moves
  Space : O(1)      →  Why: only r, c pointers

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 8 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  matrix = [[1,4,7,11,15],
            [2,5,8,12,19],
            [3,6,9,16,22],
            [10,13,14,17,24],
            [18,21,23,26,30]], target=5

  Start: r=0, c=4 → matrix[0][4]=15 > 5 → c=3
  r=0, c=3 → matrix[0][3]=11 > 5 → c=2
  r=0, c=2 → matrix[0][2]=7  > 5 → c=1
  r=0, c=1 → matrix[0][1]=4  < 5 → r=1
  r=1, c=1 → matrix[1][1]=5 == 5 → return True ✓

  ಇನ್ನೊಂದು — target not found (target=20):
  r=0,c=4→15<20→r=1
  r=1,c=4→19<20→r=2
  r=2,c=4→22>20→c=3
  r=2,c=3→16<20→r=3
  r=3,c=3→17<20→r=4
  r=4,c=3→26>20→c=2
  r=4,c=2→23>20→c=1
  r=4,c=1→21>20→c=0
  r=4,c=0→18<20→r=5
  r=5 >= m=5 → return False ✓

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 9 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ 1×1 matrix?            →  [[5]], target=5 → True
  ✓ Target smaller than all →  target < matrix[0][0] → False
  ✓ Target larger than all  →  target > matrix[m-1][n-1] → False
  ✓ Single row?             →  [[1,2,3,4]] → works fine
  ✓ Single column?          →  [[1],[2],[3]] → works fine

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 10 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                  Time          Space
  Brute Force     O(m × n)      O(1)
  Per row BS      O(m log n)    O(1)
  Staircase       O(m + n)      O(1)   ← use this ✅

  Time yaake O(m+n)?
    → At most m steps down + n steps left
    → Total moves bounded by m+n
  Space yaake O(1)?
    → Only r and c pointers

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 11 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Staircase Search (Saddle Point)

  KEY DIFFERENCE between #74 and #240:
  ┌─────────────────┬──────────────────┬────────────────────┐
  │                 │ LC #74           │ LC #240            │
  ├─────────────────┼──────────────────┼────────────────────┤
  │ Row property    │ sorted           │ sorted             │
  │ Col property    │ sorted           │ sorted             │
  │ Row connection  │ YES (first>prev) │ NO                 │
  │ Approach        │ 1D binary search │ Staircase search   │
  │ Complexity      │ O(log(m×n))      │ O(m+n)             │
  └─────────────────┴──────────────────┴────────────────────┘

  Ee pattern yaavaaga use maadabeeku?
  → Row sorted + Column sorted matrix search
  → Need better than O(m log n)
  → "Saddle point" available at corners

  Idee pattern beere problemsalli kaanisatte:
  → Kth Smallest in Sorted Matrix #378
  → Count Negatives in Sorted Matrix #1351
  → Find Peak Element II #1901 (next problem!)

  Next time intaha problem bandre naanu modalu idannu think maadtene:
  → "Row sorted, col sorted matrix, rows don't connect?
     → Staircase! Top-right inda start. > iddre left, < iddre down.
     O(m+n) — very elegant!"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 12 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "Search in matrix where both rows and columns are sorted
      independently (unlike #74 where rows connect)."

  2. Brute force:
     "Check every cell — O(m×n). Binary search each row — O(m log n)."

  3. Optimize:
     "Start from top-right corner — it's a saddle point:
      largest in its row, smallest in its column.
      If current > target → entire column eliminated → go left.
      If current < target → entire row eliminated → go down.
      At most m+n steps → O(m+n)!"

  4. Code:
     "r=0, c=n-1. While in bounds: compare, adjust r or c."

  5. Complexity:
     "Time O(m+n). Space O(1)."

  Mukhya: summane kuutu code bareyabeda!
          LC #74 vs #240 difference — interviewers love this!
          Saddle point concept — explain clearly!
          Bottom-left also works — mention as alternative!
"""


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(m×n) Time | O(1) Space
# ═══════════════════════════════════════════════════════════════════
def search_matrix_brute(matrix, target):
    """Idu modala aaloochane — check every cell"""
    for row in matrix:
        for val in row:
            if val == target:
                return True
    return False


# ═══════════════════════════════════════════════════════════════════
# BETTER — O(m log n) Time | O(1) Space
# ═══════════════════════════════════════════════════════════════════
def search_matrix_binary(matrix, target):
    """Binary search on each row — O(m log n)"""
    from bisect import bisect_left
    for row in matrix:
        idx = bisect_left(row, target)
        if idx < len(row) and row[idx] == target:
            return True
    return False


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(m+n) Time | O(1) Space
# ═══════════════════════════════════════════════════════════════════
def search_matrix(matrix, target):
    """
    Idu final answer — staircase search from top-right
    Saddle point: max of row, min of column
    > target → go left (c--)
    < target → go down (r++)
    """
    m, n = len(matrix), len(matrix[0])
    r, c = 0, n - 1           # start at top-right corner

    while r < m and c >= 0:
        if matrix[r][c] == target:
            return True
        elif matrix[r][c] > target:
            c -= 1             # too big → eliminate this column
        else:
            r += 1             # too small → eliminate this row

    return False


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    matrix = [
        [1,  4,  7,  11, 15],
        [2,  5,  8,  12, 19],
        [3,  6,  9,  16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]

    # Test 1 — Found
    assert search_matrix(matrix, 5)  == True
    assert search_matrix(matrix, 1)  == True
    assert search_matrix(matrix, 30) == True

    # Test 2 — Not found
    assert search_matrix(matrix, 20) == False
    assert search_matrix(matrix, 0)  == False
    assert search_matrix(matrix, 31) == False

    # Test 3 — 1×1 matrix
    assert search_matrix([[5]], 5)   == True
    assert search_matrix([[5]], 3)   == False

    # Test 4 — Single row
    assert search_matrix([[1, 2, 3, 4, 5]], 3) == True

    # Test 5 — Single column
    assert search_matrix([[1],[2],[3],[4],[5]], 4) == True

    print("All tests passed!")
