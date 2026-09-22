"""
╔══════════════════════════════════════════════════════════════════╗
║  BOOK ALLOCATION PROBLEM                                         ║
║  GFG Classic  |  Difficulty: Medium  |  Topic: Binary Search    ║
║  Link: https://www.geeksforgeeks.org/allocate-minimum-number-   ║
║        pages/                                                    ║
║  Also known as: Allocate Minimum Pages                          ║
╚══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  There are n books with pages[i] pages each. Allocate books to m
  students such that:
    - Each student gets AT LEAST one book
    - Each student gets CONTIGUOUS books
    - No book is given to more than one student
  Minimize the MAXIMUM number of pages assigned to any student.

  Input : pages = list of page counts, m = number of students
  Output: minimum possible maximum pages assigned to any student
          Return -1 if allocation is impossible (m > n)

  Example 1 — basic:
    Input : pages=[12,34,67,90], m=2
    Output: 113
    Why?  : Best split: [12,34,67] and [90]
            sums = 113 and 90 → max = 113
            Other split [12,34] and [67,90] → max=157 ✗
            [12] and [34,67,90] → max=191 ✗

  Example 2 — slightly tricky (impossible):
    Input : pages=[12,34,67,90], m=5
    Output: -1
    Why?  : 4 books, 5 students → impossible!

  Constraints:
    - 1 <= n <= 10^5
    - 1 <= pages[i] <= 10^6
    - 1 <= m <= n

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Problem odi aada mele namma brain enu think maadabeeku:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  pages array + m students     │
  │  Output ಏನು ಬೇಕು?     →  minimize the MAXIMUM pages   │
  │                           any student gets              │
  │  Constraints ಏನಿದೆ?   →  contiguous books only,       │
  │                           m > n iddre -1 return        │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ನನಗೆ ಗೊತ್ತಿರೋ simple way ಏನು?
  →  All possible splits try ಮಾಡಿ minimum of maximum ಹುಡುಕೋಣ
  →  ಆದರೆ ಇದು slow ಯಾಕೆ?
     C(n-1, m-1) splits → exponential → TLE!

  ಹಂತ 3 — Better way ಹೇಗೆ ಯೋಚಿಸುವುದು?
  →  "Split Array Largest Sum #410 exact same problem!"
  →  Answer space: [max(pages), sum(pages)]
     min = max(pages) → each student at least one book
     max = sum(pages) → one student gets all books
  →  Monotonic: larger max_pages → fewer students needed
     if capacity C works in m students → C+1 also works
  →  Binary search on max_pages, check if m students sufficient!

  ಹಂತ 4 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  MINIMIZE maximum → same direction as Split Array/Ship Packages
  →  if feasible → try SMALLER (right=mid-1)
  →  Feasibility: greedy assign books, count students needed

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು:
  →  "This is Split Array Largest Sum with books and students!"
  →  "Binary search on [max(pages), sum(pages)]"
  →  "Feasibility: greedily assign contiguous books, count students"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Binary Search → On Answer Space (MINIMIZE maximum)
  Secondary : Greedy (feasibility check — assign books greedily)

  Comparison with similar problems:
  → Split Array #410  : nums → subarrays → k pieces
  → Ship Packages #1011: weights → days → k days
  → Book Allocation   : pages → students → m students
  ALL THREE are the EXACT same template!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Binary search on the answer: "What is the minimum possible
  maximum pages any student can be assigned?"

  For any candidate maximum C:
  - Greedily assign books left to right
  - If adding next book exceeds C → give to next student
  - Count students needed
  - If students needed <= m → C is feasible

  Monotonic: larger C → easier to fit in m students → if C works,
  C+1 also works. Binary search for MINIMUM feasible C.

  The journey from brute to optimal:
    Brute thought   →  Try all contiguous splits → exponential
    Problem with it →  TLE
    Better question →  "Same as Split Array / Ship Packages?"
    Insight         →  YES! Identical template — books=packages,
                       students=days, pages=weights
    Optimal         →  O(n log(sum)) — binary search + greedy

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Try every possible maximum pages from max(pages) to sum(pages).
    Return first value where m students can cover all books.

  Time  : O(n × sum(pages))  →  TLE for large inputs
  Space : O(1)

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ?
    → sum up to 10^11 → TLE!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 6 — APPROACH 2 — OPTIMAL (Binary Search on Answer)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Binary search on max pages [max(pages), sum(pages)].
    For each mid, check if m students can cover all books.
    If yes → try smaller. If no → try larger.

  Key steps:
    1. If m > n → return -1 (impossible)
    2. left=max(pages), right=sum(pages), ans=right
    3. While left <= right:
       a. mid = (left+right)//2
       b. if can_allocate(mid, m) → ans=mid, right=mid-1
       c. else → left=mid+1
    4. return ans

  can_allocate(max_pages, m):
    students=1, current=0
    for p in pages:
      if current + p > max_pages:
        students += 1     # new student
        current = 0
      current += p
    return students <= m

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ:
    → "m > n iddre -1. Answer space [max(pages), sum(pages)].
       Binary search maadu. Mid = max pages allowed per student.
       Greedy: exceed iddre new student, count <= m iddre feasible.
       Feasible iddre smaller try (right=mid-1).
       Split Array/Ship Packages EXACT same template!"

  Time  : O(n × log(sum(pages)))
  Space : O(1)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 7 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: pages=[12,34,67,90], m=2
  left=90, right=203, ans=203

  mid=146 → 12+34+67=113<=146, +90=203>146 → student2: 90
            students=2 <= 2 ✓ → ans=146, right=145

  mid=117 → 12+34+67=113<=117, +90=203>117 → student2: 90
            students=2 <= 2 ✓ → ans=117, right=116

  mid=103 → 12+34+67=113>103 → 12+34=46<=103, +67=113>103
            student2: 67+90=157>103 → student3: 90
            students=3 > 2 ✗ → left=104

  mid=110 → 12+34+67=113>110 → 12+34=46, +67=113>110
            student2: 67+90=157>110 → student3: 90
            students=3 > 2 ✗ → left=111

  mid=113 → 12+34+67=113<=113, +90=203>113
            student2: 90 → students=2 <=2 ✓ → ans=113, right=112

  left=111, right=112
  mid=111 → 12+34=46, +67=113>111 → student2: 67+90=157>111
            → student3: 90 → students=3 > 2 ✗ → left=112

  mid=112 → same as 111 → students=3 > 2 ✗ → left=113

  left=113 > right=112 → return ans=113 ✓

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 8 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ m > n?          →  -1 (more students than books — impossible)
  ✓ m == n?         →  Each student one book → max(pages)
  ✓ m == 1?         →  One student all books → sum(pages)
  ✓ Single book?    →  [p], m=1 → p
  ✓ All same pages? →  [5,5,5,5], m=2 → 10

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 9 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                  Time                  Space
  Brute Force     O(n × sum(pages))     O(1)
  Optimal         O(n × log(sum))       O(1)   ← use this ✅

  Time yaake O(n log sum)?
    → log(sum) binary search steps
    → Each step O(n) greedy allocation
  Space yaake O(1)?
    → Only left, right, mid, ans, current, students

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 10 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Binary Search on Answer Space — complete family

  THE COMPLETE FAMILY:
  ┌───────────────┬───────────────────┬───────────────────────┐
  │ Problem       │ Answer Range      │ Feasibility           │
  ├───────────────┼───────────────────┼───────────────────────┤
  │ Koko    #875  │ [1, max(piles)]   │ ceil sum <= h         │
  │ Bouq   #1482  │ [1, max(bloom)]   │ bouquets >= m         │
  │ Div    #1283  │ [1, max(nums)]    │ ceil sum <= threshold  │
  │ Ship   #1011  │ [max(w), sum(w)]  │ days_needed <= d      │
  │ Split   #410  │ [max(n), sum(n)]  │ pieces <= k           │
  │ Books  (GFG)  │ [max(p), sum(p)]  │ students <= m         │
  │ Cows   (GFG)  │ [1, last-first]   │ cows_placed >= k      │
  └───────────────┴───────────────────┴───────────────────────┘

  MINIMIZE max → if feasible: right=mid-1 (go smaller)
  MAXIMIZE min → if feasible: left=mid+1  (go larger)

  Next time intaha problem bandre naanu modalu idannu think maadtene:
  → "Allocate items to minimize maximum load?
     → Binary Search! [max, sum] range.
     Greedy: exceed iddre new person, count <= m?"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 11 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "Allocate contiguous books to m students minimizing the
      maximum pages any student reads. Return -1 if m > n."

  2. Brute force:
     "Try all contiguous splits — exponential. TLE."

  3. Optimize:
     "This is Split Array Largest Sum with books and students.
      Binary search on [max(pages), sum(pages)].
      Feasibility: greedily assign books, new student when exceeded.
      If students needed <= m → feasible, try smaller."

  4. Code:
     "Check m > n → -1. Binary search. can_allocate: greedy count.
      Feasible → ans=mid, right=mid-1."

  5. Complexity:
     "Time O(n log sum). Space O(1)."

  Mukhya: summane kuutu code bareyabeda!
          m > n early check — easy marks in interview!
          Show the full family table — impressive!
"""


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(n × sum) Time | O(1) Space
# ═══════════════════════════════════════════════════════════════════
def allocate_books_brute(pages, m):
    """Idu modala aaloochane — try every max pages linearly"""
    n = len(pages)
    if m > n:
        return -1

    def can_allocate(max_pages):
        students = 1
        current = 0
        for p in pages:
            if current + p > max_pages:
                students += 1
                current = 0
            current += p
        return students <= m

    for cap in range(max(pages), sum(pages) + 1):
        if can_allocate(cap):
            return cap
    return -1


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n log(sum)) Time | O(1) Space
# ═══════════════════════════════════════════════════════════════════
def allocate_books(pages, m):
    """
    Idu final answer — binary search on [max(pages), sum(pages)]
    IDENTICAL to Split Array #410 and Ship Packages #1011
    Only difference: check m > n first for impossible case
    """
    n = len(pages)

    # impossible: more students than books
    if m > n:
        return -1

    def can_allocate(max_pages):
        """Greedy: assign books, new student when exceeded"""
        students = 1
        current = 0
        for p in pages:
            if current + p > max_pages:
                students += 1     # give to next student
                current = 0
            current += p
        return students <= m

    left  = max(pages)    # must give at least one book → max pages
    right = sum(pages)    # worst case: one student all books
    ans   = right

    while left <= right:
        mid = (left + right) // 2

        if can_allocate(mid):
            ans   = mid           # feasible! try smaller
            right = mid - 1
        else:
            left = mid + 1        # not enough, need bigger cap

    return ans


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # Test 1 — Basic
    assert allocate_books([12, 34, 67, 90], 2) == 113

    # Test 2 — Impossible
    assert allocate_books([12, 34, 67, 90], 5) == -1

    # Test 3 — m == n (each student one book)
    assert allocate_books([12, 34, 67, 90], 4) == 90

    # Test 4 — m == 1 (one student all books)
    assert allocate_books([12, 34, 67, 90], 1) == 203

    # Test 5 — Single book
    assert allocate_books([100], 1) == 100

    # Test 6 — All same pages
    assert allocate_books([5, 5, 5, 5], 2) == 10

    # Test 7 — GFG example
    assert allocate_books([10, 20, 30, 40], 2) == 60

    print("All tests passed!")
