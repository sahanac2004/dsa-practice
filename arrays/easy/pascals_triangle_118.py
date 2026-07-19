"""
╔══════════════════════════════════════════════════════════════════╗
║  PASCAL'S TRIANGLE                                               ║
║  LeetCode #118  |  Difficulty: Easy  |  Topic: Arrays / 2D-DP    ║
║  Link: https://leetcode.com/problems/pascals-triangle/           ║
╚══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Given numRows, generate the first numRows of Pascal's Triangle.
  Each number is the sum of the two numbers directly above it
  (edges of every row are always 1).

  Input : numRows = 5
  Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

  Example 1 — basic:
    Input : numRows = 4
    Output: [[1],[1,1],[1,2,1],[1,3,3,1]]
    Why?  : each row's middle = sum of two values above it

  Example 2 — slightly tricky:
    Input : numRows = 1
    Output: [[1]]
    Why?  : just the single top row, no building needed

  Constraints:
    - 1 <= numRows <= 30
    - row[i][j] = row[i-1][j-1] + row[i-1][j] for 0 < j < len(row)-1

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ಮೊದಲು problem odidaga ನಮ್ಮ brain ಏನು think ಮಾಡಬೇಕು:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ (What are they asking?)
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  numRows — ಎಷ್ಟು rows ಬೇಕು       │
  │  Output ಏನು ಬೇಕು?     →  ಮೊದಲ numRows Pascal's Triangle  │
  │                          rows                              │
  │  Constraints ಏನಿದೆ?   →  ಪ್ರತಿ row ನ first, last element  │
  │                          ಯಾವಾಗ್ಲೂ 1                        │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ನನಗೆ ಗೊತ್ತಿರೋ simple way ಏನು? (Brute force thought)
  →  ಪ್ರತಿ cell (i,j) ಗೂ binomial coefficient formula C(i,j) =
     i! / (j! * (i-j)!) ಬಳಸಿ ನೇರವಾಗಿ calculate ಮಾಡೋದು.
  →  ಆದರೆ ಇದು ಯಾಕೆ ideal ಅಲ್ಲ? → factorial calculation ಪ್ರತಿ
     cell ಗೂ repeat ಆಗುತ್ತೆ, ಬೇಡದೇ ಇರೋ overhead, elegant ಅಲ್ಲ.

  ಹಂತ 3 — Better way ಹೇಗೆ ಯೋಚಿಸುವುದು? (Optimization thought)
  →  "ಪ್ರತಿ row ಅನ್ನ ಅದರ ಹಿಂದಿನ row ಇಂದ ಡೈರೆಕ್ಟ್ ಆಗಿ build
     ಮಾಡಬಹುದಲ್ವಾ? factorial ಯಾಕೆ ಬೇಕು?"
  →  ಅಹಾ moment: row 0 = [1] ಇಂದ ಶುರು ಮಾಡಿ, ಪ್ರತಿ next row ಗೂ
     1 ಇಂದ ಶುರು ಮಾಡಿ 1 ಇಂದ ಮುಗಿಸಿ, ಮಧ್ಯದ values ಎಲ್ಲಾ
     "ಹಿಂದಿನ row ನ ಪಕ್ಕ-ಪಕ್ಕ ಎರಡು values ನ sum" ಆಗಿರುತ್ತೆ.
  →  ಇದರಿಂದ ನಾವು Bottom-Up 2D Construction use ಮಾಡಬಹುದು!

  ಹಂತ 4 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  ಪ್ರತಿ row ಬರೀ ಅದರ IMMEDIATE ಹಿಂದಿನ row ಮೇಲೆ depend
     ಆಗ್ತಿದೆ, ಎಲ್ಲಾ previous rows ಮೇಲೆ ಅಲ್ಲ — ಇದೇ bottom-up
     DP ಗೆ classic signal.
  →  Pascal's identity: C(n,k) = C(n-1,k-1) + C(n-1,k) — ಇದೇ
     recurrence ಅನ್ನ closed-form ಬದ್ಲು iteratively apply
     ಮಾಡ್ತಿದ್ದೀವಿ.

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು (Think out loud):
  →  "So I need to build the first numRows rows of Pascal's Triangle."
  →  "I could use the binomial coefficient formula per cell, but
      that recomputes factorials unnecessarily."
  →  "I notice each row is built entirely from the row above it,
      so I can construct it bottom-up instead."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : 2D Array Construction / Bottom-Up DP
  Secondary : Row-by-row build using the PREVIOUS row only

  WHY this technique?
  → Every row is fully determined by the row before it
  → No need to recompute from scratch via factorials
  → Textbook bottom-up DP: state depends only on prior state

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 INTUITION (How to think)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Each row is built from the ROW ABOVE — can I generate row i
  directly from row i-1, instead of computing each cell via
  factorials?

  The journey from brute to optimal:
    Brute thought   →  binomial coefficient formula C(i,j) per cell
    Problem with it →  wasteful factorial recomputation
    Better question →  "reuse the row directly above instead?"
    Insight         →  start/end with 1, middle = sum of pair above
    Optimal         →  build each row from the previous one

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 APPROACH 1 — BRUTE FORCE (Binomial Coefficient Formula)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Compute each cell directly using factorials: C(i, j).

  Pseudocode:
    step 1: from math import comb
    step 2: triangle = [[comb(i,j) for j in range(i+1)] for i in range(numRows)]

  Time  : O(numRows²) cells, each comb() costs more internally
  Space : O(numRows²)  — total output size

  ಇದು ಯಾಕೆ ideal ಅಲ್ಲ? (Why not ideal?)
    → ಹಿಂದಿನ row ಬಳಸೋ ಬದ್ಲು, ಪ್ರತಿ cell ಅನ್ನ ಪ್ರತ್ಯೇಕ ಆಗಿ
      factorial ಇಂದ calculate ಮಾಡ್ತಿದ್ದೀವಿ — ಬೇಡದೇ ಇರೋ overhead.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚶 APPROACH 2 — BETTER (skip — brute jumps straight to optimal)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ಇಲ್ಲಿ intermediate approach ಇಲ್ಲ — previous-row insight ಸಿಕ್ಕ
  ತಕ್ಷಣ ನೇರವಾಗಿ bottom-up optimal ಗೆ ಹೋಗಬಹುದು.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 APPROACH 3 — OPTIMAL   (Build Row from Previous Row)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Start with [1], build each next row from the last one added.

  Key steps:
    1. triangle = [[1]]  (row 0 is always just [1])
    2. For each new row from 1 to numRows-1:
         prev = triangle[-1]
         new_row = [1]
         for j in range(1, len(prev)): new_row.append(prev[j-1]+prev[j])
         new_row.append(1)
         triangle.append(new_row)
    3. Return triangle[:numRows]

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ (Say it once in Kanglish so it sticks):
    → "[1] ಇಂದ ಶುರು ಮಾಡು. ಪ್ರತಿ ಹೊಸ row ಗೂ, 1 ಇಂದ ಶುರು ಮಾಡಿ,
        ಹಿಂದಿನ row ನ ಪಕ್ಕ-ಪಕ್ಕ values ಸೇರಿಸಿ ಮಧ್ಯದ values
        ಬರೆ, ಕೊನೆಗೆ 1 ಸೇರಿಸು."

  Time  : O(numRows²)  →  Why: total cells across all rows
  Space : O(numRows²)  →  Why: required by output size itself

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: numRows = 4

  triangle = [[1]]

  Build row 1: prev=[1]  →  new_row=[1], no middle (range empty), append 1 → [1,1]
  triangle = [[1],[1,1]]

  Build row 2: prev=[1,1]  →  new_row=[1]
    j=1: prev[0]+prev[1]=1+1=2 → new_row=[1,2]
    append 1 → [1,2,1]
  triangle = [[1],[1,1],[1,2,1]]

  Build row 3: prev=[1,2,1]  →  new_row=[1]
    j=1: prev[0]+prev[1]=1+2=3 → new_row=[1,3]
    j=2: prev[1]+prev[2]=2+1=3 → new_row=[1,3,3]
    append 1 → [1,3,3,1]
  triangle = [[1],[1,1],[1,2,1],[1,3,3,1]]

  Output: [[1],[1,1],[1,2,1],[1,3,3,1]]

  ಇನ್ನೊಂದು example — tricky case:
  Input: numRows = 1
  triangle = [[1]], loop runs 0 times (range(1-1)=range(0))
  Output: [[1]]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ numRows = 1?     →  [[1]] (just the single top row)
  ✓ numRows = 2?     →  [[1], [1,1]]
  ✓ Larger numRows?  →  each row should be a palindrome (symmetric)
  ✓ Row length?      →  always equals its row index + 1

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                Time            Space
  Brute Force   O(numRows²)*    O(numRows²)   (* worse constant, factorials)
  Optimal       O(numRows²)     O(numRows²)    ← use this  

  Time ಯಾಕೆ O(numRows²)?  → Total cells across all rows ಇಷ್ಟೇ ಇರೋದು.
  Space ಯಾಕೆ O(numRows²)? → Output ಸ್ವತಃ ಅಷ್ಟು size ಇರುತ್ತೆ.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Bottom-Up Row Construction (2D DP via Previous Row)

  ಈ pattern ಯಾವಾಗ use ಮಾಡಬೇಕು?
  → ಪ್ರತಿ "row" ಅಥವಾ "layer" ಬರೀ IMMEDIATE ಹಿಂದಿನ row ಮೇಲೆ
    depend ಆಗ್ತಿದ್ದಾಗ (all previous rows ಮೇಲಲ್ಲ)
  → Closed-form formula ಗಿಂತ, ಹಿಂದಿನ result ಇಂದ iteratively
    build ಮಾಡೋದು ಸುಲಭ ಆಗಿದ್ದಾಗ

  ಇದೇ pattern ಬೇರೆ problems ನಲ್ಲಿ ಕಾಣಿಸುತ್ತೆ:
  → Pascal's Triangle II (space-optimized, ಒಂದೇ row track ಮಾಡೋದು)
  → General "build level N from level N-1" DP problems

  Next time ಇಂತಹ problem ಬಂದ್ರೆ ನಾನು ಮೊದಲು ಇದನ್ನ think ಮಾಡ್ತೇನೆ:
  → "'ಪ್ರತಿ row ಹಿಂದಿನ row ಮೇಲೆ depend' ಅಂತ ಕಂಡ ತಕ್ಷಣ, bottom-up
      row-by-row build ಮೊದಲು ಯೋಚಿಸು."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ INTERVIEW ನಲ್ಲಿ ಹೇಗೆ EXPLAIN ಮಾಡಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "So I need to generate the first numRows rows of Pascal's
      Triangle, where each middle value is the sum of the two
      values above it."

  2. Brute force:
     "I could compute each cell with the binomial coefficient
      formula, but that recomputes factorials for every cell
      instead of reusing the row above."

  3. Optimize:
     "I notice each row is fully determined by the row before it,
      so I can build it bottom-up: start and end with 1, and each
      middle value is the sum of the adjacent pair above."

  4. Code:
     "I'll keep triangle = [[1]] and append a new row built from
      triangle[-1] each iteration."

  5. Complexity:
     "Time O(numRows²) and space O(numRows²) — both required by
      the output size itself."

  ಮುಖ್ಯ: ಸುಮ್ಮನೆ ಕೂತು code ಬರೆಯಬೇಡ!
         Interviewer ಗೆ ನಿನ್ನ thinking process ಕಾಣಬೇಕು.
"""


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(numRows²) Time | O(numRows²) Space
# ═══════════════════════════════════════════════════════════════════
def pascals_triangle_brute(numRows):
    """ಇದು ಮೊದಲ ಆಲೋಚನೆ — binomial coefficient formula, per-cell factorial"""
    from math import comb
    return [[comb(i, j) for j in range(i + 1)] for i in range(numRows)]


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(numRows²) Time | O(numRows²) Space
# ═══════════════════════════════════════════════════════════════════
def pascals_triangle(numRows):
    """ಇದು final answer — ಹಿಂದಿನ row ಇಂದ ಪ್ರತಿ row build ಮಾಡೋದು"""
    triangle = [[1]]

    for _ in range(numRows - 1):
        prev = triangle[-1]
        new_row = [1]
        for j in range(1, len(prev)):
            new_row.append(prev[j - 1] + prev[j])
        new_row.append(1)
        triangle.append(new_row)

    return triangle[:numRows]


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")   # Windows cp1252 can't print   otherwise

    # Test 1 — Basic example
    assert pascals_triangle(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

    # Test 2 — Edge case: single row
    assert pascals_triangle(1) == [[1]]

    # Test 3 — Edge case: two rows
    assert pascals_triangle(2) == [[1], [1, 1]]

    print("All tests passed!  ")
