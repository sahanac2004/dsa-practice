"""
╔══════════════════════════════════════════════════════════════════╗
║  FIND A PEAK ELEMENT II                                          ║
║  LeetCode #1901  |  Difficulty: Hard  |  Topic: Binary Search   ║
║  Link: https://leetcode.com/problems/find-a-peak-element-ii/    ║
╚══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Given an m×n matrix where no two adjacent cells are equal,
  find ANY peak element and return its [row, col] position.
  A peak element is strictly greater than ALL its neighbors
  (up, down, left, right — within bounds).
  Boundary cells only need to beat their existing neighbors.
  Must solve in O(m log n) or O(n log m).

  Input : mat = m×n matrix of distinct integers
  Output: [row, col] of any peak element

  Example 1 — basic:
    Input : mat=[[1,4],[3,2]]
    Output: [0,1]  (value 4)
    Why?  : mat[0][1]=4 > mat[0][0]=1 and mat[1][1]=2
            (top boundary — no neighbor above) → peak!

  Example 2 — slightly tricky:
    Input : mat=[[10,20,15],[21,30,14],[7,16,32]]
    Output: [1,1] or [2,2] (both valid peaks)
    Why?  : mat[1][1]=30 > 10,15,21,16 → peak!
            mat[2][2]=32 > 14,16 → peak!

  Constraints:
    - 1 <= m, n <= 500
    - 1 <= mat[i][j] <= 10^5
    - No two adjacent cells equal
    - Must be O(m log n) time

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Problem odi aada mele namma brain enu think maadabeeku:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  m×n matrix                  │
  │  Output ಏನು ಬೇಕು?     →  [row, col] of any peak       │
  │  Constraints ಏನಿದೆ?   →  O(m log n) must,             │
  │                           peak > all 4 neighbors        │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ನನಗೆ ಗೊತ್ತಿರೋ simple way ಏನು?
  →  Every cell check ಮಾಡಿ 4 neighbors compare ಮಾಡೋಣ → O(m×n)
  →  ಆದರೆ ಇದು slow ಯಾಕೆ?
     O(m log n) beeku!

  ಹಂತ 3 — Better way ಹೇಗೆ ಯೋಚಿಸುವುದು?
  →  "1D peak element #162 ಲ್ಲಿ binary search ಮಾಡಿದ್ವಿ..."
  →  2D ಗೆ extend ಮಾಡಬಹudaa?
  →  Key insight: Binary search on COLUMNS (or rows)!
     For each mid column → find the maximum element in that column
     → Compare with its left and right neighbors
     → If mat[max_row][mid] > both neighbors → PEAK found!
     → If left neighbor bigger → peak is in left half
     → If right neighbor bigger → peak is in right half

  ಹಂತ 4 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  Column max is guaranteed > all elements in its column
     (up and down) — so only need to check left/right!
  →  This makes it essentially 1D peak finding on column maxima
  →  O(m) to find col max × O(log n) binary search = O(m log n)

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು:
  →  "Extend 1D peak element to 2D using binary search on columns"
  →  "For mid column, find its maximum row element"
  →  "Column max beats up/down neighbors — only check left/right"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Binary Search → On Columns (extend 1D peak to 2D)
  Secondary : —

  WHY Binary Search on Columns?
  → Find max in mid column → it beats all column neighbors
  → Only check left/right neighbors for peak condition
  → If not peak → move toward larger side (like 1D peak #162)
  → O(m log n) total

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Think of each column as a "candidate" — its maximum element
  beats all other elements in that column (up and down neighbors).
  So we only need to check if that maximum beats its left and
  right neighbors!

  This reduces 2D peak finding to 1D peak finding on column maxima:
  - Find max of mid column → (max_row, mid)
  - If mat[max_row][mid-1] > mat[max_row][mid] → peak in left half
  - If mat[max_row][mid+1] > mat[max_row][mid] → peak in right half
  - Else → (max_row, mid) IS a peak!

  This is exactly Find Peak Element #162 applied column by column!

  The journey from brute to optimal:
    Brute thought   →  Check all cells → O(m×n)
    Problem with it →  O(m log n) needed
    Better question →  "Can I apply 1D peak search to 2D?"
    Insight         →  YES! Binary search on columns.
                       Column max beats up/down → only check left/right
    Optimal         →  O(m log n)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Check every cell. For each cell, verify it beats all 4 neighbors.

  Pseudocode:
    step 1: for each (r, c):
    step 2:   if mat[r][c] > all valid neighbors → return [r,c]

  Time  : O(m × n)  →  Why: check all cells
  Space : O(1)

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ?
    → O(m log n) beeku — O(m×n) too slow!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 6 — APPROACH 2 — OPTIMAL (Binary Search on Columns)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Binary search on columns. For mid column, find its max element.
    Check left and right neighbors of that max element.
    Move toward larger neighbor (like 1D peak #162).

  Key steps:
    1. left=0, right=n-1
    2. While left <= right:
       a. mid = (left+right)//2
       b. max_row = index of max element in column mid
       c. left_val  = mat[max_row][mid-1] if mid>0 else -inf
       d. right_val = mat[max_row][mid+1] if mid<n-1 else -inf
       e. if mat[max_row][mid] > left_val and > right_val:
             return [max_row, mid]   ← PEAK!
       f. elif left_val > right_val:
             right = mid - 1         ← peak in left half
       g. else:
             left = mid + 1          ← peak in right half

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ:
    → "Columns ಮೇಲೆ binary search maadu. Mid column ರ max
       element find maadu (row direction ಲ್ಲಿ). ಆ element ರ
       left ಮತ್ತು right neighbors compare maadu.
       Both ಗಿಂತ ದೊಡ್ಡದಾದ್ರೆ → peak! Left ದೊಡ್ಡದಾದ್ರೆ →
       left half ಲ್ಲಿ peak ಇದೆ. Right ದೊಡ್ಡದಾದ್ರೆ →
       right half ಲ್ಲಿ peak ಇದೆ. O(m log n)!"

  Time  : O(m log n)  →  Why: O(m) to find col max × O(log n) BS
  Space : O(1)        →  Why: only pointers

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 7 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: mat=[[10,20,15],[21,30,14],[7,16,32]]
  m=3, n=3, left=0, right=2

  mid=1 → column 1 = [20,30,16]
    max_row=1 (value 30)
    left_val  = mat[1][0] = 21
    right_val = mat[1][2] = 14
    30 > 21 AND 30 > 14 → PEAK! return [1,1] ✓

  ಇನ್ನೊಂದು example: mat=[[1,4],[3,2]]
  m=2, n=2, left=0, right=1

  mid=0 → column 0 = [1,3]
    max_row=1 (value 3)
    left_val  = -inf (mid=0, no left)
    right_val = mat[1][1] = 2
    3 > -inf AND 3 > 2 → PEAK! return [1,0] ✓
    (also [0,1] is valid — any peak acceptable)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 8 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ 1×1 matrix?      →  Only element is peak → [0,0]
  ✓ Single row?       →  Apply 1D peak search on that row
  ✓ Single column?    →  Find max of single column → peak
  ✓ Peak at corner?   →  Only 2 neighbors → still handled by -inf
  ✓ Multiple peaks?   →  Return any one — all valid

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 9 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                  Time          Space
  Brute Force     O(m × n)      O(1)
  Optimal         O(m log n)    O(1)   ← use this ✅

  Time yaake O(m log n)?
    → log n binary search steps on columns
    → Each step O(m) to find column maximum
  Space yaake O(1)?
    → Only left, right, mid, max_row pointers

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 10 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Extend 1D Binary Search to 2D

  1D → 2D extension pattern:
  ┌─────────────────────┬──────────────────────────────────┐
  │ 1D Peak #162        │ 2D Peak #1901                    │
  ├─────────────────────┼──────────────────────────────────┤
  │ Binary search on    │ Binary search on COLUMNS         │
  │ indices             │                                  │
  │ Check left/right    │ Find col max → check left/right  │
  │ neighbors           │ (up/down already beaten by max)  │
  │ O(log n)            │ O(m log n)                       │
  └─────────────────────┴──────────────────────────────────┘

  Idee pattern beere problemsalli kaanisatte:
  → Find Peak Element #162 (1D version — simpler)
  → Search a 2D Matrix II #240 (staircase search)
  → Kth Smallest in Sorted Matrix #378

  Next time intaha problem bandre naanu modalu idannu think maadtene:
  → "2D peak, O(m log n) beeku?
     → Binary search on columns!
     Col max find maadu (O(m)), left/right check maadu.
     1D peak logic exactly — just on column maxima!"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 11 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "Find any peak in 2D matrix — element greater than all 4
      neighbors. Must be O(m log n)."

  2. Brute force:
     "Check all cells — O(m×n). Too slow."

  3. Optimize:
     "Extend 1D peak element (#162) to 2D.
      Binary search on columns. For mid column, find its maximum
      element (row). That element beats all up/down neighbors.
      Only need to check left/right neighbors.
      If beats both → peak! Else move toward larger side."

  4. Code:
     "left=0, right=n-1. For each mid: find max_row in col mid.
      Compare with left/right neighbors using -inf guard.
      Peak found or move left/right."

  5. Complexity:
     "Time O(m log n) — O(log n) column steps × O(m) max search.
      Space O(1)."

  Mukhya: summane kuutu code bareyabeda!
          "Column max beats up/down" — this is the KEY insight!
          1D peak #162 connection — show pattern recognition!
"""


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(m×n) Time | O(1) Space
# ═══════════════════════════════════════════════════════════════════
def find_peak_grid_brute(mat):
    """Idu modala aaloochane — check every cell O(m×n)"""
    m, n = len(mat), len(mat[0])
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]

    for r in range(m):
        for c in range(n):
            is_peak = True
            for dr, dc in dirs:
                nr, nc = r+dr, c+dc
                if 0 <= nr < m and 0 <= nc < n:
                    if mat[nr][nc] >= mat[r][c]:
                        is_peak = False
                        break
            if is_peak:
                return [r, c]


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(m log n) Time | O(1) Space
# ═══════════════════════════════════════════════════════════════════
def find_peak_grid(mat):
    """
    Idu final answer — binary search on columns
    Find col max → col max beats up/down → only check left/right
    Extends 1D peak element #162 to 2D!
    """
    m, n = len(mat), len(mat[0])
    left, right = 0, n - 1

    while left <= right:
        mid = (left + right) // 2

        # find row with maximum value in column mid
        max_row = 0
        for r in range(m):
            if mat[r][mid] > mat[max_row][mid]:
                max_row = r

        # get left and right neighbors
        left_val  = mat[max_row][mid-1] if mid > 0   else float('-inf')
        right_val = mat[max_row][mid+1] if mid < n-1 else float('-inf')

        if mat[max_row][mid] > left_val and mat[max_row][mid] > right_val:
            # column max beats left and right → it's a peak!
            # (already beats up/down since it's column maximum)
            return [max_row, mid]

        elif left_val > right_val:
            right = mid - 1     # peak exists in left half
        else:
            left = mid + 1      # peak exists in right half

    return [-1, -1]             # never reached (peak always exists)


# ═══════════════════════════════════════════════════════════════════
# HELPER — Verify a position is actually a peak
# ═══════════════════════════════════════════════════════════════════
def is_peak(mat, r, c):
    """Verify [r,c] is a valid peak"""
    m, n = len(mat), len(mat[0])
    for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
        nr, nc = r+dr, c+dc
        if 0 <= nr < m and 0 <= nc < n:
            if mat[nr][nc] >= mat[r][c]:
                return False
    return True


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # Test 1 — Basic 2×2
    mat1 = [[1,4],[3,2]]
    r, c = find_peak_grid(mat1)
    assert is_peak(mat1, r, c), f"[{r},{c}] is not a peak"

    # Test 2 — 3×3 with clear peak
    mat2 = [[10,20,15],[21,30,14],[7,16,32]]
    r, c = find_peak_grid(mat2)
    assert is_peak(mat2, r, c), f"[{r},{c}] is not a peak"

    # Test 3 — 1×1
    mat3 = [[5]]
    assert find_peak_grid(mat3) == [0, 0]

    # Test 4 — Single row
    mat4 = [[1, 3, 2, 4, 1]]
    r, c = find_peak_grid(mat4)
    assert is_peak(mat4, r, c), f"[{r},{c}] is not a peak"

    # Test 5 — Single column
    mat5 = [[1],[5],[3],[2]]
    r, c = find_peak_grid(mat5)
    assert is_peak(mat5, r, c), f"[{r},{c}] is not a peak"

    # Test 6 — Peak at corner
    mat6 = [[10, 8],[7, 5]]
    r, c = find_peak_grid(mat6)
    assert is_peak(mat6, r, c), f"[{r},{c}] is not a peak"

    print("All tests passed!")
