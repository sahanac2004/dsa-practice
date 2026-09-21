"""
╔══════════════════════════════════════════════════════════════════╗
║  AGGRESSIVE COWS                                                 ║
║  GFG / Classic  |  Difficulty: Medium  |  Topic: Binary Search  ║
║  Link: https://www.geeksforgeeks.org/aggressive-cows/           ║
║  Note: Also appears on SPOJ and various coding platforms         ║
╚══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  There are n stalls at different positions. You need to place k
  cows in these stalls such that the MINIMUM distance between any
  two cows is MAXIMIZED. Return that maximum minimum distance.

  Cows are aggressive — they fight if placed too close together.
  So we want to spread them as far apart as possible.

  Input : stalls = positions of stalls, k = number of cows
  Output: maximum possible minimum distance between any two cows

  Example 1 — basic:
    Input : stalls=[1,2,4,8,9], k=3
    Output: 3
    Why?  : Place cows at positions 1, 4, 9
            distances: 4-1=3, 9-4=5 → min distance = 3
            No better placement gives min distance > 3

  Example 2 — slightly tricky:
    Input : stalls=[10,1,2,7,5], k=3
    Output: 4
    Why?  : Sort → [1,2,5,7,10]
            Place at 1, 5, 10
            distances: 5-1=4, 10-5=5 → min=4 ✓

  Constraints:
    - 2 <= k <= n <= 10^5
    - 0 <= stalls[i] <= 10^9
    - All stall positions are distinct

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Problem odi aada mele namma brain enu think maadabeeku:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  stall positions + k cows     │
  │  Output ಏನು ಬೇಕು?     →  maximize the MINIMUM distance │
  │                           between any two cows          │
  │  Constraints ಏನಿದೆ?   →  positions unsorted, distinct  │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ನನಗೆ ಗೊತ್ತಿರೋ simple way ಏನು?
  →  All possible placements try ಮಾಡಿ max min distance ಹುಡುಕೋಣ
  →  ಆದರೆ ಇದು slow ಯಾಕೆ?
     C(n,k) combinations → exponential → TLE!

  ಹಂತ 3 — Better way ಹೇಗೆ ಯೋಚಿಸುವುದು?
  →  "MAXIMIZE the MINIMUM" — opposite of previous problems!
     (Koko/Ship was MINIMIZE the MAXIMUM)
  →  Answer space: [1, stalls[-1]-stalls[0]] after sorting
     min = 1 (adjacent stalls), max = last-first (2 cows only)
  →  Monotonic: larger min_dist → harder to place k cows
     if min_dist d works → d-1 also works (easier constraint)
  →  Binary search on min_dist, check if k cows placeable!

  ಹಂತ 4 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  Sort stalls first — then greedy placement works!
  →  Greedy: place cow at first stall, then next stall
     that is >= min_dist away from last placed cow
  →  Count cows placed, check if >= k

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು:
  →  "Maximize minimum — binary search on the answer (distance)"
  →  "Sort stalls first, then greedy placement check"
  →  "Opposite direction from Koko — here feasible means MORE cows"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Binary Search → On Answer Space (MAXIMIZE minimum)
  Secondary : Greedy (feasibility — place cows greedily)
  Pre-step  : Sort stalls

  Key difference from previous problems:
  → Previous: MINIMIZE maximum → if feasible, try smaller → right=mid-1
  → This:     MAXIMIZE minimum → if feasible, try larger  → left=mid+1
  → Direction of search FLIPS!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  After sorting stalls, the answer (min distance) lies in [1, last-first].

  For any candidate minimum distance d:
  - Place first cow at stalls[0]
  - For each subsequent stall, place cow there only if its distance
    from last placed cow >= d
  - Count total cows placed
  - If cows placed >= k → d is feasible! (we CAN maintain min dist d)

  Monotonic property (REVERSE of Koko!):
  - Smaller d → easier to place more cows → feasible
  - Larger d → harder to place cows → might not be feasible
  - We want the LARGEST d that is still feasible
  - So: if feasible → try LARGER (left=mid+1), save ans
  - If not feasible → try SMALLER (right=mid-1)

  The journey from brute to optimal:
    Brute thought   →  Try all placements → exponential
    Problem with it →  TLE
    Better question →  "Binary search on the answer distance?"
    Insight         →  Yes! Sort + greedy check + binary search
                       But direction FLIPS — maximize not minimize!
    Optimal         →  O(n log n) sort + O(n log(max_dist)) search

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Sort stalls. Try every possible minimum distance from 1 to
    max_gap. Return the largest distance where k cows fit.

  Pseudocode:
    step 1: sort stalls
    step 2: for d from max_gap down to 1:
    step 3:   if can_place(d, k): return d

  Time  : O(n log n + max_gap × n)  →  Why: sort + linear scan
  Space : O(1)

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ?
    → max_gap = 10^9 → 10^14 ops → TLE!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 6 — APPROACH 2 — OPTIMAL (Binary Search on Answer)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Sort stalls. Binary search on minimum distance [1, last-first].
    For each mid distance, greedily check if k cows can be placed.
    If yes → try LARGER distance (maximize!).
    If no → try SMALLER distance.

  Key steps:
    1. Sort stalls
    2. left=1, right=stalls[-1]-stalls[0], ans=1
    3. While left <= right:
       a. mid = (left+right)//2
       b. if can_place(mid, k) → ans=mid, left=mid+1  ← go LARGER!
       c. else → right=mid-1
    4. return ans

  can_place(min_dist, k):
    cows=1, last=stalls[0]
    for i in range(1, n):
      if stalls[i] - last >= min_dist:
        cows += 1
        last = stalls[i]
        if cows == k: return True
    return cows >= k

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ:
    → "Sort maadu. [1, last-first] ಮೇಲೆ binary search maadu.
       Mid = minimum distance try maadu.
       Greedy: first stall ಲ್ಲಿ cow, next stall >= mid away iddre
       cow place maadu. Total >= k iddre feasible!
       Feasible iddre LARGER try maadu (left=mid+1) — maximize!
       Infeasible iddre smaller try (right=mid-1)."

  Time  : O(n log n + n log(max_dist))  →  sort + binary search
  Space : O(1)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 7 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: stalls=[1,2,4,8,9], k=3
  Already sorted. left=1, right=9-1=8, ans=1

  mid=4 → place: cow1@1, stall2=2(2-1=1<4)skip, stall3=4(4-1=3<4)
          skip, stall4=8(8-1=7>=4)cow2@8, stall5=9(9-8=1<4)skip
          cows=2 < 3 ✗ → right=3

  mid=2 → place: cow1@1, stall2=2(2-1=1<2)skip, stall3=4(4-1=3>=2)
          cow2@4, stall4=8(8-4=4>=2)cow3@8
          cows=3 >= 3 ✓ → ans=2, left=3

  mid=3 → place: cow1@1, stall2=2(1<3)skip, stall3=4(3>=3)cow2@4,
          stall4=8(4>=3)cow3@8
          cows=3 >= 3 ✓ → ans=3, left=4

  left=4 > right=3 → return ans=3 ✓

  ಇನ್ನೊಂದು:
  Input: stalls=[10,1,2,7,5], k=3
  Sort → [1,2,5,7,10], left=1, right=9

  mid=5 → cow1@1, 2(1<5)skip, 5(4<5)skip, 7(6>=5)cow2@7,
          10(3<5)skip → cows=2 < 3 ✗ → right=4

  mid=2 → cow1@1, 2(1<2)skip, 5(4>=2)cow2@5, 7(2>=2)cow3@7
          cows=3 >= 3 ✓ → ans=2, left=3

  mid=3 → cow1@1, 2(1<3)skip, 5(4>=3)cow2@5, 7(2<3)skip,
          10(5>=3)cow3@10 → cows=3 >= 3 ✓ → ans=3, left=4

  mid=4 → cow1@1, 2(1<4)skip, 5(4>=4)cow2@5, 7(2<4)skip,
          10(5>=4)cow3@10 → cows=3 >= 3 ✓ → ans=4, left=5

  left=5 > right=4 → return ans=4 ✓

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 8 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ k == 2?          →  Just first and last stall → stalls[-1]-stalls[0]
  ✓ k == n?          →  Every stall has one cow → min adjacent gap
  ✓ Unsorted input?  →  MUST sort first!
  ✓ All same gaps?   →  [1,3,5,7], k=2 → max gap = 6

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 9 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                  Time                      Space
  Brute Force     O(n log n + max_gap × n)  O(1)
  Optimal         O(n log n + n log(range)) O(1)   ← use this ✅

  Time yaake O(n log n + n log range)?
    → Sort: O(n log n)
    → Binary search: log(range) steps × O(n) each
  Space yaake O(1)?
    → Only pointers and cow counter

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 10 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Binary Search on Answer Space — MAXIMIZE minimum

  TWO flavors of binary search on answer space:

  MINIMIZE maximum (Koko, Ship, Split):
  → if feasible → try SMALLER → right=mid-1, ans=mid
  → answer converges from RIGHT

  MAXIMIZE minimum (Aggressive Cows, Book Allocation):
  → if feasible → try LARGER → left=mid+1, ans=mid
  → answer converges from LEFT

  Ee pattern yaavaaga use maadabeeku?
  → "Maximize minimum distance/gap between k elements"
  → "Place k items to maximize the minimum separation"
  → Always sort first, then greedy placement check

  Idee pattern beere problemsalli kaanisatte:
  → Book Allocation GFG (next problem — same pattern!)
  → EKO on SPOJ (classic problem — same as Koko)
  → Painter's Partition GFG

  Next time intaha problem bandre naanu modalu idannu think maadtene:
  → "Maximize minimum iddre → Binary Search on answer!
     Sort maadu. Greedy check: place items with min dist.
     Feasible iddre LARGER try (left=mid+1) — maximize direction!"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 11 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "Place k cows in stalls to maximize the minimum distance
      between any two cows."

  2. Brute force:
     "Try all placements — exponential. TLE."

  3. Optimize:
     "Binary search on the answer (minimum distance).
      Range: [1, last_stall - first_stall] after sorting.
      Key difference from Koko: we MAXIMIZE minimum, so when
      feasible we go LARGER (left=mid+1), not smaller.
      Feasibility: greedily place cows, each >= mid dist apart."

  4. Code:
     "Sort stalls. left=1, right=stalls[-1]-stalls[0].
      can_place: cow1@stalls[0], for each stall if dist>=mid
      place cow, count. Return count>=k.
      If feasible → ans=mid, left=mid+1."

  5. Complexity:
     "Time O(n log n + n log range). Space O(1)."

  Mukhya: summane kuutu code bareyabeda!
          MAXIMIZE vs MINIMIZE direction flip — mention this clearly!
          Sort first — easy to forget, mention it!
"""


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(n log n + max_gap × n) Time | O(1) Space
# ═══════════════════════════════════════════════════════════════════
def aggressive_cows_brute(stalls, k):
    """Idu modala aaloochane — try every distance linearly"""
    stalls.sort()
    n = len(stalls)

    def can_place(min_dist):
        cows = 1
        last = stalls[0]
        for i in range(1, n):
            if stalls[i] - last >= min_dist:
                cows += 1
                last = stalls[i]
                if cows == k:
                    return True
        return cows >= k

    ans = 1
    for d in range(1, stalls[-1] - stalls[0] + 1):
        if can_place(d):
            ans = d
        else:
            break   # once infeasible, larger d also infeasible

    return ans


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n log n + n log range) Time | O(1) Space
# ═══════════════════════════════════════════════════════════════════
def aggressive_cows(stalls, k):
    """
    Idu final answer — binary search on answer space
    MAXIMIZE minimum → if feasible go LARGER (left=mid+1)
    Sort first! Greedy placement check.
    """
    stalls.sort()
    n = len(stalls)

    def can_place(min_dist):
        """Greedy: place cows maintaining minimum distance"""
        cows = 1
        last = stalls[0]       # place first cow at first stall
        for i in range(1, n):
            if stalls[i] - last >= min_dist:
                cows += 1
                last = stalls[i]   # update last placed position
                if cows == k:
                    return True
        return cows >= k

    left  = 1                           # min possible distance
    right = stalls[-1] - stalls[0]     # max possible distance
    ans   = 1

    while left <= right:
        mid = (left + right) // 2

        if can_place(mid):
            ans  = mid          # feasible! try LARGER distance
            left = mid + 1      # ← KEY: go right to maximize!
        else:
            right = mid - 1     # not feasible, try smaller

    return ans


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # Test 1 — Basic
    assert aggressive_cows([1, 2, 4, 8, 9], 3) == 3

    # Test 2 — Unsorted input
    assert aggressive_cows([10, 1, 2, 7, 5], 3) == 4

    # Test 3 — k == 2 (just first and last)
    assert aggressive_cows([1, 2, 3, 4, 5], 2) == 4

    # Test 4 — k == n (every stall one cow)
    assert aggressive_cows([1, 3, 5, 7], 4) == 2

    # Test 5 — Large gap
    assert aggressive_cows([1, 100], 2) == 99

    # Test 6 — Three cows, even spread
    assert aggressive_cows([0, 3, 4, 7, 10, 9], 3) == 4

    print("All tests passed!")
