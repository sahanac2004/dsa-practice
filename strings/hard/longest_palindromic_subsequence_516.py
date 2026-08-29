"""
╔════════════════════════════════════════════════════════════════════╗
║  LONGEST PALINDROMIC SUBSEQUENCE                                   ║
║  LeetCode #516  |  Difficulty: Hard  |  Topic: DP/LCS              ║
║  Link: https://leetcode.com/problems/                              ║
║        longest-palindromic-subsequence/                            ║
╚════════════════════════════════════════════════════════════════════╝

  NOTE: This is literally the internal computation from #21
  (Minimum Insertions to Make String Palindrome) — that problem
  computed dp[n][n] = LCS(s, reverse(s)) and returned n minus it.
  Here, we're asked for dp[n][n] itself, directly.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Given a string `s`, find the length of the LONGEST
  PALINDROMIC SUBSEQUENCE in it. A subsequence does NOT need to
  be contiguous — you can skip characters, but must keep the
  remaining ones in their original relative order.

  Input : s = a string
  Output: integer — length of the longest palindromic subsequence

  Example 1 — basic:
    Input : s = "bbbab"
    Output: 4
    Why?  : "bbbb" (skip the 'a') is a palindromic subsequence
            of length 4 — the longest possible here

  Example 2 — slightly tricky (short answer):
    Input : s = "cbbd"
    Output: 2
    Why?  : "bb" (the two middle characters) is the longest
            palindromic subsequence — "cbbd" itself isn't a
            palindrome, and no length-3+ palindromic subsequence
            exists

  Example 3 — already a palindrome:
    Input : s = "racecar"
    Output: 7
    Why?  : the whole string is already a palindrome, so it IS
            its own longest palindromic subsequence

  Constraints:
    - 1 <= s.length <= 1000
    - s consists only of lowercase English letters

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Problem odi aada mele namma brain enu think maadabeeku:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  ಒಂದು string s                   │
  │  Output ಏನು ಬೇಕು?     →  ಅತಿ ಉದ್ದ PALINDROMIC             │
  │                           SUBSEQUENCE ರ length (contiguous  │
  │                           ಆಗಿ ಇರಬೇಕಾಗಿಲ್ಲ!)              │
  │  Constraints ಏನಿದೆ?   →  characters SKIP ಮಾಡಬಹುದು, ಆದ್ರೆ │
  │                           order ಬದಲಾಗಬಾರದು                │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ಇದನ್ನ previous problem (#21 Minimum Insertions) ಜೊತೆ
           ಸಂಪೂರ್ಣ CONNECT ಮಾಡಿ ನೋಡಿ!
  →  #21 ರಲ್ಲಿ, "n - Longest Palindromic Subsequence length" ಅನ್ನ
     answer ಆಗಿ return ಮಾಡಿದ್ವಿ
  →  ಆ LPS length ಅನ್ನೇ ಇಲ್ಲಿ ನೇರವಾಗಿ ಕೇಳ್ತಾ ಇದ್ದಾರೆ! Same DP
     table, ಬರೀ FINAL return statement ಬೇರೆ

  ಹಂತ 3 — LPS(s) ಅನ್ನ ಹೇಗೆ ಕಂಡುಹಿಡಿಯೋದು?
  →  "s ರ LPS", "s ಮತ್ತು reverse(s) ರ LONGEST COMMON
      SUBSEQUENCE (LCS)" ಗೆ ಸಮ! ಯಾಕಂದ್ರೆ s ಒಳಗಿನ ಯಾವುದೇ
      subsequence, reverse(s) ಒಳಗೂ (reverse order ನಲ್ಲಿ)
      ಸಿಗುತ್ತೆ ಅಂದ್ರೆ ಅದೇ palindrome!
  →  classic 2D LCS DP table ಬಳಸಿ s ಮತ್ತು reverse(s) ರ LCS
     ಕಂಡುಹಿಡಿಯಿರಿ

  ಹಂತ 4 — ಮೊದಲ simple idea (brute recursion) ಏನು?
  →  helper(i,j) = "s[i..j] ರ longest palindromic subsequence
      length"
  →  s[i]==s[j] ಆದ್ರೆ: 2 + helper(i+1,j-1) (ಎರಡೂ ends ಸೇರಿಸಿ,
     ಒಳಗಿನ ಭಾಗ recurse ಮಾಡು)
  →  ಇಲ್ಲಾಂದ್ರೆ: max(helper(i+1,j), helper(i,j-1)) (ಒಂದು end
     skip ಮಾಡಿ ನೋಡು)
  →  memoization ಇಲ್ಲದೇ exponential (overlapping subproblems
     ಪುನಃ ಪುನಃ compute)

  ಹಂತ 5 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  ಅದೇ recursion ರ overlapping subproblems ಅನ್ನ, s ಮತ್ತು
     reverse(s) ನಡುವಿನ LCS DP table ಆಗಿ ಪುನಃ ಬರೆದ್ರೆ, ಒಮ್ಮೆ
     ಮಾತ್ರ compute ಮಾಡಿ reuse ಮಾಡಬಹುದು — O(n^2) ಗೆ ಇಳಿಸಬಹುದು

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು:
  →  "Longest palindromic subsequence of s equals LCS(s,
      reverse(s)) — a classic reduction"
  →  "Build the standard O(n^2) LCS DP table between s and its
      reverse, and dp[n][n] IS the answer directly"
  →  "This is the exact same table I built for the 'minimum
      insertions' variant of this problem — just returning it
      raw instead of subtracting from n"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Dynamic Programming — LCS(s, reverse(s))
  Secondary : Naive recursion (no memoization)

  WHY LCS(s, reverse(s))?
  → Any subsequence common to both s and reverse(s) reads the
    same forwards (as part of s) and backwards (as part of
    reverse(s)) — that's exactly the definition of a palindromic
    subsequence. The LONGEST such common subsequence is
    therefore the longest palindromic subsequence, directly
    solvable with the standard two-string LCS DP recurrence.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  The key insight: a palindrome reads identically forwards and
  backwards — so any palindromic subsequence of s, when read
  backwards, is ALSO a valid subsequence of reverse(s) (using the
  same underlying characters, just traversed from the other
  end). This means the search for "longest palindromic
  subsequence" collapses exactly onto "longest common
  subsequence between s and its reverse" — a much more familiar
  and well-studied DP problem.

  The journey from brute to optimal:
    Brute thought   →  Recursive helper(i, j): if ends match,
                       add 2 and recurse inward; otherwise skip
                       one end or the other and take the max
    Problem with it →  Massive overlapping subproblems
                       recomputed repeatedly → exponential time
    Better question →  "Isn't this just the LCS recurrence
                       between s and its own reverse?"
    Insight         →  LPS(s) = LCS(s, reverse(s)); reuse the
                       classic O(n^2) LCS DP table
    Optimal         →  O(n^2) time, O(n^2) space (or O(n) with
                       rolling rows)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE (naive recursion)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Recursively solve on the shrinking window [i, j]. If the
    ends match, both belong to the palindrome — add 2 and
    recurse inward. Otherwise, skip one end or the other and
    take whichever gives the longer subsequence.

  Pseudocode:
    step 1: def helper(i, j):
    step 2:   if i > j: return 0
    step 3:   if i == j: return 1
    step 4:   if s[i] == s[j]: return 2 + helper(i+1, j-1)
    step 5:   return max(helper(i+1, j), helper(i, j-1))
    step 6: return helper(0, n-1)

  Time  : O(2^n)  →  Why: each mismatched pair branches into two
                          recursive calls, with massive overlap
                          between subproblems left uncached
  Space : O(n)     →  Why: recursion depth up to n

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ?
    → Exponential blowup from recomputing the SAME (i,j)
      subproblems repeatedly — the classic DP fix maps this
      directly onto the well-known LCS table structure.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 6 — APPROACH 2 — OPTIMAL (DP — LCS with reverse)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Build `rev = reverse(s)`. Fill the standard LCS DP table
    between `s` and `rev`: dp[i][j] = LCS length of s[:i] and
    rev[:j]. The final dp[n][n] IS the longest palindromic
    subsequence length — return it directly.

  Key steps:
    1. rev = s[::-1]
    2. dp = (n+1) x (n+1) table of zeros
    3. for i in 1..n, for j in 1..n:
    4.   if s[i-1] == rev[j-1]: dp[i][j] = dp[i-1][j-1] + 1
    5.   else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    6. return dp[n][n]

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ:
    → "s ರ reverse build ಮಾಡು. s ಮತ್ತು reverse(s) ನಡುವೆ classic
       LCS DP table ಕಟ್ಟು — characters ಸಮ ಇದ್ರೆ diagonal+1,
       ಇಲ್ಲಾಂದ್ರೆ ಮೇಲಿನ/ಎಡ ಗರಿಷ್ಠ. ಕೊನೆಯ dp[n][n] ನೇ ಉತ್ತರ —
       #21 ರಂತೆ n ಇಂದ ಕಳೆಯೋ ಅಗತ್ಯ ಇಲ್ಲ ಇಲ್ಲಿ!"

  Time  : O(n^2)  →  Why: filling an (n+1) x (n+1) DP table,
                          O(1) work per cell
  Space : O(n^2)  →  Why: the full 2D DP table (can be optimized
                          to O(n) using two rolling rows)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 7 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: s = "bbbab"   (n = 5)

  rev = "babbb"

  Building the LCS DP table between "bbbab" and "babbb": the
  final dp[5][5] comes out to 4 — the longest palindromic
  subsequence is "bbbb" (using s indices 0, 1, 2, 4 — skipping
  the 'a' at index 3).

  Output: 4 ✓

  ಇನ್ನೊಂದು example — short answer:
  Input: s = "cbbd"

  rev = "dbbc"
  LCS(s, rev) → the middle "bb" overlaps on both sides →
  dp[4][4] = 2

  Output: 2 ✓

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 8 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ Already a palindrome "racecar"? →  7 — the whole string is
                                        its own LPS
  ✓ Single character "a"?           →  1 — trivially itself
  ✓ No repeated characters "abcd"?  →  1 — any single character
                                        (nothing pairs up)
  ✓ All same character "aaaa"?      →  4 — the whole string
                                        qualifies
  ✓ Two identical characters "aa"?  →  2 — both characters form
                                        the palindrome together

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 9 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                        Time    Space
  Brute (recursion)      O(2^n)  O(n)
  Optimal (LCS DP)        O(n^2)  O(n^2)   ← use this ✅

  Time yaake O(n^2)?  → (n+1) x (n+1) DP table, O(1) transition
                         per cell
  Space yaake O(n^2)? → Full 2D table stored (optimizable to
                         O(n) with two rolling rows)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 10 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Longest Palindromic Subsequence via LCS(s, reverse(s))

  Ee pattern yaavaaga use maadabeeku?
  → Any "palindromic SUBSEQUENCE" (not substring!) question —
     contiguity doesn't matter, only relative character order
  → "Minimum insertions/deletions to make a string palindrome"
     family — this LPS value is the core building block

  Idee pattern beere problemsalli kaanisatte:
  → Minimum Insertions to Make String Palindrome #1312
     (previous problem — SAME dp[n][n] table, computes
     n - dp[n][n] instead of dp[n][n] directly)
  → Longest Palindromic Substring #5 (contrast — that one needs
     CONTIGUOUS characters, solved with expand-around-center
     instead of DP)
  → Palindromic Substrings #647 (also substring-based, same
     expand-around-center family as #5)

  Next time intaha problem bandre naanu modalu idannu think maadtene:
  → "Palindromic SUBSEQUENCE (contiguous illa) bekagidre → LPS(s)
     = LCS(s, reverse(s)) — classic 2D DP table use madu! (SUBSTRING
     bekagidre matra, expand-around-center try madu instead.)"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 11 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "Find the length of the longest subsequence of s that is a
      palindrome — characters can be skipped, but relative order
      must be preserved."

  2. Brute force:
     "Recursive helper(i,j): if ends match, add 2 and recurse
      inward; otherwise skip one end, take the max. Exponential
      without memoization."

  3. Optimize:
     "This equals LCS(s, reverse(s)) — build the standard LCS DP
      table between s and its reverse. dp[n][n] is the answer,
      no further adjustment needed."

  4. Code:
     "rev = s[::-1]. Standard (n+1)x(n+1) LCS DP: match →
      diagonal+1, else → max(up, left). Return dp[n][n] directly."

  5. Complexity:
     "Time O(n^2) — filling the DP table. Space O(n^2), or O(n)
      with a rolling-row optimization."

  Mukhya: Longest Palindromic SUBSEQUENCE = LCS(s, reverse(s)) —
          this single DP table quietly powers several palindrome-
          insertion/deletion problems across the curriculum!
"""


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(2^n) Time | O(n) Space (naive recursion, no memo)
# ═══════════════════════════════════════════════════════════════════
def longest_palindromic_subsequence_brute(s):
    """
    Idu modala aaloochane — [i,j] window mele recursion, ends
    match aadre 2+inward, illa andre max(skip left, skip right)
    """
    def helper(i, j):
        if i > j:
            return 0
        if i == j:
            return 1
        if s[i] == s[j]:
            return 2 + helper(i + 1, j - 1)
        return max(helper(i + 1, j), helper(i, j - 1))

    return helper(0, len(s) - 1)


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n^2) Time | O(n^2) Space (DP — LCS with reverse)
# ═══════════════════════════════════════════════════════════════════
def longest_palindromic_subsequence(s):
    """
    Idu final answer — s mattu reverse(s) naduve classic LCS DP
    table build madi, dp[n][n] ne answer, direct return madu
    """
    n = len(s)
    rev = s[::-1]
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if s[i - 1] == rev[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[n][n]


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # Test 1 — Basic
    assert longest_palindromic_subsequence("bbbab") == 4

    # Test 2 — Short answer
    assert longest_palindromic_subsequence("cbbd") == 2

    # Test 3 — Already a palindrome
    assert longest_palindromic_subsequence("racecar") == 7

    # Test 4 — Single character
    assert longest_palindromic_subsequence("a") == 1

    # Test 5 — No repeated characters
    assert longest_palindromic_subsequence("abcd") == 1

    # Cross-check: brute force must agree on all of the above
    assert longest_palindromic_subsequence_brute("bbbab") == 4
    assert longest_palindromic_subsequence_brute("cbbd") == 2
    assert longest_palindromic_subsequence_brute("racecar") == 7
    assert longest_palindromic_subsequence_brute("a") == 1
    assert longest_palindromic_subsequence_brute("abcd") == 1

    print("All tests passed!")
