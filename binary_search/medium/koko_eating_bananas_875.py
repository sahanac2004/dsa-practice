"""
╔══════════════════════════════════════════════════════════════════╗
║  KOKO EATING BANANAS                                             ║
║  LeetCode #875  |  Difficulty: Medium  |  Topic: Binary Search  ║
║  Link: https://leetcode.com/problems/koko-eating-bananas/       ║
╚══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Koko loves bananas. There are n piles of bananas, piles[i] is
  the number of bananas in the ith pile. Guards will come in h hours.
  Koko can eat k bananas per hour. If a pile has fewer than k bananas,
  she eats them all and does not eat more. She wants to eat all
  bananas before guards come. Find the MINIMUM k such that she can
  finish all bananas within h hours.

  Input : piles = list of pile sizes, h = hours available
  Output: minimum eating speed k (bananas per hour)

  Example 1 — basic:
    Input : piles = [3,6,7,11], h = 8
    Output: 4
    Why?  : speed=4 → ceil(3/4)+ceil(6/4)+ceil(7/4)+ceil(11/4)
                     = 1+2+2+3 = 8 hours ✓ (exactly h hours)

  Example 2 — slightly tricky:
    Input : piles = [30,11,23,4,20], h = 5
    Output: 30
    Why?  : h == n means she must eat each pile in exactly 1 hour
            so speed must be >= max pile = 30

  Constraints:
    - 1 <= piles.length <= 10^4
    - piles.length <= h <= 10^9
    - 1 <= piles[i] <= 10^9

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Problem odi aada mele namma brain enu think maadabeeku:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  piles array + h hours        │
  │  Output ಏನು ಬೇಕು?     →  minimum speed k to finish    │
  │                           all bananas in h hours        │
  │  Constraints ಏನಿದೆ?   →  piles.length <= h (so always │
  │                           possible), piles[i] up to 10^9│
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ನನಗೆ ಗೊತ್ತಿರೋ simple way ಏನು?
  →  k=1 ಇಂದ max(piles) ತನಕ try ಮಾಡಿ first valid k return ಮಾಡೋಣ
  →  ಆದರೆ ಇದು slow ಯಾಕೆ?
     max(piles) = 10^9 → 10^9 iterations → TLE!

  ಹಂತ 3 — Better way ಹೇಗೆ ಯೋಚಿಸುವುದು?
  →  "Answer space 1 to max(piles) — sorted range!"
  →  Key property: k ಜಾಸ್ತಿ ಆದಷ್ಟೂ hours ಕಡಿಮೆ ಬೇಕಾಗತ್ತೆ
     → monotonic! k increase → hours decrease
  →  If k works → k+1 also works (faster = always valid)
     If k doesn't work → k-1 also doesn't work
  →  Binary search on answer space 1 to max(piles)!

  ಹಂತ 4 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  Answer space sorted (1 to max_pile) + monotonic property
  →  is_feasible(k): ceil(pile/k) sum <= h ಅಂತ check ಮಾಡಬಹуದು
  →  Binary search on feasibility → O(n log(max_pile))

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು:
  →  "This is binary search on the ANSWER, not on the array"
  →  "Answer range: 1 (slowest) to max(piles) (finish each in 1hr)"
  →  "Property: if speed k works, k+1 also works → monotonic
      → binary search on feasibility"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Binary Search → On Answer Space
  Secondary : Math — ceiling division trick

  WHY Binary Search on Answer Space?
  → We are NOT searching in the array
  → We are searching for the minimum valid ANSWER
  → Answer range [1, max(piles)] is sorted + monotonic
  → feasible(k) function lets us eliminate half each step
  → This is the GATEWAY pattern — many hard problems use this!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Instead of searching for target IN the array, we are searching
  for the minimum VALUE that satisfies a condition.

  Think of it this way — for any speed k:
  - Hours needed = sum of ceil(pile / k) for all piles
  - If hours_needed <= h → k is feasible (but maybe not minimum)
  - If hours_needed > h → k is too slow, need faster speed

  The feasibility is MONOTONIC:
  - Too slow (small k) → not feasible
  - Fast enough (large k) → feasible
  - There's a cutoff point — binary search finds it!

  The journey from brute to optimal:
    Brute thought   →  Try every k from 1 to max(piles) → O(n × max)
    Problem with it →  max = 10^9 → TLE
    Better question →  "Is feasibility monotonic in k?"
    Insight         →  Yes! Higher k = fewer hours = always feasible
                       → Binary search on k from 1 to max(piles)
    Optimal         →  O(n log(max_pile))

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Try every speed from 1 to max(piles). For each speed,
    calculate total hours needed. Return first speed where
    hours <= h.

  Pseudocode:
    step 1: for k from 1 to max(piles):
    step 2:   hours = sum(ceil(pile/k) for pile in piles)
    step 3:   if hours <= h: return k

  Time  : O(n × max(piles))  →  Why: max_pile speeds × n piles each
  Space : O(1)               →  Why: no extra space

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ?
    → max(piles) = 10^9, n = 10^4 → 10^13 operations → TLE!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 6 — APPROACH 2 — OPTIMAL (Binary Search on Answer)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Binary search on the answer space [1, max(piles)].
    For each mid speed, check if it's feasible.
    If feasible → try smaller (find minimum). If not → try larger.

  Key steps:
    1. left=1, right=max(piles)
    2. While left <= right:
       a. mid = (left+right)//2
       b. hours = sum(ceil(pile/mid) for pile in piles)
          → use math: ceil(a/b) = (a + b - 1) // b
       c. if hours <= h → feasible! save answer, try smaller
          → ans=mid, right=mid-1
       d. if hours > h → too slow, need faster → left=mid+1
    3. return ans

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ:
    → "Speed 1 to max(piles) ಮೇಲೆ binary search maadu.
       Mid speed ಗೆ total hours calculate maadu using ceil(pile/mid).
       hours <= h ಆದ್ರೆ → valid! ans save maadu, smaller try maadu.
       hours > h ಆದ್ರೆ → too slow, faster try maadu. O(n log max)!"

  Time  : O(n × log(max(piles)))  →  Why: log(max) binary search
                                        steps, each step O(n) check
  Space : O(1)                    →  Why: only pointers and ans

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 7 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: piles=[3,6,7,11], h=8
  left=1, right=11, ans=11

  mid=6 → hours=ceil(3/6)+ceil(6/6)+ceil(7/6)+ceil(11/6)
                = 1 + 1 + 2 + 2 = 6 <= 8 ✓ → ans=6, right=5

  mid=3 → hours=ceil(3/3)+ceil(6/3)+ceil(7/3)+ceil(11/3)
                = 1 + 2 + 3 + 4 = 10 > 8 ✗ → left=4

  mid=4 → hours=ceil(3/4)+ceil(6/4)+ceil(7/4)+ceil(11/4)
                = 1 + 2 + 2 + 3 = 8 <= 8 ✓ → ans=4, right=3

  left=4 > right=3 → exit
  return 4 ✓

  ಇನ್ನೊಂದು — h equals pile count:
  Input: piles=[30,11,23,4,20], h=5

  left=1, right=30
  mid=15 → hours=2+1+2+1+2=8 > 5 → left=16
  mid=23 → hours=2+1+1+1+1=6 > 5 → left=24
  mid=27 → hours=2+1+1+1+1=6 > 5 → left=28
  mid=29 → hours=2+1+1+1+1=6 > 5 → left=30
  mid=30 → hours=1+1+1+1+1=5 <= 5 ✓ → ans=30, right=29
  left=30 > right=29 → return 30 ✓

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 8 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ h == n (piles count)?    →  Speed must be max(piles)
  ✓ h very large?            →  Speed = 1 (lots of time available)
  ✓ Single pile?             →  [10], h=10 → speed=1
  ✓ All piles same size?     →  [5,5,5], h=3 → speed=5
  ✓ Large pile values?       →  piles[i] up to 10^9 → use //
                                 not division to avoid float issues

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 9 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                  Time                    Space
  Brute Force     O(n × max(piles))       O(1)
  Optimal         O(n × log(max(piles)))  O(1)   ← use this ✅

  Time yaake O(n log max)?
    → log(max) binary search steps on answer space
    → Each step O(n) to compute total hours
  Space yaake O(1)?
    → Only left, right, mid, ans variables

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 10 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Binary Search on Answer Space

  Ee pattern yaavaaga use maadabeeku?
  → "Find minimum/maximum X such that condition is satisfied"
  → Answer range is bounded and monotonic (if X works, X+1 works)
  → Can write a feasibility check function

  Signal words in problem:
  → "minimum speed", "minimum days", "minimum capacity"
  → "maximum pages per student", "minimum force"

  Idee pattern beere problemsalli kaanisatte:
  → Minimum Days to Make Bouquets #1482
  → Capacity to Ship Packages #1011
  → Split Array Largest Sum #410
  → Aggressive Cows GFG
  → Book Allocation GFG
  → ALL next problems in our binary search list!

  Next time intaha problem bandre naanu modalu idannu think maadtene:
  → "Minimum/maximum value find maadabekittu + feasibility check
     possible iddre → Binary Search on Answer Space!
     left=min_possible, right=max_possible, mid check maadu!"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 11 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "Find minimum eating speed k so Koko finishes all piles
      within h hours. Each pile takes ceil(pile/k) hours."

  2. Brute force:
     "Try every speed from 1 to max(piles) — O(n × max_pile).
      max can be 10^9 → TLE."

  3. Optimize:
     "Key insight: this is binary search on the ANSWER SPACE.
      Speed range is [1, max(piles)]. Property is monotonic —
      higher speed always works if lower speed works.
      So binary search on speed, check feasibility each time."

  4. Code:
     "left=1, right=max(piles). For each mid, compute total hours
      using ceil(pile/mid) = (pile+mid-1)//mid. If hours<=h →
      feasible, save answer, try smaller. Else try larger."

  5. Complexity:
     "Time O(n log(max_pile)) — log steps × O(n) check each.
      Space O(1)."

  Mukhya: summane kuutu code bareyabeda!
          "Binary search on answer space" — say this clearly!
          ceil(a/b) = (a+b-1)//b — important trick, mention it!
          This pattern applies to next 6 problems too!
"""

import math


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(n × max(piles)) Time | O(1) Space
# ═══════════════════════════════════════════════════════════════════
def min_eating_speed_brute(piles, h):
    """Idu modala aaloochane — try every speed 1 to max"""
    for k in range(1, max(piles) + 1):
        hours = sum(math.ceil(pile / k) for pile in piles)
        if hours <= h:
            return k


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n log(max(piles))) Time | O(1) Space
# ═══════════════════════════════════════════════════════════════════
def min_eating_speed(piles, h):
    """
    Idu final answer — binary search on answer space [1, max(piles)]
    ceil(pile/k) = (pile + k - 1) // k  → integer math, no float!
    """
    left, right = 1, max(piles)
    ans = right                    # worst case: eat fastest pile speed

    while left <= right:
        mid = (left + right) // 2

        # compute total hours needed at speed mid
        hours = sum((pile + mid - 1) // mid for pile in piles)

        if hours <= h:
            ans = mid              # feasible! save, try smaller speed
            right = mid - 1
        else:
            left = mid + 1        # too slow, need faster speed

    return ans


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # Test 1 — Basic
    assert min_eating_speed([3, 6, 7, 11], 8) == 4

    # Test 2 — h equals pile count (must eat each in 1 hour)
    assert min_eating_speed([30, 11, 23, 4, 20], 5) == 30

    # Test 3 — h equals pile count variant
    assert min_eating_speed([30, 11, 23, 4, 20], 6) == 23

    # Test 4 — Single pile
    assert min_eating_speed([10], 10) == 1

    # Test 5 — Lots of hours available
    assert min_eating_speed([1, 1, 1, 1], 100) == 1

    # Test 6 — All same piles
    assert min_eating_speed([5, 5, 5], 3) == 5

    print("All tests passed!")

