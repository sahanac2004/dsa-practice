"""
╔══════════════════════════════════════════════════════════════════╗
║  MAXIMUM SUBARRAY (KADANE'S ALGORITHM)                           ║
║  LeetCode #53  |  Difficulty: Medium  |  Topic: Arrays / DP      ║
║  Link: https://leetcode.com/problems/maximum-subarray/           ║
╚══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ಮೊದಲು problem odidaga ನಮ್ಮ brain ಏನು think ಮಾಡಬೇಕು:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ (What are they asking?)
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  positive/negative numbers      │
  │                          ಇರೋ array                       │
  │  Output ಏನು ಬೇಕು?     →  CONTIGUOUS subarray ನ max sum  │
  │  Constraints ಏನಿದೆ?   →  ಕಡಿಮೆ ಪಕ್ಷ ಒಂದು element ಬೇಕು,  │
  │                          empty subarray return ಮಾಡಲ್ಲ    │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ನನಗೆ ಗೊತ್ತಿರೋ simple way ಏನು? (Brute force thought)
  →  ಪ್ರತಿ start i ಗೂ, ಪ್ರತಿ end j >= i ಗೂ, sum(nums[i:j+1])
     calculate ಮಾಡಿ max track ಮಾಡೋದು.
  →  ಆದರೆ ಇದು slow ಯಾಕೆ? → O(n²) ಆಗುತ್ತೆ, n=10^5 ಆದ್ರೆ TLE.

  ಹಂತ 3 — Better way ಹೇಗೆ ಯೋಚಿಸುವುದು? (Optimization thought)
  →  "index i ಲ್ಲಿ ನಿಂತಿದ್ದೀನಿ ಅಂತ ಇಟ್ಕೊಳ್ಳಿ — ಹಿಂದಿನ subarray
     ಅನ್ನ EXTEND ಮಾಡ್ಬೇಕಾ, ಅಥವಾ ಇಲ್ಲಿಂದ ಹೊಸದಾಗಿ START ಮಾಡ್ಬೇಕಾ?"
  →  ಅಹಾ moment: ಹಿಂದಿನ running sum POSITIVE ಆಗಿ help ಮಾಡ್ತಿದ್ರೆ
     extend ಮಾಡು, NEGATIVE ಆಗಿ ದೂರ ಎಳೀತಿದ್ರೆ ಬಿಟ್ಟುಬಿಡು — ಈ ಒಂದೇ
     local decision ಪ್ರತಿ index ಗೂ ಮಾಡಿದ್ರೆ ಸಾಕು.
  →  ಇದರಿಂದ ನಾವು Kadane's Algorithm (1-D DP) use ಮಾಡಬಹುದು!

  ಹಂತ 4 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  Answer CONTIGUOUS segment ಆಗಿರಬೇಕು ಅನ್ನೋ constraint ಇರೋದ್ರಿಂದ
     sort/set use ಮಾಡಕ್ಕಾಗಲ್ಲ — order respect ಮಾಡ್ಬೇಕು.
  →  "extend or restart" decision ಪ್ರತಿ index ಗೂ local ಆಗಿ take
     ಮಾಡಬಹುದು ಅನ್ನೋದೇ ಇದು DP ಆಗಿ ಕೆಲಸ ಮಾಡೋಕ್ಕೆ ಕಾರಣ.
  →  O(1) space ಸಾಕು ಅಂದ್ರೆ, rolling variable DP signal ಸಿಗುತ್ತೆ.

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು (Think out loud):
  →  "So I need the max sum of any CONTIGUOUS subarray."
  →  "The brute force checks every (start, end) pair — O(n²)."
  →  "I notice that at each index, I only need to decide: extend
      the running sum, or restart from here — that's Kadane's."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Kadane's Algorithm (1-D DP / Greedy hybrid)
  Secondary : Running "best ending here" state

  WHY Kadane's?
  → Contiguous subarray means order matters — can't sort/hash
  → At each index: extend if running sum still helps, else restart
  → dp[i] = max(nums[i], dp[i-1] + nums[i]), collapsed to O(1) space

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Given an integer array nums, find the contiguous subarray
  (at least one number) with the largest sum, and return that sum.

  Input : nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
  Output: 6

  Example 1 — basic:
    Input : nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    Output: 6
    Why?  : subarray [4, -1, 2, 1] has the largest sum = 6

  Example 2 — slightly tricky:
    Input : nums = [-3, -1, -2]
    Output: -1
    Why?  : all negative, must still pick a non-empty subarray —
            the LEAST negative single element wins

  Constraints:
    - At least one element must be included
    - Array can be all negative
    - 1 <= nums.length <= 10⁵

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 INTUITION (How to think)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  If I'm standing at index i, should I EXTEND the subarray that
  ended at i-1, or should I START FRESH at i?

  The journey from brute to optimal:
    Brute thought   →  check every (start, end) pair
    Problem with it →  O(n²), TLE for n=10⁵
    Better question →  "extend or restart — which helps more?"
    Insight         →  extend only if running sum is still positive
    Optimal         →  current_sum = max(num, current_sum + num)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 APPROACH 1 — BRUTE FORCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Try every subarray start i, extend end j, track running sum.

  Pseudocode:
    step 1: max_sum = nums[0]
    step 2: for i in range(n): current = 0
    step 3:     for j in range(i, n): current += nums[j]; update max_sum

  Time  : O(n²)  →  Why: every (i, j) pair considered
  Space : O(1)   →  Why: no extra data structure

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ? (Why is this not enough?)
    → n = 10⁵ ಆದ್ರೆ ~10¹⁰ operations → TLE.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚶 APPROACH 2 — BETTER (skip — brute jumps straight to Kadane's)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ಇಲ್ಲಿ intermediate approach ಇಲ್ಲ — "extend or restart" insight
  ಸಿಕ್ಕ ತಕ್ಷಣ ನೇರವಾಗಿ O(n) Kadane's ಗೆ ಹೋಗಬಹುದು.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 APPROACH 3 — OPTIMAL   (Kadane's)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Single pass — at each index decide "extend or restart".

  Key steps:
    1. current_sum = nums[0], best_sum = nums[0]
    2. For each num starting from index 1:
         a. current_sum = max(num, current_sum + num)
         b. best_sum = max(best_sum, current_sum)
    3. Return best_sum

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ (Say it once in Kanglish so it sticks):
    → "Array ಅನ್ನ ಒಮ್ಮೆ scan ಮಾಡ್ತಾ, ಪ್ರತಿ number ಗೂ 'ಈಗಿನ running
        sum ಜೊತೆ ಸೇರಿಸೋದಾ, ಅಥವಾ ಇಲ್ಲಿಂದ ಹೊಸದಾಗಿ ಶುರು ಮಾಡೋದಾ' ಅಂತ
        max ತಗೊಂಡು decide ಮಾಡು. ಪ್ರತಿ step ಗೂ best_sum ಅನ್ನ
        update ಮಾಡ್ತಾ ಹೋಗು."

  Time  : O(n)  →  Why: single pass
  Space : O(1)  →  Why: two variables only

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

  Start: current_sum=-2, best_sum=-2

  num=1   →  current=max(1,-2+1=-1)=1     →  best=max(-2,1)=1
  num=-3  →  current=max(-3,1-3=-2)=-2    →  best stays 1
  num=4   →  current=max(4,-2+4=2)=4      →  best=4
  num=-1  →  current=max(-1,4-1=3)=3      →  best stays 4
  num=2   →  current=max(2,3+2=5)=5       →  best=5
  num=1   →  current=max(1,5+1=6)=6       →  best=6
  num=-5  →  current=max(-5,6-5=1)=1      →  best stays 6
  num=4   →  current=max(4,1+4=5)=5       →  best stays 6

  Output: 6 (subarray [4, -1, 2, 1])

  ಇನ್ನೊಂದು example — tricky case:
  Input: nums = [-3, -1, -2]
  current_sum starts -3, best=-3
  num=-1  current=max(-1,-3-1=-4)=-1  best=max(-3,-1)=-1
  num=-2  current=max(-2,-1-2=-3)=-2  best stays -1
  Output: -1 (least negative single element)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ All negative?          →  [-3,-1,-2] → -1 (least negative single element)
  ✓ Single element?        →  [5] → 5
  ✓ All positive?          →  [1,2,3,4] → 10 (whole array)
  ✓ Restart after negative start?  →  [-1,2,3] → 5
  ✓ Single negative element?  →  [-5] → -5 (can't return 0 / empty)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                Time      Space
  Brute Force   O(n²)     O(1)
  Optimal       O(n)      O(1)    ← use this  

  Time ಯಾಕೆ O(n)?  → Array ಒಮ್ಮೆ ಮಾತ್ರ traverse ಮಾಡ್ತೇವೆ.
  Space ಯಾಕೆ O(1)? → current_sum, best_sum ಎರಡು variables ಸಾಕು.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Kadane's Algorithm — Extend or Restart

  ಈ pattern ಯಾವಾಗ use ಮಾಡಬೇಕು?
  → Answer BEST CONTIGUOUS segment ಆಗಿದ್ದಾಗ (max sum, max product)
  → "ಹಿಂದಿನದನ್ನ ಮುಂದುವರಿಸೋದಾ, ಬಿಟ್ಟುಬಿಡೋದಾ" ಅನ್ನೋ local decision
    ಪ್ರತಿ step ಗೂ ಸಾಕಾಗುತ್ತೆ ಅಂತ ಗೊತ್ತಾದಾಗ

  ಇದೇ pattern ಬೇರೆ problems ನಲ್ಲಿ ಕಾಣಿಸುತ್ತೆ:
  → Maximum Product Subarray (#152) — track min AND max both
  → Best Time to Buy/Sell Stock (#121) — running min sibling idea
  → Best Time to Buy/Sell Stock III/IV — DP state machine extension

  Next time ಇಂತಹ problem ಬಂದ್ರೆ ನಾನು ಮೊದಲು ಇದನ್ನ think ಮಾಡ್ತೇನೆ:
  → "'Contiguous' word ಕಂಡ ತಕ್ಷಣ, extend-or-restart Kadane's
      pattern ಆಗುತ್ತಾ ಅಂತ ಮೊದಲು ಯೋಚಿಸು."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ INTERVIEW ನಲ್ಲಿ ಹೇಗೆ EXPLAIN ಮಾಡಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "So I need the max sum of any contiguous subarray, and I
      must pick at least one element even if all are negative."

  2. Brute force:
     "The naive approach checks every (start, end) pair — O(n²),
      which would TLE for n up to 10⁵."

  3. Optimize:
     "I notice that at each index, I only need one local decision:
      extend the running sum if it's still helping, or restart
      fresh — this is Kadane's Algorithm."

  4. Code:
     "I'll keep current_sum and best_sum, updating current_sum as
      max(num, current_sum + num) at each step."

  5. Complexity:
     "Time O(n) — one pass. Space O(1) — two rolling variables."

  ಮುಖ್ಯ: ಸುಮ್ಮನೆ ಕೂತು code ಬರೆಯಬೇಡ!
         Interviewer ಗೆ ನಿನ್ನ thinking process ಕಾಣಬೇಕು.
"""


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(n²) Time | O(1) Space
# ═══════════════════════════════════════════════════════════════════
def max_subarray_brute(nums):
    """ಇದು ಮೊದಲ ಆಲೋಚನೆ — every (start, end) pair check, simple but slow"""
    n = len(nums)
    max_sum = nums[0]
    for i in range(n):
        current = 0
        for j in range(i, n):
            current += nums[j]
            max_sum = max(max_sum, current)
    return max_sum


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n) Time | O(1) Space  (Kadane's)
# ═══════════════════════════════════════════════════════════════════
def max_subarray(nums):
    """ಇದು final answer — Kadane's, extend or restart at each index"""
    current_sum = nums[0]
    best_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        best_sum = max(best_sum, current_sum)

    return best_sum


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")   # Windows cp1252 can't print   otherwise

    # Test 1 — Basic example
    assert max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

    # Test 2 — Edge case: all negative
    assert max_subarray([-3, -1, -2]) == -1

    # Test 3 — Edge case: single element
    assert max_subarray([5]) == 5

    # Test 4 — Tricky: restart after negative start
    assert max_subarray([-1, 2, 3]) == 5

    print("All tests passed!  ")
