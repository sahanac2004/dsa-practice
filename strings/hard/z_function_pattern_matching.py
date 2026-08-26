"""
╔════════════════════════════════════════════════════════════════════╗
║  Z-FUNCTION / PATTERN MATCHING                                     ║
║  Classic Algorithm  |  Difficulty: Hard  |  Topic: Z-Algorithm     ║
║  Link: https://cp-algorithms.com/string/z-function.html            ║
╚════════════════════════════════════════════════════════════════════╝

  NOTE: The curriculum sheet lists this as slot #19 with no
  LeetCode number ("—"). It's the classic Z-function algorithm —
  the general-purpose sibling of KMP for pattern matching. This
  file implements the standard "find all occurrences of `pattern`
  in `text`" application.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Given a `text` and a `pattern`, find EVERY starting index in
  `text` where `pattern` occurs as a contiguous substring.

  The Z-FUNCTION of a string `s` is an array `z` where `z[i]` is
  the length of the longest substring starting at `s[i]` that
  matches a PREFIX of `s` (z[0] is conventionally left as 0/unused).

  Input : text, pattern = two strings
  Output: list of integers — all starting indices in `text`
          where `pattern` occurs

  Example 1 — basic (multiple occurrences):
    Input : text = "ababcababcabc", pattern = "abc"
    Output: [2, 7, 10]
    Why?  : "abc" appears starting at index 2 ("...abc..."),
            again at index 7, and again at index 10

  Example 2 — slightly tricky (overlapping potential matches):
    Input : text = "aaaa", pattern = "aa"
    Output: [0, 1, 2]
    Why?  : "aa" occurs starting at every index except the last
            possible one being out of range — occurrences CAN
            overlap

  Example 3 — no match at all:
    Input : text = "hello", pattern = "world"
    Output: []
    Why?  : "world" never appears as a substring of "hello"

  Constraints (typical competitive-programming bounds):
    - 1 <= len(pattern) <= len(text) <= 10^5
    - strings consist of lowercase English letters

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Problem odi aada mele namma brain enu think maadabeeku:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  text, pattern ಎರಡು strings      │
  │  Output ಏನು ಬೇಕು?     →  pattern ಎಲ್ಲಿ ಎಲ್ಲಿ text ಒಳಗೆ    │
  │                           ಸಿಗುತ್ತೋ ಆ starting indices     │
  │  Constraints ಏನಿದೆ?   →  matches OVERLAP ಆಗಬಹುದು          │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ಮೊದಲ simple idea ಏನು?
  →  text ರ ಪ್ರತಿ starting position ಇಂದ, pattern ಜೊತೆ
     character-by-character compare ಮಾಡಿ, ಪೂರ್ತಿ match
     ಆಯ್ತಾ ಚೆಕ್ ಮಾಡಿ

  ಹಂತ 3 — Z-function ಅಂದ್ರೆ ಏನು?
  →  ಒಂದು string s ಗೆ Z[i] ಅಂದ್ರೆ, "s[i] ಇಂದ ಶುರುವಾಗೋ
      substring, s ರ PREFIX ಜೊತೆ ಎಷ್ಟು characters match
      ಆಗುತ್ತೆ" ಅಂತ
  →  "pattern + separator + text" ಅಂತ combined string build
     ಮಾಡಿದ್ರೆ, text portion ನ ಪ್ರತಿ position ಗೂ Z value
     compute ಮಾಡಬಹುದು
  →  Z value == pattern ರ length ಆಗಿದ್ರೆ, ಆ position ನಲ್ಲಿ
     pattern ಪೂರ್ತಿ match ಆಗಿದೆ ಅಂತ ಅರ್ಥ!

  ಹಂತ 4 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  Z-array computation ಸ್ವತಃ O(n) — ಪ್ರತಿ position ಗೂ
     separately match check ಮಾಡೋ ಬದಲು, ಈಗಾಗಲೇ compute ಆದ
     [l, r] window (Z-box) ಬಳಸಿ, ಹೊಸ position ಗೆ ಎಷ್ಟು match
     ಆಗಿ ಇರುತ್ತೆ ಅಂತ REUSE ಮಾಡುತ್ತೆ (mismatch ಸಿಗೋವರೆಗೆ ಮಾತ್ರ
     extra check ಮಾಡುತ್ತೆ)
  →  separator character (pattern ಅಥವಾ text ನಲ್ಲಿ ಇಲ್ಲದ char)
     match ಎರಡು ಭಾಗಗಳ ನಡುವೆ cross ಆಗದ ಹಾಗೆ ತಡೆಯುತ್ತೆ

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು:
  →  "Concatenate pattern + sentinel + text, so the sentinel
      stops any match from crossing between the two halves"
  →  "Compute the Z-array of this combined string — any position
      in the text portion with Z value equal to pattern length
      is a full match"
  →  "The Z-array itself is built in O(n) using a sliding [l, r]
      window that avoids re-comparing already-matched characters"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Z-Algorithm (Z-function on pattern + sentinel + text)
  Secondary : Brute-force sliding comparison

  WHY the Z-Algorithm?
  → It computes, for EVERY position in one linear pass, "how
    much does the string starting here match the string's own
    prefix." By putting the pattern first, every position in the
    text becomes a candidate match check against that prefix —
    all in O(n + m) instead of checking each position separately.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  The key insight: if we place `pattern` at the very front of a
  combined string, then Z[i] for any position `i` tells us
  exactly how many characters starting there match the pattern.
  A full match happens exactly when Z[i] equals the pattern's
  length. The Z-array itself avoids redundant comparisons by
  tracking a window [l, r] — the rightmost matched-prefix segment
  found so far — and reusing that information for positions
  still inside it.

  The journey from brute to optimal:
    Brute thought   →  For each starting index in text, compare
                       character by character against pattern
    Problem with it →  Worst case (e.g. text="aaaa...a",
                       pattern="aaa...ab") re-does almost the
                       same comparisons at every shifted start
                       → O(n*m)
    Better question →  "Can I reuse work from a previous
                       position's match instead of starting
                       fresh every time?"
    Insight         →  Track the furthest-reaching prefix-match
                       window found so far; positions inside it
                       can reuse already-known Z values
    Optimal         →  Z-array computed in O(n) over the
                       combined string

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE (sliding comparison)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Slide the pattern across every valid starting position in
    the text and directly compare characters.

  Pseudocode:
    step 1: results = []
    step 2: for i in range(len(text) - len(pattern) + 1):
    step 3:   if text[i:i+len(pattern)] == pattern:
    step 4:     results.append(i)
    step 5: return results

  Time  : O(n*m)  →  Why: up to n-m+1 starting positions, each
                          comparison costs O(m) in the worst case
  Space : O(m)     →  Why: each slice comparison copies up to m
                          characters

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ?
    → Correct, but degrades to O(n*m) on adversarial inputs
      (e.g. many near-matches) — for n,m up to 10^5 this is far
      too slow. Z-function reuses previous comparisons instead.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 6 — APPROACH 2 — OPTIMAL (Z-Algorithm)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Build `combined = pattern + '$' + text` (the '$' sentinel
    must not appear in either string, preventing a match from
    crossing the boundary). Compute the Z-array of `combined`.
    Any index `i` in the text portion where `z[i] == len(pattern)`
    marks a full match starting at `i - len(pattern) - 1` in the
    original text.

  Key steps:
    1. combined = pattern + '$' + text
    2. z = compute_z_array(combined)   # O(n) sliding window
    3. for i in range(len(pattern) + 1, len(combined)):
    4.   if z[i] == len(pattern):
    5.     record match at i - len(pattern) - 1
    6. return matches

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ:
    → "pattern + '$' + text ಅಂತ combined string build ಮಾಡು.
       ಇದಕ್ಕೆ Z-array compute ಮಾಡು. text portion ನಲ್ಲಿ ಎಲ್ಲಿ
       Z value pattern ರ length ಗೆ ಸಮ ಇರುತ್ತೋ, ಅಲ್ಲಿ ಪೂರ್ತಿ
       match ಆಗಿದೆ ಅಂತ ಅರ್ಥ — ಆ index ಅನ್ನ text ಗೆ ಸಂಬಂಧಿಸಿದ
       ಹಾಗೆ adjust ಮಾಡಿ record ಮಾಡು!"

  Time  : O(n + m)  →  Why: Z-array computation is linear in the
                            combined string's length
  Space : O(n + m)  →  Why: combined string + Z-array, both
                            proportional to total length

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 7 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: text = "ababcababcabc", pattern = "abc"

  combined = "abc$ababcababcabc"
             (indices: 0='a',1='b',2='c',3='$', then text starts
              at index 4)

  Computing the Z-array (sliding [l,r] window, standard Z-algo):
  the entries within the text portion that equal 3 (= len
  ("abc")) occur at combined-indices 6, 11, 14.

  Convert back to text-relative indices:
    text_index = combined_index - len(pattern) - 1
    6  - 3 - 1 = 2
    11 - 3 - 1 = 7
    14 - 3 - 1 = 10

  Output: [2, 7, 10] ✓

  ಇನ್ನೊಂದು example — overlapping matches:
  Input: text = "aaaa", pattern = "aa"

  combined = "aa$aaaa"
  Z values equal to 2 (len("aa")) found at text-relative indices
  0, 1, 2 — overlapping matches are all captured correctly since
  each starting position is checked independently.

  Output: [0, 1, 2] ✓

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 8 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ No match "hello"/"world"?      →  [] — empty result
  ✓ Pattern == text exactly?       →  [0] — single full match
  ✓ Overlapping matches "aaaa"/"aa"? →  [0,1,2] — all valid
                                        starts included
  ✓ Pattern longer than text?      →  [] — impossible to match,
                                        must guard against this
  ✓ Pattern matches at the very
    end of text?                   →  last valid index included

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 9 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                          Time      Space
  Brute (sliding compare) O(n*m)    O(m)
  Optimal (Z-function)     O(n+m)    O(n+m)   ← use this ✅

  Time yaake O(n+m)?  → Z-array computed once over the combined
                         string of length n+m+1, each position
                         processed in amortized O(1)
  Space yaake O(n+m)? → Combined string and Z-array both scale
                         with total input length

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 10 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Z-Algorithm (pattern + sentinel + text)

  Ee pattern yaavaaga use maadabeeku?
  → Pattern matching / "find all occurrences" problems — a
     direct alternative to KMP, and often simpler to REASON
     about since Z[i] has an intuitive "match length" meaning
  → Any "how much does this position match the string's own
     prefix" question — string periodicity, repeated patterns

  Idee pattern beere problemsalli kaanisatte:
  → KMP Algorithm / Pattern Matching #28 (next problem —
     alternative technique for the SAME pattern-matching goal,
     using a failure function instead of Z-array)
  → Longest Happy Prefix #1392 (previous KMP-based problem — Z-
     array could solve this too: find the largest i+z[i]==n)

  Next time intaha problem bandre naanu modalu idannu think maadtene:
  → "Pattern matching / prefix-overlap bekagidre → Z-function
     try maadu! pattern + sentinel + text build madi, Z-array
     compute madi, target length ge equal aada positions hudku!"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 11 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "Find every position where pattern occurs as a substring of
      text — overlapping matches all count."

  2. Brute force:
     "Slide pattern across every position, compare directly.
      O(n*m) worst case."

  3. Optimize:
     "Build pattern + sentinel + text, compute the Z-array in
      O(n+m) using a sliding window that reuses previously
      matched segments. Any position with Z value equal to the
      pattern's length is a full match."

  4. Code:
     "Standard Z-array builder (two-pointer [l,r] window). Scan
      the text portion of the combined string for Z values equal
      to len(pattern), adjust indices back to text-relative."

  5. Complexity:
     "Time O(n+m) — one Z-array pass. Space O(n+m) for the
      combined string and Z-array."

  Mukhya: Z-function = 'how much does THIS position match the
          string's own prefix' — put your pattern up front and
          every match becomes a simple equality check!
"""


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(n*m) Time | O(m) Space (sliding comparison)
# ═══════════════════════════════════════════════════════════════════
def find_pattern_occurrences_brute(text, pattern):
    """
    Idu modala aaloochane — text ra prati position inda pattern
    jothe direct compare madu
    """
    n, m = len(text), len(pattern)
    results = []

    for i in range(n - m + 1):
        if text[i:i + m] == pattern:
            results.append(i)

    return results


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n + m) Time | O(n + m) Space (Z-Algorithm)
# ═══════════════════════════════════════════════════════════════════
def _compute_z_array(s):
    """Standard Z-array: z[i] = longest match between s[i:] and s's own prefix."""
    n = len(s)
    z = [0] * n
    left, right = 0, 0

    for i in range(1, n):
        if i < right:
            z[i] = min(right - i, z[i - left])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] > right:
            left, right = i, i + z[i]

    return z


def find_pattern_occurrences(text, pattern):
    """
    Idu final answer — pattern + '$' + text build madi Z-array
    compute madi, Z value == pattern length sikkidkoodle match
    """
    if not pattern or len(pattern) > len(text):
        return []

    combined = pattern + '$' + text
    z = _compute_z_array(combined)
    m = len(pattern)

    results = []
    for i in range(m + 1, len(combined)):
        if z[i] == m:
            results.append(i - m - 1)

    return results


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # Test 1 — Basic (multiple occurrences)
    assert find_pattern_occurrences("ababcababcabc", "abc") == [2, 7, 10]

    # Test 2 — Overlapping matches
    assert find_pattern_occurrences("aaaa", "aa") == [0, 1, 2]

    # Test 3 — No match at all
    assert find_pattern_occurrences("hello", "world") == []

    # Test 4 — Pattern equals text
    assert find_pattern_occurrences("abc", "abc") == [0]

    # Test 5 — Pattern longer than text
    assert find_pattern_occurrences("ab", "abc") == []

    # Cross-check: brute force must agree on all of the above
    assert find_pattern_occurrences_brute("ababcababcabc", "abc") == [2, 7, 10]
    assert find_pattern_occurrences_brute("aaaa", "aa") == [0, 1, 2]
    assert find_pattern_occurrences_brute("hello", "world") == []
    assert find_pattern_occurrences_brute("abc", "abc") == [0]
    assert find_pattern_occurrences_brute("ab", "abc") == []

    print("All tests passed!")
