"""
╔════════════════════════════════════════════════════════════════════╗
║  SHORTEST PALINDROME                                               ║
║  LeetCode #214  |  Difficulty: Hard  |  Topic: Strings/KMP         ║
║  Link: https://leetcode.com/problems/shortest-palindrome/          ║
╚════════════════════════════════════════════════════════════════════╝

  NOTE: This is the SAME core algorithm as #16 (Minimum
  Characters to Add at Front to Make Palindrome) — that problem
  asked only for the COUNT of characters needed; this one asks
  for the actual resulting PALINDROME STRING.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Given a string `s`, you may add characters ONLY in FRONT of it
  to convert it into a palindrome. Return the SHORTEST palindrome
  achievable this way (i.e., the whole resulting string, not just
  a count).

  Input : s = a string
  Output: string — the shortest palindrome formed by prepending
          characters to s

  Example 1 — basic:
    Input : s = "aacecaaa"
    Output: "aaacecaaa"
    Why?  : the longest palindromic PREFIX of s is "aacecaa"
            (length 7 of 8). Only the trailing "a" falls outside
            it, so prepending its reverse ("a") gives the answer

  Example 2 — slightly tricky (short palindromic prefix):
    Input : s = "abcd"
    Output: "dcbabcd"
    Why?  : the longest palindromic prefix is just "a" (length
            1). Prepending the reverse of the remaining "bcd"
            (which is "dcb") gives "dcbabcd" — a full palindrome

  Example 3 — already a palindrome:
    Input : s = "racecar"
    Output: "racecar"
    Why?  : the whole string is already its own longest
            palindromic prefix — nothing needs to be prepended

  Constraints:
    - 0 <= s.length <= 5 * 10^4
    - s consists of lowercase English letters only (or empty)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Problem odi aada mele namma brain enu think maadabeeku:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  ಒಂದು string s                   │
  │  Output ಏನು ಬೇಕು?     →  FRONT ಗೆ characters ಸೇರಿಸಿ,     │
  │                           ಅತಿ ಚಿಕ್ಕ palindrome — ಪೂರ್ತಿ   │
  │                           resulting string return ಮಾಡಬೇಕು│
  │  Constraints ಏನಿದೆ?   →  ಇದೇ #16 ರ algorithm — ಆದ್ರೆ      │
  │                           count ಬದಲು ಪೂರ್ತಿ string ಬೇಕು  │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — #16 ಜೊತೆ ಇದೇ ಸಂಪೂರ್ಣ CONNECT ಮಾಡಿ ನೋಡಿ!
  →  #16 ರಲ್ಲಿ: answer = n - (longest palindromic prefix length)
     — ಬರೀ COUNT return ಮಾಡಿದ್ವಿ
  →  ಇಲ್ಲಿ: ಅದೇ longest palindromic prefix ಕಂಡುಹಿಡಿದ ಮೇಲೆ,
     ಉಳಿದ (leftover) ಭಾಗ ಅನ್ನ REVERSE ಮಾಡಿ, ಅದನ್ನ s ರ ಮುಂದೆ
     ಸೇರಿಸಿದ್ರೆ ಪೂರ್ತಿ ANSWER STRING ಸಿಗುತ್ತೆ!
  →  So algorithm ಒಂದೇ, ಬರೀ FINAL STEP ಬೇರೆ (count vs actual
     string construction)

  ಹಂತ 3 — ಮೊದಲ simple idea (longest palindromic prefix find
           ಮಾಡೋಕೆ) ಏನು?
  →  ಪ್ರತಿ length L ಅನ್ನ n ಇಂದ 1 ವರೆಗೆ try ಮಾಡಿ, s[:L]
     palindrome ಆಗಿದ್ಯಾ ಚೆಕ್ ಮಾಡಿ — ಮೊದಲ (ಅತಿ ಉದ್ದ) match
     ಸಿಕ್ಕಿದ್ದೇ ಅದು

  ಹಂತ 4 — Smart trick (KMP failure function) ಏನಿದೆ?
  →  "s + '#' + reverse(s)" combined string build ಮಾಡಿ, KMP LPS
     array compute ಮಾಡಿ. ಕೊನೆಯ entry ನೇ longest palindromic
     prefix ರ length
  →  remainder = s[longest_len:]  (leftover suffix, palindrome
     ಆಗಿಲ್ಲದ ಭಾಗ)
  →  answer = reverse(remainder) + s

  ಹಂತ 5 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  ಅದೇ #16 ರ logic — reverse(s) ರ suffix, s ರ prefix ಜೊತೆ
     ಎಷ್ಟು overlap ಆಗುತ್ತೋ ಅಷ್ಟೇ palindrome-ready — ಉಳಿದಿದ್ದನ್ನ
     mirror ಮಾಡಿ front ಗೆ ಸೇರಿಸಿದ್ರೆ ಪೂರ್ತಿ palindrome ಆಗುತ್ತೆ

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು:
  →  "This is the identical algorithm to finding the minimum
      characters needed at the front — same KMP LPS trick on
      s + '#' + reverse(s)"
  →  "The only difference: instead of returning n minus the LPS
      length, I take the leftover suffix, reverse it, and
      prepend it to s to get the actual palindrome string"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : KMP Failure Function (LPS array) on s + '#' + reverse(s)
  Secondary : Brute-force palindromic-prefix check + construction

  WHY the same KMP LPS trick as #16?
  → Finding "how much do I need to add" and "what exactly do I
    add" are the SAME underlying question — both require knowing
    the longest palindromic prefix. Once you have its length,
    building the actual string is just one extra reverse + concat
    step.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  The key insight: whatever falls OUTSIDE the longest palindromic
  prefix must be mirrored and placed in front — there's exactly
  one way to do this optimally, and it's fully determined by
  where that prefix ends. So the "shortest palindrome" question
  and "minimum characters to add" question share one computation
  (the longest palindromic prefix length via KMP LPS); this
  problem just asks us to go one step further and materialize
  the actual string.

  The journey from brute to optimal:
    Brute thought   →  Check s[:L] for palindrome-ness for every
                       L from n down to 1; once found, reverse
                       the remainder and prepend it
    Problem with it →  Each palindrome check costs O(L), giving
                       O(n^2) total in the worst case
    Better question →  Reuse the O(n) KMP LPS trick from #16 to
                       find the longest palindromic prefix directly
    Optimal         →  One O(n) LPS computation, then O(n) string
                       construction

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE (check every prefix length)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Starting from the FULL length and shrinking down, check
    whether s[:L] is a palindrome. The first (longest) L that
    qualifies tells us exactly what to mirror and prepend.

  Pseudocode:
    step 1: for L in range(n, 0, -1):
    step 2:   if s[:L] == s[:L][::-1]:
    step 3:     return s[L:][::-1] + s
    step 4: return s   # only reached if s is empty

  Time  : O(n^2)  →  Why: up to n candidate lengths, each
                          palindrome check costs O(L)
  Space : O(n)     →  Why: each candidate slice/reverse copies
                          up to n characters

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ?
    → Correct, but quadratic — for n = 5*10^4 this is far too
      slow. KMP's LPS array finds the same longest palindromic
      prefix in one linear pass, exactly as in #16.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 6 — APPROACH 2 — OPTIMAL (KMP Failure Function)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Build `combined = s + '#' + reverse(s)`, compute its KMP LPS
    array (identical to #16). The last value gives the longest
    palindromic prefix length. Take the leftover suffix of `s`
    beyond that prefix, reverse it, and prepend it to `s`.

  Key steps:
    1. if not s: return s
    2. combined = s + '#' + s[::-1]
    3. lps = compute_lps(combined)
    4. longest_pal_prefix_len = lps[-1]
    5. remainder = s[longest_pal_prefix_len:]
    6. return remainder[::-1] + s

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ:
    → "s + '#' + reverse(s) build ಮಾಡಿ KMP LPS compute ಮಾಡು.
       ಕೊನೆಯ value ಇಂದ longest palindromic prefix length
       ಸಿಗುತ್ತೆ. ಆ prefix ನ ಆಚೆ ಇರೋ remainder ಅನ್ನ reverse
       ಮಾಡಿ, s ರ ಮುಂದೆ ಸೇರಿಸಿದ್ರೆ ಪೂರ್ತಿ answer ಸಿಗುತ್ತೆ!"

  Time  : O(n)  →  Why: combined string has length 2n+1, KMP LPS
                        computation is linear in string length
  Space : O(n)  →  Why: combined string, LPS array, and final
                        result string are all O(n)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 7 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: s = "aacecaaa"   (n = 8)

  combined = "aacecaaa#aaacecaa"
  KMP LPS's final value = 7 (longest palindromic prefix is
  "aacecaa" — check: a,a,c,e,c,a,a reversed is a,a,c,e,c,a,a,
  same!)

  remainder = s[7:] = "a"
  reverse(remainder) = "a"

  Answer: "a" + "aacecaaa" = "aaacecaaa"

  Output: "aaacecaaa" ✓

  ಇನ್ನೊಂದು example — short palindromic prefix:
  Input: s = "abcd"

  combined = "abcd#dcba"
  Longest palindromic prefix of "abcd" is just "a" (length 1)
  remainder = s[1:] = "bcd" → reversed = "dcb"

  Answer: "dcb" + "abcd" = "dcbabcd"

  Output: "dcbabcd" ✓

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 8 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ Empty string ""?                →  "" — nothing to do
  ✓ Already a palindrome "racecar"? →  "racecar" — unchanged,
                                        nothing prepended
  ✓ Single character "a"?           →  "a" — trivially a palindrome
  ✓ No repeats at all "abcd"?       →  "dcbabcd" — only the first
                                        character forms a
                                        palindromic prefix
  ✓ All same character "aaaa"?      →  "aaaa" — already a
                                        palindrome, nothing added

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 9 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                          Time    Space
  Brute (check prefixes)  O(n^2)  O(n)
  Optimal (KMP LPS)        O(n)    O(n)   ← use this ✅

  Time yaake O(n)?  → LPS computation on a string of length
                       2n+1 is linear — same as #16
  Space yaake O(n)? → Combined string, LPS array, and result
                       string all scale with n

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 10 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: KMP LPS on s + sentinel + reverse(s) — string construction

  Ee pattern yaavaaga use maadabeeku?
  → Same as #16, but whenever the problem asks for the ACTUAL
     result (not just a count/length) — compute the key quantity
     (longest palindromic prefix length) exactly as before, then
     do one extra construction step
  → Reinforces: many "count vs construct" problem pairs share
     100% of their core algorithm

  Idee pattern beere problemsalli kaanisatte:
  → Minimum Characters to Add at Front to Make Palindrome
     (previous problem — the COUNT-only version of this exact
     algorithm)
  → Rabin-Karp Algorithm (next problem in curriculum — yet
     another string-hashing based technique, different mechanism
     but same "avoid brute-force re-comparison" spirit)

  Next time intaha problem bandre naanu modalu idannu think maadtene:
  → "Idu earlier problem (COUNT version) na SAME algorithm
     alva? Ondu vela match aadre, core computation reuse madi,
     bari FINAL construction step matra add madu!"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 11 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "Prepend the minimum characters to s to make it a
      palindrome, and return the resulting FULL string."

  2. Brute force:
     "Check s[:L] for palindrome-ness from L=n down to 1; at the
      first match, mirror the remainder and prepend it. O(n^2)."

  3. Optimize:
     "Identical to the count-only version: build s + '#' +
      reverse(s), run KMP's LPS preprocessing, and the final LPS
      value gives the longest palindromic prefix length in
      O(n). Then mirror the leftover suffix and prepend it."

  4. Code:
     "Same LPS builder as before. remainder = s[lps[-1]:].
      Return remainder[::-1] + s."

  5. Complexity:
     "Time O(n) — one LPS pass. Space O(n) for the combined
      string, LPS array, and result."

  Mukhya: 'count' and 'construct' variants of the same palindrome
          problem usually share their ENTIRE core algorithm —
          recognize the reuse before reinventing anything!
"""


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(n^2) Time | O(n) Space (check every prefix length)
# ═══════════════════════════════════════════════════════════════════
def shortest_palindrome_brute(s):
    """
    Idu modala aaloochane — n inda 1 varge prati prefix length
    try madi, palindrome sikkidkoodle remainder mirror madi prepend madu
    """
    n = len(s)
    for length in range(n, 0, -1):
        prefix = s[:length]
        if prefix == prefix[::-1]:
            return s[length:][::-1] + s
    return s  # only reached if s is empty


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


def shortest_palindrome(s):
    """
    Idu final answer — s + '#' + reverse(s) build madi, KMP LPS
    run madi, remainder mirror madi s munde prepend madu
    """
    if not s:
        return s

    combined = s + '#' + s[::-1]
    lps = _compute_lps(combined)
    longest_palindromic_prefix_len = lps[-1]

    remainder = s[longest_palindromic_prefix_len:]
    return remainder[::-1] + s


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # Test 1 — Basic
    assert shortest_palindrome("aacecaaa") == "aaacecaaa"

    # Test 2 — Short palindromic prefix
    assert shortest_palindrome("abcd") == "dcbabcd"

    # Test 3 — Already a palindrome
    assert shortest_palindrome("racecar") == "racecar"

    # Test 4 — Single character
    assert shortest_palindrome("a") == "a"

    # Test 5 — Empty string
    assert shortest_palindrome("") == ""

    # Cross-check: brute force must agree on all of the above
    assert shortest_palindrome_brute("aacecaaa") == "aaacecaaa"
    assert shortest_palindrome_brute("abcd") == "dcbabcd"
    assert shortest_palindrome_brute("racecar") == "racecar"
    assert shortest_palindrome_brute("a") == "a"
    assert shortest_palindrome_brute("") == ""

    print("All tests passed!")
