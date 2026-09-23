"""
╔══════════════════════════════════════════════════════════════════╗
║  PAINTER'S PARTITION PROBLEM                                     ║
║  GFG Classic  |  Difficulty: Medium  |  Topic: Binary Search    ║
║  Link: https://www.geeksforgeeks.org/painters-partition-problem/ ║
╚══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  There are n boards of different lengths and k painters. Each
  painter paints CONTIGUOUS boards. A painter takes 1 unit of time
  per unit of board length. All painters work simultaneously.
  Minimize the TIME taken to paint all boards.

  This is IDENTICAL to Book Allocation — just different story:
    books    → boards
    students → painters
    pages    → board lengths
    minimize max pages → minimize max time (= max total length)

  Input : boards = list of board lengths, k = number of painters
  Output: minimum time to paint all boards

  Example 1 — basic:
    Input : boards=[10,20,30,40], k=2
    Output: 60
    Why?  : Painter1: [10,20,30]=60, Painter2: [40]=40
            Time = max(60,40) = 60 ✓
            Any other split gives larger max.

  Example 2 — slightly tricky:
    Input : boards=[10,20,30,40], k=4
    Output: 40
    Why?  : Each painter paints one board → max = 40

  Constraints:
    - 1 <= k <= n <= 10^5
    - 1 <= boards[i] <= 10^6

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Problem odi aada mele namma brain enu think maadabeeku:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  board lengths + k painters  │
  │  Output ಏನು ಬೇಕು?     →  minimize max time             │
  │                           (= minimize max total length) │
  │  Constraints ಏನಿದೆ?   →  contiguous boards only,      │
  │                           all paint simultaneously      │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ನನಗೆ ಗೊತ್ತಿರೋ simple way ಏನು?
  →  All splits try ಮಾಡಿ minimum of maximum ಹುಡುಕೋಣ → slow

  ಹಂತ 3 — Better way ಹೇಗೆ ಯೋಚಿಸುವುದು?
  →  "Book Allocation exact same problem different words!"
  →  books=boards, students=painters, pages=lengths
  →  Binary search on [max(boards), sum(boards)]
  →  Feasibility: greedy assign, count painters <= k

  ಹಂತ 4 — ಇಲ್ಲಿ ಒಂದು KEY difference:
  →  Book Allocation: m > n iddre -1 (impossible)
  →  Painter's Partition: k >= n iddre ALWAYS possible
     (each painter paints one board max)
  →  So no -1 case here! Always return a valid answer

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು:
  →  "This is Book Allocation — boards instead of books!"
  →  "No -1 case — k painters can always paint n boards"
  →  "Binary search on [max(boards), sum(boards)]"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Binary Search → On Answer Space
  Secondary : Greedy (feasibility — assign boards greedily)

  Identical to: Book Allocation, Split Array, Ship Packages
  Only story changes — code template is the same!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Same intuition as Book Allocation — just map the variables:
    books    → boards
    pages    → board lengths
    students → painters
    max pages assigned → max time taken

  Since all painters work simultaneously, the total time is
  determined by the painter who gets the most work (max sum).
  We want to minimize this maximum.

  The journey from brute to optimal:
    Brute thought   →  Try all splits → exponential
    Problem with it →  TLE
    Better question →  "Same as Book Allocation?"
    Insight         →  YES! Exact same template
    Optimal         →  O(n log(sum)) binary search + greedy

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea: Try every possible max time from max(boards) to sum(boards).

  Time  : O(n × sum)  →  TLE
  Space : O(1)

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ?
    → sum up to 10^11 → TLE!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 6 — APPROACH 2 — OPTIMAL (Binary Search)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Binary search on max time [max(boards), sum(boards)].
    For each mid, check if k painters can finish in time mid.
    If yes → try smaller. If no → try larger.

  can_paint(max_time, k):
    painters=1, current=0
    for length in boards:
      if current + length > max_time:
        painters += 1
        current = 0
      current += length
    return painters <= k

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ:
    → "[max(boards), sum(boards)] ಮೇಲೆ binary search maadu.
       Mid = max time allowed per painter.
       Greedy: exceed iddre new painter, count <= k iddre feasible.
       Feasible iddre smaller try. Book Allocation same template!"

  Time  : O(n log(sum))
  Space : O(1)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 7 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: boards=[10,20,30,40], k=2
  left=40, right=100, ans=100

  mid=70 → 10+20+30=60<=70, +40=100>70 → painter2: 40
           painters=2 <=2 ✓ → ans=70, right=69

  mid=54 → 10+20+30=60>54 → 10+20=30, +30=60>54
           painter2: 30+40=70>54 → painter3: 40
           painters=3 > 2 ✗ → left=55

  mid=62 → 10+20+30=60<=62, +40=100>62
           painter2: 40 → painters=2 <=2 ✓ → ans=62, right=61

  mid=58 → 10+20+30=60>58 → 10+20=30,+30=60>58
           painter2: 30+40=70>58 → painter3: 40
           painters=3 > 2 ✗ → left=59

  mid=60 → 10+20+30=60<=60, +40=100>60
           painter2: 40 → painters=2 <=2 ✓ → ans=60, right=59

  left=59 > right=59... wait left=59, right=59
  mid=59 → 10+20+30=60>59 → painters=3 > 2 ✗ → left=60

  left=60 > right=59 → return ans=60 ✓

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 8 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ k >= n?         →  Each painter ≤1 board → max(boards)
  ✓ k == 1?         →  One painter all boards → sum(boards)
  ✓ Single board?   →  [l], k=1 → l
  ✓ All same?       →  [5,5,5,5], k=2 → 10
  ✓ No -1 case!     →  Unlike Book Allocation, always possible

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 9 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                  Time              Space
  Brute Force     O(n × sum)        O(1)
  Optimal         O(n × log(sum))   O(1)   ← use this ✅

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 10 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Binary Search on Answer Space — Complete Family

  THE COMPLETE FAMILY (final version):
  ┌───────────────────┬────────────────────┬───────────────────┐
  │ Problem           │ Answer Range       │ Direction         │
  ├───────────────────┼────────────────────┼───────────────────┤
  │ Koko      #875    │ [1, max(piles)]    │ MINIMIZE → right  │
  │ Bouquets  #1482   │ [1, max(bloom)]    │ MINIMIZE → right  │
  │ Divisor   #1283   │ [1, max(nums)]     │ MINIMIZE → right  │
  │ Ship      #1011   │ [max(w), sum(w)]   │ MINIMIZE → right  │
  │ Split     #410    │ [max(n), sum(n)]   │ MINIMIZE → right  │
  │ Books     GFG     │ [max(p), sum(p)]   │ MINIMIZE → right  │
  │ Painters  GFG     │ [max(b), sum(b)]   │ MINIMIZE → right  │
  │ Cows      GFG     │ [1, last-first]    │ MAXIMIZE → left   │
  └───────────────────┴────────────────────┴───────────────────┘

  Ship, Split, Books, Painters ← ALL SAME CODE, different names!

  Next time intaha problem bandre naanu modalu idannu think maadtene:
  → "Assign items to workers minimize maximum load?
     → Binary search [max, sum]. Greedy count. Same template!"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 11 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "Assign contiguous boards to k painters (working simultaneously)
      to minimize the maximum time taken."

  2. Brute force:
     "Try all splits — exponential. TLE."

  3. Optimize:
     "This is Book Allocation — boards instead of books, painters
      instead of students. Binary search on [max(boards), sum(boards)].
      Feasibility: greedy assign, count painters <= k."

  4. Code:
     "Same as Book Allocation minus the -1 check.
      can_paint: greedy count painters. Binary search template."

  5. Complexity:
     "Time O(n log sum). Space O(1)."

  Mukhya: summane kuutu code bareyabeda!
          "Identical to Book Allocation" — show pattern mastery!
          No -1 case here — important difference to mention!
"""


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n log(sum)) Time | O(1) Space
# ═══════════════════════════════════════════════════════════════════
def painters_partition(boards, k):
    """
    Idu final answer — IDENTICAL to Book Allocation
    boards=books, lengths=pages, painters=students
    No -1 case — k painters can always paint n boards
    """
    def can_paint(max_time):
        """Greedy: assign boards, new painter when exceeded"""
        painters = 1
        current = 0
        for length in boards:
            if current + length > max_time:
                painters += 1
                current = 0
            current += length
        return painters <= k

    left  = max(boards)    # min: painter must paint longest board
    right = sum(boards)    # max: one painter paints everything
    ans   = right

    while left <= right:
        mid = (left + right) // 2

        if can_paint(mid):
            ans   = mid           # feasible! try smaller time
            right = mid - 1
        else:
            left = mid + 1        # not feasible, need more time

    return ans


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # Test 1 — Basic
    assert painters_partition([10, 20, 30, 40], 2) == 60

    # Test 2 — k == n (each painter one board)
    assert painters_partition([10, 20, 30, 40], 4) == 40

    # Test 3 — k == 1 (one painter all boards)
    assert painters_partition([10, 20, 30, 40], 1) == 100

    # Test 4 — k > n (extra painters idle)
    assert painters_partition([10, 20, 30], 5) == 30

    # Test 5 — All same lengths
    assert painters_partition([5, 5, 5, 5], 2) == 10

    # Test 6 — Single board
    assert painters_partition([100], 1) == 100

    # Test 7 — GFG example
    assert painters_partition([10, 20, 30, 40], 2) == 60

    print("All tests passed!")
