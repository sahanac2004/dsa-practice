"""
╔════════════════════════════════════════════════════════════════════╗
║  PALINDROMIC SUBSTRINGS                                            ║
║  LeetCode #647  |  Difficulty: Medium  |  Topic: Strings/Two Pointers║
║  Link: https://leetcode.com/problems/palindromic-substrings/       ║
╚════════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Given a string `s`, return the NUMBER of palindromic
  substrings it contains. A substring is a contiguous run of
  characters — two substrings that occupy different positions
  count SEPARATELY even if their text is identical.

  Input : s = a string
  Output: integer — total count of palindromic substrings

  Example 1 — basic:
    Input : s = "abc"
    Output: 3
    Why?  : only the three single-character substrings "a", "b",
            "c" are palindromes — no longer substring reads the
            same both ways

  Example 2 — slightly tricky (overlapping palindromes):
    Input : s = "aaa"
    Output: 6
    Why?  : three single-char palindromes ("a","a","a"), two
            two-char palindromes ("aa","aa"), and one three-char
            palindrome ("aaa") → 3 + 2 + 1 = 6

  Example 3 — mixed characters:
    Input : s = "aba"
    Output: 4
    Why?  : "a", "b", "a" (three single chars) plus "aba" itself
            → 4 total

  Constraints:
    - 1 <= s.length <= 1000
    - s consists of lowercase English letters

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Problem odi aada mele namma brain enu think maadabeeku:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  ಒಂದು string s                   │
  │  Output ಏನು ಬೇಕು?     →  ಎಷ್ಟು substrings palindrome     │
  │                           ಆಗಿವೆ ಅಂತ COUNT                │
  │  Constraints ಏನಿದೆ?   →  ಬೇರೆ ಬೇರೆ position ರ substrings  │
  │                           text ಒಂದೇ ಆದ್ರೂ ಪ್ರತ್ಯೇಕ ಆಗಿ     │
  │                           ಎಣಿಸಬೇಕು                        │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ಇದನ್ನ previous problem (#13 Longest Palindromic
           Substring) ಜೊತೆ connect ಮಾಡಿ ನೋಡಿ!
  →  ಅಲ್ಲಿ ನಾವು "Expand Around Center" technique ಬಳಸಿ ಅತಿ
     ಉದ್ದ palindrome ಅನ್ನ TRACK ಮಾಡಿದ್ವಿ
  →  ಇಲ್ಲಿ ಕೂಡ ಅದೇ technique — ಆದ್ರೆ TRACK ಮಾಡೋ ಬದಲು, ಪ್ರತಿ
     valid expansion step ಗೂ ಒಂದು COUNT ಹೆಚ್ಚಿಸಿದ್ರೆ ಸಾಕು!

  ಹಂತ 3 — Key observation ಏನಿದೆ?
  →  ಒಂದು center ಇಂದ expand ಮಾಡುವಾಗ, ಪ್ರತಿ ಸಲ characters
     match ಆದಾಗ (left,right ಎಡ-ಬಲ ಸರಿಸಿದಾಗ), ಆ position ಗಳ
     ಒಳಗಿನ substring ಒಂದು NEW palindrome ಆಗಿರುತ್ತೆ
  →  So expand ಮಾಡ್ತಾ ಇರೋವರೆಗೆ, ಪ್ರತಿ successful match ಗೂ
     count += 1 ಮಾಡಿದ್ರೆ, ಆ center ಇಂದ ಸಿಗೋ ಎಲ್ಲಾ palindromes
     ಎಣಿಸಿದ ಹಾಗೆ ಆಗುತ್ತೆ

  ಹಂತ 4 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  2n-1 possible centers (n odd + n-1 even) ಗೂ ಇದೇ ಮಾಡಿದ್ರೆ,
     string ನಲ್ಲಿ ಇರೋ ಎಲ್ಲಾ palindromic substrings (double
     counting ಇಲ್ಲದೇ) cover ಆಗುತ್ತೆ — ಯಾಕಂದ್ರೆ ಪ್ರತಿ palindrome
     ಗೂ EXACTLY ಒಂದೇ center ಇರುತ್ತೆ

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು:
  →  "Same expand-around-center technique as Longest Palindromic
      Substring, but instead of tracking the widest window, I
      increment a counter on every successful expansion step"
  →  "Every palindrome has exactly one center, so trying all
      2n-1 centers counts every palindromic substring exactly
      once"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Expand Around Center (count instead of track-longest)
  Secondary : Brute-force substring generation + palindrome check

  WHY Expand Around Center for counting?
  → Every palindromic substring has exactly one center (single
    char for odd length, gap between two chars for even length).
    Expanding from every possible center and counting each
    successful match visits every palindrome exactly once —
    no double-counting, no missed substrings.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  The key insight: this problem is almost identical to #13
  (Longest Palindromic Substring) in mechanism — only the GOAL
  changes. There, we tracked the WIDEST successful expansion.
  Here, we care about EVERY successful expansion step, since
  each one corresponds to a distinct valid palindromic substring
  centered at that point.

  The journey from brute to optimal:
    Brute thought   →  Generate every substring, check if it's a
                       palindrome by reversing and comparing,
                       count the ones that qualify
    Problem with it →  O(n^2) substrings, each check costs O(n)
                       → O(n^3) total
    Better question →  "Can I count palindromes AS I expand from
                       their centers, instead of checking fully-
                       built substrings after the fact?"
    Insight         →  Every successful expansion step from a
                       center IS a new palindromic substring —
                       just count them as they're found
    Optimal         →  2n-1 centers, each expansion up to O(n),
                       O(n^2) total, O(1) extra space

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE (check every substring)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Generate every substring s[i:j+1] for all i ≤ j. Check if
    each one equals its own reverse; if so, count it.

  Pseudocode:
    step 1: count = 0
    step 2: for i in range(n):
    step 3:   for j in range(i, n):
    step 4:     candidate = s[i:j+1]
    step 5:     if candidate == candidate[::-1]:
    step 6:       count += 1
    step 7: return count

  Time  : O(n^3)  →  Why: O(n^2) substrings, each palindrome
                          check (reverse + compare) costs O(n)
  Space : O(n)     →  Why: each candidate slice is a new string
                          copy up to length n

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ?
    → Correct, but cubic time — for n = 1000 this is far too
      slow. Expanding from centers avoids re-checking substrings
      that are already known to fail.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 6 — APPROACH 2 — OPTIMAL (Expand Around Center, counting)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    For every index `i`, try both possible centers — (i, i) for
    odd-length palindromes and (i, i+1) for even-length ones.
    Expand outward with two pointers while characters match,
    incrementing a counter on EVERY successful match (not just
    tracking the final width).

  Key steps:
    1. count = 0
    2. def expand(left, right):
    3.   while left >= 0 and right < n and s[left] == s[right]:
    4.     count += 1
    5.     left -= 1; right += 1
    6. for i in range(n):
    7.   expand(i, i)          # odd-length center
    8.   expand(i, i + 1)      # even-length center
    9. return count

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ:
    → "ಪ್ರತಿ index i ಗೆ ಎರಡು centers try ಮಾಡು: (i,i) ಮತ್ತು
       (i,i+1). ಪ್ರತಿ center ಇಂದ ಎಡ-ಬಲ pointers ಹೊರಗಡೆ
       ಸರಿಸ್ತಾ ಹೋಗು, characters match ಆದಾಗಲೆಲ್ಲಾ count += 1
       ಮಾಡು. ಎಲ್ಲಾ centers ಗೂ ಇದೇ ಮಾಡಿ, ಕೊನೆಗೆ total count
       return ಮಾಡು!"

  Time  : O(n^2)  →  Why: 2n-1 centers, each expansion can go
                          up to O(n) in the worst case (e.g. all
                          same character)
  Space : O(1)     →  Why: only a counter and a few pointers
                          tracked

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 7 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: s = "aaa"

  i=0: expand(0,0) → match at (0,0): count=1; try (-1,1): out
       of bounds, stop
       expand(0,1) → s[0]='a'==s[1]='a': count=2; try (-1,2):
       out of bounds, stop
  i=1: expand(1,1) → match at (1,1): count=3; try (0,2):
       s[0]='a'==s[2]='a': count=4; try (-1,3): out of bounds, stop
       expand(1,2) → s[1]='a'==s[2]='a': count=5; try (0,3):
       right=3 out of bounds (n=3), stop
  i=2: expand(2,2) → match at (2,2): count=6; try (1,3): right
       out of bounds, stop
       expand(2,3) → right=3 out of bounds immediately, no match

  Total count = 6

  Output: 6 ✓  (matches: "a","a","a","aa","aa","aaa")

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 8 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ Single character "a"?          →  1 — just itself
  ✓ No repeated characters "abc"?  →  3 — only single chars count
  ✓ All same character "aaaa"?     →  10 — every substring is a
                                       palindrome (4+3+2+1=10)
  ✓ Palindrome with center gap
    "aba"?                         →  4 — includes the whole
                                       string itself
  ✓ Two identical adjacent chars
    "aa"?                          →  3 — "a","a","aa"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 9 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                          Time    Space
  Brute (all substrings)  O(n^3)  O(n)
  Optimal (expand-center) O(n^2)  O(1)   ← use this ✅

  Time yaake O(n^2)?  → 2n-1 centers, each expansion bounded by
                         string length in the worst case
  Space yaake O(1)?   → Just a counter and pointers — no extra
                         data structures

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 10 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Expand Around Center — count variant

  Ee pattern yaavaaga use maadabeeku?
  → Palindrome COUNTING problems — same expand-around-center
     mechanism as Longest Palindromic Substring (#13), just
     count every successful expansion instead of tracking the
     widest one
  → Reinforces: any "find/count palindromic substrings" family
     problem starts with "try every center"

  Idee pattern beere problemsalli kaanisatte:
  → Longest Palindromic Substring #5 (previous problem — same
     technique, tracks WIDEST instead of counting ALL)
  → Longest Palindromic Subsequence #516 (next problem in
     curriculum — different technique, DP/LCS based, since
     SUBSEQUENCE doesn't need contiguous characters)

  Next time intaha problem bandre naanu modalu idannu think maadtene:
  → "Palindromic substrings COUNT madbekagidre → expand around
     center, but TRACK widest bittu, EVERY successful expansion
     ge count += 1 madu — same mechanism, different goal!"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 11 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "Count every contiguous substring that's a palindrome —
      overlapping and repeated-text substrings all count
      separately by position."

  2. Brute force:
     "Check every substring for palindrome-ness by reversing and
      comparing. O(n^3) — too slow for n=1000."

  3. Optimize:
     "Same expand-around-center idea as Longest Palindromic
      Substring: try all 2n-1 centers, expand while characters
      match. Instead of tracking the widest window, increment a
      counter on every successful match — each one is a distinct
      palindromic substring."

  4. Code:
     "A helper expand(left, right) that grows while s[left] ==
      s[right], incrementing count each time. Call it twice per
      index — once odd, once even."

  5. Complexity:
     "Time O(n^2) — 2n-1 centers, each expansion up to O(n).
      Space O(1) — just a counter."

  Mukhya: same expand-around-center mechanism as #13 — the ONLY
          difference is what you DO with each successful match:
          track the widest, or count every one!
"""


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(n^3) Time | O(n) Space (check every substring)
# ═══════════════════════════════════════════════════════════════════
def count_palindromic_substrings_brute(s):
    """
    Idu modala aaloochane — prati substring generate madi,
    reverse == original antha check madi count madu
    """
    n = len(s)
    count = 0

    for i in range(n):
        for j in range(i, n):
            candidate = s[i:j + 1]
            if candidate == candidate[::-1]:
                count += 1

    return count


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n^2) Time | O(1) Space (expand around center, counting)
# ═══════════════════════════════════════════════════════════════════
def count_palindromic_substrings(s):
    """
    Idu final answer — prati index na odd/even center aagi try
    madi, ella successful expansion ge count += 1 madu
    """
    n = len(s)
    count = 0

    def expand(left, right):
        nonlocal count
        while left >= 0 and right < n and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1

    for i in range(n):
        expand(i, i)          # odd-length palindromes
        expand(i, i + 1)      # even-length palindromes

    return count


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # Test 1 — Basic (no palindromes beyond single chars)
    assert count_palindromic_substrings("abc") == 3

    # Test 2 — All same character
    assert count_palindromic_substrings("aaa") == 6

    # Test 3 — Whole string palindrome
    assert count_palindromic_substrings("aba") == 4

    # Test 4 — Single character
    assert count_palindromic_substrings("a") == 1

    # Test 5 — Two identical adjacent characters
    assert count_palindromic_substrings("aa") == 3

    # Cross-check: brute force must agree on all of the above
    assert count_palindromic_substrings_brute("abc") == 3
    assert count_palindromic_substrings_brute("aaa") == 6
    assert count_palindromic_substrings_brute("aba") == 4
    assert count_palindromic_substrings_brute("a") == 1
    assert count_palindromic_substrings_brute("aa") == 3

    print("All tests passed!")
