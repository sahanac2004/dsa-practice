"""
╔════════════════════════════════════════════════════════════════════╗
║  LONGEST SUBSTRING WITH AT LEAST K REPEATING CHARACTERS             ║
║  LeetCode #395  |  Difficulty: Medium  |  Topic: Sliding Window     ║
║  Link: https://leetcode.com/problems/                              ║
║        longest-substring-with-at-least-k-repeating-characters/     ║
╚════════════════════════════════════════════════════════════════════╝

  NOTE: The curriculum sheet lists slot #12 as "Count Substrings
  with K Different Characters" tagged #395 — but LeetCode #395 is
  actually THIS problem (Longest Substring with At Least K
  Repeating Characters). It still fits the "sliding-window/
  variable" technique tag well, so it's implemented here as the
  real #395.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Given a string `s` and an integer `k`, return the length of
  the LONGEST substring of `s` such that EVERY character
  appearing in that substring occurs at least `k` times.

  Input : s = a string, k = minimum required repeat count
  Output: integer — length of the longest valid substring
          (0 if no non-empty substring qualifies)

  Example 1 — basic:
    Input : s = "aaabb", k = 3
    Output: 3
    Why?  : "aaa" has 'a' appearing 3 times (≥ k). Including any
            'b' would need 'b' to appear ≥ 3 times too, but 'b'
            only appears twice total — so "aaa" is the longest
            valid substring

  Example 2 — slightly tricky (mixed characters, all valid):
    Input : s = "ababbc", k = 2
    Output: 5
    Why?  : "ababb" has a:2, b:3 — both ≥ 2. Extending to
            "ababbc" would need 'c' ≥ 2 times, but 'c' appears
            only once — so we must stop before it

  Example 3 — impossible to satisfy:
    Input : s = "abcde", k = 2
    Output: 0
    Why?  : every character appears exactly once — no substring
            (except length 0) can have every character repeat
            at least twice

  Constraints:
    - 1 <= s.length <= 10^4
    - s consists of only lowercase English letters
    - 1 <= k <= 10^5

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Problem odi aada mele namma brain enu think maadabeeku:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  string s, minimum count k       │
  │  Output ಏನು ಬೇಕು?     →  ಅತಿ ಉದ್ದ substring, ಅದರಲ್ಲಿ    │
  │                           ಪ್ರತಿ character ≥ k ಸಲ ಬರಬೇಕು  │
  │  Constraints ಏನಿದೆ?   →  ಒಂದೇ character k ಗಿಂತ ಕಡಿಮೆ    │
  │                           ಬಂದ್ರೆ ಆ substring INVALID     │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ಮೊದಲ simple idea ಏನು?
  →  ಪ್ರತಿ starting point ಇಂದ, window ಅನ್ನ grow ಮಾಡ್ತಾ ಹೋಗಿ,
     ಪ್ರತಿ ಸಲ ಎಲ್ಲಾ character counts ≥ k ಇದ್ಯಾ ಚೆಕ್ ಮಾಡಿ
  →  ಇದು normal sliding window ಗಿಂತ ಸ್ವಲ್ಪ ಕಷ್ಟ — ಯಾಕಂದ್ರೆ
     window ಅನ್ನ ಯಾವಾಗ SHRINK ಮಾಡಬೇಕು ಅಂತ simple rule ಇಲ್ಲ
     (ಒಂದು character ಕಡಿಮೆ ಇದ್ರೆ, ಅದು ಪೂರ್ತಿ window ಅನ್ನ
     invalid ಮಾಡುತ್ತೆ, ಆದ್ರೆ ಮುಂದೆ ಹೋದ್ರೆ fix ಆಗಬಹುದು!)

  ಹಂತ 3 — Smart trick: "distinct characters count FIX ಮಾಡಿದ್ರೆ?"
  →  "String ನಲ್ಲಿ ಗರಿಷ್ಠ 26 distinct lowercase letters ಮಾತ್ರ
      ಇರಬಹುದು" ಅಂತ ಗಮನಿಸಿ
  →  "distinct characters ಸಂಖ್ಯೆ EXACTLY t ಅಂತ FIX ಮಾಡಿದ್ರೆ,
      ಈಗ normal sliding window (window ಒಳಗೆ distinct count ≤ t
      ಇರೋ ಹಾಗೆ shrink ಮಾಡಿ) apply ಮಾಡಬಹುದಲ್ವಾ?"
  →  t = 1 ಇಂದ 26 ವರೆಗೆ ಪ್ರತಿ value ಗೂ ಒಂದು sliding window pass
     ಮಾಡಿ, ಆ window ಒಳಗೆ ಎಲ್ಲಾ characters ≥ k ಸಲ ಬಂದಿದ್ಯಾ ಚೆಕ್
     ಮಾಡಿ max length track ಮಾಡಿ

  ಹಂತ 4 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  distinct character count FIX ಮಾಡಿದ ಮೇಲೆ, window shrink
     ಮಾಡೋ rule ಸ್ಪಷ್ಟ ಆಗುತ್ತೆ: "distinct count > t ಆದ್ರೆ shrink
     ಮಾಡು" — ಇದೇ normal variable sliding window!
  →  26 (constant) ಸಲ sliding window run ಮಾಡಿದ್ರೂ, ಒಟ್ಟು time
     O(26n) = O(n) ಆಗಿ ಉಳಿಯುತ್ತೆ

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು:
  →  "The tricky part is that a window's validity isn't
      monotonic as we shrink it — so I fix the number of
      DISTINCT characters allowed in the window first"
  →  "For each possible distinct-character count from 1 to 26,
      run a standard variable sliding window, shrinking whenever
      distinct count exceeds the target"
  →  "A window is valid exactly when every character it contains
      has reached the required frequency k — track that count too"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Sliding Window (Variable) — fixed distinct-char budget
  Secondary : Brute-force substring frequency scan

  WHY fix the distinct-character count?
  → A plain variable sliding window needs a monotonic shrink
    rule ("if condition X breaks, shrink until it's fixed").
    Here, one under-represented character can invalidate an
    otherwise-good window, but growing further might fix it —
    that's NOT monotonic. Fixing "exactly t distinct characters
    allowed" restores a clean, monotonic shrink condition.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  The key insight: since there are at most 26 lowercase letters,
  we can afford to try EVERY possible "distinct character budget"
  (1 through 26) separately. For a FIXED budget t, the sliding
  window rule becomes simple and monotonic again: grow the
  window, and if the number of distinct characters inside ever
  exceeds t, shrink from the left until it's back to t. Within
  each such window, we separately track how many of those t
  distinct characters have ALREADY reached frequency k — if all
  of them have, the window is valid, and we record its length.

  The journey from brute to optimal:
    Brute thought   →  For every substring (all O(n^2) of them),
                       count character frequencies and check if
                       all satisfy ≥ k
    Problem with it →  O(n^2) substrings, each needing an O(26)
                       (or worse) frequency check → O(26 n^2)
    Better question →  "Can I make the shrink condition
                       monotonic so a normal sliding window
                       works?"
    Insight         →  Fix the number of allowed distinct
                       characters — now "distinct > budget" is a
                       clean, monotonic shrink trigger
    Optimal         →  Run the sliding window once per budget
                       (1 to 26, a constant), O(26n) = O(n) total

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE (check every substring)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    For every starting index `left`, extend `right` outward one
    character at a time, maintaining a running frequency array.
    After each extension, check (in O(26)) whether every
    character currently in the window has frequency ≥ k; if so,
    this window is valid — update the max length.

  Pseudocode:
    step 1: max_len = 0
    step 2: for left in range(n):
    step 3:   freq = [0]*26
    step 4:   for right in range(left, n):
    step 5:     freq[s[right]] += 1
    step 6:     if all(f == 0 or f >= k for f in freq):
    step 7:       max_len = max(max_len, right - left + 1)
    step 8: return max_len

  Time  : O(26 * n^2)  →  Why: O(n^2) (left, right) substring
                              starts, O(26) validity check each
  Space : O(26) = O(1)  →  Why: one fixed-size frequency array

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ?
    → Correct, but quadratic in the string length — for
      n = 10^4 this is far too slow. We can reuse the "fixed
      distinct count" trick to bring it down to linear.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 6 — APPROACH 2 — OPTIMAL (Sliding Window, fixed distinct budget)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    For each possible distinct-character budget `t` from 1 to
    26: run a standard variable sliding window over `s`. Track a
    frequency map, how many distinct characters are currently in
    the window, and how many of those have ALREADY reached
    frequency k. Whenever distinct count exceeds `t`, shrink from
    the left. Whenever distinct count equals `t` AND all of them
    have reached k, the window is valid — record its length.

  Key steps:
    1. max_len = 0
    2. for t in range(1, 27):
    3.   left = 0, freq = {}, distinct = 0, at_least_k = 0
    4.   for right in range(n):
    5.     if freq.get(s[right], 0) == 0: distinct += 1
    6.     freq[s[right]] = freq.get(s[right], 0) + 1
    7.     if freq[s[right]] == k: at_least_k += 1
    8.     while distinct > t:
    9.       shrink from left, updating distinct/at_least_k/freq
    10.    if distinct == t and distinct == at_least_k:
    11.      max_len = max(max_len, right - left + 1)
    12. return max_len

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ:
    → "1 ಇಂದ 26 ವರೆಗೆ ಪ್ರತಿ 'distinct character budget' t ಗೂ
       ಒಂದು sliding window run ಮಾಡು. distinct count > t ಆದ್ರೆ
       shrink ಮಾಡು. distinct count == t ಮತ್ತು ಎಲ್ಲಾ ಆ t
       characters ≥ k ಸಲ ಬಂದಿದ್ರೆ ಮಾತ್ರ window valid — length
       track ಮಾಡು!"

  Time  : O(26 n) = O(n)  →  Why: 26 (constant) full sliding-
                                 window passes, each O(n)
  Space : O(26) = O(1)     →  Why: frequency map bounded by
                                 alphabet size

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 7 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: s = "ababbc", k = 2

  Try t = 2 (budget of exactly 2 distinct characters):
    Window grows: "a"(distinct=1) → "ab"(distinct=2) →
    "aba"(distinct=2, a:2,b:1) → "abab"(distinct=2, a:2,b:2) →
    at this point at_least_k=2==distinct=2 → VALID, length 4
    → "ababb"(distinct=2, a:2,b:3) → still valid → length 5
    → next char 'c': distinct would become 3 > budget 2 → shrink
    from left until distinct back to 2 (drops leading 'a's)

  Best window found at t=2: "ababb", length 5

  (Other budgets t=1,3,...,26 are also tried, but none beat 5
   for this particular input)

  Output: 5 ✓

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 8 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ k = 1?                         →  the whole string always
                                       qualifies (every char
                                       appears ≥ 1 time)
  ✓ No valid substring "abcde",k=2? →  0 — every char appears
                                       only once
  ✓ Whole string already valid
    "aaabb",k... (all chars ≥ k)?  →  the entire string's length
  ✓ Single character "a", k=1?     →  1
  ✓ Single character "a", k=2?     →  0 — can't reach k=2 with
                                       only one occurrence

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 9 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                              Time        Space
  Brute (all substrings)     O(26 n^2)    O(26)
  Optimal (26x sliding win)  O(26 n)      O(26)   ← use this ✅

  Both bound by the 26-letter alphabet as a constant factor —
  the real win is n^2 → n

  Time yaake O(26n)?  → 26 separate O(n) sliding-window passes,
                         one per distinct-character budget
  Space yaake O(26)?  → Frequency map holds at most 26 keys
                         (lowercase English letters)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 10 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Fix-a-Parameter Sliding Window

  Ee pattern yaavaaga use maadabeeku?
  → Sliding window ge NORMAL monotonic shrink rule sigadhe
     iddaga ("condition break aadre shrink madu" clean aagi
     define aagadhe iddaga) → ondu bounded parameter (distinct
     count, sum, etc.) FIX madi, aa parameter ge separate
     sliding window run madu
  → Alphabet-bounded problems (≤26 lowercase letters) — constant
     factor loops are still O(n) overall

  Idee pattern beere problemsalli kaanisatte:
  → Subarrays with K Different Integers #992 (similar "exactly
     K distinct" trick, using at-most(K) - at-most(K-1))
  → Longest Palindromic Substring #5 (next problem in curriculum
     — different technique, expand-from-center)

  Next time intaha problem bandre naanu modalu idannu think maadtene:
  → "Sliding window shrink rule monotonic aagadhe iddaga →
     ondu bounded parameter FIX madi, aa fixed value ge
     separate clean sliding window run madu — alphabet bounded
     aadre (26) constant factor matra!"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 11 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "Find the longest substring where every character present
      occurs at least k times."

  2. Brute force:
     "Check every substring, verify all character frequencies
      are ≥ k. O(26 n^2) — too slow for the constraints."

  3. Optimize:
     "The shrink rule isn't monotonic directly, so I fix the
      number of distinct characters allowed (1 to 26) and run a
      clean sliding window for each fixed budget — shrink when
      distinct count exceeds the budget, and track how many of
      those characters have reached frequency k."

  4. Code:
     "Outer loop over budget t = 1..26. Inner sliding window
      with freq map, distinct count, and at_least_k count.
      Window valid when distinct == t == at_least_k."

  5. Complexity:
     "Time O(26n) = O(n) — 26 constant sliding-window passes.
      Space O(26) = O(1) — bounded frequency map."

  Mukhya: shrink rule monotonic illa antadre, ondu bounded
          parameter fix madi separate clean window run madu —
          constant-factor loops still give linear overall time!
"""


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(26 n^2) Time | O(26) Space (check every substring)
# ═══════════════════════════════════════════════════════════════════
def longest_substring_brute(s, k):
    """
    Idu modala aaloochane — prati (left,right) window ge freq
    array update madi, ella chars >= k antha O(26) check madu
    """
    n = len(s)
    max_len = 0

    for left in range(n):
        freq = [0] * 26
        for right in range(left, n):
            freq[ord(s[right]) - ord('a')] += 1
            if all(f == 0 or f >= k for f in freq):
                max_len = max(max_len, right - left + 1)

    return max_len


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(26n) = O(n) Time | O(26) Space (sliding window, fixed budget)
# ═══════════════════════════════════════════════════════════════════
def longest_substring(s, k):
    """
    Idu final answer — 1 inda 26 varge prati distinct-character
    budget t ge, ondu clean sliding window run madu
    """
    n = len(s)
    max_len = 0

    for t in range(1, 27):
        left = 0
        freq = {}
        distinct = 0
        at_least_k = 0

        for right in range(n):
            ch = s[right]
            if freq.get(ch, 0) == 0:
                distinct += 1
            freq[ch] = freq.get(ch, 0) + 1
            if freq[ch] == k:
                at_least_k += 1

            while distinct > t:
                left_ch = s[left]
                if freq[left_ch] == k:
                    at_least_k -= 1
                freq[left_ch] -= 1
                if freq[left_ch] == 0:
                    distinct -= 1
                left += 1

            if distinct == t and distinct == at_least_k:
                max_len = max(max_len, right - left + 1)

    return max_len


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # Test 1 — Basic
    assert longest_substring("aaabb", 3) == 3

    # Test 2 — Mixed characters, valid window in the middle
    assert longest_substring("ababbc", 2) == 5

    # Test 3 — No valid substring at all
    assert longest_substring("abcde", 2) == 0

    # Test 4 — k = 1, whole string always qualifies
    assert longest_substring("abcde", 1) == 5

    # Test 5 — Single character, exactly meets k
    assert longest_substring("a", 1) == 1

    # Test 6 — Single character, cannot meet k
    assert longest_substring("a", 2) == 0

    # Cross-check: brute force must agree on all of the above
    assert longest_substring_brute("aaabb", 3) == 3
    assert longest_substring_brute("ababbc", 2) == 5
    assert longest_substring_brute("abcde", 2) == 0
    assert longest_substring_brute("abcde", 1) == 5
    assert longest_substring_brute("a", 1) == 1
    assert longest_substring_brute("a", 2) == 0

    print("All tests passed!")
