"""
╔══════════════════════════════════════════════════════════════════╗
║  SINGLE NUMBER                                                   ║
║  LeetCode #136  |  Difficulty: Easy  |  Topic: Arrays / Bit Manipulation ║
║  Link: https://leetcode.com/problems/single-number/              ║
╚══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Every element in nums appears EXACTLY TWICE except for one
  element which appears exactly ONCE. Find that single element.

  Input : nums = [4, 1, 2, 1, 2]
  Output: 4

  Example 1 — basic:
    Input : nums = [4, 1, 2, 1, 2]
    Output: 4
    Why?  : 1 and 2 each appear twice, 4 appears once

  Example 2 — slightly tricky:
    Input : nums = [-1, -1, -3]
    Output: -3
    Why?  : XOR works fine on negative numbers via two's complement

  Constraints:
    - Every element appears exactly twice, except one appears once
    - Must run in O(n) time, O(1) extra space

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ಮೊದಲು problem odidaga ನಮ್ಮ brain ಏನು think ಮಾಡಬೇಕು:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ (What are they asking?)
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  array, ಪ್ರತಿ number 2 ಸಲ       │
  │                          ಬಿಟ್ಟು ಒಂದೇ number ಒಂದೇ ಸಲ      │
  │  Output ಏನು ಬೇಕು?     →  ಆ ಒಂದೇ ಸಲ ಇರೋ number           │
  │  Constraints ಏನಿದೆ?   →  O(n) time, O(1) space ಬೇಕು —    │
  │                          hashmap counting ಬಳಸೋ ಹಾಗಿಲ್ಲ    │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ನನಗೆ ಗೊತ್ತಿರೋ simple way ಏನು? (Brute force thought)
  →  Frequency count ಮಾಡೋ hashmap ಇಟ್ಕೊಂಡು, count==1 ಇರೋ
     number ಅನ್ನ return ಮಾಡೋದು.
  →  ಆದರೆ ಇದು ಯಾಕೆ enough ಅಲ್ಲ? → O(n) space ಬಳಸುತ್ತೆ, problem
     O(1) space ಕೇಳ್ತಿದೆ.

  ಹಂತ 3 — Better way ಹೇಗೆ ಯೋಚಿಸುವುದು? (Optimization thought)
  →  "ಒಂದು operation ಇದ್ಯಾ, ಎಲ್ಲಿ ಸಮ ಸಂಖ್ಯೆ pairs cancel ಆಗಿ,
     odd ಒಂದು ಮಾತ್ರ ಉಳಿತಾವೆ?"
  →  ಅಹಾ moment: XOR! x^x=0 (ಸಮಾನ numbers cancel), x^0=x
     (identity). ಎಲ್ಲಾ numbers ಅನ್ನ XOR ಮಾಡಿದ್ರೆ, pairs ಎಲ್ಲಾ
     0 ಆಗಿ, ಒಂಟಿ number ಮಾತ್ರ ಉಳೀತದೆ.
  →  ಇದರಿಂದ ನಾವು XOR Cancellation use ಮಾಡಬಹುದು!

  ಹಂತ 4 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  O(1) space, O(n) time ಬೇಕು ಅನ್ನೋ constraint XOR ಗೆ ಪರ್ಫೆಕ್ಟ್
     fit — hashmap counting ಗಿಂತ ಸುಲಭ.
  →  XOR commutative + associative ಆಗಿರೋದ್ರಿಂದ, order ಮ್ಯಾಟರ್
     ಆಗಲ್ಲ — array ಯಾವ order ಲ್ಲಿ ಇದ್ರೂ ಪರವಾಗಿಲ್ಲ.
  →  "every element TWICE except one" ಅನ್ನೋ exact phrase ಕಂಡ
     ತಕ್ಷಣ XOR signal ಸಿಗುತ್ತೆ.

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು (Think out loud):
  →  "So every number appears twice except one — I need that one."
  →  "A hashmap would count frequencies, but that's O(n) space."
  →  "I notice XOR cancels pairs to zero, so XOR-ing the whole
      array leaves only the lone number — O(1) space."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Bit Manipulation → XOR Cancellation
  Secondary : —

  WHY XOR?
  → Rules out hashmap counting (O(n) space) immediately
  → x^x=0 (a number cancels itself), x^0=x (identity)
  → XOR-ing the whole array: pairs cancel, lone value survives

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 INTUITION (How to think)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Is there an operation where pairs of EQUAL numbers cancel to
  nothing, leaving only the odd one out?

  The journey from brute to optimal:
    Brute thought   →  hashmap frequency count
    Problem with it →  O(n) space, violates constraint
    Better question →  "does an operation exist that cancels pairs?"
    Insight         →  XOR: x^x=0, x^0=x
    Optimal         →  XOR every element together

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 APPROACH 1 — BRUTE FORCE (HashMap counting)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Count frequency of each number, return the one with count 1.

  Pseudocode:
    step 1: freq = {}; for num in nums: freq[num] = freq.get(num,0)+1
    step 2: for num, count in freq.items(): if count == 1: return num

  Time  : O(n)  →  Why: one pass to build, one pass to scan
  Space : O(n)  →  Why: hashmap stores up to n/2 + 1 keys

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ? (Why is this not enough?)
    → Problem O(1) extra space ಕೇಳ್ತಿದೆ; hashmap O(n) ಬಳಸುತ್ತೆ.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚶 APPROACH 2 — BETTER (skip — brute jumps straight to optimal)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ಇಲ್ಲಿ intermediate approach ಇಲ್ಲ — XOR insight ಸಿಕ್ಕ ತಕ್ಷಣ
  ನೇರವಾಗಿ O(1) space optimal ಗೆ ಹೋಗಬಹುದು.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 APPROACH 3 — OPTIMAL   (XOR Cancellation)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    XOR every element together — pairs cancel, lone value survives.

  Key steps:
    1. result = 0
    2. For each num in nums: result ^= num
    3. Return result

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ (Say it once in Kanglish so it sticks):
    → "Array ನ ಎಲ್ಲಾ numbers ಅನ್ನ ಒಂದೇ variable ಜೊತೆ XOR ಮಾಡ್ತಾ
        ಹೋಗು. ಎರಡು ಸಲ ಬಂದ numbers ಒಂದಕ್ಕೊಂದು cancel ಆಗಿ 0
        ಆಗ್ತಾವೆ, ಕೊನೆಗೆ ಒಂಟಿ number ಮಾತ್ರ ಉಳೀತದೆ."

  Time  : O(n)  →  Why: single pass
  Space : O(1)  →  Why: one accumulator variable

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: nums = [4, 1, 2, 1, 2]

  result=0
  num=4  →  variables: result=0   →  0^4=4
  num=1  →  variables: result=4   →  4^1=5
  num=2  →  variables: result=5   →  5^2=7
  num=1  →  variables: result=7   →  7^1=6
  num=2  →  variables: result=6   →  6^2=4

  Output: 4

  ಇನ್ನೊಂದು example — tricky case:
  Input: nums = [-1, -1, -3]
  result=0 ^ -1 = -1
  result=-1 ^ -1 = 0
  result=0 ^ -3 = -3
  Output: -3

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ Single element array?     →  [7] → 7 (nothing to cancel against)
  ✓ Negative numbers?         →  [-1,-1,-3] → -3
  ✓ Lone value at the start?  →  [5,3,3] → 5
  ✓ Lone value at the end?    →  [3,3,5] → 5
  ✓ Larger array, many pairs?  →  [2,2,3,3,4,4,9] → 9

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                Time      Space
  Brute Force   O(n)      O(n)
  Optimal       O(n)      O(1)    ← use this  

  Time ಯಾಕೆ O(n)?  → Array ಒಮ್ಮೆ ಮಾತ್ರ traverse ಮಾಡ್ತೇವೆ.
  Space ಯಾಕೆ O(1)? → result ಅನ್ನೋ ಒಂದೇ accumulator variable ಸಾಕು.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: XOR Cancellation

  ಈ pattern ಯಾವಾಗ use ಮಾಡಬೇಕು?
  → "every element appears TWICE except one" ಥರ pairing rule
    ಇದ್ದಾಗ
  → O(1) space demand ಇದ್ದಾಗ (hashmap ಬಳಸೋಕ್ಕಾಗಲ್ಲ ಅಂದಾಗ)

  ಇದೇ pattern ಬೇರೆ problems ನಲ್ಲಿ ಕಾಣಿಸುತ್ತೆ:
  → Missing Number (#268) — XOR indices against values
  → Single Number II (every element THREE times except one)
  → Single Number III (two lone numbers instead of one)

  Next time ಇಂತಹ problem ಬಂದ್ರೆ ನಾನು ಮೊದಲು ಇದನ್ನ think ಮಾಡ್ತೇನೆ:
  → "'Every element appears N times except one' ಅಂತ ಕಂಡ ತಕ್ಷಣ,
      XOR ಅಥವಾ bit-counting ಮೊದಲು ಯೋಚಿಸು."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ INTERVIEW ನಲ್ಲಿ ಹೇಗೆ EXPLAIN ಮಾಡಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "So every number appears exactly twice except one, and I
      need to find that one — in O(n) time, O(1) space."

  2. Brute force:
     "A hashmap frequency count works but uses O(n) extra space,
      which violates the constraint."

  3. Optimize:
     "I notice XOR has two properties that fit perfectly: x^x=0
      and x^0=x. XOR-ing the entire array cancels every pair,
      leaving only the lone number."

  4. Code:
     "I'll fold the array with XOR into a single accumulator
      variable, starting at 0."

  5. Complexity:
     "Time O(n) — one pass. Space O(1) — one variable."

  ಮುಖ್ಯ: ಸುಮ್ಮನೆ ಕೂತು code ಬರೆಯಬೇಡ!
         Interviewer ಗೆ ನಿನ್ನ thinking process ಕಾಣಬೇಕು.
"""


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(n) Time | O(n) Space
# ═══════════════════════════════════════════════════════════════════
def single_number_brute(nums):
    """ಇದು ಮೊದಲ ಆಲೋಚನೆ — hashmap frequency count, extra space"""
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
    for num, count in freq.items():
        if count == 1:
            return num


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n) Time | O(1) Space  (XOR)
# ═══════════════════════════════════════════════════════════════════
def single_number(nums):
    """ಇದು final answer — XOR cancellation, pairs vanish, odd one survives"""
    result = 0
    for num in nums:
        result ^= num
    return result


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")   # Windows cp1252 can't print   otherwise

    # Test 1 — Basic example
    assert single_number([4, 1, 2, 1, 2]) == 4

    # Test 2 — Edge case: single element
    assert single_number([7]) == 7

    # Test 3 — Edge case: negative numbers
    assert single_number([-1, -1, -3]) == -3

    # Test 4 — Tricky: lone value at start
    assert single_number([5, 3, 3]) == 5

    print("All tests passed!  ")
