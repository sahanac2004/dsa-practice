"""
╔══════════════════════════════════════════════════════════════════╗
║  MISSING NUMBER                                                  ║
║  LeetCode #268  |  Difficulty: Easy  |  Topic: Arrays / Bit Manipulation ║
║  Link: https://leetcode.com/problems/missing-number/             ║
╚══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  nums contains n DISTINCT numbers from range [0, n] (n+1 possible
  values). Find the ONE number missing from nums.

  Input : nums = [3, 0, 1]
  Output: 2

  Example 1 — basic:
    Input : nums = [3, 0, 1]
    Output: 2
    Why?  : range is [0,1,2,3] (n=3), nums has 3,0,1 — missing 2

  Example 2 — slightly tricky:
    Input : nums = [0, 1, 2]
    Output: 3
    Why?  : the missing number is n itself, the largest possible value

  Constraints:
    - nums.length == n, values drawn from [0, n]
    - Exactly one value is missing, all present values are distinct

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ಮೊದಲು problem odidaga ನಮ್ಮ brain ಏನು think ಮಾಡಬೇಕು:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ (What are they asking?)
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  [0,n] range ಇಂದ n distinct     │
  │                          numbers ಇರೋ array               │
  │  Output ಏನು ಬೇಕು?     →  ಆ range ಲ್ಲಿ missing ಇರೋ ಒಂದೇ  │
  │                          number                            │
  │  Constraints ಏನಿದೆ?   →  ideally O(n) time, O(1) space   │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ನನಗೆ ಗೊತ್ತಿರೋ simple way ಏನು? (Brute force thought)
  →  Array ಅನ್ನ sort ಮಾಡಿ, index ಮತ್ತು value compare ಮಾಡ್ತಾ,
     ಮೊದಲ mismatch ಎಲ್ಲಿ ಸಿಗುತ್ತೋ ಅದೇ missing number.
  →  ಆದರೆ ಇದು ಯಾಕೆ enough ಅಲ್ಲ? → Sorting O(n log n) ತಗೋತ್ತೆ,
     ಬೇಡದೇ ಇರೋ overhead.

  ಹಂತ 3 — Better way ಹೇಗೆ ಯೋಚಿಸುವುದು? (Optimization thought)
  →  "ಈ array ಲ್ಲಿ EXACT ಆಗಿ ಏನಿರ್ಬೇಕು ಅಂತ ನನಗೆ ಈಗಾಗಲೇ ಗೊತ್ತು
     (0 ಇಂದ n ವರೆಗೆ) — expected ಅನ್ನ actual ಜೊತೆ ನೇರವಾಗಿ
     compare ಮಾಡಿದ್ರೆ ಆಗಲ್ವಾ?"
  →  ಅಹಾ moment: 0..n indices ಮತ್ತು nums ನ ಎಲ್ಲಾ values ಅನ್ನ ಒಟ್ಟಿಗೆ
     XOR ಮಾಡಿದ್ರೆ, present ಆಗಿರೋ numbers ತಮ್ಮ matching index ಜೊತೆ
     cancel ಆಗಿ, missing number ಮಾತ್ರ ಉಳೀತದೆ.
  →  ಇದರಿಂದ ನಾವು XOR Cancellation (indices vs values) use ಮಾಡಬಹುದು!

  ಹಂತ 4 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  Expected set (0..n) EXACT ಆಗಿ ಗೊತ್ತಿರೋದ್ರಿಂದ, hashset ಬೇಕಿಲ್ಲ
     — expected vs actual cancel ಮಾಡಿದ್ರೆ ಸಾಕು.
  →  Single Number (#136) ನ ಅದೇ XOR trick, ಆದ್ರೆ ಇಲ್ಲಿ "pair"
     ಆಗಿ ಆಡ್ತಿರೋದು indices.
  →  O(1) space ಬೇಕು ಅಂದ್ರೆ, XOR ಅಥವಾ Gauss sum ಇಬ್ಬರೂ fit ಆಗ್ತಾರೆ.

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು (Think out loud):
  →  "So the array has n distinct numbers from [0, n], one is missing."
  →  "I know exactly what SHOULD be there, so I don't need a set."
  →  "I can XOR every index 0..n with every value in nums — present
      numbers cancel with their index, leaving the missing one."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Bit Manipulation → XOR Cancellation (indices vs values)
  Secondary : Gauss Sum Formula (arithmetic alternative)

  WHY XOR (or Sum)?
  → We know exactly what {0..n} should contain — cancel expected
    against actual instead of hashing what's present
  → XOR every index AND every value: present numbers cancel,
    only the missing number survives

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 INTUITION (How to think)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  I know exactly what SHOULD be in this array — can I compare
  "expected" against "actual" directly, without sorting or hashing?

  The journey from brute to optimal:
    Brute thought   →  sort, find first index where value != index
    Problem with it →  O(n log n), sorting is unnecessary overhead
    Better question →  "can I cancel expected vs actual directly?"
    Insight         →  XOR indices 0..n with values in nums
    Optimal         →  XOR fold, O(n) time, O(1) space

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 APPROACH 1 — BRUTE FORCE (Sort + Scan)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Sort nums, then find the first index where value != index.

  Pseudocode:
    step 1: nums.sort()
    step 2: for i, v in enumerate(nums): if v != i: return i
    step 3: return len(nums)   # missing number is n itself

  Time  : O(n log n)  →  Why: sorting dominates
  Space : O(1) extra  →  Why: depends on sort implementation

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ? (Why is this not enough?)
    → Sorting ಬೇಡದೇ ಇರೋ overhead; O(n) solutions ಇವೆ.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚶 APPROACH 2 — BETTER (Gauss Sum Formula)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    expected_sum(0..n) - actual_sum(nums) = missing number.

  Time  : O(n)  — one pass to sum nums
  Space : O(1)

  ಇನ್ನೂ better ಮಾಡಬಹುದಾ? → time/space ಒಂದೇ ಇದ್ರೂ, XOR ಇನ್ನೂ
  ಒಳ್ಳೇದು ಯಾಕಂದ್ರೆ overflow ಚಿಂತೆ ಇರಲ್ಲ (Python ಗೆ ಅಪ್ರಸ್ತುತ,
  ಆದ್ರೆ ಬೇರೆ languages ಗೆ ಮುಖ್ಯ).

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 APPROACH 3 — OPTIMAL   (XOR Cancellation)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    XOR every index 0..n with every value in nums — survivor is
    the missing number.

  Key steps:
    1. result = len(nums)  (pre-seed with index n)
    2. For i in range(len(nums)): result ^= i ^ nums[i]
    3. Return result

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ (Say it once in Kanglish so it sticks):
    → "result ಅನ್ನ n ಇಂದ ಶುರು ಮಾಡು (ಯಾಕಂದ್ರೆ loop 0..n-1 indices
        ಮಾತ್ರ cover ಮಾಡುತ್ತೆ). ಪ್ರತಿ i ಗೂ, i ಮತ್ತು nums[i] ಎರಡನ್ನೂ
        result ಜೊತೆ XOR ಮಾಡು. ಕೊನೆಗೆ ಉಳಿಯೋದೇ missing number."

  Time  : O(n)  →  Why: single pass
  Space : O(1)  →  Why: one accumulator variable

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: nums = [3, 0, 1]   (n=3, expected range [0,1,2,3])

  result = len(nums) = 3

  i=0  →  variables: result=3  →  result ^= 0 ^ 3 → 3^0^3 = 0
  i=1  →  variables: result=0  →  result ^= 1 ^ 0 → 0^1^0 = 1
  i=2  →  variables: result=1  →  result ^= 2 ^ 1 → 1^2^1 = 2

  Output: 2 (2 is indeed missing from [3,0,1])

  ಇನ್ನೊಂದು example — tricky case:
  Input: nums = [0, 1, 2]
  result = 3
  i=0  result ^= 0^0 → 3^0^0 = 3
  i=1  result ^= 1^1 → 3^1^1 = 3
  i=2  result ^= 2^2 → 3^2^2 = 3
  Output: 3

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ Missing number is 0?    →  [1,2,3] → 0
  ✓ Missing number is n?    →  [0,1,2] → 3 (largest)
  ✓ Single element array?   →  [0] → 1, or [1] → 0
  ✓ Missing in the middle?  →  [0,1,3,4] → 2
  ✓ Nothing skipped except end?  →  [0,1,2,3] → 4

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                Time        Space
  Brute Force   O(n log n)  O(1)
  Sum Formula   O(n)        O(1)
  Optimal (XOR) O(n)        O(1)    ← use this  

  Time ಯಾಕೆ O(n)?  → Array ಒಮ್ಮೆ ಮಾತ್ರ traverse ಮಾಡ್ತೇವೆ.
  Space ಯಾಕೆ O(1)? → result ಅನ್ನೋ ಒಂದೇ accumulator variable ಸಾಕು.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: XOR/Sum Cancellation Against a KNOWN Expected Set

  ಈ pattern ಯಾವಾಗ use ಮಾಡಬೇಕು?
  → Complete/expected collection ಹೇಗಿರಬೇಕು ಅಂತ EXACT ಆಗಿ ಗೊತ್ತಿದ್ದಾಗ
    (0..n range, full permutation, etc.)
  → Missing ಅಥವಾ duplicate ಹುಡುಕೋಕ್ಕೆ hashset ಬದ್ಲು cancel
    ಮಾಡಬಹುದು ಅಂತ ಗೊತ್ತಾದಾಗ

  ಇದೇ pattern ಬೇರೆ problems ನಲ್ಲಿ ಕಾಣಿಸುತ್ತೆ:
  → Single Number (#136) — expected ಇಲ್ಲಿ implicit (pairs cancel)
  → Find All Numbers Disappeared in an Array
  → Find the Duplicate Number (#287, cycle detection twist)

  Next time ಇಂತಹ problem ಬಂದ್ರೆ ನಾನು ಮೊದಲು ಇದನ್ನ think ಮಾಡ್ತೇನೆ:
  → "Expected set EXACT ಆಗಿ ಗೊತ್ತಿದ್ಯಾ? ಇದ್ರೆ, hashset ಬದ್ಲು
      XOR/sum cancellation ಮೊದಲು ಯೋಚಿಸು."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ INTERVIEW ನಲ್ಲಿ ಹೇಗೆ EXPLAIN ಮಾಡಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "So nums has n distinct values from [0, n], and exactly one
      is missing — I need to find it."

  2. Brute force:
     "I could sort and find the first mismatch, but that's
      O(n log n), and sorting isn't necessary here."

  3. Optimize:
     "Since I know exactly what SHOULD be present — 0 through n —
      I can XOR every index with every value. Present numbers
      cancel with their matching index, leaving only the missing one."

  4. Code:
     "I'll seed result with n (the extra index the loop doesn't
      naturally cover), then XOR in i and nums[i] for each i."

  5. Complexity:
     "Time O(n) — one pass. Space O(1) — one accumulator."

  ಮುಖ್ಯ: ಸುಮ್ಮನೆ ಕೂತು code ಬರೆಯಬೇಡ!
         Interviewer ಗೆ ನಿನ್ನ thinking process ಕಾಣಬೇಕು.
"""


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(n log n) Time | O(1) Space  (Sort + Scan)
# ═══════════════════════════════════════════════════════════════════
def missing_number_brute(nums):
    """ಇದು ಮೊದಲ ಆಲೋಚನೆ — sort ಮಾಡಿ, ಮೊದಲ mismatch ಹುಡುಕೋದು"""
    nums = sorted(nums)
    for i, v in enumerate(nums):
        if v != i:
            return i
    return len(nums)


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n) Time | O(1) Space  (XOR)
# ═══════════════════════════════════════════════════════════════════
def missing_number(nums):
    """ಇದು final answer — indices vs values XOR cancellation"""
    result = len(nums)
    for i, num in enumerate(nums):
        result ^= i ^ num
    return result


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")   # Windows cp1252 can't print   otherwise

    # Test 1 — Basic example
    assert missing_number([3, 0, 1]) == 2

    # Test 2 — Edge case: missing is 0
    assert missing_number([1, 2, 3]) == 0

    # Test 3 — Edge case: missing is n (largest)
    assert missing_number([0, 1, 2]) == 3

    # Test 4 — Tricky: missing in the middle
    assert missing_number([0, 1, 3, 4]) == 2

    print("All tests passed!  ")
