"""
╔═══════════════════════════════════════════════════════════════════╗
║  SET MATRIX ZEROES                                                ║
║  LeetCode #73  |  Difficulty: Medium  |  Topic: Arrays / Matrix   ║
║  Link: https://leetcode.com/problems/set-matrix-zeroes/           ║
╚═══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Given an m x n matrix, if any cell contains a 0, set its ENTIRE row
  AND entire column to 0 — done in-place. The tricky part is not
  letting newly-zeroed cells trigger MORE zeroing in a chain reaction.

  Input : matrix = [[1,1,1],[1,0,1],[1,1,1]]
  Output: [[1,0,1],[0,0,0],[1,0,1]]

  Example 1 — basic:
    Input : matrix = [[1,1,1],[1,0,1],[1,1,1]]
    Output: [[1,0,1],[0,0,0],[1,0,1]]
    Why?  : the single 0 at (1,1) zeroes out all of row 1 and all of column 1

  Example 2 — slightly tricky (a zero sits in row/col 0 — the marker area):
    Input : matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
    Why?  : the two zeros at (0,0) and (0,3) are IN row 0 itself —
             must still correctly mark and zero using row/col 0 as
             markers without losing track of the original zero positions

  Constraints:
    - m == matrix.length, n == matrix[0].length
    - 1 <= m, n <= 200
    - -2^31 <= matrix[i][j] <= 2^31 - 1
    - Follow-up: an O(1) extra space in-place solution exists

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ಮೊದಲು problem odidaga ನಮ್ಮ brain ಏನು think ಮಾಡಬೇಕು:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ (What are they asking?)
  ┌───────────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  m x n matrix                         │
  │  Output ಏನು ಬೇಕು?     →  0 ಇರೋ cell ನ ಪೂರ್ತಿ row+column   │
  │                          zero ಮಾಡ್ಬೇಕು, in-place              │
  │  Constraints ಏನಿದೆ?   →  m,n<=200, follow-up: O(1) space      │
  └───────────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ನನಗೆ ಗೊತ್ತಿರೋ simple way ಏನು? (Brute force thought)
  →  ಎಲ್ಲಾ 0 ಗಳ (row, col) positions ಒಂದು separate set ನಲ್ಲಿ store
     ಮಾಡಿ, ಆಮೇಲೆ ಆ rows/cols ಅನ್ನ zero ಮಾಡೋದು.
  →  ಆದರೆ ಇದು slow ಯಾಕೆ? → O(m*n) extra space ಬೇಕಾಗುತ್ತೆ (rows set +
     cols set) — follow-up O(1) space ಕೇಳ್ತಾ ಇದೆ. ಮೊದಲೇ direct
     matrix ನಲ್ಲಿ 0 ಬರೆದ್ರೆ, ಅದೇ 0 ಅನ್ನ ಮತ್ತೆ "original zero" ಅಂತ
     ತಪ್ಪಾಗಿ ಗುರುತಿಸಿ chain reaction ಆಗುತ್ತೆ — ಅದಕ್ಕೇ separate
     tracking ಬೇಕು.

  ಹಂತ 3 — Better way ಹೇಗೆ ಯೋಚಿಸುವುದು? (Optimization thought)
  →  "ಹೊಸ set ಬೇಡ, matrix ನ ಸ್ವತಃ first row ಮತ್ತು first column ಅನ್ನೇ
     marker ಆಗಿ ಬಳಸ್ಬಹುದಾ? matrix[i][0]=0 ಅಂದ್ರೆ 'row i ಗೆ 0 ಇದೆ',
     matrix[0][j]=0 ಅಂದ್ರೆ 'col j ಗೆ 0 ಇದೆ' ಅಂತ."
  →  ಅಹಾ moment: ಆದ್ರೆ matrix[0][0] ಎರಡೂ row0 ಮತ್ತು col0 ಗೆ marker
     ಆಗಿ conflict ಆಗುತ್ತೆ! ಅದಕ್ಕೆ ಒಂದು separate boolean
     (first_row_has_zero) ಇಟ್ಕೊಂಡು row 0 ಗೆ ಪ್ರತ್ಯೇಕ handle ಮಾಡ್ಬೇಕು,
     matrix[0][0] ಅನ್ನ column 0 ಗೆ marker ಆಗಿ ಬಳಸ್ಬಹುದು. ಮೊದಲು
     inner matrix (row>=1, col>=1) ಅನ್ನ scan ಮಾಡಿ markers set ಮಾಡಿ,
     ಆಮೇಲೆ markers ಪ್ರಕಾರ inner matrix zero ಮಾಡಿ, ಕೊನೆಗೆ column 0 ಮತ್ತು
     row 0 ಅನ್ನ separately handle ಮಾಡಬೇಕು.
  →  ಇದರಿಂದ ನಾವು Matrix → In-Place Marking (use first row/col as markers)
     use ಮಾಡಬಹುದು!

  ಹಂತ 4 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  Matrix ಸ್ವತಃ enough "space" ಕೊಡುತ್ತೆ — first row/col ಅನ್ನ marker
     ಆಗಿ reuse ಮಾಡ್ಬಹುದು, ಹೊಸ set/array ಬೇಡ.
  →  matrix[0][0] overlap problem ಅನ್ನ ಒಂದೇ extra boolean variable
     ಇಂದ solve ಮಾಡ್ಬಹುದು — O(1) space ಗುರಿ ಮುಟ್ಟುತ್ತೆ.
  →  Order ಮುಖ್ಯ: ಮೊದಲು markers set ಮಾಡು (inner cells scan ಮಾಡಿ),
     ಆಮೇಲೆ markers ಪ್ರಕಾರ zero ಮಾಡು — ಇಲ್ಲಾಂದ್ರೆ marker ಗಳೇ zero
     ಆಗಿ information ಕಳ್ಕೊಂಡು ಹೋಗುತ್ತೆ.

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು (Think out loud):
  →  "The straightforward approach stores the set of zero rows and
      zero columns separately — O(m+n) extra space."
  →  "For the O(1) space follow-up, I can reuse the first row and
      first column of the matrix itself as marker space, since I'll
      overwrite them with zeros anyway wherever needed."
  →  "The one tricky overlap is cell (0,0), which would serve as
      marker for both row 0 and column 0 — I handle that with a
      single extra boolean for row 0's own zero status."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Matrix → In-Place Marking (first row/col as markers)
  Secondary : None

  WHY this technique?
  → Follow-up explicitly asks for O(1) extra space, ruling out a
    separate rows/cols tracking set
  → The matrix's own first row and first column have exactly enough
    cells (m + n) to record "this row/col needs zeroing"
  → A single extra boolean resolves the only overlap conflict — cell
    (0,0) shared between row-0 and column-0 marking

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION (How to think — English)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Key observation: we don't need a separate data structure to
  remember which rows/columns must be zeroed — the matrix's own first
  row and first column can double as that memory, since we're going
  to overwrite cells with zero anyway. We just need to record the
  markers BEFORE we start zeroing, and handle the (0,0) overlap with
  one boolean flag for row 0.

  The journey from brute to optimal:
    Brute thought   →  track zero rows/cols in a separate set,
                        then do a second pass to zero them out
    Problem with it →  O(m+n) extra space; the follow-up wants O(1)
    Better question →  "can the matrix itself store which rows/cols
                        need zeroing, without losing the original data
                        I still need to read?"
    Insight         →  use first row and first column as markers,
                        process inner cells first, apply markers last,
                        handle (0,0) overlap with a single boolean
    Optimal         →  in-place marking with O(1) extra space (besides
                        the one boolean)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE (Track Zero Rows/Cols Separately)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    First pass: scan the whole matrix, recording which rows and which
    columns contain at least one zero, in two separate sets. Second
    pass: for every cell, if its row or column is in the zero set,
    set it to 0.

  Pseudocode:
    step 1: zero_rows = set(), zero_cols = set()
    step 2: for r,c in matrix: if matrix[r][c]==0: zero_rows.add(r); zero_cols.add(c)
    step 3: for r,c in matrix: if r in zero_rows or c in zero_cols: matrix[r][c] = 0
    step 4: return matrix

  Time  : O(m*n)  →  Why: two full passes over the matrix
  Space : O(m+n)  →  Why: sets store up to m row indices and n col indices

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ? (Why is this not enough?)
    → Correct, ಆದ್ರೆ follow-up ಸ್ಪಷ್ಟವಾಗಿ O(1) extra space ಕೇಳ್ತಾ
      ಇದೆ — matrix ನ first row/col ಅನ್ನೇ marker ಆಗಿ ಬಳಸಿ ಈ sets
      ಅನ್ನ avoid ಮಾಡ್ಬೋದು.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚶 SECTION 6 — APPROACH 2 — BETTER (skip — brute jumps straight to optimal)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ಇಲ್ಲಿ intermediate approach ಇಲ್ಲ — separate-sets brute force ಇಂದ
  ನೇರವಾಗಿ in-place marking optimal ಗೆ ಹೋಗಬಹುದು.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 7 — APPROACH 3 — OPTIMAL   (In-Place Marking — First Row/Col as Markers)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Use matrix[i][0] and matrix[0][j] as markers for "row i has a
    zero" / "col j has a zero". Since matrix[0][0] belongs to both,
    track row 0's own zero-status separately in a boolean. Steps:
    (1) record whether row 0 originally has any zero, (2) scan cells
    from row 1 onward — whenever matrix[i][j]==0, set matrix[i][0]=0
    and matrix[0][j]=0, (3) using those markers, zero out all inner
    cells (i>=1, j>=1), (4) zero out column 0 if matrix[0][0]==0], and
    zero out row 0 entirely if the boolean from step 1 was True.

  Key steps:
    1. first_row_has_zero = 0 in matrix[0]
    2. for i in range(1, m): for j in range(n): if matrix[i][j]==0: matrix[i][0]=0; matrix[0][j]=0
    3. for i in range(1, m): for j in range(1, n): if matrix[i][0]==0 or matrix[0][j]==0: matrix[i][j]=0
    4. if matrix[0][0]==0: for i in range(1,m): matrix[i][0]=0
    5. if first_row_has_zero: for j in range(n): matrix[0][j]=0

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ (Say it once in Kanglish so it sticks):
    → "row 0 ಗೆ 0 ಇದ್ಯಾ ಅಂತ ಮೊದಲೇ ಒಂದು boolean ನಲ್ಲಿ save ಮಾಡ್ಕೋ. ಆಮೇಲೆ
        row1 ಇಂದ scan ಮಾಡಿ, 0 ಸಿಕ್ಕಾಗ matrix[i][0] ಮತ್ತು matrix[0][j]
        ಗೆ 0 ಬರಿ (markers). ಆಮೇಲೆ ಆ markers ನೋಡಿ inner cells (i,j>=1)
        zero ಮಾಡು. ಕೊನೆಗೆ matrix[0][0]==0 ಆದ್ರೆ column 0 zero ಮಾಡು,
        ಮೊದಲಿನ boolean True ಆಗಿದ್ರೆ row 0 ಪೂರ್ತಿ zero ಮಾಡು!"

  Time  : O(m*n)  →  Why: a constant number of full passes over the matrix
  Space : O(1)    →  Why: only one boolean extra, markers stored in
                    the matrix itself

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 8 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]

  first_row_has_zero = (0 in [1,1,1]) = False

  Scan rows 1..2:
    (1,1)=0 → matrix[1][0]=0, matrix[0][1]=0
    matrix now: [[1,0,1],[0,0,1],[1,1,1]]

  Zero inner cells using markers (i,j from 1..2, 1..2):
    (1,1): matrix[1][0]=0 → set matrix[1][1]=0 (already 0)
    (1,2): matrix[1][0]=0 → set matrix[1][2]=0
    (2,1): matrix[0][1]=0 → set matrix[2][1]=0
    (2,2): matrix[1][0]!=0? matrix[2][0]=1, matrix[0][2]=1 → no change
    matrix now: [[1,0,1],[0,0,0],[1,0,1]]

  matrix[0][0]=1 (not 0) → skip zeroing column 0
  first_row_has_zero=False → skip zeroing row 0

  Output: [[1,0,1],[0,0,0],[1,0,1]]   matches expected

  ಇನ್ನೊಂದು example — tricky case (zero already in row/col 0):
  Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

  first_row_has_zero = (0 in [0,1,2,0]) = True

  Scan rows 1..2 (only original data cells, row 0 untouched here):
    row1 [3,4,5,2] → no zeros
    row2 [1,3,1,5] → no zeros
    (no markers set from inner scan since no zeros in rows 1,2)

  Zero inner cells using markers (i,j from 1..2, 1..3):
    matrix[i][0] and matrix[0][j] checked — matrix[0][0]=0 and
    matrix[0][3]=0 are markers already present from the ORIGINAL data
    → column 0 and column 3 markers are set (they were 0 already)
    (1,1): matrix[0][1]=1, matrix[1][0]=3 → no zero
    (1,2): matrix[0][2]=2, matrix[1][0]=3 → no zero
    (1,3): matrix[0][3]=0 → matrix[1][3]=0
    (2,1): matrix[0][1]=1, matrix[2][0]=1 → no zero
    (2,2): matrix[0][2]=2, matrix[2][0]=1 → no zero
    (2,3): matrix[0][3]=0 → matrix[2][3]=0
    matrix now: [[0,1,2,0],[3,4,5,0],[1,3,1,0]]

  matrix[0][0]==0 → zero out column 0 for rows 1..2:
    matrix[1][0]=0, matrix[2][0]=0
    matrix now: [[0,1,2,0],[0,4,5,0],[0,3,1,0]]

  first_row_has_zero=True → zero out row 0 entirely:
    matrix[0] = [0,0,0,0]

  Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]   matches expected

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 9 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ No zeros at all?           →  no markers ever set, matrix stays
                                   completely unchanged
  ✓ Zero in row 0 or col 0?    →  handled explicitly via the boolean
                                   and matrix[0][0] checks (see Example 2)
  ✓ Single row or single column matrix? →  loops over inner cells
                                   simply don't run, outer marker logic
                                   still correct
  ✓ Entire matrix is zero already? →  every cell stays 0, no issue
  ✓ Zero at matrix[0][0] specifically? →  correctly triggers both the
                                   column-0 zeroing AND (if row 0 had
                                   a zero) row-0 zeroing

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 10 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                Time      Space
  Brute Force   O(m*n)    O(m+n)
  Optimal       O(m*n)    O(1)    ← use this 

  Time ಯಾಕೆ ಅಷ್ಟು?  → constant number of full matrix passes (mark,
                        apply, cleanup) — ಎಲ್ಲಾ ಸೇರಿ ಇನ್ನೂ O(m*n).
  Space ಯಾಕೆ ಅಷ್ಟು? → ಒಂದೇ boolean variable ಬಿಟ್ಟು ಬೇರೆ extra
                        structure ಬೇಡ — markers matrix ಒಳಗೇ store.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 11 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Matrix → In-Place Marking (Reuse Structure as Memory)

  ಈ pattern ಯಾವಾಗ use ಮಾಡಬೇಕು?
  → Matrix ಒಳಗೆ "ಈ row/column affected ಆಗಿದೆ" ಅಂತ ಗುರುತು ಹಾಕ್ಬೇಕಾದಾಗ,
    ಆದ್ರೆ extra space allow ಇಲ್ಲದಾಗ
  → Matrix ನ ಒಂದು part (first row/col) ಅನ್ನ marker ಆಗಿ safely reuse
    ಮಾಡ್ಬಹುದು ಅಂತ ಗೊತ್ತಾದಾಗ (ಆ part ಅನ್ನ ಕೊನೆಗೆ overwrite ಮಾಡೋದೇ ಆಗಿದ್ರೆ)
  → Order ಮುಖ್ಯ ಆಗಿರೋ multi-pass problems (mark first, then apply)

  ಇದೇ pattern ಬೇರೆ problems ನಲ್ಲಿ ಕಾಣಿಸುತ್ತೆ:
  → Rotate Image (#48) — different matrix technique, same in-place mutation family
  → Spiral Matrix (#54) — different problem, same matrix-traversal family
  → Find All Numbers Disappeared in an Array (#448) — array-as-marker trick

  Next time ಇಂತಹ problem ಬಂದ್ರೆ ನಾನು ಮೊದಲು ಇದನ್ನ think ಮಾಡ್ತೇನೆ:
  → "Matrix/array ಒಳಗೆ extra space ಇಲ್ಲದೆ 'affected rows/cols/indices'
      track ಮಾಡ್ಬೇಕು ಅಂತ ಕೇಳಿದ ತಕ್ಷಣ, structure ನ ಒಂದು part ಅನ್ನೇ
      marker ಆಗಿ reuse ಮಾಡ್ಬಹುದಾ ಅಂತ ಮೊದಲು ಯೋಚಿಸು."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 12 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "I need to zero out the entire row and column of every cell that
      originally contains a 0, done in-place, without letting newly
      zeroed cells cause extra zeroing."

  2. Brute force:
     "I could store zero rows/columns in separate sets in one pass,
      then apply them in a second pass — O(m+n) extra space."

  3. Optimize:
     "For O(1) space, I reuse the matrix's own first row and first
      column as marker storage, since I'll be overwriting parts of
      them with zero anyway. The only conflict is cell (0,0), shared
      by both markers, which I resolve with one extra boolean for
      row 0's original zero status."

  4. Code:
     "I will first scan from row 1 onward to set markers in row 0 and
      column 0, then use those markers to zero the inner matrix, and
      finally handle column 0 and row 0 themselves using
      matrix[0][0] and the boolean."

  5. Complexity:
     "Time O(m*n) — a constant number of full passes. Space O(1) —
      only one boolean beyond the matrix itself."

  ಮುಖ್ಯ: ಸುಮ್ಮನೆ ಕೂತು code ಬರೆಯಬೇಡ!
         Interviewer ಗೆ ನಿನ್ನ thinking process ಕಾಣಬೇಕು.
"""


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(m*n) Time | O(m+n) Space  (Track Zero Rows/Cols Separately)
# ═══════════════════════════════════════════════════════════════════
def set_zeroes_brute(matrix):
    """ಇದು ಮೊದಲ ಆಲೋಚನೆ — zero rows/cols ಅನ್ನ separate sets ನಲ್ಲಿ track ಮಾಡೋದು"""
    m, n = len(matrix), len(matrix[0])
    zero_rows, zero_cols = set(), set()

    for r in range(m):
        for c in range(n):
            if matrix[r][c] == 0:
                zero_rows.add(r)
                zero_cols.add(c)

    for r in range(m):
        for c in range(n):
            if r in zero_rows or c in zero_cols:
                matrix[r][c] = 0

    return matrix


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(m*n) Time | O(1) Space  (In-Place Marking — First Row/Col)
# ═══════════════════════════════════════════════════════════════════
def set_zeroes(matrix):
    """ಇದು final answer — matrix ನ first row/col ಅನ್ನೇ marker ಆಗಿ ಬಳಸೋದು"""
    m, n = len(matrix), len(matrix[0])
    first_row_has_zero = 0 in matrix[0]

    # Step 1 — use row 0 and col 0 as markers, scanning from row 1
    for i in range(1, m):
        for j in range(n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    # Step 2 — zero out inner cells based on markers
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    # Step 3 — handle column 0
    if matrix[0][0] == 0:
        for i in range(1, m):
            matrix[i][0] = 0

    # Step 4 — handle row 0
    if first_row_has_zero:
        for j in range(n):
            matrix[0][j] = 0

    return matrix


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")   # Windows cp1252 can't print emoji otherwise

    # Test 1 — Basic example
    assert set_zeroes([[1, 1, 1], [1, 0, 1], [1, 1, 1]]) == [[1, 0, 1], [0, 0, 0], [1, 0, 1]]

    # Test 2 — Edge case: single element, zero
    assert set_zeroes([[0]]) == [[0]]

    # Test 3 — Edge case: no zeros at all
    assert set_zeroes([[1, 2], [3, 4]]) == [[1, 2], [3, 4]]

    # Test 4 — Tricky: zero already sitting in row 0 / col 0
    assert set_zeroes([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]) == \
        [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]

    print("All tests passed! ")
