"""
╔══════════════════════════════════════════════════════════════════╗
║  PLUS ONE                                                        ║
║  LeetCode #66  |  Difficulty: Easy  |  Topic: Arrays / Simulation ║
║  Link: https://leetcode.com/problems/plus-one/                   ║
╚══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  A non-negative integer is represented as digits, MSB first, no
  leading zeros (except the number 0 itself). Add one, return the
  new digit array.

  Input : digits = [1, 2, 3]
  Output: [1, 2, 4]

  Example 1 — basic:
    Input : digits = [1, 2, 3]
    Output: [1, 2, 4]
    Why?  : 123 + 1 = 124, only the last digit changes

  Example 2 — slightly tricky:
    Input : digits = [9, 9]
    Output: [1, 0, 0]
    Why?  : 99 + 1 = 100 — carry propagates all the way, array GROWS

  Constraints:
    - digits[i] is a single digit 0-9
    - No leading zeros in input (except digits == [0])
    - Output array may need to be one element LONGER than input

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ಮೊದಲು problem odidaga ನಮ್ಮ brain ಏನು think ಮಾಡಬೇಕು:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ (What are they asking?)
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  ಒಂದು number ನ digits, MSB      │
  │                          ಮೊದಲು ಇರೋ array                 │
  │  Output ಏನು ಬೇಕು?     →  ಆ number ಗೆ +1 ಮಾಡಿದ digits    │
  │  Constraints ಏನಿದೆ?   →  9,9,9 ಥರ ಎಲ್ಲಾ 9 ಇದ್ರೆ, array   │
  │                          length ಒಂದು ಜಾಸ್ತಿ ಆಗಬಹುದು       │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ನನಗೆ ಗೊತ್ತಿರೋ simple way ಏನು? (Brute force thought)
  →  Digits ಅನ್ನ ಒಂದು number ಆಗಿ join ಮಾಡಿ, +1 ಮಾಡಿ, ಮತ್ತೆ
     digits ಆಗಿ split ಮಾಡೋದು.
  →  ಆದರೆ ಇದು ಯಾಕೆ ideal ಅಲ್ಲ? → Python ನಲ್ಲಿ ಸರಿಯಾಗಿ ಕೆಲಸ
     ಮಾಡುತ್ತೆ, ಆದ್ರೆ ಇದು array/carry manipulation practice ನ
     purpose defeat ಮಾಡುತ್ತೆ, ಬೇರೆ languages ನಲ್ಲಿ overflow
     ಆಗಬಹುದು.

  ಹಂತ 3 — Better way ಹೇಗೆ ಯೋಚಿಸುವುದು? (Optimization thought)
  →  "ಕೈಯಲ್ಲಿ addition ಮಾಡುವಾಗ ನಾನು ಹೇಗೆ +1 ಮಾಡ್ತೀನಿ? ಕೊನೆ digit
     ಇಂದ ಶುರು ಮಾಡ್ತೀನಿ."
  →  ಅಹಾ moment: ಕೊನೆ digit < 9 ಆಗಿದ್ರೆ, ಬರೀ +1 ಮಾಡಿ STOP —
     ಬೇರೇನೂ change ಆಗಲ್ಲ. digit == 9 ಆಗಿದ್ರೆ, 0 ಆಗಿ roll over
     ಆಗುತ್ತೆ, carry ಎಡಕ್ಕೆ ಹೋಗುತ್ತೆ — repeat.
  →  ಇದರಿಂದ ನಾವು Reverse Carry Propagation use ಮಾಡಬಹುದು!

  ಹಂತ 4 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  digits MSB-first ಆಗಿರೋದ್ರಿಂದ, +1 ಯಾವಾಗ್ಲೂ ಕೊನೆ digit ಇಂದ
     ಶುರುವಾಗುತ್ತೆ — ಕೈಯಿಂದ addition ಮಾಡೋ ಥರ.
  →  ಒಂದು digit roll over ಆಗದೇ ಇದ್ದ ತಕ್ಷಣ, ಮುಂದೆ ಏನೂ change
     ಆಗಲ್ಲ ಅಂತ ಗ್ಯಾರಂಟಿ — ಇದೇ early-exit efficiency.
  →  All-9s case ನಲ್ಲಿ array GROW ಆಗ್ಬೇಕು ಅನ್ನೋದನ್ನ explicit
     ಆಗಿ handle ಮಾಡ್ಬೇಕು.

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು (Think out loud):
  →  "So I need to add 1 to a number represented as a digit array."
  →  "I could convert to int and back, but that defeats the
      array-manipulation intent and risks overflow in other languages."
  →  "I'll simulate manual addition: right to left, propagate carry,
      and stop early the moment a digit doesn't roll over."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Array Manipulation → Reverse Carry Propagation
  Secondary : Right-to-left scan (same shape as manual addition)

  WHY this technique?
  → digits is MSB-first, so +1 always affects the LAST digit first
  → Carry only propagates left while a digit rolls 9→0
  → The moment a digit doesn't roll over, we're done — early exit

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 INTUITION (How to think)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  How would I add 1 to a number BY HAND, digit by digit?

  The journey from brute to optimal:
    Brute thought   →  int(digits) + 1, split back to digits
    Problem with it →  defeats the array/carry practice, risky elsewhere
    Better question →  "simulate manual addition, right to left?"
    Insight         →  a digit < 9 just gets +1 and we STOP
    Optimal         →  carry propagation, early exit, handle all-9s

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 APPROACH 1 — BRUTE FORCE (int conversion)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Join digits into a number, add 1, split back into digits.

  Pseudocode:
    step 1: num = int("".join(map(str, digits))) + 1
    step 2: return [int(c) for c in str(num)]

  Time  : O(n)  →  Why: string ops are linear in digit count
  Space : O(n)  →  Why: string/int representation

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ? (Why is this not enough?)
    → Python ಲ್ಲಿ ಸರಿ ಆಗುತ್ತೆ, ಆದ್ರೆ array/carry practice defeat
      ಮಾಡುತ್ತೆ, ಬೇರೆ languages ಲ್ಲಿ fixed-width int overflow ಆಗುತ್ತೆ.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚶 APPROACH 2 — BETTER (skip — brute jumps straight to optimal)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ಇಲ್ಲಿ intermediate approach ಇಲ್ಲ — carry propagation insight
  ಸಿಕ್ಕ ತಕ್ಷಣ ನೇರವಾಗಿ optimal ಗೆ ಹೋಗಬಹುದು.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 APPROACH 3 — OPTIMAL   (Carry Propagation)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Walk right to left, add carry, stop early when possible.

  Key steps:
    1. For i from last index down to 0:
         if digits[i] < 9: digits[i] += 1; return digits  (done!)
         else: digits[i] = 0  (rolls over, carry continues left)
    2. If loop exits (all digits WERE 9, all became 0):
         prepend 1 → [1] + digits

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ (Say it once in Kanglish so it sticks):
    → "ಕೊನೆ digit ಇಂದ ಶುರು ಮಾಡು. digit 9 ಗಿಂತ ಕಡಿಮೆ ಇದ್ರೆ, +1
        ಮಾಡಿ ತಕ್ಷಣ return ಮಾಡು — ಬೇರೇನೂ change ಆಗಲ್ಲ. digit 9
        ಆಗಿದ್ರೆ, 0 ಮಾಡಿ, ಎಡಕ್ಕೆ ಹೋಗಿ ಇದೇ ಪ್ರಶ್ನೆ ಮತ್ತೆ ಕೇಳು. ಎಲ್ಲಾ
        digits ಮುಗಿದ್ರೂ carry ಉಳಿದಿದ್ರೆ, ಮುಂದೆ ಒಂದು 1 ಸೇರಿಸು."

  Time  : O(n)  →  Why: worst case (all 9s) touches every digit once
  Space : O(1) extra  →  Why: O(n) only when array must grow by one

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: digits = [1, 2, 9]

  i=2  →  variables: digits[2]=9  →  rolls over → digits=[1,2,0], carry continues
  i=1  →  variables: digits[1]=2  →  2 < 9 → digits[1]=3 → return [1,3,0]

  Output: [1, 3, 0] (129 + 1 = 130)

  ಇನ್ನೊಂದು example — tricky case:
  Input: digits = [9, 9]
  i=1  digits[1]=9 → rolls over → digits=[9,0]
  i=0  digits[0]=9 → rolls over → digits=[0,0]
  Loop ends (all were 9s) → prepend 1 → [1,0,0]
  Output: [1, 0, 0] (99 + 1 = 100)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ Single digit, no rollover?  →  [5] → [6]
  ✓ Single digit, rollover?     →  [9] → [1, 0]
  ✓ All nines?                  →  [9,9,9] → [1,0,0,0] (array grows)
  ✓ Zero?                       →  [0] → [1]
  ✓ No carry needed at all?     →  [1,2,3] → [1,2,4] (early exit)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                Time      Space
  Brute Force   O(n)      O(n)   (int/string conversion)
  Optimal       O(n)      O(1) extra    ← use this  

  Time ಯಾಕೆ O(n)?  → Worst case (all 9s) ಪ್ರತಿ digit ಒಮ್ಮೆ touch ಆಗುತ್ತೆ.
  Space ಯಾಕೆ O(1)? → All-9s case ಬಿಟ್ಟು ಬೇರೆ ಎಲ್ಲಾ case ಲ್ಲಿ extra
                       space ಬೇಕಿಲ್ಲ, in-place modify ಮಾಡ್ತೀವಿ.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Reverse Carry Propagation

  ಈ pattern ಯಾವಾಗ use ಮಾಡಬೇಕು?
  → Problem number ಅನ್ನ digit array ಆಗಿ represent ಮಾಡಿ, arithmetic
    ಕೇಳಿದಾಗ
  → ಕೈಯಿಂದ addition ಮಾಡೋ ಹಾಗೇ simulate ಮಾಡಬಹುದಾ ಅಂತ ಯೋಚಿಸಿ

  ಇದೇ pattern ಬೇರೆ problems ನಲ್ಲಿ ಕಾಣಿಸುತ್ತೆ:
  → Add Binary
  → Add Two Numbers (linked list version)
  → Multiply Strings

  Next time ಇಂತಹ problem ಬಂದ್ರೆ ನಾನು ಮೊದಲು ಇದನ್ನ think ಮಾಡ್ತೇನೆ:
  → "Digit array arithmetic ಬಂತು ಅಂದ್ರೆ, right-to-left carry
      propagation ಮತ್ತು early-exit ಮೊದಲು ಯೋಚಿಸು. All-9s edge
      case ಮರೀಬೇಡ."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ INTERVIEW ನಲ್ಲಿ ಹೇಗೆ EXPLAIN ಮಾಡಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "So I need to add 1 to a number given as an MSB-first digit
      array, and handle the case where the array needs to grow."

  2. Brute force:
     "I could convert to an int, add 1, and split back into
      digits — that works in Python but defeats the intent of
      practicing carry manipulation."

  3. Optimize:
     "I'll simulate manual addition: walk right to left, and the
      moment a digit doesn't roll over from 9, I can stop — no
      further digits change."

  4. Code:
     "If digits[i] < 9, increment and return immediately. Else
      set it to 0 and continue left. If the loop finishes, prepend
      a 1 for the all-9s case."

  5. Complexity:
     "Time O(n) worst case (all 9s). Space O(1) extra, except when
      the array must grow by one slot."

  ಮುಖ್ಯ: ಸುಮ್ಮನೆ ಕೂತು code ಬರೆಯಬೇಡ!
         Interviewer ಗೆ ನಿನ್ನ thinking process ಕಾಣಬೇಕು.
"""


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(n) Time | O(n) Space  (int conversion)
# ═══════════════════════════════════════════════════════════════════
def plus_one_brute(digits):
    """ಇದು ಮೊದಲ ಆಲೋಚನೆ — int ಗೆ convert ಮಾಡಿ +1, ಮತ್ತೆ digits ಗೆ split"""
    num = int("".join(map(str, digits))) + 1
    return [int(c) for c in str(num)]


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n) Time | O(1) Extra Space  (Carry Propagation)
# ═══════════════════════════════════════════════════════════════════
def plus_one(digits):
    """ಇದು final answer — right-to-left carry propagation, early exit"""
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0

    return [1] + digits


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")   # Windows cp1252 can't print   otherwise

    # Test 1 — Basic example
    assert plus_one([1, 2, 3]) == [1, 2, 4]

    # Test 2 — Edge case: all nines, array grows
    assert plus_one([9, 9, 9]) == [1, 0, 0, 0]

    # Test 3 — Edge case: zero
    assert plus_one([0]) == [1]

    # Test 4 — Tricky: partial carry propagation
    assert plus_one([1, 2, 9]) == [1, 3, 0]

    print("All tests passed!  ")
