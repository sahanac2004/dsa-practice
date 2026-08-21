"""
╔════════════════════════════════════════════════════════════════════╗
║  LONGEST PALINDROMIC SUBSTRING                                     ║
║  LeetCode #5  |  Difficulty: Medium  |  Topic: Strings/Two Pointers║
║  Link: https://leetcode.com/problems/longest-palindromic-substring/║
╚════════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Given a string `s`, return the LONGEST substring of `s` that
  is also a palindrome (reads the same forwards and backwards).
  If more than one substring achieves the maximum length, any of
  them is acceptable.

  Input : s = a string
  Output: string — the longest palindromic substring found

  Example 1 — basic:
    Input : s = "babad"
    Output: "bab" (or "aba" — both length 3, both valid)
    Why?  : "bab" reads the same both ways; no longer
            palindromic substring exists in "babad"

  Example 2 — slightly tricky (even-length palindrome):
    Input : s = "cbbd"
    Output: "bb"
    Why?  : "bb" is a palindrome of even length — palindromes
            can be centered BETWEEN two characters, not just ON
            one character

  Example 3 — whole string is the answer:
    Input : s = "racecar"
    Output: "racecar"
    Why?  : the entire string itself already reads the same
            forwards and backwards

  Constraints:
    - 1 <= s.length <= 1000
    - s consists of digits and English letters

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Problem odi aada mele namma brain enu think maadabeeku:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  ಒಂದು string s                   │
  │  Output ಏನು ಬೇಕು?     →  ಅದರ ಒಳಗಿನ ಅತಿ ಉದ್ದ palindrome  │
  │                           substring                       │
  │  Constraints ಏನಿದೆ?   →  palindrome ODD length (single    │
  │                           center) ಅಥವಾ EVEN length (two   │
  │                           center chars) ಎರಡೂ ಆಗಿರಬಹುದು   │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ಮೊದಲ simple idea ಏನು?
  →  ಎಲ್ಲಾ possible substrings generate ಮಾಡಿ, ಪ್ರತಿಯೊಂದೂ
     palindrome ಆಗಿದ್ಯಾ ಚೆಕ್ ಮಾಡಿ (reverse ಮಾಡಿ compare ಮಾಡಿ),
     ಉದ್ದ ಇರೋದನ್ನ track ಮಾಡಿ

  ಹಂತ 3 — Palindrome ಬಗ್ಗೆ ಒಂದು key observation ಏನಿದೆ?
  →  "ಪ್ರತಿ palindrome ಗೂ ಒಂದು CENTER ಇರುತ್ತೆ" ಅಂತ ಗಮನಿಸಿ
  →  Odd length palindrome ಗೆ, center ಒಂದೇ character
     ("aba" ಗೆ center 'b')
  →  Even length palindrome ಗೆ, center ಎರಡು characters ನಡುವೆ
     ("abba" ಗೆ center 'b' ಮತ್ತು 'b' ನಡುವೆ)
  →  "center ಇಂದ ಎರಡೂ ಕಡೆ EXPAND ಮಾಡಿದ್ರೆ, characters match
      ಆಗ್ತಾ ಇರೋವರೆಗೆ palindrome ಬೆಳಿತಾ ಹೋಗುತ್ತೆ!" ಅಂತ ಯೋಚಿಸಿ

  ಹಂತ 4 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  ಪ್ರತಿ index ಅನ್ನ ಒಂದು POSSIBLE center ಆಗಿ ಪರಿಗಣಿಸಿ (odd
     ಗೆ ಒಂದು index, even ಗೆ ಎರಡು adjacent indices), ಎಡ ಮತ್ತು
     ಬಲ pointer ಗಳನ್ನ ಹೊರಗಡೆ ಸರಿಸ್ತಾ ಹೋಗಿ
  →  Characters match ಆಗ್ತಾ ಇರೋವರೆಗೆ ಮಾತ್ರ ಸರಿಸಿ — mismatch
     ಸಿಕ್ಕ ತಕ್ಷಣ ಆ center ಗೆ ಆ palindrome ಮುಗಿತು ಅಂತ ಗೊತ್ತಾಗುತ್ತೆ
  →  2n-1 ಸಾಧ್ಯ centers (n odd + n-1 even) ಗೆ ಇದೇ ಮಾಡಿದ್ರೆ,
     ಎಲ್ಲಾ palindromes cover ಆಗುತ್ತೆ

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು:
  →  "Every palindrome has a center — either a single character
      (odd length) or a gap between two characters (even length)"
  →  "For each of the 2n-1 possible centers, expand outward with
      two pointers while characters match"
  →  "Track the widest expansion seen across all centers — that
      gives the longest palindromic substring"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Expand Around Center (two pointers per center)
  Secondary : Brute-force substring generation + palindrome check

  WHY Expand Around Center?
  → It exploits the STRUCTURE of a palindrome directly (it must
    be symmetric around some center) instead of blindly checking
    every substring — we only ever expand from valid centers,
    never wasting work on substrings that couldn't be palindromes
    in the first place.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  The key insight: EVERY palindrome is defined by its center —
  you can't have a palindrome without one. Instead of asking
  "is this substring a palindrome?" for every possible substring
  (most of which aren't even close), we flip the question to
  "starting from this center, how FAR can I expand while staying
  a palindrome?" There are only 2n-1 possible centers (n single-
  character centers for odd length, n-1 between-character
  centers for even length), and expanding each one directly
  finds the answer.

  The journey from brute to optimal:
    Brute thought   →  Generate every substring, reverse it and
                       compare to check if it's a palindrome,
                       track the longest one found
    Problem with it →  O(n^2) substrings, each palindrome check
                       costs O(n) → O(n^3) total, way too slow
    Better question →  "Can I use the SYMMETRY of a palindrome
                       to avoid checking substrings that can't
                       possibly be one?"
    Insight         →  Expand outward from every possible center;
                       a mismatch means STOP — no need to check
                       anything beyond that point for this center
    Optimal         →  2n-1 centers, each expansion up to O(n),
                       O(n^2) total, O(1) extra space

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE (check every substring)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Generate every substring s[i:j+1] for all i ≤ j. For each
    one, check if it equals its own reverse (a palindrome check).
    Track the longest one found so far.

  Pseudocode:
    step 1: best = ""
    step 2: for i in range(n):
    step 3:   for j in range(i, n):
    step 4:     candidate = s[i:j+1]
    step 5:     if candidate == candidate[::-1] and len(candidate) > len(best):
    step 6:       best = candidate
    step 7: return best

  Time  : O(n^3)  →  Why: O(n^2) substrings, each palindrome
                          check (reverse + compare) costs O(n)
  Space : O(n)     →  Why: each candidate slice is a new string
                          copy up to length n

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ?
    → Correct, but cubic time — for n = 1000 this is far too
      slow. Checking substrings that COULDN'T possibly be
      palindromes (mismatched first/last chars) wastes huge
      amounts of work.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 6 — APPROACH 2 — OPTIMAL (Expand Around Center)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    For every index `i`, try TWO centers: the single character
    at `i` (for odd-length palindromes) and the gap between `i`
    and `i+1` (for even-length palindromes). From each center,
    expand two pointers outward while the characters on both
    sides match. Track the widest expansion seen across all
    centers.

  Key steps:
    1. def expand(left, right):
    2.   while left >= 0 and right < n and s[left] == s[right]:
    3.     left -= 1; right += 1
    4.   return left + 1, right - 1   # bounds of the palindrome
    5. start, end = 0, 0
    6. for i in range(n):
    7.   l1, r1 = expand(i, i)         # odd-length center
    8.   l2, r2 = expand(i, i + 1)     # even-length center
    9.   update (start, end) with whichever is widest
    10. return s[start:end+1]

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ:
    → "ಪ್ರತಿ index i ಗೆ ಎರಡು centers try ಮಾಡು: (i,i) — odd
       length ಗೆ, (i,i+1) — even length ಗೆ. ಪ್ರತಿ center ಇಂದ
       ಎಡ-ಬಲ pointers ಹೊರಗಡೆ ಸರಿಸ್ತಾ ಹೋಗು, characters match
       ಆಗ್ತಾ ಇರೋವರೆಗೆ. ಎಲ್ಲಾ centers ಗೂ try ಮಾಡಿ, ಅತಿ ಉದ್ದ
       ಸಿಕ್ಕಿದ್ದನ್ನ track ಮಾಡು!"

  Time  : O(n^2)  →  Why: 2n-1 centers, each expansion can go
                          up to O(n) in the worst case (e.g. all
                          same character)
  Space : O(1)     →  Why: only a few pointers/indices tracked
                          (excluding the final output slice)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 7 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: s = "babad"

  i=0 'b': odd expand(0,0) → "b" (length 1)
           even expand(0,1) → 'b'≠'a', invalid
  i=1 'a': odd expand(1,1) → grows: s[0]='b'==s[2]='b' → "bab"
           (length 3) ← new best!
           even expand(1,2) → 'a'≠'b', invalid
  i=2 'b': odd expand(2,2) → grows: s[1]='a'==s[3]='a' → "aba"
           (length 3, ties current best — kept as "bab" since
           we only replace on STRICTLY longer)
           even expand(2,3) → 'b'≠'a', invalid
  i=3 'a': odd expand(3,3) → s[2]='b'≠s[4]='d' → "a" (length 1)
           even expand(3,4) → 'a'≠'d', invalid
  i=4 'd': odd expand(4,4) → "d" (length 1)
           even expand(4,5) → out of bounds, invalid

  Best found: "bab" (start=0, end=2)

  Output: "bab" ✓ (a valid answer — "aba" is equally valid)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 8 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ Single character "a"?          →  "a" — trivially itself
  ✓ Even-length palindrome "cbbd"? →  "bb" — must try
                                       between-character centers
  ✓ Whole string palindrome
    "racecar"?                     →  "racecar" itself
  ✓ No repeated characters "abcd"? →  any single character —
                                       length-1 palindromes only
  ✓ All same character "aaaa"?     →  "aaaa" — expands fully
                                       from any center

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 9 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                          Time    Space
  Brute (all substrings)  O(n^3)  O(n)
  Optimal (expand-center) O(n^2)  O(1)   ← use this ✅

  Time yaake O(n^2)?  → 2n-1 centers, each expansion bounded by
                         string length in the worst case
  Space yaake O(1)?   → Just pointers/indices; no extra data
                         structures beyond the final answer slice

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 10 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Expand Around Center

  Ee pattern yaavaaga use maadabeeku?
  → Palindrome-related problems where you need to FIND or COUNT
     palindromic substrings — exploit the center-symmetry
     instead of checking arbitrary substrings
  → Remember: always try BOTH odd-length (single center) and
     even-length (between-two-chars center) cases

  Idee pattern beere problemsalli kaanisatte:
  → Palindromic Substrings #647 (next problem in the hard
     section — count ALL palindromic substrings, same expand
     technique, just count instead of track longest)
  → Sum of Beauty of All Substrings #1781 (next problem in
     curriculum — different technique, frequency-based)

  Next time intaha problem bandre naanu modalu idannu think maadtene:
  → "Palindrome substring bekagidre → expand around center try
     maadu! Odd AND even length centers, eradu try maadbeku
     mareyabeda — mismatch sikkidkoodle andina center ge stop
     madu."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 11 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "Find the longest substring that reads the same forwards
      and backwards — any tied-length answer is acceptable."

  2. Brute force:
     "Check every substring for the palindrome property by
      reversing and comparing. O(n^3) — too slow for n=1000."

  3. Optimize:
     "Every palindrome has a center. For each of the 2n-1
      possible centers (single char for odd length, between two
      chars for even length), expand two pointers outward while
      characters match. Track the widest result."

  4. Code:
     "A helper expand(left, right) that grows while s[left] ==
      s[right], returning the final valid bounds. Call it twice
      per index — once for odd, once for even — and keep the
      best (start, end) pair."

  5. Complexity:
     "Time O(n^2) — 2n-1 centers, each expansion up to O(n).
      Space O(1) extra, beyond the returned substring."

  Mukhya: palindrome = symmetry around a center — exploit that
          structure directly instead of blind substring checking!
"""


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(n^3) Time | O(n) Space (check every substring)
# ═══════════════════════════════════════════════════════════════════
def longest_palindrome_brute(s):
    """
    Idu modala aaloochane — prati substring generate madi,
    reverse == original antha check madi longest track madu
    """
    n = len(s)
    best = ""

    for i in range(n):
        for j in range(i, n):
            candidate = s[i:j + 1]
            if candidate == candidate[::-1] and len(candidate) > len(best):
                best = candidate

    return best


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n^2) Time | O(1) Space (expand around center)
# ═══════════════════════════════════════════════════════════════════
def longest_palindrome(s):
    """
    Idu final answer — prati index na odd/even center aagi try
    madi, characters match aaguva tanaka expand madu
    """
    if not s:
        return ""

    n = len(s)

    def expand(left, right):
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1

    start, end = 0, 0

    for i in range(n):
        l1, r1 = expand(i, i)          # odd-length palindrome
        if r1 - l1 > end - start:
            start, end = l1, r1

        l2, r2 = expand(i, i + 1)      # even-length palindrome
        if r2 - l2 > end - start:
            start, end = l2, r2

    return s[start:end + 1]


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
def _is_palindrome(candidate):
    return candidate == candidate[::-1]


def _is_valid_longest_palindrome(original, candidate, expected_length):
    return (
        len(candidate) == expected_length
        and _is_palindrome(candidate)
        and candidate in original
    )


if __name__ == "__main__":
    # Test 1 — Basic (odd-length answer)
    assert _is_valid_longest_palindrome("babad", longest_palindrome("babad"), 3)

    # Test 2 — Even-length palindrome
    assert longest_palindrome("cbbd") == "bb"

    # Test 3 — Whole string is the palindrome
    assert longest_palindrome("racecar") == "racecar"

    # Test 4 — Single character
    assert longest_palindrome("a") == "a"

    # Test 5 — All same character
    assert longest_palindrome("aaaa") == "aaaa"

    # Cross-check: brute force must also produce valid (possibly
    # differently-tied) longest palindromes
    assert _is_valid_longest_palindrome("babad", longest_palindrome_brute("babad"), 3)
    assert longest_palindrome_brute("cbbd") == "bb"
    assert longest_palindrome_brute("racecar") == "racecar"
    assert longest_palindrome_brute("a") == "a"
    assert longest_palindrome_brute("aaaa") == "aaaa"

    print("All tests passed!")
