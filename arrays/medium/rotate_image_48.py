"""
╔══════════════════════════════════════════════════════════════════╗
║  ROTATE IMAGE                                                     ║
║  LeetCode #48  |  Difficulty: Medium  |  Topic: Arrays / Matrix   ║
║  Link: https://leetcode.com/problems/rotate-image/                ║
╚══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Given an n x n 2D matrix representing an image, rotate it 90
  degrees CLOCKWISE, IN-PLACE — you must not allocate another 2D
  matrix for the rotation.

  Input : matrix = [[1,2,3],[4,5,6],[7,8,9]]
  Output: [[7,4,1],[8,5,2],[9,6,3]]

  Example 1 — basic:
    Input : matrix = [[1,2,3],[4,5,6],[7,8,9]]
    Output: [[7,4,1],[8,5,2],[9,6,3]]
    Why?  : the first column (7,4,1 bottom-to-top) becomes the first
             row after a 90° clockwise turn

  Example 2 — slightly tricky (4x4, even-sized matrix):
    Input : matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
    Why?  : even n means no single "center" cell, but the same
             transpose+reverse logic still handles every layer cleanly

  Constraints:
    - n == matrix.length == matrix[i].length
    - 1 <= n <= 20
    - -1000 <= matrix[i][j] <= 1000
    - Must rotate in-place (O(1) extra space, no new matrix)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ಮೊದಲು problem odidaga ನಮ್ಮ brain ಏನು think ಮಾಡಬೇಕು:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ (What are they asking?)
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  n x n square matrix               │
  │  Output ಏನು ಬೇಕು?     →  90° clockwise rotate, IN-PLACE    │
  │  Constraints ಏನಿದೆ?   →  n<=20, ಹೊಸ matrix allocate         │
  │                          ಮಾಡ್ಬಾರ್ದು (O(1) space)            │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ನನಗೆ ಗೊತ್ತಿರೋ simple way ಏನು? (Brute force thought)
  →  ಹೊಸ n x n matrix create ಮಾಡಿ, new[c][n-1-r] = old[r][c] ಅಂತ formula
     ಬಳಸಿ ತುಂಬಿಸೋದು.
  →  ಆದರೆ ಇದು slow ಯಾಕೆ? → Correct ಆಗಿದ್ರೂ, extra O(n²) space ಬೇಕಾಗುತ್ತೆ
     — problem explicitly in-place ಕೇಳ್ತಾ ಇದೆ.

  ಹಂತ 3 — Better way ಹೇಗೆ ಯೋಚಿಸುವುದು? (Optimization thought)
  →  "90° clockwise rotation ಅನ್ನ ಎರಡು simple steps ಆಗಿ break
     ಮಾಡ್ಬಹುದಾ? Transpose (rows↔columns swap) ಮಾಡಿದ ಮೇಲೆ, ಪ್ರತಿ row
     ಅನ್ನ reverse ಮಾಡಿದ್ರೆ clockwise rotation ಸಿಗುತ್ತೆ ಅಂತ ಗೊತ್ತಿದೆ."
  →  ಅಹಾ moment: Transpose (matrix[i][j], matrix[j][i] swap, i<j ಗೆ
     ಮಾತ್ರ — in-place ಆಗಿ) ಮಾಡಿದ ಮೇಲೆ, ಪ್ರತಿ row ಅನ್ನ horizontally
     reverse ಮಾಡಿದ್ರೆ, ಇದೇ 90° clockwise rotation ಆಗುತ್ತೆ — ಎರಡೂ
     steps in-place ಆಗಿ ಮಾಡ್ಬಹುದು, ಹೊಸ matrix ಬೇಡ!
  →  ಇದರಿಂದ ನಾವು Matrix → Transpose + Reverse Rows (in-place) use ಮಾಡಬಹುದು!

  ಹಂತ 4 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  Transpose swap ಇಂದ (i,j) ↔ (j,i) — n² space ಬೇಡ, in-place swap.
  →  Row reverse ಸಹ in-place two-pointer swap ಇಂದ ಆಗುತ್ತೆ.
  →  ಎರಡೂ steps combine ಆದ್ರೆ mathematically exact 90° clockwise
     rotation ಆಗುತ್ತೆ (transpose = reflect across main diagonal,
     reverse rows = reflect horizontally — ಎರಡೂ ಸೇರಿ 90° clockwise).

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು (Think out loud):
  →  "The naive approach builds a new matrix using the rotation
      formula directly — correct, but uses O(n²) extra space."
  →  "I recall that a 90-degree clockwise rotation can be decomposed
      into transpose followed by reversing each row."
  →  "Both the transpose and the row-reversal can be done in-place
      with simple swaps, so no extra matrix is needed."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Matrix → Transpose + Reverse Rows (in-place)
  Secondary : Two Pointers (for the row reversal step)

  WHY this technique?
  → In-place O(1) extra space is explicitly required, ruling out
    building a second matrix
  → 90° clockwise rotation is mathematically equal to
    transpose-then-reverse-each-row, both doable with swaps
  → Square matrix (n x n) makes transpose a clean in-place operation
    (no shape mismatch to worry about)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION (How to think — English)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Key observation: a 90° clockwise rotation moves matrix[r][c] to
  position [c][n-1-r]. Doing that directly in-place is messy because
  many cells depend on each other. But splitting it into transpose
  (matrix[r][c] <-> matrix[c][r]) followed by reversing each row
  achieves the exact same final positions using only simple, safe
  pairwise swaps.

  The journey from brute to optimal:
    Brute thought   →  allocate a new matrix, fill it using the
                        rotation formula directly
    Problem with it →  O(n²) extra space, violates in-place constraint
    Better question →  "can rotation be decomposed into two simpler
                        in-place operations?"
    Insight         →  transpose + reverse-each-row equals a 90°
                        clockwise rotation
    Optimal         →  transpose in-place, then reverse every row
                        in-place — O(1) extra space

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE (New Matrix via Formula)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Create a new n x n matrix. For every cell (r, c) in the original,
    place its value at (c, n-1-r) in the new matrix, which is exactly
    where it belongs after a 90° clockwise turn.

  Pseudocode:
    step 1: new_matrix = n x n grid of zeros
    step 2: for r in range(n):
    step 3:   for c in range(n): new_matrix[c][n-1-r] = matrix[r][c]
    step 4: copy new_matrix values back into matrix (or return new_matrix)

  Time  : O(n²)  →  Why: visits every cell once
  Space : O(n²)  →  Why: a full second matrix is allocated

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ? (Why is this not enough?)
    → Problem explicitly "do not allocate another 2D matrix" ಅಂತ
      ಕೇಳ್ತಾ ಇದೆ — in-place transpose+reverse ಇಂದ O(1) extra space
      ಗೆ ಇಳಿಸ್ಬೋದು.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚶 SECTION 6 — APPROACH 2 — BETTER (skip — brute jumps straight to optimal)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ಇಲ್ಲಿ intermediate approach ಇಲ್ಲ — new-matrix brute force ಇಂದ
  ನೇರವಾಗಿ in-place transpose+reverse optimal ಗೆ ಹೋಗಬಹುದು.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 7 — APPROACH 3 — OPTIMAL   (Transpose + Reverse Rows, in-place)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Step A — Transpose the matrix in-place: for every i < j, swap
    matrix[i][j] with matrix[j][i]. Step B — Reverse every row
    in-place using two pointers. The combination equals a 90°
    clockwise rotation.

  Key steps:
    1. for i in range(n):
         for j in range(i+1, n): swap matrix[i][j], matrix[j][i]
    2. for row in matrix: reverse row in-place (two-pointer swap)
    3. matrix is now rotated 90° clockwise, in-place

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ (Say it once in Kanglish so it sticks):
    → "ಮೊದಲು matrix ಅನ್ನ transpose ಮಾಡು — i<j ಗೆ matrix[i][j] ಮತ್ತು
        matrix[j][i] swap ಮಾಡು. ಆಮೇಲೆ ಪ್ರತಿ row ಅನ್ನ horizontally
        reverse ಮಾಡು — ಇದೇ 90° clockwise rotation!"

  Time  : O(n²)  →  Why: transpose touches ~n²/2 pairs, row reversal
                    touches all n² cells once more
  Space : O(1)   →  Why: all swaps happen in-place on the given matrix

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 8 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]

  Step A — Transpose (swap (i,j) for i<j):
    swap (0,1): 2<->4  → [[1,4,3],[2,5,6],[7,8,9]]
    swap (0,2): 3<->7  → [[1,4,7],[2,5,6],[3,8,9]]
    swap (1,2): 6<->8  → [[1,4,7],[2,5,8],[3,6,9]]
  After transpose: [[1,4,7],[2,5,8],[3,6,9]]

  Step B — Reverse each row:
    row0 [1,4,7] → [7,4,1]
    row1 [2,5,8] → [8,5,2]
    row2 [3,6,9] → [9,6,3]

  Output: [[7,4,1],[8,5,2],[9,6,3]]   matches expected

  ಇನ್ನೊಂದು example — tricky case (4x4, even n, no single center):
  Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]

  After transpose:
    [[5,2,13,15],[1,4,3,14],[9,8,6,12],[11,10,7,16]]
  After reversing each row:
    row0: [15,13,2,5]
    row1: [14,3,4,1]
    row2: [12,6,8,9]
    row3: [16,7,10,11]

  Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]   matches expected

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 9 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ 1x1 matrix?                →  transpose loop and reverse are both
                                   no-ops, matrix unchanged (correct)
  ✓ 2x2 matrix?                →  smallest case where both steps
                                   actually do work, easy to hand-verify
  ✓ Even-sized matrix (4x4)?   →  no single center cell, but the
                                   logic doesn't rely on one — still works
  ✓ All same elements?         →  swaps are no-ops visually, matrix
                                   "changes" but looks identical
  ✓ Negative numbers?          →  swaps and reversal are value-agnostic

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 10 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                Time      Space
  Brute Force   O(n²)     O(n²)
  Optimal       O(n²)     O(1)    ← use this 

  Time ಯಾಕೆ ಅಷ್ಟು?  → Transpose ~n²/2 swaps, row reversal n² cells —
                        ಎರಡೂ ಸೇರಿ ಇನ್ನೂ O(n²).
  Space ಯಾಕೆ ಅಷ್ಟು? → ಎಲ್ಲಾ swaps in-place, ಹೊಸ matrix ಬೇಡ.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 11 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Matrix → Transpose + Reverse (In-Place Rotation)

  ಈ pattern ಯಾವಾಗ use ಮಾಡಬೇಕು?
  → Square matrix ಅನ್ನ 90° rotate ಮಾಡ್ಬೇಕು ಅಂತ ಕೇಳಿದಾಗ, in-place
    constraint ಇದ್ದಾಗ
  → Complex direct-index rotation formula ಬದ್ಲು, ಎರಡು simple
    in-place operations ಗೆ break ಮಾಡ್ಬಹುದು ಅಂತ ಗೊತ್ತಾದಾಗ
    (clockwise = transpose + reverse rows; counter-clockwise =
    transpose + reverse columns)
  → O(1) extra space explicitly ಬೇಕಾದಾಗ

  ಇದೇ pattern ಬೇರೆ problems ನಲ್ಲಿ ಕಾಣಿಸುತ್ತೆ:
  → Spiral Matrix (#54) — different matrix technique, same "layer" family
  → Set Matrix Zeroes (#73) — different problem, same in-place matrix mutation idea
  → Transpose Matrix (#867) — the exact building-block operation used here

  Next time ಇಂತಹ problem ಬಂದ್ರೆ ನಾನು ಮೊದಲು ಇದನ್ನ think ಮಾಡ್ತೇನೆ:
  → "Matrix rotate in-place ಅಂತ ಕೇಳಿದ ತಕ್ಷಣ, direct formula ಬಳಸ್ದೆ,
      transpose + reverse rows/columns ಗೆ break ಮಾಡು ಅಂತ ಮೊದಲು
      ಯೋಚಿಸು."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 12 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "I need to rotate an n x n matrix 90 degrees clockwise, strictly
      in-place — no second matrix allowed."

  2. Brute force:
     "The direct approach builds a new matrix using the rotation
      formula new[c][n-1-r] = old[r][c] — correct, but O(n²) extra
      space, which violates the in-place requirement."

  3. Optimize:
     "I recall that a 90° clockwise rotation decomposes into two
      simpler steps: transpose the matrix, then reverse each row —
      both of which can be done with in-place swaps."

  4. Code:
     "I will transpose by swapping matrix[i][j] with matrix[j][i] for
      i < j, then reverse each row with a two-pointer swap — this
      combination produces the exact rotated result with O(1) extra
      space."

  5. Complexity:
     "Time O(n²) — both the transpose and row reversal touch every
      cell a constant number of times. Space O(1) — everything
      happens via in-place swaps."

  ಮುಖ್ಯ: ಸುಮ್ಮನೆ ಕೂತು code ಬರೆಯಬೇಡ!
         Interviewer ಗೆ ನಿನ್ನ thinking process ಕಾಣಬೇಕು.
"""


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(n^2) Time | O(n^2) Space  (New Matrix via Formula)
# ═══════════════════════════════════════════════════════════════════
def rotate_brute(matrix):
    """ಇದು ಮೊದಲ ಆಲೋಚನೆ — ಹೊಸ matrix create ಮಾಡಿ rotation formula ಬಳಸೋದು"""
    n = len(matrix)
    new_matrix = [[0] * n for _ in range(n)]

    for r in range(n):
        for c in range(n):
            new_matrix[c][n - 1 - r] = matrix[r][c]

    for r in range(n):
        for c in range(n):
            matrix[r][c] = new_matrix[r][c]

    return matrix


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n^2) Time | O(1) Space  (Transpose + Reverse Rows, in-place)
# ═══════════════════════════════════════════════════════════════════
def rotate(matrix):
    """ಇದು final answer — in-place transpose ಮಾಡಿ ಆಮೇಲೆ ಪ್ರತಿ row reverse ಮಾಡು"""
    n = len(matrix)

    # Step A — transpose in-place
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step B — reverse every row in-place
    for row in matrix:
        left, right = 0, n - 1
        while left < right:
            row[left], row[right] = row[right], row[left]
            left += 1
            right -= 1

    return matrix


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")   # Windows cp1252 can't print emoji otherwise

    # Test 1 — Basic example
    assert rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

    # Test 2 — Edge case: single element
    assert rotate([[5]]) == [[5]]

    # Test 3 — Edge case: all same elements
    assert rotate([[1, 1], [1, 1]]) == [[1, 1], [1, 1]]

    # Test 4 — Tricky: even-sized 4x4 matrix
    assert rotate([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]) == \
        [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]

    print("All tests passed! ")
