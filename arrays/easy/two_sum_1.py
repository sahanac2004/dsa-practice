"""
╔══════════════════════════════════════════════════════════════════╗
║  TWO SUM                                                         ║
║  LeetCode #1  |  Difficulty: Easy  |  Topic: Arrays / Hashing   ║
║  Link: https://leetcode.com/problems/two-sum/                    ║
╚══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Array ಕೊಡ್ತಾರೆ ಮತ್ತು ಒಂದು target number ಕೊಡ್ತಾರೆ.
  ಯಾವ 2 numbers add ಮಾಡಿದ್ರೆ target ಸಿಗತ್ತೆ ಅವುಗಳ
  indices return ಮಾಡು. Exactly one answer always ಇರತ್ತೆ.

  Input : nums array + target integer
  Output: [index1, index2] such that nums[i] + nums[j] == target

  Example 1:
    Input : nums = [2, 7, 11, 15], target = 9
    Output: [0, 1]
    Why?  : nums[0] + nums[1] = 2 + 7 = 9 ✓

  Example 2 (tricky — answer not at start):
    Input : nums = [3, 2, 4], target = 6
    Output: [1, 2]
    Why?  : nums[1] + nums[2] = 2 + 4 = 6 ✓

  Constraints:
    - 2 <= nums.length <= 10^4
    - Exactly one valid answer exists
    - Cannot use same element twice (different indices)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ಮೊದಲು problem odidaga ನಮ್ಮ brain ಏನು think ಮಾಡಬೇಕು:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ (What are they asking?)
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  numbers array + target sum   │
  │  Output ಏನು ಬೇಕು?     →  2 numbers add ಆದ್ರೆ target   │
  │                           ಆಗತ್ತೆ ಅವುಗಳ indices ಬೇಕು  │
  │  Constraints ಏನಿದೆ?   →  exactly one answer ಇರತ್ತೆ,   │
  │                           same element twice use ಮಾಡಲ್ಲ │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ನನಗೆ ಗೊತ್ತಿರೋ simple way ಏನು? (Brute force thought)
  →  Every pair check ಮಾಡೋಣ — i ಮತ್ತು j loop ಹಾಕಿ
     nums[i] + nums[j] == target ಆದ್ರೆ return [i, j]
  →  ಆದರೆ ಇದು slow ಯಾಕೆ? → n=10^4 ಆದ್ರೆ 10^8 operations!
     TLE ಆಗತ್ತೆ, ಬೇರೆ way ಯೋಚಿಸಬೇಕು

  ಹಂತ 3 — Better way ಹೇಗೆ ಯೋಚಿಸುವುದು? (Optimization thought)
  →  "nums[i] ನೋಡಿದಾಗ, ನನಗೆ target - nums[i] ಬೇಕು"
  →  "ಆ number already seen ಆಗಿದ್ಯಾ? ಅಂತ O(1) ಲ್ಲಿ check ಮಾಡಬಹುದಾ?"
  →  YES! HashMap ಲ್ಲಿ store ಮಾಡ್ತಾ ಹೋದ್ರೆ O(1) lookup ಸಾಧ್ಯ!
  →  ಇದರಿಂದ ನಾವು HashMap / Complement Lookup use ಮಾಡಬಹುದು!

  ಹಂತ 4 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  ಪ್ರತಿ number ಗೆ ಒಂದು "complement" ಇದೆ (target - num)
  →  Complement ಮೊದಲೇ seen ಆಗಿದ್ಯಾ ಅಂತ check ಮಾಡಬೇಕು
  →  HashMap = perfect for "have I seen this before?" questions

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು:
  →  "I see that for every number x, I need target - x"
  →  "Brute force checks every pair — that's O(n²)"
  →  "If I store seen numbers in a HashMap, I can look up the
      complement in O(1) — making the whole thing O(n)"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : HashMap → Complement Lookup
  Secondary : —

  WHY HashMap?
  → Every number x needs a partner (target - x)
  → Instead of searching the whole array again (O(n) search),
    store what you've seen → O(1) lookup
  → Trade space O(n) for time O(n) — classic pattern

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 INTUITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  For every number x, the number I need is (target - x).
  The question becomes: "Have I already seen (target - x)?"

  The journey from brute to optimal:
    Brute thought   →  Check every pair (i, j)
    Problem with it →  O(n²) — too slow for n=10^4
    Better question →  "Can I find the complement faster?"
    Insight         →  HashMap gives O(1) lookup!
    Optimal         →  Single pass + HashMap to store seen values

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 APPROACH 1 — BRUTE FORCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Every possible pair (i, j) check ಮಾಡು.
    nums[i] + nums[j] == target ಆದ್ರೆ [i, j] return ಮಾಡು.

  Pseudocode:
    for i in 0 to n:
        for j in i+1 to n:
            if nums[i] + nums[j] == target → return [i, j]

  Time  : O(n²)  →  Why: 2 nested loops, each runs n times
  Space : O(1)   →  Why: no extra space used

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ?
    → n = 10^4 ಆದ್ರೆ → 10^4 × 10^4 = 10^8 operations
    → LeetCode ಲ್ಲಿ ~10^8 ops per second limit ಇರತ್ತೆ → TLE!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 APPROACH 2 — OPTIMAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Single pass with HashMap {value: index}.
    Each number ನೋಡಿದಾಗ complement check ಮಾಡು.
    Complement ಇದ್ರೆ → answer ಸಿಕ್ಕಿತು!
    ಇಲ್ಲದಿದ್ರೆ → current number HashMap ಗೆ add ಮಾಡು.

  Key steps:
    1. seen = {} empty HashMap ತೆಗೊ
    2. Each number ಗೆ: complement = target - num
    3. complement already seen ಅಲ್ಲಿ ಇದ್ಯಾ? → YES: return indices
    4. NO: seen[num] = i ಮಾಡಿ continue

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ:
    → "ಪ್ರತಿ number ನೋಡಿದಾಗ, target ಆಗಲು ಅದಕ್ಕೆ ಯಾವ number ಬೇಕು
       ಅಂತ calculate ಮಾಡು. ಆ number ಮೊದಲೇ HashMap ಲ್ಲಿ ಇದ್ಯಾ?
       ಇದ್ರೆ answer ಸಿಕ್ಕಿತು, ಇಲ್ಲದಿದ್ರೆ current ನ store ಮಾಡು."

  Time  : O(n)  →  Why: array ಒಮ್ಮೆ traverse, HashMap O(1) lookup
  Space : O(n)  →  Why: worst case n elements HashMap ಲ್ಲಿ store

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: nums = [2, 7, 11, 15], target = 9

  i=0  num=2   comp=9-2=7   seen={}        7 not in seen → seen={2:0}
  i=1  num=7   comp=9-7=2   seen={2:0}     2 IN seen! → return [seen[2], 1] = [0, 1] ✓

  Output: [0, 1]

  ಇನ್ನೊಂದು example — tricky case:
  Input: nums = [3, 2, 4], target = 6

  i=0  num=3   comp=6-3=3   seen={}           3 not in seen → seen={3:0}
  i=1  num=2   comp=6-2=4   seen={3:0}        4 not in seen → seen={3:0, 2:1}
  i=2  num=4   comp=6-4=2   seen={3:0, 2:1}   2 IN seen! → return [seen[2], 2] = [1, 2] ✓

  Output: [1, 2]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ Same value, different indices?  → [3,3] target=6 → [0,1] ✓
                                       seen ಲ್ಲಿ index store ಮಾಡ್ತೇವೆ, value ಅಲ್ಲ
  ✓ Negative numbers?               → [-1,-2,-3,-4] target=-7 → works fine ✓
  ✓ Only 2 elements?                → [1,9] target=10 → [0,1] ✓
  ✓ Answer at end?                  → [1,2,3,4,5] target=9 → [3,4] ✓

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                Time      Space
  Brute Force   O(n²)     O(1)
  Optimal       O(n)      O(n)      use this  

  Time ಯಾಕೆ O(n)?  → Array ಒಮ್ಮೆ ಮಾತ್ರ traverse ಮಾಡ್ತೇವೆ
  Space ಯಾಕೆ O(n)? → Worst case ಎಲ್ಲ n elements HashMap ಲ್ಲಿ ಹೋಗ್ತಾವೆ

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: HashMap Complement Lookup

  ಈ pattern ಯಾವಾಗ use ಮಾಡಬೇಕು?
  → "Find a PAIR that satisfies some condition" ಅಂದ್ರೆ
  → "Have I seen X before?" ಅಂತ O(1) ಲ್ಲಿ check ಮಾಡಬೇಕಾದ್ರೆ
  → Array ಒಮ್ಮೆ traverse ಮಾಡಿ answer ಸಿಗಬೇಕಾದ್ರೆ

  ಇದೇ pattern ಬೇರೆ problems ನಲ್ಲಿ ಕಾಣಿಸುತ್ತೆ:
  → Two Sum II (sorted array — two pointers variant)
  → 4Sum, 3Sum (extensions of this same idea)
  → Subarray Sum Equals K (prefix sum + HashMap)
  → Longest Substring Without Repeating (HashMap + sliding window)

  Next time ಇಂತಹ problem ಬಂದ್ರೆ ನಾನು ಮೊದಲು ಇದನ್ನ think ಮಾಡ್ತೇನೆ:
  → "Pair/complement find ಮಾಡಬೇಕಾ? → HashMap ತೆಗೋ, traverse ಮಾಡ್ತಾ
     complement check ಮಾಡ್ತಾ ಹೋಗು — O(n) ಲ್ಲಿ solve ಆಗತ್ತೆ!"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ INTERVIEW ನಲ್ಲಿ ಹೇಗೆ EXPLAIN ಮಾಡಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  1. Understand:
     "So the problem is asking me to find two indices whose
      values add up to the target. Exactly one answer exists."

  2. Brute force:
     "The naive approach would be to check every pair using
      two nested loops — that gives O(n²) time, which might
      TLE for n up to 10^4."

  3. Optimize:
     "I notice that for every number x, I just need (target - x).
      If I store numbers I've already seen in a HashMap,
      I can check if the complement exists in O(1)."

  4. Code:
     "I'll use a HashMap mapping value to index.
      Single pass — check complement, else store current."

  5. Complexity:
     "Time O(n) — single pass. Space O(n) — HashMap."

  ಮುಖ್ಯ: ಸುಮ್ಮನೆ ಕೂತು code ಬರೆಯಬೇಡ!
         Interviewer ಗೆ ನಿನ್ನ thinking process ಕಾಣಬೇಕು.
"""


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(n²) Time | O(1) Space
# ═══════════════════════════════════════════════════════════════════
def two_sum_brute(nums, target):
    """ಇದು ಮೊದಲ ಆಲೋಚನೆ — simple but slow O(n²)"""
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n) Time | O(n) Space
# ═══════════════════════════════════════════════════════════════════
def two_sum(nums, target):
    """ಇದು final answer — HashMap complement lookup O(n)"""
    seen = {}                           # {value: index}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:          # complement already seen?
            return [seen[complement], i]
        seen[num] = i                   # store current for future


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")   # Windows cp1252 can't print   otherwise

    # Test 1 — Basic
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]

    # Test 2 — Answer not at start
    assert two_sum([3, 2, 4], 6) == [1, 2]

    # Test 3 — Same value, different indices
    assert two_sum([3, 3], 6) == [0, 1]

    # Test 4 — Negative numbers
    assert two_sum([-1, -2, -3, -4], -7) == [2, 3]

    print("All tests passed!  ")
