"""
╔════════════════════════════════════════════════════════════════════╗
║  FIND THE INDEX OF THE FIRST OCCURRENCE IN A STRING (strStr)       ║
║  LeetCode #28  |  Difficulty: Easy/Hard (as KMP)  |  Topic: KMP    ║
║  Link: https://leetcode.com/problems/                              ║
║        find-the-index-of-the-first-occurrence-in-a-string/         ║
╚════════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Given two strings `haystack` and `needle`, return the index of
  the FIRST occurrence of `needle` in `haystack`, or -1 if
  `needle` does not occur in `haystack` at all.

  Input : haystack, needle = two strings
  Output: integer — index of the first match, or -1

  Example 1 — basic:
    Input : haystack = "sadbutsad", needle = "sad"
    Output: 0
    Why?  : "sad" appears starting at index 0 (and again at
            index 6, but we only want the FIRST occurrence)

  Example 2 — slightly tricky (near-match that fails):
    Input : haystack = "leetcode", needle = "leeto"
    Output: -1
    Why?  : "leetcode" starts matching "leeto" for 4 characters
            ("leet") but then 'c' ≠ 'o' — no full match anywhere

  Example 3 — needle at the very end:
    Input : haystack = "hello", needle = "llo"
    Output: 2
    Why?  : "llo" matches the last three characters of "hello"

  Constraints:
    - 1 <= haystack.length, needle.length <= 10^4
    - haystack and needle consist of only lowercase English
      characters

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Problem odi aada mele namma brain enu think maadabeeku:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  haystack, needle ಎರಡು strings   │
  │  Output ಏನು ಬೇಕು?     →  needle ಮೊದಲ ಸಲ ಎಲ್ಲಿ ಸಿಗುತ್ತೋ    │
  │                           ಆ index (ಇಲ್ಲಾಂದ್ರೆ -1)          │
  │  Constraints ಏನಿದೆ?   →  FIRST occurrence ಮಾತ್ರ ಬೇಕು      │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ಇದನ್ನ previous problems (#16 #17 KMP LPS, #19
           Z-function) ಜೊತೆ connect ಮಾಡಿ ನೋಡಿ!
  →  ಅಲ್ಲಿ ನಾವು LPS array / Z-array ಅನ್ನ "prefix-suffix
     analysis" ಗೆ ಬಳಸಿದ್ವಿ
  →  ಇಲ್ಲಿ ಅದೇ LPS array ಅನ್ನ ಅದರ ORIGINAL purpose ಗೆ ಬಳಸ್ತೀವಿ
     — actual PATTERN SEARCHING (mismatch ಆದಾಗ ಎಷ್ಟು back
     ಹೋಗಬೇಕು ಅಂತ ಗೊತ್ತಾಗುತ್ತೆ, restart ಮಾಡೋ ಅಗತ್ಯ ಇಲ್ಲ!)

  ಹಂತ 3 — ಮೊದಲ simple idea ಏನು?
  →  haystack ರ ಪ್ರತಿ starting position ಇಂದ needle ಜೊತೆ
     character-by-character compare ಮಾಡಿ, ಮೊದಲ ಪೂರ್ತಿ match
     ಸಿಕ್ಕ position return ಮಾಡಿ

  ಹಂತ 4 — KMP ಇಲ್ಲಿ ಹೇಗೆ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  Mismatch ಆದಾಗ, brute force ಆಗಿದ್ರೆ ಪೂರ್ತಿ needle ಅನ್ನ
     ಒಂದು position ಮುಂದಕ್ಕೆ ಸರಿಸಿ ಮತ್ತೆ ಶುರುವಿಂದ compare
     ಮಾಡ್ತೀವಿ — ಈಗಾಗಲೇ match ಆದ characters ರ information
     WASTE ಆಗುತ್ತೆ!
  →  "needle ರ LPS array ಬಳಸಿದ್ರೆ, mismatch ಆದಾಗ needle
      pointer ಅನ್ನ EXACTLY ಎಲ್ಲಿಗೆ ಹಿಂದಕ್ಕೆ ಸರಿಸಬೇಕು ಅಂತ
      ಗೊತ್ತಾಗುತ್ತೆ — haystack pointer ಮಾತ್ರ ಯಾವಾಗಲೂ ಮುಂದಕ್ಕೆ
      ಹೋಗುತ್ತೆ, ಹಿಂದಕ್ಕೆ ಹೋಗೋದೇ ಇಲ್ಲ!" ಅಂತ ಗಮನಿಸಿ

  ಹಂತ 5 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  haystack pointer i ಎಂದಿಗೂ back ಹೋಗಲ್ಲ — ಇದೇ O(n) guarantee
     ಕೊಡುತ್ತೆ (n = haystack length)
  →  needle pointer j ಮಾತ್ರ mismatch ಆದಾಗ lps[j-1] ಗೆ ಜಂಪ್
     ಆಗುತ್ತೆ — ಇದೂ ಕೂಡ total O(m) ಗಿಂತ ಜಾಸ್ತಿ ಜಂಪ್ ಮಾಡಲ್ಲ

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು:
  →  "First build the LPS array of needle — same preprocessing
      as before"
  →  "Then scan haystack with two pointers: on a match, advance
      both; on a mismatch, use the LPS array to jump the needle
      pointer back intelligently, WITHOUT ever moving the
      haystack pointer backward"
  →  "This guarantees O(n + m) instead of the O(n*m) brute force"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : KMP Algorithm — LPS array + two-pointer scan
  Secondary : Brute-force sliding comparison

  WHY KMP's two-pointer scan (not just the LPS array alone)?
  → The LPS array by itself (as in #16/#17) only analyzes ONE
    string's internal structure. Here we use it DURING a live
    scan of a second string (haystack) to decide how far to roll
    back the needle pointer on a mismatch — this is the actual
    matching phase the LPS array was designed to support.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  The key insight: when a mismatch happens after some partial
  match of length `j`, we already KNOW those `j` matched
  characters — throwing that information away (like brute force
  does, by restarting from the very next haystack position) is
  wasteful. The needle's own LPS array tells us the longest
  prefix of needle that's also a suffix of what we just matched
  — we can resume comparing from THERE instead of from scratch,
  and the haystack pointer never needs to move backward.

  The journey from brute to optimal:
    Brute thought   →  For each position in haystack, compare
                       needle character by character from scratch
    Problem with it →  On a partial-match-then-mismatch, all the
                       matched characters' information is
                       discarded — O(n*m) worst case
    Better question →  "Can needle's own internal structure tell
                       me how far back to roll on a mismatch,
                       without ever un-advancing the haystack
                       pointer?"
    Insight         →  That's exactly what needle's LPS array
                       encodes — reuse it during the scan
    Optimal         →  O(n+m): O(m) to build LPS, O(n) to scan
                       haystack (haystack pointer never regresses)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE (sliding comparison)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Try every starting position in haystack; at each one,
    compare needle character by character. Return the first
    position where the full needle matches.

  Pseudocode:
    step 1: for i in range(len(haystack) - len(needle) + 1):
    step 2:   if haystack[i:i+len(needle)] == needle:
    step 3:     return i
    step 4: return -1

  Time  : O(n*m)  →  Why: up to n-m+1 starting positions, each
                          comparison costs O(m) in the worst case
  Space : O(m)     →  Why: each slice comparison copies up to m
                          characters

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ?
    → Correct, but degrades badly on adversarial inputs (e.g.
      haystack of repeated near-matches) — O(n*m) worst case.
      KMP guarantees O(n+m) regardless of input structure.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 6 — APPROACH 2 — OPTIMAL (KMP Algorithm)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Precompute needle's LPS array. Scan haystack with pointer
    `i` and needle with pointer `j`. On a character match,
    advance both. On a full needle match (j reaches needle's
    length), return the starting index. On a mismatch, jump `j`
    back using lps[j-1] (or reset to 0 and advance `i` if j is
    already 0) — `i` NEVER moves backward.

  Key steps:
    1. lps = compute_lps(needle)
    2. i = j = 0
    3. while i < len(haystack):
    4.   if haystack[i] == needle[j]:
    5.     i += 1; j += 1
    6.     if j == len(needle): return i - j
    7.   elif j != 0:
    8.     j = lps[j - 1]
    9.   else:
    10.    i += 1
    11. return -1

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ:
    → "needle ರ LPS array compute ಮಾಡು. haystack ಗೆ i pointer,
       needle ಗೆ j pointer ಇಟ್ಕೊಳ್ಳಿ. match ಆದ್ರೆ ಎರಡೂ ಮುಂದಕ್ಕೆ
       ಸರಿಸು. j needle length ತಲುಪಿದ್ರೆ, match ಸಿಕ್ಕಿತು —
       return ಮಾಡು. mismatch ಆದ್ರೆ, j ಅನ್ನ lps[j-1] ಗೆ ಜಂಪ್
       ಮಾಡು (j=0 ಆಗಿದ್ರೆ ಬರೀ i ಮುಂದಕ್ಕೆ ಸರಿಸು) — i ಎಂದಿಗೂ
       ಹಿಂದಕ್ಕೆ ಹೋಗಲ್ಲ!"

  Time  : O(n + m)  →  Why: O(m) to build LPS, O(n) to scan —
                            haystack pointer i strictly
                            non-decreasing throughout
  Space : O(m)       →  Why: LPS array sized to needle's length

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 7 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: haystack = "sadbutsad", needle = "sad"

  LPS of "sad" = [0, 0, 0]  (no internal repeats)

  i  j  haystack[i]  needle[j]  action
  0  0  's'          's'        match → i=1, j=1
  1  1  'a'          'a'        match → i=2, j=2
  2  2  'd'          'd'        match → i=3, j=3 → j==len(needle)!
                                 return i-j = 3-3 = 0

  Output: 0 ✓

  ಇನ್ನೊಂದು example — near-match that fails:
  Input: haystack = "leetcode", needle = "leeto"

  LPS of "leeto" = [0, 0, 1, 0, 0]

  i=0..3: 'l','e','e','t' all match needle[0..3] → i=4, j=4
  i=4: haystack[4]='c', needle[4]='o' → MISMATCH
       j=4 != 0 → j = lps[3] = 0
  i=4: haystack[4]='c', needle[0]='l' → MISMATCH, j==0 → i=5
  ... continues scanning, no further match found anywhere

  Output: -1 ✓

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 8 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ needle at index 0?             →  0 — first char already matches
  ✓ needle at the very end?        →  hello/llo → 2
  ✓ needle == haystack?            →  0 — full match immediately
  ✓ needle not found at all?       →  -1
  ✓ needle appears multiple times
    ("sadbutsad","sad")?           →  0 — only the FIRST index

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 9 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                          Time    Space
  Brute (sliding compare) O(n*m)  O(m)
  Optimal (KMP)            O(n+m)  O(m)   ← use this ✅

  Time yaake O(n+m)?  → O(m) to preprocess needle's LPS array,
                         O(n) for the scan since haystack pointer
                         `i` only ever moves forward
  Space yaake O(m)?   → LPS array sized to needle's length only

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 10 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: KMP Algorithm (LPS-guided two-pointer scan)

  Ee pattern yaavaaga use maadabeeku?
  → CLASSIC pattern-matching/substring-search problems where
     O(n*m) brute force is too slow — the LPS array (built from
     #16/#17's technique) now used for its ORIGINAL purpose:
     guiding a live scan without ever backtracking the main
     pointer
  → Any "find occurrence(s) of pattern in text" family problem

  Idee pattern beere problemsalli kaanisatte:
  → Z-Function / Pattern Matching (previous problem — SAME goal,
     different mechanism: Z-array instead of LPS array + resync)
  → Minimum Insertions to Make String Palindrome #1312 (next
     problem in curriculum — different technique, DP/LCS based)
  → Repeated String Match / Shortest Palindrome #214 (KMP/LPS
     reused again in different framings)

  Next time intaha problem bandre naanu modalu idannu think maadtene:
  → "Pattern search bekagidre → KMP try maadu! needle ge LPS
     array build madi, haystack scan maadtha j mismatch aadre
     lps array bhalasi jump madu — main pointer i eskoo hindakke
     hogadu!"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 11 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "Find the first index where needle occurs as a substring of
      haystack, or -1 if it never occurs."

  2. Brute force:
     "Slide needle across every position in haystack, comparing
      character by character. O(n*m) worst case."

  3. Optimize:
     "Precompute needle's LPS array. Scan with two pointers —
      one for haystack (never moves backward), one for needle.
      On mismatch, use the LPS array to jump the needle pointer
      to the right resume point instead of restarting from
      scratch."

  4. Code:
     "Standard LPS builder on needle. Two-pointer scan: match →
      advance both; full match → return start index; mismatch →
      j = lps[j-1] if j>0 else i += 1."

  5. Complexity:
     "Time O(n+m) — LPS build plus a single scan where the
      haystack pointer never regresses. Space O(m) for LPS."

  Mukhya: KMP's real power is 'the main pointer never goes
          backward' — the LPS array does all the smart
          bookkeeping so we never redo already-verified work!
"""


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(n*m) Time | O(m) Space (sliding comparison)
# ═══════════════════════════════════════════════════════════════════
def str_str_brute(haystack, needle):
    """
    Idu modala aaloochane — haystack ra prati position inda
    needle jothe direct compare madu
    """
    n, m = len(haystack), len(needle)

    for i in range(n - m + 1):
        if haystack[i:i + m] == needle:
            return i

    return -1


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n + m) Time | O(m) Space (KMP Algorithm)
# ═══════════════════════════════════════════════════════════════════
def _compute_lps(pattern):
    """Standard KMP preprocessing — longest proper prefix that's also a suffix."""
    m = len(pattern)
    lps = [0] * m
    length = 0
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        elif length != 0:
            length = lps[length - 1]
        else:
            lps[i] = 0
            i += 1

    return lps


def str_str(haystack, needle):
    """
    Idu final answer — needle ge LPS array build madi, haystack
    scan madtha mismatch aadre LPS bhalasi jump madu (i eskoo
    hindakke hogadu)
    """
    n, m = len(haystack), len(needle)
    if m == 0:
        return 0

    lps = _compute_lps(needle)
    i = j = 0

    while i < n:
        if haystack[i] == needle[j]:
            i += 1
            j += 1
            if j == m:
                return i - j
        elif j != 0:
            j = lps[j - 1]
        else:
            i += 1

    return -1


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # Test 1 — Basic
    assert str_str("sadbutsad", "sad") == 0

    # Test 2 — Near-match that ultimately fails
    assert str_str("leetcode", "leeto") == -1

    # Test 3 — Needle at the very end
    assert str_str("hello", "llo") == 2

    # Test 4 — Needle equals haystack
    assert str_str("abc", "abc") == 0

    # Test 5 — Needle repeats internally (tests LPS jump)
    assert str_str("aaaaab", "aaab") == 2

    # Cross-check: brute force must agree on all of the above
    assert str_str_brute("sadbutsad", "sad") == 0
    assert str_str_brute("leetcode", "leeto") == -1
    assert str_str_brute("hello", "llo") == 2
    assert str_str_brute("abc", "abc") == 0
    assert str_str_brute("aaaaab", "aaab") == 2

    print("All tests passed!")
