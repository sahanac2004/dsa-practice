"""
╔════════════════════════════════════════════════════════════════════╗
║  MINIMUM INSERTION STEPS TO MAKE A STRING PALINDROME               ║
║  LeetCode #1312  |  Difficulty: Hard  |  Topic: DP/LCS             ║
║  Link: https://leetcode.com/problems/                              ║
║        minimum-insertion-steps-to-make-a-string-palindrome/        ║
╚════════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Given a string `s`, find the MINIMUM number of characters that
  must be INSERTED (anywhere in the string, not just at the
  front) to make it a palindrome.

  Unlike #16 (Minimum Characters to Add at FRONT), insertions
  here can go ANYWHERE — which allows a much smaller answer in
  many cases.

  Input : s = a string
  Output: integer — minimum insertions needed

  Example 1 — basic (already a palindrome):
    Input : s = "zzazz"
    Output: 0
    Why?  : the string already reads the same forwards and
            backwards — nothing to insert

  Example 2 — slightly tricky (a few insertions needed):
    Input : s = "mbadm"
    Output: 2
    Why?  : inserting 2 characters can turn it into a palindrome,
            e.g. "mbdadbm" — the key is that "mbadm" already
            contains a length-3 palindromic SUBSEQUENCE "m_a_m"
            (not contiguous!), so only the other 2 characters
            need mirrored partners

  Example 3 — no useful subsequence overlap:
    Input : s = "leetcode"
    Output: 5
    Why?  : very little of "leetcode" is already "palindrome-
            friendly" (longest palindromic subsequence has
            length 3, e.g. "e_e" via "eet...e"-ish), so most
            characters need a mirrored partner inserted

  Constraints:
    - 1 <= s.length <= 500
    - s consists of lowercase English letters

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Problem odi aada mele namma brain enu think maadabeeku:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  ಒಂದು string s                   │
  │  Output ಏನು ಬೇಕು?     →  ಎಲ್ಲಿ ಬೇಕಾದ್ರೂ characters       │
  │                           insert ಮಾಡಿ palindrome ಮಾಡೋಕೆ  │
  │                           ಬೇಕಾದ MINIMUM count             │
  │  Constraints ಏನಿದೆ?   →  #16 ಗಿಂತ ಭಿನ್ನ — ಇಲ್ಲಿ FRONT     │
  │                           ಮಾತ್ರ ಅಲ್ಲ, ಎಲ್ಲಿ ಬೇಕಾದ್ರೂ insert│
  │                           ಮಾಡಬಹುದು — ಆದ್ರೆ ಸಣ್ಣ answer!   │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — Key observation ಏನಿದೆ?
  →  "s ಒಳಗೆ ಈಗಾಗಲೇ ಎಷ್ಟು ಉದ್ದದ PALINDROMIC SUBSEQUENCE
      (contiguous ಆಗಿ ಇಲ್ಲದೇ ಇದ್ರೂ ಪರವಾಗಿಲ್ಲ) ಇದ್ಯೋ, ಆ ಭಾಗ
      ಈಗಾಗ್ಲೇ 'palindrome-ready' — ಉಳಿದ characters ಗೆ ಮಾತ್ರ
      mirror partner insert ಮಾಡಬೇಕು"
  →  So answer = n - (Longest Palindromic Subsequence ರ length)

  ಹಂತ 3 — Longest Palindromic Subsequence (LPS) ಹೇಗೆ
           ಕಂಡುಹಿಡಿಯೋದು?
  →  "s ರ LPS", "s ಮತ್ತು reverse(s) ರ LONGEST COMMON
      SUBSEQUENCE (LCS)" ಗೆ ಸಮ ಆಗಿರುತ್ತೆ! ಯಾಕಂದ್ರೆ, s ರ ಒಳಗಿನ
      ಯಾವುದೇ subsequence, reverse(s) ರ ಒಳಗೆ ಕೂಡ (reverse
      order ನಲ್ಲಿ) ಸಿಗುತ್ತೆ ಅಂದ್ರೆ ಅದು palindrome ಆಗಿರುತ್ತೆ
  →  So classic LCS DP (2D table) ಬಳಸಿ s ಮತ್ತು reverse(s) ರ
     LCS ಕಂಡುಹಿಡಿಯಿರಿ

  ಹಂತ 4 — ಮೊದಲ simple idea (brute) ಏನು?
  →  Recursion: helper(i,j) = "s[i..j] ಅನ್ನ palindrome ಮಾಡೋಕೆ
      ಎಷ್ಟು insertions ಬೇಕು"
  →  s[i]==s[j] ಆದ್ರೆ ಒಳಗಿನ helper(i+1,j-1) ಸಾಕು (ends already
     match)
  →  ಇಲ್ಲಾಂದ್ರೆ, either s[i] ಗೆ mirror insert ಮಾಡು (helper(i,j-1))
     ಅಥವಾ s[j] ಗೆ mirror insert ಮಾಡು (helper(i+1,j)) — ಇವೆರಡರ
     minimum + 1
  →  ಇದು memoization ಇಲ್ಲದೇ exponential ಆಗುತ್ತೆ (overlapping
     subproblems ಪುನಃ ಪುನಃ compute ಆಗುತ್ತೆ)

  ಹಂತ 5 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  Recursion ರ overlapping subproblems ಅನ್ನ DP table
     (bottom-up LCS) ಮೂಲಕ ಒಮ್ಮೆ ಮಾತ್ರ compute ಮಾಡಿ reuse
     ಮಾಡಿದ್ರೆ, O(n^2) ಗೆ ಇಳಿಸಬಹುದು

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು:
  →  "The characters that DON'T need insertions are exactly the
      ones forming the longest palindromic subsequence"
  →  "Longest palindromic subsequence of s equals the LCS of s
      and its reverse — classic DP table"
  →  "Answer = n minus that LCS length"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Dynamic Programming — LCS(s, reverse(s))
  Secondary : Naive recursion (no memoization)

  WHY LCS(s, reverse(s))?
  → Any subsequence of s that's also a subsequence of reverse(s)
    reads the same forwards and backwards by construction — it's
    exactly a palindromic subsequence of s. The LONGEST such
    overlap is therefore the longest palindromic subsequence,
    computable with the standard LCS DP recurrence.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  The key insight: every character NOT part of the longest
  palindromic subsequence needs exactly one inserted mirror
  partner to balance it out. So minimizing insertions is the
  same as MAXIMIZING how many characters are already "free" —
  i.e., finding the longest palindromic subsequence (LPS). And
  LPS(s) has a beautiful reduction: it equals LCS(s, reverse(s)),
  turning a palindrome problem into a classic two-string DP.

  The journey from brute to optimal:
    Brute thought   →  Recursive helper(i, j): if ends match,
                       recurse inward; otherwise try inserting a
                       mirror for either end and take the min + 1
    Problem with it →  Massive overlapping subproblems recomputed
                       repeatedly → exponential time without
                       memoization
    Better question →  "Isn't this exactly the LCS recurrence,
                       applied to s and its reverse?"
    Insight         →  LPS(s) = LCS(s, reverse(s)); build the
                       standard O(n^2) LCS DP table
    Optimal         →  O(n^2) time, O(n^2) space (or O(n) with
                       rolling rows)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE (naive recursion)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Recursively solve on the shrinking window [i, j]. If the
    ends match, no insertion needed there — recurse inward. If
    they don't, we must insert a mirror for one end or the
    other — try both and take the cheaper option, plus 1.

  Pseudocode:
    step 1: def helper(i, j):
    step 2:   if i >= j: return 0
    step 3:   if s[i] == s[j]: return helper(i+1, j-1)
    step 4:   return 1 + min(helper(i+1, j), helper(i, j-1))
    step 5: return helper(0, n-1)

  Time  : O(2^n)  →  Why: each mismatched pair branches into two
                          recursive calls, with massive overlap
                          between subproblems left uncached
  Space : O(n)     →  Why: recursion depth up to n

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ?
    → Exponential blowup — the SAME (i,j) subproblems get
      recomputed over and over. The classic fix is memoization/
      bottom-up DP, and this problem maps directly onto the
      well-known LCS DP structure.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 6 — APPROACH 2 — OPTIMAL (DP — LCS with reverse)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Build `rev = reverse(s)`. Fill a standard LCS DP table
    between `s` and `rev`: dp[i][j] = LCS length of s[:i] and
    rev[:j]. The final dp[n][n] is the longest palindromic
    subsequence length. Answer = n - dp[n][n].

  Key steps:
    1. rev = s[::-1]
    2. dp = (n+1) x (n+1) table of zeros
    3. for i in 1..n, for j in 1..n:
    4.   if s[i-1] == rev[j-1]: dp[i][j] = dp[i-1][j-1] + 1
    5.   else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    6. return n - dp[n][n]

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ:
    → "s ರ reverse build ಮಾಡು. s ಮತ್ತು reverse(s) ನಡುವೆ classic
       LCS DP table ಕಟ್ಟು — characters ಸಮ ಇದ್ರೆ diagonal+1,
       ಇಲ್ಲಾಂದ್ರೆ ಮೇಲಿನ/ಎಡ ಗರಿಷ್ಠ. ಕೊನೆಯ dp[n][n] ಅಂದ್ರೆ
       Longest Palindromic Subsequence ರ length. n ಇಂದ ಅದನ್ನ
       ಕಳೆದ್ರೆ answer ಸಿಗುತ್ತೆ!"

  Time  : O(n^2)  →  Why: filling an (n+1) x (n+1) DP table,
                          O(1) work per cell
  Space : O(n^2)  →  Why: the full 2D DP table (can be optimized
                          to O(n) using two rolling rows)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 7 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: s = "mbadm"   (n = 5)

  rev = "mdabm"

  Building the LCS DP table between "mbadm" and "mdabm" (rows
  indexed by s, columns by rev), the final dp[5][5] comes out to
  3 — the longest palindromic subsequence is "m_a_m" (using s
  indices 0, 2, 4: 'm','a','m').

  Answer: n - LCS = 5 - 3 = 2

  Output: 2 ✓  (matches: e.g. "mbdadbm" is a valid palindrome
  formed by inserting 2 characters)

  ಇನ್ನೊಂದು example — already a palindrome:
  Input: s = "zzazz"

  rev = "zzazz" (same, since s is already a palindrome!)
  LCS(s, rev) = LCS(s, s) = len(s) = 5 (the whole string matches
  itself trivially)

  Answer: 5 - 5 = 0

  Output: 0 ✓

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 8 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ Already a palindrome "zzazz"?  →  0 — LCS(s, reverse(s)) = n
  ✓ Single character "a"?          →  0 — trivially a palindrome
  ✓ No repeated characters "abcd"? →  3 — LPS length 1 (any
                                       single char), n-1=3
  ✓ All same character "aaaa"?     →  0 — already a palindrome
  ✓ Worst case, little overlap
    ("leetcode")?                  →  5 — small LPS relative to
                                       string length

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 9 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                        Time    Space
  Brute (recursion)      O(2^n)  O(n)
  Optimal (LCS DP)        O(n^2)  O(n^2)   ← use this ✅

  Time yaake O(n^2)?  → (n+1) x (n+1) DP table, O(1) transition
                         per cell
  Space yaake O(n^2)? → Full 2D table stored (optimizable to
                         O(n) with two rolling rows, not shown
                         here for clarity)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 10 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Longest Palindromic Subsequence via LCS(s, reverse(s))

  Ee pattern yaavaaga use maadabeeku?
  → "Minimum insertions/deletions to make a string palindrome"
     family — always reduces to finding the LPS, and LPS always
     reduces to LCS(s, reverse(s))
  → Any "palindromic SUBSEQUENCE" (not substring!) question —
     contiguity doesn't matter, only relative order

  Idee pattern beere problemsalli kaanisatte:
  → Longest Palindromic Subsequence #516 (next problem in
     curriculum — literally THE SAME dp[n][n] value this problem
     computes internally, asked directly!)
  → Minimum Characters to Add at Front to Make Palindrome
     (contrast — that one only allows FRONT insertions and uses
     KMP LPS array, a totally different technique for a related
     but distinct constraint)

  Next time intaha problem bandre naanu modalu idannu think maadtene:
  → "Palindrome ge insertions/deletions minimize madbekagidre →
     Longest Palindromic Subsequence hudku! LPS(s) = LCS(s,
     reverse(s)) — classic 2D DP table use madu."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 11 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "Find the minimum characters to insert ANYWHERE in s to
      make it a palindrome — insertions aren't restricted to the
      front, unlike a related earlier problem."

  2. Brute force:
     "Recursive helper(i,j): if ends match, recurse inward;
      otherwise insert a mirror for one end, take the cheaper
      branch + 1. Exponential without memoization."

  3. Optimize:
     "Characters not needing insertion are exactly the longest
      palindromic subsequence. LPS(s) equals LCS(s, reverse(s)),
      so build the standard LCS DP table between s and its
      reverse. Answer = n - dp[n][n]."

  4. Code:
     "rev = s[::-1]. Standard (n+1)x(n+1) LCS DP: match →
      diagonal+1, else → max(up, left). Return n - dp[n][n]."

  5. Complexity:
     "Time O(n^2) — filling the DP table. Space O(n^2), or O(n)
      with a rolling-row optimization."

  Mukhya: 'minimum insertions/deletions for palindrome' problems
          always boil down to Longest Palindromic Subsequence —
          and LPS is just LCS(s, reverse(s)) in disguise!
"""


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(2^n) Time | O(n) Space (naive recursion, no memo)
# ═══════════════════════════════════════════════════════════════════
def min_insertions_brute(s):
    """
    Idu modala aaloochane — [i,j] window mele recursion, ends
    match aadre inward hogu, illa andre mirror insert try madu
    """
    def helper(i, j):
        if i >= j:
            return 0
        if s[i] == s[j]:
            return helper(i + 1, j - 1)
        return 1 + min(helper(i + 1, j), helper(i, j - 1))

    return helper(0, len(s) - 1)


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n^2) Time | O(n^2) Space (DP — LCS with reverse)
# ═══════════════════════════════════════════════════════════════════
def min_insertions(s):
    """
    Idu final answer — s mattu reverse(s) naduve classic LCS DP
    table build madi, n - LCS(s, reverse(s)) return madu
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

    longest_palindromic_subsequence = dp[n][n]
    return n - longest_palindromic_subsequence


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # Test 1 — Already a palindrome
    assert min_insertions("zzazz") == 0

    # Test 2 — Basic
    assert min_insertions("mbadm") == 2

    # Test 3 — Little useful overlap
    assert min_insertions("leetcode") == 5

    # Test 4 — Single character
    assert min_insertions("a") == 0

    # Test 5 — No repeated characters
    assert min_insertions("abcd") == 3

    # Cross-check: brute force must agree on all of the above
    assert min_insertions_brute("zzazz") == 0
    assert min_insertions_brute("mbadm") == 2
    assert min_insertions_brute("leetcode") == 5
    assert min_insertions_brute("a") == 0
    assert min_insertions_brute("abcd") == 3

    print("All tests passed!")
