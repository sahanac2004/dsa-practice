"""
╔════════════════════════════════════════════════════════════════════╗
║  CHECK IF STRING IS ROTATION OF ANOTHER (ROTATE STRING)            ║
║  LeetCode #796  |  Difficulty: Easy  |  Topic: Strings/Concatenation║
║  Link: https://leetcode.com/problems/rotate-string/                ║
╚════════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Given two strings `s` and `goal`, return True if and only if
  `s` can become `goal` after some number of SHIFTS.

  A shift moves the LEFTMOST character of `s` to the RIGHTMOST
  position, e.g. one shift of "abcde" → "bcdea".

  Input : s, goal = two strings
  Output: boolean — True if goal is some rotation of s

  Example 1 — basic:
    Input : s = "abcde", goal = "cdeab"
    Output: True
    Why?  : two left-shifts of "abcde" → "bcdea" → "cdeab"

  Example 2 — slightly tricky (same letters, wrong order):
    Input : s = "abcde", goal = "abced"
    Output: False
    Why?  : "abced" has the same letters as "abcde" but they're
            NOT in a rotated order — no sequence of shifts
            produces this from "abcde"

  Example 3 — different lengths:
    Input : s = "abc", goal = "abcd"
    Output: False
    Why?  : rotation can never change the length — different
            lengths mean it's impossible right away

  Constraints:
    - 1 <= s.length, goal.length <= 100
    - s and goal consist of lowercase English letters

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Problem odi aada mele namma brain enu think maadabeeku:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  ಎರಡು strings s, goal            │
  │  Output ಏನು ಬೇಕು?     →  goal, s ರ ಯಾವುದಾದ್ರೂ            │
  │                           rotation ಆಗಿದ್ಯಾ ಅಂತ ಚೆಕ್       │
  │  Constraints ಏನಿದೆ?   →  length ಬೇರೆ ಇದ್ರೆ ಸಾಧ್ಯನೇ ಇಲ್ಲ  │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ಮೊದಲ simple idea ಏನು?
  →  s ಅನ್ನ actual ಆಗಿ ಪ್ರತಿ ಸಲ shift ಮಾಡ್ತಾ ಹೋಗಿ, ಪ್ರತಿ
     rotation ಅನ್ನ goal ಜೊತೆ compare ಮಾಡಿ
  →  len(s) sಲ್ಲಿ ಎಷ್ಟು characters ಇವೆಯೋ ಅಷ್ಟು rotations
     try ಮಾಡಿದ್ರೆ ಎಲ್ಲಾ possibilities cover ಆಗುತ್ತೆ

  ಹಂತ 3 — Smart trick ಏನಿದೆ?
  →  "s+s (s ಅನ್ನ ತನ್ನ ಜೊತೆ concatenate ಮಾಡಿದ್ರೆ) ಒಳಗೆ,
      s ರ ಎಲ್ಲಾ ಸಾಧ್ಯ ಇರೋ ROTATIONS ಒಂದು substring ಆಗಿ
      ಸಿಗುತ್ತಾ ಇರುತ್ತೆ!" ಅಂತ ಗಮನಿಸಿ
  →  Example: s="abcde" → s+s="abcdeabcde"
     ಇದರಲ್ಲಿ "bcdea" (index1-5), "cdeab" (index2-6),
     "deabc" (index3-7)... ಎಲ್ಲಾ rotations ಇವೆ!
  →  So goal ಅನ್ನ s+s ಒಳಗೆ substring ಆಗಿ ಹುಡುಕಿದ್ರೆ ಸಾಕು
     (ಜೊತೆಗೆ length ಸಮ ಆಗಿರಬೇಕು)

  ಹಂತ 4 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  ಪ್ರತಿ rotation ಅಂದ್ರೆ, s ಅನ್ನ ಒಂದು point ನಲ್ಲಿ "cut" ಮಾಡಿ,
     ಮುಂಚಿನ ಭಾಗ ಅನ್ನ ಹಿಂದೆ ಇಟ್ಟಂತೆ
  →  s+s ಮಾಡಿದಾಗ, ಆ ಎಲ್ಲಾ "cut points" ಇಂದ ಶುರುವಾಗೋ length-n
     substrings ಎಲ್ಲಾ rotations ಆಗಿ ಸಿಗುತ್ತವೆ — ಒಂದೇ
     concatenation ನಲ್ಲಿ ಎಲ್ಲಾ ಸಾಧ್ಯತೆ cover ಆಗುತ್ತೆ!

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು:
  →  "First check lengths match — rotation preserves length"
  →  "Then the classic trick: concatenate s with itself (s+s).
      Every possible rotation of s appears as a contiguous
      substring somewhere in s+s"
  →  "So just check if goal is a substring of s+s"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : String Concatenation Trick (s + s contains all rotations)
  Secondary : Brute-force rotation generation

  WHY the Concatenation Trick?
  → Doubling the string turns "check all rotations" into a
    single substring-search problem — no need to construct and
    compare each rotation one at a time.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  The key insight: any rotation of `s` just picks a "cut point"
  in `s` and swaps the two halves. If you glue `s` to itself
  (s + s), every one of those cut points becomes a valid starting
  index for a length-n window — and that window IS the rotation
  starting at that cut. So ALL rotations of `s` live inside `s+s`
  as substrings, simultaneously, without building any of them.

  The journey from brute to optimal:
    Brute thought   →  Physically perform each shift (move first
                       char to the end), compare against goal,
                       repeat up to n times
    Problem with it →  O(n) work per rotation attempt (slicing +
                       comparing), O(n) rotations → O(n^2) total
    Better question →  "Do I need to physically rotate the
                       string, or can I just LOOK for the
                       rotated pattern somewhere?"
    Insight         →  s+s already contains every rotation as a
                       substring — just search for goal in it
    Optimal         →  One length check + one substring search,
                       O(n) with an efficient search

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE (physically rotate)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    If lengths differ, immediately False. Otherwise, perform up
    to len(s) shifts one at a time (move the first character to
    the end), checking after every shift whether the result
    equals `goal`.

  Pseudocode:
    step 1: if len(s) != len(goal): return False
    step 2: current = s
    step 3: for _ in range(len(s)):
    step 4:   if current == goal: return True
    step 5:   current = current[1:] + current[0]   # one shift
    step 6: return False

  Time  : O(n^2)  →  Why: n possible shifts, each shift + compare
                          costs O(n) (slicing/rebuilding a string)
  Space : O(n)     →  Why: each shifted string is a new O(n) copy

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ?
    → Correct, but rebuilds and compares a full string on every
      single shift attempt — wasteful when the "s+s contains all
      rotations" trick gets the same answer with one search.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 6 — APPROACH 2 — OPTIMAL (Concatenation Trick)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    If lengths differ, immediately False (rotation never changes
    length). Otherwise, concatenate `s` with itself and check if
    `goal` appears anywhere inside as a substring.

  Key steps:
    1. if len(s) != len(goal): return False
    2. return goal in (s + s)

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ:
    → "ಮೊದಲು length ಸಮ ಇದ್ಯಾ ಚೆಕ್ ಮಾಡು. ಆಮೇಲೆ s ಅನ್ನ ತನ್ನ
       ಜೊತೆ ಸೇರಿಸಿ (s+s) ಮಾಡಿ, goal ಅದರೊಳಗೆ substring ಆಗಿ
       ಸಿಗುತ್ತಾ ಅಂತ ಚೆಕ್ ಮಾಡಿದ್ರೆ ಸಾಕು — ಎಲ್ಲಾ rotations
       ಆಗಲೇ ಅಲ್ಲಿ ಇರುತ್ತೆ!"

  Time  : O(n)  →  Why: string concatenation is O(n), and
                        Python's `in` substring search runs in
                        O(n) on average for this size of input
  Space : O(n)  →  Why: the concatenated string s+s is 2n chars

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 7 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: s = "abcde", goal = "cdeab"

  Step 1: len(s) == len(goal)? 5 == 5 → yes, continue

  Step 2: s + s = "abcdeabcde"
          highlight all length-5 windows:
            "abcde" (0-4), "bcdea" (1-5), "cdeab" (2-6) ← MATCH!
            "deabc" (3-7), "eabcd" (4-8)

  "cdeab" found inside "abcdeabcde" at index 2

  Output: True ✓

  ಇನ್ನೊಂದು example — not a rotation:
  Input: s = "abcde", goal = "abced"

  Step 1: lengths match (5 == 5), continue
  Step 2: s + s = "abcdeabcde"
          Is "abced" anywhere in there? Scanning all length-5
          windows (abcde, bcdea, cdeab, deabc, eabcd) — none of
          them is "abced"

  Output: False ✓

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 8 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ Different lengths?             →  False immediately, no need
                                       to even build s+s
  ✓ Identical strings s == goal?   →  True — zero shifts is valid
  ✓ Single character "a","a"?      →  True — trivially itself
  ✓ Same letters, wrong order
    ("abcde" vs "abced")?          →  False — anagram ≠ rotation
  ✓ Full rotation back to original
    (n shifts)?                    →  True — s itself is a valid
                                       "rotation" of s (0 shifts,
                                       or equivalently n shifts)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 9 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                        Time    Space
  Brute (rotate each)   O(n^2)  O(n)
  Optimal (s+s trick)   O(n)    O(n)   ← use this ✅

  Time yaake O(n)?  → One O(n) concatenation + one O(n) average
                       substring search
  Space yaake O(n)? → The concatenated string s+s holds 2n chars

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 10 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Double-and-Search (self-concatenation trick)

  Ee pattern yaavaaga use maadabeeku?
  → "Is X a rotation/cyclic-shift of Y?" type problems — instead
     of generating every shift, double one string and search
  → Circular array / circular buffer problems where wrap-around
     matters — doubling the array is a common trick there too

  Idee pattern beere problemsalli kaanisatte:
  → Valid Anagram #242 (next problem — same LETTERS but ORDER
     doesn't matter at all, nice contrast to rotation where
     order matters completely!)
  → Circular Array Loop / Rotate Array (doubling trick reused)
  → Repeated String Match (also uses string doubling/tripling)

  Next time intaha problem bandre naanu modalu idannu think maadtene:
  → "Rotation/cyclic-shift check bekagidre → string ge tanna
     jothe concatenate maadu (s+s), aamele goal string ge
     substring search madu — ella rotations already alli
     iruttave!"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 11 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "Determine if goal can be produced from s using repeated
      left-shifts (moving the first char to the end)."

  2. Brute force:
     "Physically perform each shift and compare to goal, up to
      n times. O(n^2) since each shift+compare is O(n)."

  3. Optimize:
     "First check lengths match. Then use the classic trick:
      s+s contains every rotation of s as a substring. So just
      check if goal is a substring of s+s."

  4. Code:
     "if len(s) != len(goal): return False.
      return goal in (s + s)."

  5. Complexity:
     "Time O(n) — one concatenation, one substring search.
      Space O(n) for the doubled string."

  Mukhya: "double the string, then search" — turns an O(n^2)
          rotation-check into a single O(n) substring lookup!
"""


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(n^2) Time | O(n) Space (physically rotate)
# ═══════════════════════════════════════════════════════════════════
def is_rotation_brute(s, goal):
    """
    Idu modala aaloochane — s ge nija agi shift madtha hogi,
    prati shift na goal jothe compare madu
    """
    if len(s) != len(goal):
        return False

    current = s
    for _ in range(len(s)):
        if current == goal:
            return True
        current = current[1:] + current[0]     # one left shift

    return False


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n) Time | O(n) Space (self-concatenation trick)
# ═══════════════════════════════════════════════════════════════════
def is_rotation(s, goal):
    """
    Idu final answer — length check madi, aamele s+s ondu string
    inside goal substring aagi sigutta antha check madu
    """
    if len(s) != len(goal):
        return False

    return goal in (s + s)


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # Test 1 — Basic rotation
    assert is_rotation("abcde", "cdeab") is True

    # Test 2 — Same letters, wrong order (not a rotation)
    assert is_rotation("abcde", "abced") is False

    # Test 3 — Different lengths
    assert is_rotation("abc", "abcd") is False

    # Test 4 — Identical strings (zero shifts)
    assert is_rotation("abcde", "abcde") is True

    # Test 5 — Single character
    assert is_rotation("a", "a") is True

    # Cross-check: brute force must agree on all of the above
    assert is_rotation_brute("abcde", "cdeab") is True
    assert is_rotation_brute("abcde", "abced") is False
    assert is_rotation_brute("abc", "abcd") is False
    assert is_rotation_brute("abcde", "abcde") is True
    assert is_rotation_brute("a", "a") is True

    print("All tests passed!")
