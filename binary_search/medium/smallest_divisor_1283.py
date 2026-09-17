"""
╔══════════════════════════════════════════════════════════════════╗
║  FIND THE SMALLEST DIVISOR GIVEN A THRESHOLD                     ║
║  LeetCode #1283  |  Difficulty: Medium  |  Topic: Binary Search  ║
║  Link: https://leetcode.com/problems/find-the-smallest-divisor-  ║
║        given-a-threshold/                                         ║
╚══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Given an array of integers nums and an integer threshold, find
  the SMALLEST divisor such that the sum of ceil(num/divisor)
  for all nums is <= threshold.

  Input : nums = list of integers, threshold = integer
  Output: smallest divisor satisfying the condition

  Example 1 — basic:
    Input : nums = [1,2,5,9], threshold = 6
    Output: 5
    Why?  : divisor=5 → ceil(1/5)+ceil(2/5)+ceil(5/5)+ceil(9/5)
                       = 1+1+1+2 = 5 <= 6 ✓
            divisor=4 → 1+1+2+3 = 7 > 6 ✗
            So 5 is the smallest valid divisor

  Example 2 — slightly tricky:
    Input : nums = [44,22,33,11,100], threshold = 5
    Output: 44
    Why?  : Need sum <= 5 with 5 numbers → each must contribute 1
            → divisor >= max(nums) = 100? No, ceil(44/44)=1... 
            divisor=44 → 1+1+1+1+3=7 > 5
            divisor=100 → 1+1+1+1+1=5 <= 5 ✓
            Answer = 44 after binary search

  Constraints:
    - 1 <= nums.length <= 5 × 10^4
    - 1 <= nums[i] <= 10^6
    - nums.length <= threshold <= 10^6

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Problem odi aada mele namma brain enu think maadabeeku:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  nums array + threshold       │
  │  Output ಏನು ಬೇಕು?     →  smallest divisor d such that  │
  │                           sum(ceil(num/d)) <= threshold │
  │  Constraints ಏನಿದೆ?   →  nums.length <= threshold      │
  │                           (so divisor=1 always possible)│
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ನನಗೆ ಗೊತ್ತಿರೋ simple way ಏನು?
  →  d=1 ಇಂದ max(nums) ತನಕ try ಮಾಡಿ first valid d return ಮಾಡೋಣ
  →  ಆದರೆ ಇದು slow ಯಾಕೆ?
     max(nums) = 10^6, n = 5×10^4 → 5×10^10 ops → TLE!

  ಹಂತ 3 — Better way ಹೇಗೆ ಯೋಚಿಸುವುದು?
  →  "Koko + Bouquets same pattern ಅಲ್ಲವಾ?"
  →  Answer space [1, max(nums)] — sorted range
  →  Monotonic: divisor ಜಾಸ್ತಿ → sum ಕಡಿಮೆ → easier to satisfy
     if d works → d+1 also works!
  →  Binary search on answer space [1, max(nums)]!

  ಹಂತ 4 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  Same template as Koko and Bouquets
  →  Feasibility = sum(ceil(num/d)) <= threshold
  →  ceil(a/b) = (a+b-1)//b — same integer trick!

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು:
  →  "Third problem in binary search on answer space series!"
  →  "Larger divisor → smaller sum → monotonic → binary search"
  →  "Same template as Koko — just different feasibility check"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Binary Search → On Answer Space
  Secondary : Math — ceiling division (a+b-1)//b

  WHY Binary Search on Answer Space?
  → "Smallest divisor" = minimum valid answer in range [1, max(nums)]
  → Feasibility monotonic: bigger d → smaller sum → always valid if smaller d was valid
  → Exact same pattern as Koko #875 and Bouquets #1482

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  This is the THIRD problem in the binary search on answer space
  family. The pattern is always the same:

  1. Identify the answer range: [min_possible, max_possible]
  2. Identify the monotonic property
  3. Write a feasibility check function
  4. Binary search — if feasible save ans and go left, else go right

  Here:
  - Range: [1, max(nums)]
  - Monotonic: larger divisor → smaller ceiling sum → easier
  - Feasibility: sum(ceil(num/d)) <= threshold

  The journey from brute to optimal:
    Brute thought   →  Try every d from 1 to max(nums) → O(n × max)
    Problem with it →  10^10 ops → TLE
    Better question →  "Same as Koko — binary search on d?"
    Insight         →  Yes! Monotonic property holds → binary search
    Optimal         →  O(n log(max(nums)))

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Try every divisor from 1 to max(nums).
    Return first d where sum(ceil(num/d)) <= threshold.

  Pseudocode:
    step 1: for d from 1 to max(nums):
    step 2:   total = sum((num+d-1)//d for num in nums)
    step 3:   if total <= threshold: return d

  Time  : O(n × max(nums))  →  Why: max divisors × n nums each
  Space : O(1)              →  Why: no extra space

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ?
    → max(nums)=10^6, n=5×10^4 → 5×10^10 ops → TLE!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 6 — APPROACH 2 — OPTIMAL (Binary Search on Answer)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Binary search on divisor range [1, max(nums)].
    For each mid divisor, check if sum <= threshold.
    If yes → try smaller divisor. If no → try larger.

  Key steps:
    1. left=1, right=max(nums), ans=right
    2. While left <= right:
       a. mid = (left+right)//2
       b. total = sum((num+mid-1)//mid for num in nums)
       c. if total <= threshold → ans=mid, right=mid-1
       d. else → left=mid+1
    3. return ans

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ:
    → "Divisor range [1, max(nums)] ಮೇಲೆ binary search maadu.
       Mid divisor ಗೆ sum(ceil(num/mid)) calculate maadu.
       sum <= threshold ಆದ್ರೆ → valid! ans save, smaller try.
       sum > threshold ಆದ್ರೆ → larger divisor try maadu.
       Koko exact same template — just different feasibility!"

  Time  : O(n × log(max(nums)))  →  Why: log steps × O(n) sum
  Space : O(1)                   →  Why: only pointers

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 7 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: nums=[1,2,5,9], threshold=6
  left=1, right=9, ans=9

  mid=5 → (1+4)//5+(2+4)//5+(5+4)//5+(9+4)//5
         = 1+1+1+2 = 5 <= 6 ✓ → ans=5, right=4

  mid=2 → (1+1)//2+(2+1)//2+(5+1)//2+(9+1)//2
         = 1+1+3+5 = 10 > 6 ✗ → left=3

  mid=3 → (1+2)//3+(2+2)//3+(5+2)//3+(9+2)//3
         = 1+1+2+3 = 7 > 6 ✗ → left=4

  mid=4 → (1+3)//4+(2+3)//4+(5+3)//4+(9+3)//4
         = 1+1+2+3 = 7 > 6 ✗ → left=5

  left=5 > right=4 → return ans=5 ✓

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 8 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ threshold == n?    →  Each element must contribute 1
                          → divisor >= max(nums)
  ✓ Single element?   →  Binary search on [1, nums[0]]
  ✓ All ones?         →  [1,1,1], threshold=3 → divisor=1
  ✓ Large values?     →  Use integer division — no float issues

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 9 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                  Time                  Space
  Brute Force     O(n × max(nums))      O(1)
  Optimal         O(n × log(max(nums))) O(1)   ← use this ✅

  Time yaake O(n log max)?
    → log(max) binary search steps
    → Each step O(n) to compute sum
  Space yaake O(1)?
    → Only left, right, mid, ans

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 10 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Binary Search on Answer Space (3rd in series)

  Template that works for ALL these problems:
  ┌────────────────────────────────────────────────────────┐
  │  left, right = min_possible, max_possible              │
  │  ans = right                                           │
  │  while left <= right:                                  │
  │      mid = (left + right) // 2                        │
  │      if is_feasible(mid):                              │
  │          ans = mid                                     │
  │          right = mid - 1   # try smaller               │
  │      else:                                             │
  │          left = mid + 1    # need larger               │
  │  return ans                                            │
  └────────────────────────────────────────────────────────┘

  Only thing that changes: is_feasible() function!

  | Problem   | Answer Space     | Feasibility Check          |
  |-----------|-----------------|----------------------------|
  | Koko #875 | [1, max(piles)] | sum(ceil(pile/k)) <= h     |
  | Bouq #1482| [1, max(bloom)] | bouquets(day) >= m         |
  | This #1283| [1, max(nums)]  | sum(ceil(num/d)) <= thresh |
  | Ship #1011| [max, sum]      | days_to_ship(cap) <= days  |

  Next time intaha problem bandre naanu modalu idannu think maadtene:
  → "Minimum/maximum X beeka + monotonic + feasibility check?
     → Binary Search on Answer Space! Same template, change
     only the is_feasible() function!"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 11 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "Find smallest divisor d such that sum of ceil(num/d)
      for all nums is <= threshold."

  2. Brute force:
     "Try d from 1 to max(nums) — O(n × max). TLE."

  3. Optimize:
     "Same pattern as Koko and Bouquets — binary search on answer
      space [1, max(nums)]. Larger d → smaller sum → monotonic.
      Binary search on d, feasibility = sum(ceil(num/d)) <= threshold."

  4. Code:
     "left=1, right=max(nums). For each mid compute sum using
      (num+mid-1)//mid. If sum<=threshold → save ans, go left.
      Else go right."

  5. Complexity:
     "Time O(n log(max(nums))). Space O(1)."

  Mukhya: summane kuutu code bareyabeda!
          Template table show maadu — all 4 problems same pattern!
          (num+mid-1)//mid ceiling trick — always use this!
"""


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(n × max(nums)) Time | O(1) Space
# ═══════════════════════════════════════════════════════════════════
def smallest_divisor_brute(nums, threshold):
    """Idu modala aaloochane — try every divisor linearly"""
    for d in range(1, max(nums) + 1):
        total = sum((num + d - 1) // d for num in nums)
        if total <= threshold:
            return d


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n log(max(nums))) Time | O(1) Space
# ═══════════════════════════════════════════════════════════════════
def smallest_divisor(nums, threshold):
    """
    Idu final answer — binary search on answer space [1, max(nums)]
    ceil(num/d) = (num+d-1)//d — integer math, no float!
    Same template as Koko #875 and Bouquets #1482
    """
    left, right = 1, max(nums)
    ans = right

    while left <= right:
        mid = (left + right) // 2

        # feasibility check: sum of ceilings <= threshold?
        total = sum((num + mid - 1) // mid for num in nums)

        if total <= threshold:
            ans = mid           # valid! try smaller divisor
            right = mid - 1
        else:
            left = mid + 1     # too large sum, need bigger divisor

    return ans


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # Test 1 — Basic
    assert smallest_divisor([1, 2, 5, 9], 6) == 5

    # Test 2 — Threshold equals n
    assert smallest_divisor([44, 22, 33, 11, 100], 5) == 100

    # Test 3 — Single element
    assert smallest_divisor([10], 1) == 10

    # Test 4 — All ones
    assert smallest_divisor([1, 1, 1], 3) == 1

    # Test 5 — Large threshold (divisor = 1)
    assert smallest_divisor([2, 3, 5, 7], 100) == 1

    # Test 6 — Threshold exactly equals sum at answer
    assert smallest_divisor([1, 2, 3], 3) == 3

    print("All tests passed!")
