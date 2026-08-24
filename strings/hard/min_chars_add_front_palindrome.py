"""
╔════════════════════════════════════════════════════════════════════╗
║  MINIMUM CHARACTERS TO ADD AT FRONT TO MAKE PALINDROME             ║
║  GeeksforGeeks classic  |  Difficulty: Hard  |  Topic: KMP/Hashing ║
║  Link: https://www.geeksforgeeks.org/dsa/                          ║
║        minimum-characters-added-front-make-string-palindrome/      ║
╚════════════════════════════════════════════════════════════════════╝

  NOTE: The curriculum sheet lists this as slot #16 with no
  LeetCode number ("—"). It's closely related to LeetCode #214
  "Shortest Palindrome" (slot #22 later in this same curriculum)
  — #214 asks for the resulting PALINDROME STRING, this one asks
  only for the COUNT of characters needed. Same core algorithm.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Given a string `s`, find the MINIMUM number of characters that
  need to be added at the FRONT of `s` to make the whole string
  a palindrome.

  Input : s = a string
  Output: integer — minimum characters to prepend

  Example 1 — basic:
    Input : s = "ABCD"
    Output: 3
    Why?  : the longest palindromic PREFIX of "ABCD" is just "A"
            (length 1). Prepending "DCB" (the reverse of the
            remaining "BCD") gives "DCBABCD", a palindrome —
            that's 3 characters added

  Example 2 — slightly tricky (a longer palindromic prefix exists):
    Input : s = "AACECAAAA"
    Output: 2
    Why?  : the longest palindromic prefix is "AACECAA" (length
            7 out of 9) — only the last 2 characters ("AA") lie
            outside it, so we only need to prepend their reverse
            ("AA") — 2 characters added

  Example 3 — already a palindrome:
    Input : s = "racecar"
    Output: 0
    Why?  : the whole string is already a palindrome (its own
            longest palindromic prefix), nothing needs to be added

  Constraints:
    - 1 <= s.length <= 10^5
    - s consists of lowercase/uppercase English letters

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Problem odi aada mele namma brain enu think maadabeeku:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  ಒಂದು string s                   │
  │  Output ಏನು ಬೇಕು?     →  FRONT ನಲ್ಲಿ ಎಷ್ಟು characters    │
  │                           ಸೇರಿಸಿದ್ರೆ ಪೂರ್ತಿ string          │
  │                           palindrome ಆಗುತ್ತೆ ಅಂತ ಸಂಖ್ಯೆ   │
  │  Constraints ಏನಿದೆ?   →  n up to 10^5 — O(n) solution      │
  │                           ಬೇಕು (O(n^2) too slow)          │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — Key observation ಏನಿದೆ?
  →  "front ಗೆ ಸೇರಿಸೋ characters ಗಳು ಯಾವಾಗಲೂ, string ರ END
      ಭಾಗದ REVERSE ಆಗಿರುತ್ತೆ (ಯಾವ part palindrome ಆಗಿಲ್ವೋ ಅದು)"
  →  "s ರ LONGEST PALINDROMIC PREFIX ಎಷ್ಟು ಉದ್ದ ಇದ್ಯೋ, ಅಷ್ಟು
      ಭಾಗ ಈಗಾಗ್ಲೇ palindrome ಆಗಿದೆ — ಉಳಿದ (n - L) characters
      ಗೆ ಮಾತ್ರ reverse ಮಾಡಿ front ಗೆ ಸೇರಿಸಿದ್ರೆ ಸಾಕು!"
  →  So answer = n - (longest palindromic prefix ರ length)

  ಹಂತ 3 — ಮೊದಲ simple idea (longest palindromic prefix find
           ಮಾಡೋಕೆ) ಏನು?
  →  ಪ್ರತಿ length L ಅನ್ನ n ಇಂದ 1 ವರೆಗೆ try ಮಾಡಿ, s[:L]
     palindrome ಆಗಿದ್ಯಾ ಚೆಕ್ ಮಾಡಿ — ಮೊದಲ (ಅತಿ ಉದ್ದ) match
     ಸಿಕ್ಕಿದ್ದೇ answer

  ಹಂತ 4 — Smart trick (KMP failure function) ಏನಿದೆ?
  →  "s + '#' + reverse(s)" ಅಂತ ಒಂದು ಹೊಸ string build ಮಾಡಿ
     (# separator ಯಾಕಂದ್ರೆ ಇದು s ನಲ್ಲಿ ಇಲ್ಲದ char ಆಗಿರಬೇಕು)
  →  ಈ combined string ಗೆ KMP LPS (Longest Prefix Suffix) array
     compute ಮಾಡಿ
  →  ಕೊನೆಯ entry ಅಂದ್ರೆ: "s ರ prefix" ಮತ್ತು "reverse(s) ರ
      suffix" ಎಷ್ಟು overlap ಆಗುತ್ತೋ ಅಷ್ಟು — ಇದೇ s ರ LONGEST
      PALINDROMIC PREFIX ರ length!

  ಹಂತ 5 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  reverse(s) ರ suffix, s ರ prefix ಜೊತೆ match ಆಗುತ್ತೆ ಅಂದ್ರೆ,
     ಆ ಭಾಗ ಮುಂದೆಯೂ ಹಿಂದೆಯೂ ಒಂದೇ ಆಗಿ ಓದುತ್ತೆ ಅಂತ ಅರ್ಥ —
     ಅದೇ palindrome ರ definition!
  →  KMP LPS array ಇದನ್ನ single O(n) pass ನಲ್ಲಿ ಕಂಡುಹಿಡಿಯುತ್ತೆ

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು:
  →  "The characters I add are always the reverse of whatever's
      NOT part of the longest palindromic prefix"
  →  "I find that prefix length using KMP: build s + '#' +
      reverse(s), compute the LPS array, and the last value
      gives the overlap — which equals the longest palindromic
      prefix length"
  →  "Answer = n minus that length"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : KMP Failure Function (LPS array) on s + '#' + reverse(s)
  Secondary : Brute-force palindromic-prefix check

  WHY KMP's LPS array?
  → The LPS array is built EXACTLY to answer "how much does a
    prefix of this string overlap with a suffix ending here?"
    By concatenating s with its own reverse (separated by a
    sentinel), the overlap between s's prefix and reverse(s)'s
    suffix IS precisely s's longest palindromic prefix — KMP
    computes this in one O(n) pass, no separate palindrome
    checks needed.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  The key insight: whatever we prepend must exactly mirror the
  "leftover" suffix of `s` that falls outside its longest
  palindromic prefix — so the real problem is just "find the
  longest palindromic prefix," and the KMP LPS trick answers
  that directly. A prefix of `s` matching a suffix of
  reverse(s) is, by construction, a sequence that reads the same
  forwards (as part of s) and backwards (as part of reverse(s))
  — exactly a palindrome.

  The journey from brute to optimal:
    Brute thought   →  Check s[:L] for palindrome-ness for every
                       L from n down to 1, stop at the first hit
    Problem with it →  Each check costs O(L), and in the worst
                       case (no early palindromic prefix) this
                       is O(n^2) total
    Better question →  "Is there a way to find the longest
                       prefix-suffix overlap in linear time?"
    Insight         →  That's literally what KMP's failure
                       function computes — apply it to
                       s + '#' + reverse(s)
    Optimal         →  One O(n) LPS computation on a string of
                       length 2n+1

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE (check every prefix length)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Starting from the FULL length and shrinking down, check
    whether s[:L] is a palindrome. The first (longest) L that
    qualifies gives the answer: n - L characters need to be
    added.

  Pseudocode:
    step 1: for L in range(n, 0, -1):
    step 2:   if s[:L] == s[:L][::-1]:
    step 3:     return n - L
    step 4: return n - 1   # unreachable: L=1 is always a palindrome

  Time  : O(n^2)  →  Why: up to n candidate lengths, each
                          palindrome check costs O(L)
  Space : O(n)     →  Why: each candidate slice/reverse copies
                          up to n characters

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ?
    → Correct, but quadratic — for n = 10^5 this is far too
      slow. KMP's failure function finds the same "longest
      palindromic prefix" in one linear pass.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 6 — APPROACH 2 — OPTIMAL (KMP Failure Function)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Build `combined = s + '#' + reverse(s)` (the '#' sentinel
    prevents overlap from crossing between the two halves).
    Compute its KMP LPS (Longest Proper Prefix which is also
    Suffix) array. The LAST value of that array is exactly the
    length of the longest palindromic prefix of `s`. The answer
    is `n` minus that length.

  Key steps:
    1. combined = s + '#' + s[::-1]
    2. lps = compute_lps(combined)   # standard KMP preprocessing
    3. longest_pal_prefix_len = lps[-1]
    4. return n - longest_pal_prefix_len

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ:
    → "s + '#' + reverse(s) ಅಂತ combined string build ಮಾಡು.
       ಇದಕ್ಕೆ KMP LPS array compute ಮಾಡು. ಕೊನೆಯ value ಅಂದ್ರೆ,
       s ರ longest palindromic prefix ರ length. n ಇಂದ ಅದನ್ನ
       ಕಳೆದ್ರೆ answer ಸಿಗುತ್ತೆ!"

  Time  : O(n)  →  Why: combined string has length 2n+1, KMP LPS
                        computation is linear in string length
  Space : O(n)  →  Why: combined string + LPS array, both O(n)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 7 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: s = "AACECAAAA"   (n = 9)

  combined = "AACECAAAA" + "#" + "AAAACECAA"
           = "AACECAAAA#AAAACECAA"

  Computing the LPS array of `combined` (standard KMP
  preprocessing — grows the matched-prefix length as long as
  characters keep matching, falls back via lps[length-1] on a
  mismatch): the FINAL entry of the LPS array comes out to 7.

  That 7 is the longest palindromic prefix length of s
  ("AACECAA" — check: A A C E C A A reversed is A A C E C A A,
  same!).

  Answer: n - 7 = 9 - 7 = 2

  Output: 2 ✓

  ಇನ್ನೊಂದು example — no palindromic prefix beyond 1 char:
  Input: s = "ABCD"

  combined = "ABCD#DCBA"
  Longest palindromic prefix of "ABCD" is just "A" (length 1)
  → LPS final value = 1
  Answer: 4 - 1 = 3

  Output: 3 ✓

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 8 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ Already a palindrome "racecar"? →  0 — nothing to add
  ✓ Single character "a"?           →  0 — trivially a palindrome
  ✓ No repeats at all "ABCD"?       →  n-1 — only the very first
                                        character forms a
                                        palindromic prefix
  ✓ All same character "aaaa"?      →  0 — whole string already
                                        a palindrome
  ✓ Palindromic prefix mid-length
    ("AACECAAAA")?                  →  n minus that prefix's length

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 9 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                          Time    Space
  Brute (check prefixes)  O(n^2)  O(n)
  Optimal (KMP LPS)        O(n)    O(n)   ← use this ✅

  Time yaake O(n)?  → LPS computation on a string of length
                       2n+1 is linear — each pointer only ever
                       moves forward or falls back via
                       already-computed LPS values
  Space yaake O(n)? → Combined string (2n+1 chars) + LPS array
                       (2n+1 ints)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 10 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: KMP LPS on s + sentinel + reverse(s)

  Ee pattern yaavaaga use maadabeeku?
  → "Longest palindromic PREFIX or SUFFIX" type problems —
     concatenate string with its reverse (separated by a
     sentinel not present in either), run KMP LPS, read the
     last value
  → Any "find longest overlap between a string and its own
     reverse" scenario

  Idee pattern beere problemsalli kaanisatte:
  → Shortest Palindrome #214 (next-but-one in curriculum — the
     EXACT same technique, but returns the actual palindrome
     string instead of just the count)
  → Longest Happy Prefix #1392 (same core KMP LPS array idea,
     different framing — prefix that's also a suffix)

  Next time intaha problem bandre naanu modalu idannu think maadtene:
  → "Palindromic prefix/suffix length bekagidre → s + sentinel +
     reverse(s) build madi KMP LPS run madu — last value ne
     answer!"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 11 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "Find the minimum characters to prepend so the whole string
      becomes a palindrome — equivalent to finding the longest
      palindromic PREFIX and mirroring everything after it."

  2. Brute force:
     "Check s[:L] for palindrome-ness from L=n down to 1, return
      n-L at the first match. O(n^2) worst case."

  3. Optimize:
     "Concatenate s + '#' + reverse(s) and run KMP's LPS
      preprocessing on it. The final LPS value is exactly the
      overlap between s's prefix and reverse(s)'s suffix — which
      is s's longest palindromic prefix, found in O(n)."

  4. Code:
     "Standard KMP LPS array builder on the combined string.
      Answer = len(s) - lps[-1]."

  5. Complexity:
     "Time O(n) — one LPS pass over a 2n+1 length string. Space
      O(n) for the combined string and LPS array."

  Mukhya: longest palindromic prefix/suffix bekagidre, string +
          sentinel + reverse(string) build madi KMP LPS run
          madidre O(n) alli sigatte — classic combo trick!
"""


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(n^2) Time | O(n) Space (check every prefix length)
# ═══════════════════════════════════════════════════════════════════
def min_chars_to_add_brute(s):
    """
    Idu modala aaloochane — n inda 1 varge prati prefix length
    try madi, palindrome sikkidkoodle n-L return madu
    """
    n = len(s)
    for length in range(n, 0, -1):
        prefix = s[:length]
        if prefix == prefix[::-1]:
            return n - length
    return n - 1  # unreachable: length=1 is always a palindrome


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n) Time | O(n) Space (KMP failure function)
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


def min_chars_to_add(s):
    """
    Idu final answer — s + '#' + reverse(s) build madi, KMP LPS
    run madi, last value ne longest palindromic prefix length
    """
    n = len(s)
    combined = s + '#' + s[::-1]
    lps = _compute_lps(combined)
    longest_palindromic_prefix_len = lps[-1]
    return n - longest_palindromic_prefix_len


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # Test 1 — Basic
    assert min_chars_to_add("ABCD") == 3

    # Test 2 — Mid-length palindromic prefix
    assert min_chars_to_add("AACECAAAA") == 2

    # Test 3 — Already a palindrome
    assert min_chars_to_add("racecar") == 0

    # Test 4 — Single character
    assert min_chars_to_add("a") == 0

    # Test 5 — All same character
    assert min_chars_to_add("aaaa") == 0

    # Cross-check: brute force must agree on all of the above
    assert min_chars_to_add_brute("ABCD") == 3
    assert min_chars_to_add_brute("AACECAAAA") == 2
    assert min_chars_to_add_brute("racecar") == 0
    assert min_chars_to_add_brute("a") == 0
    assert min_chars_to_add_brute("aaaa") == 0

    print("All tests passed!")
