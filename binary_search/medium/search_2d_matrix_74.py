"""
╔══════════════════════════════════════════════════════════════════╗
║  SEARCH A 2D MATRIX                                              ║
║  LeetCode #74  |  Difficulty: Medium  |  Topic: Binary Search   ║
║  Link: https://leetcode.com/problems/search-a-2d-matrix/        ║
╚══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Given an m x n matrix with two properties:
    1. Each row is sorted in ascending order left to right
    2. First element of each row > last element of previous row
       (meaning the entire matrix is one continuous sorted array)
  Given a target, return True if target exists, False otherwise.
  Must solve in O(log(m × n)) time.

  Input : matrix = m×n 2D list of integers, target = integer
  Output: True if target found, False otherwise

  Example 1 — basic:
    Input : matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]],
            target = 3
    Output: True
    Why?  : 3 is at row 0, col 1

  Example 2 — slightly tricky (not found):
    Input : matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]],
            target = 13
    Output: False
    Why?  : 13 is not in the matrix

  Constraints:
    - m == matrix.length, n == matrix[i].length
    - 1 <= m, n <= 100
    - -10^4 <= matrix[i][j], target <= 10^4
    - Each row sorted ascending, first of row > last of prev row

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Problem odi aada mele namma brain enu think maadabeeku:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  m×n sorted matrix + target  │
  │  Output ಏನು ಬೇಕು?     →  target exists? True/False    │
  │  Constraints ಏನಿದೆ?   →  rows sorted, each row ರ      │
  │                           first > prev row ರ last      │
  │                           → entire matrix = 1D sorted! │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ನನಗೆ ಗೊತ್ತಿರೋ simple way ಏನು?
  →  ಪ್ರತಿ cell check ಮಾಡಿ target ಇದ್ಯಾ ಅಂತ ನೋಡೋಣ → O(m×n)
  →  ಆದರೆ ಇದು slow ಯಾಕೆ?
     O(log(m×n)) beeku anta problem says

  ಹಂತ 3 — Better way ಹೇಗೆ ಯೋಚಿಸುವುದು?
  →  "Matrix ಅನ್ನು 1D array ಅಂತ treat ಮಾಡಬಹudaa?"
  →  YES! Since each row's first > prev row's last,
     matrix is effectively ONE sorted array of m×n elements
  →  index i ಅನ್ನು → row = i//n, col = i%n ಆಗಿ convert ಮಾಡಬಹуದು!
  →  So binary search on 0 to m×n-1 → O(log(m×n))!

  ಹಂತ 4 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  Matrix ಅನ್ನು flatten ಮಾಡದೆ, index math ಮಾಡಿ
     virtual 1D array ಮೇಲೆ binary search ಮಾಡಬಹуದು
  →  mid → row = mid//n, col = mid%n → O(1) conversion
  →  Clean O(log(m×n)) solution!

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು:
  →  "The matrix is essentially a sorted 1D array!"
  →  "Binary search on indices 0 to m*n-1"
  →  "Convert mid index to row/col using mid//n and mid%n"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Binary Search → 2D to 1D index mapping
  Secondary : —

  WHY treat as 1D?
  → Both row-wise and matrix-wise sorted → one big sorted array
  → index i maps to row=i//n, col=i%n
  → Standard binary search on 0 to m*n-1 → O(log(m*n))

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  The key property: first element of each row > last element of
  previous row. This means if you read the matrix row by row,
  left to right, you get a perfectly sorted sequence!

  So instead of a 2D binary search, just do a 1D binary search
  on indices 0 to m*n-1. Convert each mid index to (row, col)
  using integer division and modulo.

  The journey from brute to optimal:
    Brute thought   →  Check every cell O(m×n)
    Problem with it →  O(log(m×n)) needed
    Better question →  "Is this really a 2D problem?"
    Insight         →  No! Row-by-row = one sorted array → 1D binary search
    Optimal         →  Binary search on 0..m*n-1, index math for row/col

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Check every cell in the matrix. Return True if target found.

  Pseudocode:
    step 1: for each row in matrix:
    step 2:   for each val in row:
    step 3:     if val == target: return True
    step 4: return False

  Time  : O(m × n)  →  Why: visit every cell
  Space : O(1)      →  Why: no extra space

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ?
    → O(m×n) valid adu, but O(log(m×n)) possible
    → Sorted property completely wasted!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 6 — APPROACH 2 — OPTIMAL (Binary Search, 1D mapping)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Treat the matrix as a 1D sorted array of m*n elements.
    Binary search on indices 0 to m*n-1.
    Convert mid to (row, col) using mid//n and mid%n.

  Key steps:
    1. m = rows, n = cols
    2. left=0, right=m*n-1
    3. While left <= right:
       a. mid = (left+right)//2
       b. row = mid//n, col = mid%n
       c. val = matrix[row][col]
       d. if val == target → return True
       e. if val < target → left = mid+1
       f. if val > target → right = mid-1
    4. return False

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ:
    → "Matrix ಅನ್ನು 1D sorted array ಅಂತ think ಮಾಡು.
       0 to m*n-1 ಮೇಲೆ binary search maadu.
       mid index → row=mid//n, col=mid%n ಆಗಿ convert maadu.
       Standard binary search — O(log(m×n))!"

  Time  : O(log(m × n))  →  Why: binary search on m*n elements
  Space : O(1)           →  Why: only pointers used

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 7 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target=3
  m=3, n=4, total=12, left=0, right=11

  mid=5 → row=5//4=1, col=5%4=1 → matrix[1][1]=11
  11 > 3 → right=4

  mid=2 → row=2//4=0, col=2%4=2 → matrix[0][2]=5
  5 > 3 → right=1

  mid=0 → row=0//4=0, col=0%4=0 → matrix[0][0]=1
  1 < 3 → left=1

  mid=1 → row=1//4=0, col=1%4=1 → matrix[0][1]=3
  3 == 3 → return True ✓

  ಇನ್ನೊಂದು — target not found:
  Input: same matrix, target=13

  mid=5 → matrix[1][1]=11 < 13 → left=6
  mid=8 → row=2, col=0 → matrix[2][0]=23 > 13 → right=7
  mid=6 → row=1, col=2 → matrix[1][2]=16 > 13 → right=5
  left=6 > right=5 → return False ✓

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 8 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ 1×1 matrix?            →  [[5]], target=5 → True
  ✓ Target smaller than min →  target < matrix[0][0] → False
  ✓ Target larger than max  →  target > matrix[m-1][n-1] → False
  ✓ Single row matrix?      →  [[1,2,3,4]], target=3 → True
  ✓ Single col matrix?      →  [[1],[2],[3]], target=2 → True

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 9 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                Time            Space
  Brute Force   O(m × n)        O(1)
  Optimal       O(log(m × n))   O(1)   ← use this ✅

  Time yaake O(log(m×n))? → Binary search on m*n elements
  Space yaake O(1)?        → Only left, right, mid variables

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 10 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Binary Search — 2D to 1D Index Mapping

  Ee pattern yaavaaga use maadabeeku?
  → Sorted 2D matrix where rows connect (first > prev last)
  → Search in matrix with O(log(m*n)) constraint
  → Any problem where 2D grid = flattened 1D sorted array

  Idee pattern beere problemsalli kaanisatte:
  → Search a 2D Matrix II #240 (different property — next problem!)
  → Find K-th Smallest in Sorted Matrix #378
  → Matrix Median GFG

  Next time intaha problem bandre naanu modalu idannu think maadtene:
  → "Sorted matrix, first of row > last of prev row?
     → 1D array treat maadu! mid//n = row, mid%n = col.
     Standard binary search — O(log(m×n))!"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 11 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "Search target in matrix where rows are sorted and each
      row's first element is greater than prev row's last."

  2. Brute force:
     "Check every cell — O(m×n). Doesn't use sorted property."

  3. Optimize:
     "Key insight: since first of each row > last of prev row,
      reading row by row gives a perfectly sorted sequence.
      So treat it as 1D binary search on indices 0 to m*n-1.
      Convert mid to row=mid//n, col=mid%n."

  4. Code:
     "Standard binary search. mid//n gives row, mid%n gives col.
      Compare matrix[row][col] with target."

  5. Complexity:
     "Time O(log(m×n)) — binary search on m*n elements.
      Space O(1)."

  Mukhya: summane kuutu code bareyabeda!
          2D → 1D insight — very clean, interviewer loves it!
          mid//n and mid%n — explain this conversion clearly!
"""


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(m×n) Time | O(1) Space
# ═══════════════════════════════════════════════════════════════════
def search_matrix_brute(matrix, target):
    """Idu modala aaloochane — check every cell O(m×n)"""
    for row in matrix:
        for val in row:
            if val == target:
                return True
    return False


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(log(m×n)) Time | O(1) Space
# ═══════════════════════════════════════════════════════════════════
def search_matrix(matrix, target):
    """
    Idu final answer — treat as 1D sorted array
    mid//n = row, mid%n = col → standard binary search
    """
    m, n = len(matrix), len(matrix[0])
    left, right = 0, m * n - 1

    while left <= right:
        mid = (left + right) // 2
        row, col = mid // n, mid % n
        val = matrix[row][col]

        if val == target:
            return True
        elif val < target:
            left = mid + 1
        else:
            right = mid - 1

    return False


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]

    # Test 1 — Target exists (middle of matrix)
    assert search_matrix(matrix, 3) == True

    # Test 2 — Target not found
    assert search_matrix(matrix, 13) == False

    # Test 3 — Target at first cell
    assert search_matrix(matrix, 1) == True

    # Test 4 — Target at last cell
    assert search_matrix(matrix, 60) == True

    # Test 5 — Single cell matrix
    assert search_matrix([[5]], 5) == True
    assert search_matrix([[5]], 3) == False

    # Test 6 — Single row
    assert search_matrix([[1, 2, 3, 4]], 3) == True

    # Test 7 — Single column
    assert search_matrix([[1], [2], [3]], 2) == True

    # Test 8 — Target smaller than all
    assert search_matrix(matrix, 0) == False

    # Test 9 — Target larger than all
    assert search_matrix(matrix, 100) == False

    print("All tests passed!")
