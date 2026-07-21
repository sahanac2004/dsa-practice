"""
╔════════════════════════════════════════════════════════════════════════════╗
║  SPIRAL MATRIX                                                             ║
║  LeetCode #54  |  Difficulty: Medium  |  Topic: Arrays / Matrix Simulation ║
║  Link: https://leetcode.com/problems/spiral-matrix/                        ║
╚════════════════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Given an m x n matrix, return all its elements in spiral order —
  right across the top row, down the right column, left across the
  bottom row, up the left column, then repeat inward.

  Input : matrix = [[1,2,3],[4,5,6],[7,8,9]]
  Output: [1,2,3,6,9,8,7,4,5]

  Example 1 — basic:
    Input : matrix = [[1,2,3],[4,5,6],[7,8,9]]
    Output: [1,2,3,6,9,8,7,4,5]
    Why?  : top row right (1,2,3), right col down (6,9), bottom row
             left (8,7), left col up (4), then the lone center (5)

  Example 2 — slightly tricky (non-square, rectangular matrix):
    Input : matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    Output: [1,2,3,4,8,12,11,10,9,5,6,7]
    Why?  : with unequal rows/cols, boundaries shrink asymmetrically —
             must carefully re-check bounds before each of the 4 directions

  Constraints:
    - m == matrix.length, n == matrix[i].length
    - 1 <= m, n <= 10
    - -100 <= matrix[i][j] <= 100

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ಮೊದಲು problem odidaga ನಮ್ಮ brain ಏನು think ಮಾಡಬೇಕು:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ (What are they asking?)
  ┌─────────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  m x n 2D matrix                    │
  │  Output ಏನು ಬೇಕು?     →  spiral order ನಲ್ಲಿ ಎಲ್ಲಾ elements  │
  │                          ಒಂದೇ list ಆಗಿ                     │
  │  Constraints ಏನಿದೆ?   →  m,n<=10, rectangular ಆಗ್ಬೋದು      │
  │                          (square ಅಲ್ಲ ಅಂತ ಸಹ)            │
  └─────────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ನನಗೆ ಗೊತ್ತಿರೋ simple way ಏನು? (Brute force thought)
  →  ನೇರವಾಗಿ direction simulate ಮಾಡೋದೇ ಇಲ್ಲಿ natural approach —
     ಬೇರೆ "brute force" ಇಲ್ಲ, simulation ಒಂದೇ way.
  →  ಆದ್ರೆ ಸರಿಯಾಗಿ ಮಾಡ್ದೇ ಇದ್ರೆ (visited array ಇಲ್ಲದೆ boundary track
     ಮಾಡ್ದೇ ಇದ್ರೆ) ಅದೇ cell ಅನ್ನ ಮತ್ತೆ visit ಮಾಡ್ಬೋದು ಅಥವಾ bounds
     ಮೀರ್ಬೋದು.

  ಹಂತ 3 — Better way ಹೇಗೆ ಯೋಚಿಸುವುದು? (Optimization thought)
  →  "4 boundaries ಇಟ್ಕೊಂಡು — top, bottom, left, right — ಪ್ರತಿ layer
     ಮುಗಿದ ಮೇಲೆ ಆ boundary ಅನ್ನ shrink ಮಾಡ್ತಾ ಹೋದ್ರೆ, visited array
     ಬೇಡ, boundaries ಸ್ವತಃ 'ಇನ್ನೂ visit ಮಾಡದ region' track ಮಾಡುತ್ತೆ."
  →  ಅಹಾ moment: ಪ್ರತಿ full "layer" (outer ring) ಗೂ 4 steps —
     top row (left→right), right col (top→bottom), ಆಮೇಲೆ *if bottom
     row still valid* bottom row (right→left), *if left col still
     valid* left col (bottom→top). ಈ "if still valid" checks ಇಲ್ಲದೆ
     rectangular/single-row/single-col matrices ನಲ್ಲಿ duplicate visit
     ಆಗುತ್ತೆ.
  →  ಇದರಿಂದ ನಾವು Matrix Simulation → 4-Boundary Shrinking use ಮಾಡಬಹುದು!

  ಹಂತ 4 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  Spiral ಅಂದ್ರೆ ಸ್ವತಃ "ring by ring shrink ಆಗ್ತಾ ಹೋಗೋ" pattern —
     top/bottom/left/right boundaries ಇಂದ ನೇರವಾಗಿ model ಮಾಡ್ಬಹುದು.
  →  Rectangular matrix ಗೂ (m != n) ಇದೇ logic ಸರಿಯಾಗಿ ಕೆಲಸ ಮಾಡುತ್ತೆ —
     boundaries independently shrink ಆಗ್ತಾ ಇರೋದ್ರಿಂದ.
  →  "top > bottom" ಅಥವಾ "left > right" check ಇಂದ single row/column
     ಉಳಿದಾಗ duplicate visits ತಪ್ಪಿಸ್ಬಹುದು.

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು (Think out loud):
  →  "This is a pure simulation problem — I'll maintain four
      boundaries: top, bottom, left, right."
  →  "I traverse the top row left-to-right, then the right column
      top-to-bottom, then — only if the boundaries are still valid —
      the bottom row right-to-left and the left column bottom-to-top."
  →  "After each side, I shrink the corresponding boundary inward,
      and repeat until top > bottom or left > right."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Matrix Simulation → 4-Boundary Shrinking
  Secondary : None

  WHY this technique?
  → Spiral order is naturally a shrinking-ring pattern — four moving
    boundaries (top, bottom, left, right) model it directly
  → Works correctly for non-square (rectangular) matrices since each
    boundary shrinks independently
  → Avoids needing a separate "visited" grid — the boundaries
    themselves define the unvisited region

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION (How to think — English)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Key observation: after finishing the top row and right column, we
  must re-check whether top <= bottom and left <= right before doing
  the bottom row and left column — otherwise a single remaining row
  or column gets traversed twice (once forward, once backward).

  The journey from brute to optimal:
    Brute thought   →  simulate directions with a visited grid or
                        careless boundary tracking
    Problem with it →  risk of double-visiting cells or going
                        out-of-bounds on rectangular/degenerate matrices
    Better question →  "can four shrinking boundaries alone define
                        exactly what's left to visit?"
    Insight         →  yes — after each side, shrink that boundary,
                        and guard the last two sides with validity checks
    Optimal         →  4-boundary simulation, O(1) extra space besides
                        the output list

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE (Simulation + Visited Grid)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Walk in the current direction (right, down, left, up cyclically),
    marking cells visited. When the next cell is out of bounds or
    already visited, turn 90 degrees clockwise and continue. Stop
    once m*n cells have been collected.

  Pseudocode:
    step 1: visited = set(), result = []
    step 2: directions = [right, down, left, up], dir_idx = 0
    step 3: r, c = 0, 0
    step 4: while len(result) < m*n:
    step 5:   result.append(matrix[r][c]); visited.add((r,c))
    step 6:   try move in current direction; if out of bounds or visited: turn
    step 7:   move to new (r,c)
    step 8: return result

  Time  : O(m*n)  →  Why: every cell visited exactly once
  Space : O(m*n)  →  Why: visited set stores every cell's coordinates

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ? (Why is this not enough?)
    → Correct, ಆದ್ರೆ visited set ಇಂದ extra O(m*n) space ಬೇಕಾಗುತ್ತೆ —
      boundary-shrinking ಇಂದ ಅದೇ result ಅನ್ನ extra space ಇಲ್ಲದೆ
      ಪಡಿಬಹುದು (output ಬಿಟ್ಟು).

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚶 SECTION 6 — APPROACH 2 — BETTER (skip — brute maps directly to boundary version)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ಇಲ್ಲಿ intermediate approach ಇಲ್ಲ — visited-set simulation ಇಂದ
  ನೇರವಾಗಿ boundary-shrinking optimal ಗೆ ಹೋಗಬಹುದು.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 7 — APPROACH 3 — OPTIMAL   (4-Boundary Shrinking)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Track top, bottom, left, right boundaries. Repeatedly: walk the
    top row left→right then top+=1; walk the right col top→bottom
    then right-=1; IF top<=bottom, walk the bottom row right→left
    then bottom-=1; IF left<=right, walk the left col bottom→top
    then left+=1. Stop when top>bottom or left>right.

  Key steps:
    1. top, bottom, left, right = 0, m-1, 0, n-1; result = []
    2. while top <= bottom and left <= right:
         for c in range(left, right+1): result.append(matrix[top][c])
         top += 1
         for r in range(top, bottom+1): result.append(matrix[r][right])
         right -= 1
         if top <= bottom:
             for c in range(right, left-1, -1): result.append(matrix[bottom][c])
             bottom -= 1
         if left <= right:
             for r in range(bottom, top-1, -1): result.append(matrix[r][left])
             left += 1
    3. Return result

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ (Say it once in Kanglish so it sticks):
    → "top,bottom,left,right boundaries ಇಟ್ಕೊಂಡು — top row left→right
        collect ಮಾಡಿ top++, right col top→bottom collect ಮಾಡಿ right--,
        (top<=bottom ಆದ್ರೆ) bottom row right→left collect ಮಾಡಿ
        bottom--, (left<=right ಆದ್ರೆ) left col bottom→top collect
        ಮಾಡಿ left++! top>bottom ಅಥವಾ left>right ಆಗೋವರೆಗೂ repeat!"

  Time  : O(m*n)  →  Why: every cell appended to result exactly once
  Space : O(1)    →  Why: excluding the output list, only 4 boundary
                     variables used

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 8 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]  (m=3,n=3)

  top=0,bottom=2,left=0,right=2
  Round 1:
    top row (c=0..2): 1,2,3 → top=1
    right col (r=1..2): 6,9 → right=1
    top(1)<=bottom(2) → bottom row (c=1..0): 8,7 → bottom=1
    left(0)<=right(1) → left col (r=1..1): 4 → left=1
  top=1,bottom=1,left=1,right=1  (still top<=bottom, left<=right)
  Round 2:
    top row (c=1..1): 5 → top=2
    right col (r=2..1): none (range empty since top=2>bottom=1) → right=0
    top(2)<=bottom(1)? No → skip bottom row
    left(1)<=right(0)? No → skip left col
  top=2>bottom=1 → outer loop ends

  Output: [1,2,3,6,9,8,7,4,5]   matches expected

  ಇನ್ನೊಂದು example — tricky case (rectangular, non-square):
  Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]  (m=3,n=4)

  top=0,bottom=2,left=0,right=3
  Round 1:
    top row: 1,2,3,4 → top=1
    right col (r=1..2): 8,12 → right=2
    top(1)<=bottom(2) → bottom row (c=2..0): 11,10,9 → bottom=1
    left(0)<=right(2) → left col (r=1..1): 5 → left=1
  top=1,bottom=1,left=1,right=2
  Round 2:
    top row (c=1..2): 6,7 → top=2
    right col (r=2..1): none → right=1
    top(2)<=bottom(1)? No → skip
    left(1)<=right(1)? Yes → left col (r=1..2): none since top=2>bottom=1
      -- wait, r ranges bottom..top-1 = 1..1: adds matrix[1][1]=6 again?
  (Note: after top row shrinks past bottom, right/left col loops
   naturally produce empty ranges once top>bottom, so nothing extra
   is added — verified by the actual code execution below.)
  top=2>bottom=1 → outer loop ends

  Output: [1,2,3,4,8,12,11,10,9,5,6,7]   matches expected (verified
    by running the code — the range guards correctly produce empty
    iterations where needed)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 9 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ Single row matrix?        →  top row loop grabs everything, all
                                  later loops produce empty ranges
  ✓ Single column matrix?     →  top row loop grabs one cell, right
                                  col loop grabs the rest
  ✓ Single cell (1x1)?        →  one element added, loop ends after
                                  first top-row pass
  ✓ Rectangular (m != n)?     →  boundaries shrink independently and
                                  correctly, guarded by top<=bottom /
                                  left<=right checks
  ✓ Negative numbers in matrix? →  values just get appended as-is,
                                  no special handling needed

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 10 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                Time      Space
  Brute Force   O(m*n)    O(m*n)  (visited set)
  Optimal       O(m*n)    O(1)    ← use this  (excluding output)

  Time ಯಾಕೆ ಅಷ್ಟು?  → ಪ್ರತಿ cell ಒಂದೇ ಸಲ result ಗೆ add ಆಗುತ್ತೆ.
  Space ಯಾಕೆ ಅಷ್ಟು? → 4 boundary variables ಬಿಟ್ಟು extra structure ಬೇಡ
                        (output list ಅನ್ನ count ಮಾಡಲ್ಲ).

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 11 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Matrix Simulation — 4-Boundary Shrinking

  ಈ pattern ಯಾವಾಗ use ಮಾಡಬೇಕು?
  → Matrix ಅನ್ನ ring-by-ring / layer-by-layer traverse ಮಾಡ್ಬೇಕಾದಾಗ
  → Direction ಬದಲಾಗ್ತಾ ಇರೋ traversal (spiral, boundary trace) ಕೇಳಿದಾಗ
  → Rectangular matrices ಗೂ ಕೆಲಸ ಮಾಡ್ಬೇಕಾದ correct boundary handling
    ಬೇಕಾದಾಗ

  ಇದೇ pattern ಬೇರೆ problems ನಲ್ಲಿ ಕಾಣಿಸುತ್ತೆ:
  → Spiral Matrix II (#59) — generate instead of read, same boundaries
  → Rotate Image (#48) — different matrix technique, same "layer" thinking
  → Set Matrix Zeroes (#73) — different problem, same matrix-traversal family

  Next time ಇಂತಹ problem ಬಂದ್ರೆ ನಾನು ಮೊದಲು ಇದನ್ನ think ಮಾಡ್ತೇನೆ:
  → "Matrix ಅನ್ನ spiral/ring order ನಲ್ಲಿ traverse ಮಾಡ್ಬೇಕು ಅಂತ ಕೇಳಿದ
      ತಕ್ಷಣ, top/bottom/left/right 4 boundaries ಇಟ್ಕೊಂಡು shrink
      ಮಾಡ್ತಾ ಹೋಗು, ಕೊನೆಯ 2 sides ಗೆ validity check ಹಾಕೋಕೆ ಮರೀಬೇಡ."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 12 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "I need to return all elements of the matrix in spiral order —
      right across the top, down the right side, left across the
      bottom, up the left side, shrinking inward each layer."

  2. Brute force:
     "I could simulate direction changes with a visited set to know
      when to turn — O(m*n) time but O(m*n) extra space for tracking
      visited cells."

  3. Optimize:
     "Instead of a visited set, I maintain four shrinking boundaries —
      top, bottom, left, right — which by themselves define exactly
      what's left to visit, no extra space needed."

  4. Code:
     "I will use 4-boundary simulation: traverse each side in order,
      shrinking that boundary afterward, and guard the bottom row and
      left column traversals with a check that top<=bottom and
      left<=right respectively, to avoid re-visiting a collapsed row
      or column."

  5. Complexity:
     "Time O(m*n) — every cell is visited exactly once. Space O(1)
      excluding the output list — just four boundary variables."

  ಮುಖ್ಯ: ಸುಮ್ಮನೆ ಕೂತು code ಬರೆಯಬೇಡ!
         Interviewer ಗೆ ನಿನ್ನ thinking process ಕಾಣಬೇಕು.
"""


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(m*n) Time | O(m*n) Space  (Simulation + Visited Set)
# ═══════════════════════════════════════════════════════════════════
def spiral_order_brute(matrix):
    """ಇದು ಮೊದಲ ಆಲೋಚನೆ — direction simulate ಮಾಡಿ visited set ಇಂದ turn ಗುರುತಿಸೋದು"""
    if not matrix or not matrix[0]:
        return []

    m, n = len(matrix), len(matrix[0])
    visited = set()
    result = []
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
    dir_idx = 0
    r, c = 0, 0

    for _ in range(m * n):
        result.append(matrix[r][c])
        visited.add((r, c))
        dr, dc = directions[dir_idx]
        nr, nc = r + dr, c + dc
        if not (0 <= nr < m and 0 <= nc < n) or (nr, nc) in visited:
            dir_idx = (dir_idx + 1) % 4
            dr, dc = directions[dir_idx]
            nr, nc = r + dr, c + dc
        r, c = nr, nc

    return result


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(m*n) Time | O(1) Space  (4-Boundary Shrinking)
# ═══════════════════════════════════════════════════════════════════
def spiral_order(matrix):
    """ಇದು final answer — top/bottom/left/right boundaries shrink ಮಾಡ್ತಾ collect ಮಾಡು"""
    if not matrix or not matrix[0]:
        return []

    m, n = len(matrix), len(matrix[0])
    top, bottom, left, right = 0, m - 1, 0, n - 1
    result = []

    while top <= bottom and left <= right:
        for c in range(left, right + 1):
            result.append(matrix[top][c])
        top += 1

        for r in range(top, bottom + 1):
            result.append(matrix[r][right])
        right -= 1

        if top <= bottom:
            for c in range(right, left - 1, -1):
                result.append(matrix[bottom][c])
            bottom -= 1

        if left <= right:
            for r in range(bottom, top - 1, -1):
                result.append(matrix[r][left])
            left += 1

    return result


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")   # Windows cp1252 can't print emoji otherwise

    # Test 1 — Basic example
    assert spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]

    # Test 2 — Edge case: single element
    assert spiral_order([[7]]) == [7]

    # Test 3 — Edge case: single row
    assert spiral_order([[1, 2, 3, 4]]) == [1, 2, 3, 4]

    # Test 4 — Tricky: rectangular (non-square) matrix
    assert spiral_order([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) == \
        [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]

    print("All tests passed! ")
