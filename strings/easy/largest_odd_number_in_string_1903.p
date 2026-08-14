"""
╔════════════════════════════════════════════════════════════════════╗
║  LARGEST ODD NUMBER IN STRING                                      ║
║  LeetCode #1903  |  Difficulty: Easy  |  Topic: Strings/Traversal  ║
║  Link: https://leetcode.com/problems/largest-odd-number-in-string/ ║
╚════════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  You are given a string `num`, representing a large integer
  (only digits '0'-'9', no leading zero). Return the largest-
  valued odd integer, AS A STRING, that is a non-empty substring
  of `num`. If no odd integer exists among the substrings,
  return an empty string "".

  A substring must be CONTIGUOUS — you can't skip digits.

  Input : num = string of digits representing a large integer
  Output: string — largest odd substring, or "" if none exists

  Example 1 — basic:
    Input : num = "52"
    Output: "5"
    Why?  : "52" itself ends in 2 (even) → invalid. Trim the last
            digit → "5", which is odd → that's the answer

  Example 2 — slightly tricky (already odd):
    Input : num = "35427"
    Output: "35427"
    Why?  : the whole string already ends in 7 (odd) → no need
            to trim anything, the full number is the answer

  Example 3 — no odd digit anywhere:
    Input : num = "4206"
    Output: ""
    Why?  : every digit is even → no substring can end in an
            odd digit → no odd integer exists at all

  Constraints:
    - 1 <= num.length <= 10^5
    - num consists of digits '0' to '9' only
    - num does not contain leading zeros

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Problem odi aada mele namma brain enu think maadabeeku:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  digits ಇರೋ ದೊಡ್ಡ number string │
  │  Output ಏನು ಬೇಕು?     →  ಅದರ ಒಳಗಿನ largest ODD substring│
  │  Constraints ಏನಿದೆ?   →  substring CONTIGUOUS ಇರಬೇಕು,   │
  │                           leading zero ಇಲ್ಲ input ನಲ್ಲಿ  │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ಮೊದಲು naive ಆಗಿ ಯೋಚಿಸಿದ್ರೆ?
  →  ಎಲ್ಲಾ substrings generate ಮಾಡಿ, last digit odd ಆಗಿರೋ
     ಎಲ್ಲಾ substrings ಅನ್ನ collect ಮಾಡಿ, ಅವುಗಳಲ್ಲಿ largest
     value ಇರೋದನ್ನ ಆರಿಸಬಹುದು
  →  ಆದ್ರೆ ಇದು O(n^2) ಅಥವಾ O(n^3) — string length 10^5 ಇದ್ರೆ
     too slow!

  ಹಂತ 3 — "Number ಅನ್ನ LARGE ಆಗಿ ಮಾಡೋಕೆ ಏನು ಬೇಕು?" ಅಂತ
           ಯೋಚಿಸಿ
  →  Number ದೊಡ್ಡದಾಗಿ ಇರಬೇಕಂದ್ರೆ, ಅದಕ್ಕೆ ಹೆಚ್ಚು DIGITS
     ಇರಬೇಕು (leading zero ಇಲ್ಲದೇ ಇದ್ದಾಗ)
  →  ಈ number ನ digits ಎಲ್ಲಿಂದ ಶುರುವಾಗುತ್ತೆ ಅಂತ ಗಮನಿಸಿ →
     num ಗೆ leading zero ಇಲ್ಲ, so ಯಾವುದೇ PREFIX (index 0
     ಇಂದ ಶುರುವಾಗೋ substring) ಕೂಡ leading zero ಇಲ್ಲದ ಒಂದು
     valid number ಆಗಿರುತ್ತೆ
  →  So "longest possible PREFIX ಯಾವುದು odd digit ನಲ್ಲಿ
     ಮುಗಿಯುತ್ತೆ" ಅಂತ ಕೇಳಿದ್ರೆ ಸಾಕು — ಅದೇ answer!

  ಹಂತ 4 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  Right side ಇಂದ scan ಮಾಡಿ, ಮೊದಲ ODD digit ಸಿಕ್ಕ ತಕ್ಷಣ
     ಅಲ್ಲಿಗೆ trim ಮಾಡಿದ್ರೆ, ಅದು longest possible odd-ending
     prefix ಆಗುತ್ತೆ — ಅದಕ್ಕಿಂತ ಜಾಸ್ತಿ digits ಇಟ್ಟುಕೊಂಡ್ರೆ
     even digit ನಲ್ಲಿ ಮುಗಿಯುತ್ತೆ (invalid)
  →  Single right-to-left pass ಸಾಕು — O(n) time, no need to
     build/compare multiple substrings!

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು:
  →  "The answer, if it exists, is always a PREFIX of num —
      because more digits (without a leading zero) means a
      bigger number"
  →  "So scan from the right, find the first odd digit, and
      slice from the start up to (and including) that digit"
  →  "If no digit is odd, there's no valid answer → return empty
      string"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : String Traversal — scan from the right
  Secondary : Greedy prefix trimming

  WHY scan from the right?
  → The rightmost odd digit gives us the LONGEST valid prefix,
    and longest (no leading zero) always means numerically
    largest — so the first odd digit found from the right IS
    the answer's cut point, no comparisons needed.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  The key insight: since `num` has no leading zero, EVERY prefix
  of `num` (starting at index 0) is itself a valid number with
  no leading zero. Among numbers with no leading zero, more
  digits always means a bigger value. So we don't need to
  compare substring VALUES at all — we just need the LONGEST
  prefix that happens to end in an odd digit.

  The journey from brute to optimal:
    Brute thought   →  Generate all substrings, keep the ones
                       ending in an odd digit, compare their
                       values (by length then lexicographically)
    Problem with it →  O(n^2) substrings to generate, plus
                       comparisons → far too slow for n = 10^5
    Better question →  "Do I even need substrings that DON'T
                       start at index 0?"
    Insight         →  No! Since num has no leading zero, the
                       best answer is always some prefix num[:i+1]
                       — just find the rightmost odd digit
    Optimal         →  Single right-to-left scan, O(n) time

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Try every possible prefix length from the full length down
    to 1. For each prefix, check if its last digit is odd — the
    FIRST (longest) one that qualifies is the answer, since
    longer no-leading-zero numbers are always bigger.

  Pseudocode:
    step 1: for length L from len(num) down to 1:
    step 2:   candidate = num[:L]
    step 3:   if int(candidate[-1]) is odd → return candidate
    step 4: return ""

  Time  : O(n)  →  Why: at most n prefixes checked, each O(1)
                        digit check
  Space : O(n)  →  Why: each candidate slice copies up to n chars

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ?
    → Actually this IS already O(n) and close to optimal — the
      real inefficiency shows up if you naively try slicing +
      re-checking substrings that DON'T start at index 0 too
      (true brute force), which balloons to O(n^2) or worse.
      This version is included to show the "longest prefix"
      insight can be applied directly without extra tricks.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 6 — APPROACH 2 — OPTIMAL (Right-to-Left Scan)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Walk from the LAST character backward. The moment we find a
    digit that's odd, we know num[:i+1] is the longest possible
    odd-ending prefix — return it immediately. If we reach the
    start without finding one, no odd substring exists.

  Key steps:
    1. for i from len(num) - 1 down to 0:
    2.   if int(num[i]) is odd → return num[:i+1]
    3. return ""   # no odd digit found anywhere

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ:
    → "ಬಲಗಡೆಯಿಂದ ಎಡಕ್ಕೆ scan ಮಾಡು. ಮೊದಲ odd digit ಸಿಕ್ಕ
       ತಕ್ಷಣ, ಶುರುವಿಂದ ಆ digit ವರೆಗಿನ substring return ಮಾಡು —
       ಅದೇ ಅತಿ ದೊಡ್ಡ odd number!"

  Time  : O(n)  →  Why: worst case scans every char once, then
                        one slice of up to n chars
  Space : O(n)  →  Why: the returned slice can be up to n chars

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 7 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: num = "1234"

  i   digit   odd?   action
  3   '4'     No     keep scanning left
  2   '3'     Yes    return num[:3] = "123"

  Output: "123" ✓
  (check: among all substrings ending in an odd digit —
   "1","3","23","123" — 123 is the largest)

  ಇನ್ನೊಂದು example — trailing even digits:
  Input: num = "52"

  i   digit   odd?   action
  1   '2'     No     keep scanning left
  0   '5'     Yes    return num[:1] = "5"

  Output: "5" ✓

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 8 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ Already odd "35427"?           →  "35427" — whole string valid
  ✓ All even digits "4206"?        →  "" — no odd digit exists
  ✓ Single odd digit "7"?          →  "7" — trivially itself
  ✓ Single even digit "8"?         →  "" — nothing odd to return
  ✓ Odd digit right at index 0?    →  return just that one digit,
                                       e.g. "9000" → "9"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 9 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                    Time    Space
  Brute (prefix)    O(n)    O(n)
  Optimal (scan)    O(n)    O(n)   ← use this ✅ (cleanest, early-exit)

  Time yaake O(n)?  → Worst case scans every digit once, from
                       the right, before finding (or not finding)
                       an odd one
  Space yaake O(n)? → The returned substring itself can be up to
                       n characters long — unavoidable, it's the answer

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 10 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Greedy Prefix Trimming via Right-to-Left Scan

  Ee pattern yaavaaga use maadabeeku?
  → "Find the best/longest valid PREFIX of a number/string that
     satisfies some ending condition" type problems
  → Whenever comparing substring VALUES can be avoided by noticing
     "longer = bigger" (no leading zero) → skip building/comparing,
     just find the right cut point

  Idee pattern beere problemsalli kaanisatte:
  → Longest Common Prefix #14 (next problem — prefix comparison
     across MULTIPLE strings this time!)
  → Remove Trailing Zeros From a String #2710 (similar trim-from-
     the-right idea)

  Next time intaha problem bandre naanu modalu idannu think maadtene:
  → "Number/string alli 'longest valid prefix' bekagidre →
     right-to-left scan try maadu, ondu condition sikkidre
     immediately cut maadu — full substring generation bekilla!"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 11 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "Find the largest odd-valued substring of a digit string,
      where 'largest' just means the numeric value is biggest."

  2. Brute force:
     "Check prefixes from longest to shortest, return the first
      one whose last digit is odd. O(n), but relies on knowing
      the answer must be a prefix."

  3. Optimize:
     "Since num has no leading zero, every prefix is a valid
      number, and longer prefixes are always bigger. So scan
      from the right — the first odd digit found gives the
      longest valid odd prefix directly."

  4. Code:
     "Loop i from the last index down to 0. If num[i] is odd,
      return num[:i+1] immediately. If the loop finishes with
      no odd digit found, return an empty string."

  5. Complexity:
     "Time O(n) — single right-to-left scan. Space O(n) for the
      returned substring itself."

  Mukhya: "longer number (no leading zero) = bigger number" —
          idu tricky substring-value comparisons ellaa avoid
          maaduttade!
"""


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(n) Time | O(n) Space (check prefixes longest-first)
# ═══════════════════════════════════════════════════════════════════
def largest_odd_number_brute(num):
    """
    Idu modala aaloochane — longest prefix inda start madi,
    last digit odd sikko tanaka try madu
    """
    for length in range(len(num), 0, -1):
        candidate = num[:length]
        if int(candidate[-1]) % 2 == 1:
            return candidate

    return ""


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n) Time | O(n) Space (right-to-left scan)
# ═══════════════════════════════════════════════════════════════════
def largest_odd_number(num):
    """
    Idu final answer — balagadeyinda scan madi, modala odd digit
    sikkidkoodle andina tanaka substring return madu
    """
    for i in range(len(num) - 1, -1, -1):
        if int(num[i]) % 2 == 1:          # found an odd digit
            return num[:i + 1]            # longest valid odd prefix

    return ""                             # no odd digit anywhere


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # Test 1 — Basic (trim trailing even digit)
    assert largest_odd_number("52") == "5"

    # Test 2 — Already odd (no trimming needed)
    assert largest_odd_number("35427") == "35427"

    # Test 3 — No odd digit at all
    assert largest_odd_number("4206") == ""

    # Test 4 — Trim multiple digits
    assert largest_odd_number("1234") == "123"

    # Test 5 — Odd digit right at index 0
    assert largest_odd_number("9000") == "9"

    # Cross-check: brute force must agree on all of the above
    assert largest_odd_number_brute("52") == "5"
    assert largest_odd_number_brute("35427") == "35427"
    assert largest_odd_number_brute("4206") == ""
    assert largest_odd_number_brute("1234") == "123"
    assert largest_odd_number_brute("9000") == "9"

    print("All tests passed!")
