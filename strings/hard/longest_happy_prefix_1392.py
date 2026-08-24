"""
╔════════════════════════════════════════════════════════════════════╗
║  LONGEST HAPPY PREFIX                                              ║
║  LeetCode #1392  |  Difficulty: Hard  |  Topic: Strings/KMP        ║
║  Link: https://leetcode.com/problems/longest-happy-prefix/         ║
╚════════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  A "happy prefix" is a non-empty PROPER prefix of `s` that is
  ALSO a suffix of `s` — proper meaning it can't be the entire
  string itself.

  Given a string `s`, return its LONGEST happy prefix. If none
  exists, return an empty string "".

  Input : s = a string
  Output: string — the longest happy prefix, or "" if none exists

  Example 1 — basic:
    Input : s = "level"
    Output: "l"
    Why?  : "l" is both a prefix and a suffix. Longer candidates
            ("le"/"el", "lev"/"vel", "leve"/"evel") don't match
            — only the single-character overlap works

  Example 2 — slightly tricky (repeating pattern):
    Input : s = "ababab"
    Output: "abab"
    Why?  : prefix "abab" equals suffix "abab" (the last 4
            characters) — the repeating "ab" pattern creates a
            long overlap

  Example 3 — no happy prefix at all:
    Input : s = "leetcode"
    Output: ""
    Why?  : no proper prefix of "leetcode" matches any suffix of
            the same length

  Constraints:
    - 1 <= s.length <= 10^5
    - s consists of only lowercase English letters

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Problem odi aada mele namma brain enu think maadabeeku:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  ಒಂದು string s                   │
  │  Output ಏನು ಬೇಕು?     →  ಅತಿ ಉದ್ದ PROPER prefix, ಅದೇ     │
  │                           string ರ suffix ಕೂಡ ಆಗಿರಬೇಕು   │
  │  Constraints ಏನಿದೆ?   →  "proper" ಅಂದ್ರೆ ಪೂರ್ತಿ string   │
  │                           ಆಗಬಾರದು (n length ಗೆ allowed ಇಲ್ಲ)│
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ಇದನ್ನ previous problem (#16, KMP LPS trick) ಜೊತೆ
           compare ಮಾಡಿ ನೋಡಿ!
  →  ಅಲ್ಲಿ ನಾವು "s ರ longest palindromic PREFIX" ಹುಡುಕೋಕೆ
     s + '#' + reverse(s) build ಮಾಡಿ KMP LPS ಬಳಸಿದ್ವಿ
  →  ಇಲ್ಲಿ ಕೂಡ KMP LPS array ಬಳಸೋದೇ, ಆದ್ರೆ ಈಗ EXTRA build
     ಮಾಡೋ ಅಗತ್ಯನೇ ಇಲ್ಲ — ಇದೇ definition, LPS array ಗೆ EXACT ಆಗಿ
     ಹೊಂದುತ್ತೆ!

  ಹಂತ 3 — ಮೊದಲ simple idea ಏನು?
  →  ಪ್ರತಿ length L ಅನ್ನ n-1 ಇಂದ 1 ವರೆಗೆ try ಮಾಡಿ, s[:L] ==
     s[-L:] ಆಗಿದ್ಯಾ ಚೆಕ್ ಮಾಡಿ — ಮೊದಲ (ಅತಿ ಉದ್ದ) match ಸಿಕ್ಕಿದ್ದೇ
     answer

  ಹಂತ 4 — Smart trick (KMP LPS — DIRECT ಆಗಿ) ಏನಿದೆ?
  →  "happy prefix" ರ definition ಅನ್ನೇ ಇನ್ನೊಂದು ಸಲ ಓದಿ:
      "PROPER prefix, string ರ SUFFIX ಕೂಡ ಆಗಿರಬೇಕು"
  →  ಇದೇ ಪ್ರಶ್ನೆಗೆ KMP LPS array ಉತ್ತರ ಕೊಡುತ್ತೆ! lps[n-1]
     ಅಂದ್ರೆ "s[0..n-1] ರ LONGEST PROPER PREFIX ಯಾವುದು SUFFIX
     ಕೂಡ ಆಗಿದೆ" ಅಂತ EXACT ಆಗಿ ಗೊತ್ತಾಗುತ್ತೆ
  →  So s ಗೆ ನೇರವಾಗಿ (ಯಾವ reverse/concatenation ಬೇಡ) LPS
     compute ಮಾಡಿ, lps[-1] length ರ prefix ಅನ್ನ return ಮಾಡಿದ್ರೆ
     ಸಾಕು!

  ಹಂತ 5 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  KMP LPS array ಪ್ರತಿ index i ಗೂ "s[0..i] ರ longest proper
     prefix-suffix overlap" ಎಷ್ಟು ಅಂತ track ಮಾಡುತ್ತೆ — ಕೊನೆಯ
     index i=n-1 ಗೆ ಇರೋ value ನೇ ಪೂರ್ತಿ string ಗೆ ನಾವು ಬೇಕಾದ
     ಉತ್ತರ

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು:
  →  "This IS the textbook definition of the KMP failure
      function — 'longest proper prefix that's also a suffix'"
  →  "So I just compute the LPS array of s directly, no need to
      concatenate with a reverse like the palindrome-prefix
      variant of this trick"
  →  "The final entry of the LPS array gives the answer's length"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : KMP Failure Function (LPS array) — applied directly to s
  Secondary : Brute-force prefix/suffix comparison

  WHY KMP's LPS array (directly, no concatenation)?
  → The problem statement's definition — "longest proper prefix
    that is also a suffix" — is LITERALLY what the LPS array is
    designed to compute, at its very last index. No auxiliary
    string construction needed this time.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  The key insight: this problem is the DEFINITION of KMP's
  failure function, not just a use-case for it. lps[i] always
  means "the length of the longest proper prefix of s[0..i] that
  is also a suffix of s[0..i]." Setting i = n-1 (the last index)
  gives exactly the longest happy prefix of the WHOLE string.

  The journey from brute to optimal:
    Brute thought   →  For every candidate length L from n-1
                       down to 1, compare s[:L] to s[-L:]
    Problem with it →  Each comparison costs O(L), giving O(n^2)
                       total across all candidate lengths
    Better question →  "Isn't this exactly what KMP's failure
                       function already computes?"
    Insight         →  Run standard KMP LPS preprocessing on `s`
                       itself; read off lps[n-1]
    Optimal         →  One O(n) LPS computation, no extra string
                       construction needed

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE (check every length)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Try every candidate length `L` from n-1 (the longest POSSIBLE
    proper prefix) down to 1. For each, compare the first L
    characters to the last L characters. The first match found
    (starting from the longest) is the answer.

  Pseudocode:
    step 1: n = len(s)
    step 2: for L in range(n - 1, 0, -1):
    step 3:   if s[:L] == s[-L:]:
    step 4:     return s[:L]
    step 5: return ""

  Time  : O(n^2)  →  Why: up to n candidate lengths, each
                          comparison costs O(L)
  Space : O(n)     →  Why: each slice comparison copies up to
                          n characters

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ?
    → Correct, but quadratic — for n = 10^5 this is far too
      slow. KMP's LPS array computes exactly this in one linear
      pass, since it's the array's core definition.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 6 — APPROACH 2 — OPTIMAL (KMP Failure Function, direct)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Compute the standard KMP LPS array directly on `s` (no
    concatenation with anything else needed). The last entry,
    lps[n-1], IS the length of the longest happy prefix by
    definition. Slice out that many characters from the front.

  Key steps:
    1. lps = compute_lps(s)     # standard KMP preprocessing
    2. happy_len = lps[-1]
    3. return s[:happy_len]

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ:
    → "s ಗೆ ನೇರವಾಗಿ KMP LPS array compute ಮಾಡು. ಕೊನೆಯ entry
       (lps[n-1]) ಅಂದ್ರೆ longest happy prefix ರ length — ಅಷ್ಟು
       characters ಅನ್ನ s ಇಂದ ಶುರುವಿಂದ ಸ್ಲೈಸ್ ಮಾಡಿ return ಮಾಡು!"

  Time  : O(n)  →  Why: LPS computation is linear in string
                        length — no auxiliary string needed here
  Space : O(n)  →  Why: LPS array of length n

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 7 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: s = "ababab"   (n = 6)

  Computing the LPS array via standard KMP preprocessing:
  index:   0  1  2  3  4  5
  char:    a  b  a  b  a  b
  lps:     0  0  1  2  3  4

  Trace: lps[0]=0 (single char, no proper prefix).
  i=1 'b' vs s[0]='a' mismatch, length stays 0 → lps[1]=0.
  i=2 'a' vs s[0]='a' match → length=1 → lps[2]=1.
  i=3 'b' vs s[1]='b' match → length=2 → lps[3]=2.
  i=4 'a' vs s[2]='a' match → length=3 → lps[4]=3.
  i=5 'b' vs s[3]='b' match → length=4 → lps[5]=4.

  lps[-1] = 4 → happy prefix length 4 → s[:4] = "abab"

  Output: "abab" ✓

  ಇನ್ನೊಂದು example — no happy prefix:
  Input: s = "leetcode"

  LPS array computation finds no proper prefix-suffix overlap
  anywhere → lps[-1] = 0 → s[:0] = ""

  Output: "" ✓

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 8 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ Single character "a"?          →  "" — no PROPER (non-empty,
                                       non-full) prefix possible
  ✓ No happy prefix "leetcode"?    →  "" — LPS array ends at 0
  ✓ Repeating pattern "aaaa"?      →  "aaa" — every prefix is
                                       also a suffix, longest
                                       proper one is n-1 chars
  ✓ Only single-char overlap
    ("level")?                     →  "l" — just the first char
  ✓ Whole-pattern repetition
    ("ababab")?                    →  "abab" — overlap from the
                                       repeating "ab" unit

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 9 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                        Time    Space
  Brute (check lengths)  O(n^2)  O(n)
  Optimal (KMP LPS)      O(n)    O(n)   ← use this ✅

  Time yaake O(n)?  → Single LPS pass over s; each pointer only
                       ever moves forward or falls back via
                       already-computed LPS values
  Space yaake O(n)? → LPS array of length n

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 10 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: KMP LPS Array — direct application

  Ee pattern yaavaaga use maadabeeku?
  → "Longest proper prefix that's also a suffix" asked LITERALLY
     → just compute the LPS array of the string directly, read
     off the last entry — no concatenation trick needed
  → Contrast with #16 (Minimum Chars to Add at Front), where we
     needed s + '#' + reverse(s) because that problem asked
     about PALINDROMIC prefixes, a different relationship than
     plain prefix-equals-suffix

  Idee pattern beere problemsalli kaanisatte:
  → Minimum Characters to Add at Front to Make Palindrome
     (previous problem — KMP LPS on a CONSTRUCTED string, for
     comparison with this DIRECT application)
  → KMP Algorithm / Pattern Matching #28 (next problem — LPS
     array used for its ORIGINAL purpose, pattern searching)

  Next time intaha problem bandre naanu modalu idannu think maadtene:
  → "'Longest prefix that's also a suffix' seedha keliddare →
     KMP LPS array compute madi lps[-1] read madu, extra string
     build madoda agatya illa!"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 11 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "Find the longest PROPER prefix of s that is also a suffix
      of s — proper meaning it can't be the whole string."

  2. Brute force:
     "Check every candidate length from n-1 down to 1, comparing
      the prefix and suffix of that length. O(n^2)."

  3. Optimize:
     "This is literally the definition of KMP's LPS array — no
      construction trick needed, just compute LPS on s directly
      and read the last entry."

  4. Code:
     "Standard KMP LPS builder on s. Answer length = lps[-1].
      Return s[:lps[-1]]."

  5. Complexity:
     "Time O(n) — one LPS pass. Space O(n) for the LPS array."

  Mukhya: sometimes the problem IS the textbook definition of a
          classic algorithm — recognize it and skip straight to
          applying the algorithm, no extra cleverness needed!
"""


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(n^2) Time | O(n) Space (check every candidate length)
# ═══════════════════════════════════════════════════════════════════
def longest_happy_prefix_brute(s):
    """
    Idu modala aaloochane — n-1 inda 1 varge prati length try
    madi, prefix == suffix sikkidkoodle andina return madu
    """
    n = len(s)
    for length in range(n - 1, 0, -1):
        if s[:length] == s[-length:]:
            return s[:length]
    return ""


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n) Time | O(n) Space (KMP failure function, direct)
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


def longest_happy_prefix(s):
    """
    Idu final answer — s ge nera KMP LPS array compute madi,
    last entry (lps[-1]) ne longest happy prefix length
    """
    lps = _compute_lps(s)
    happy_len = lps[-1]
    return s[:happy_len]


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # Test 1 — Basic (single-char overlap)
    assert longest_happy_prefix("level") == "l"

    # Test 2 — Repeating pattern
    assert longest_happy_prefix("ababab") == "abab"

    # Test 3 — No happy prefix at all
    assert longest_happy_prefix("leetcode") == ""

    # Test 4 — Classic example
    assert longest_happy_prefix("leetcodeleet") == "leet"

    # Test 5 — All same character
    assert longest_happy_prefix("aaaa") == "aaa"

    # Cross-check: brute force must agree on all of the above
    assert longest_happy_prefix_brute("level") == "l"
    assert longest_happy_prefix_brute("ababab") == "abab"
    assert longest_happy_prefix_brute("leetcode") == ""
    assert longest_happy_prefix_brute("leetcodeleet") == "leet"
    assert longest_happy_prefix_brute("aaaa") == "aaa"

    print("All tests passed!")
