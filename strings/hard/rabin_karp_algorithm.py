"""
╔════════════════════════════════════════════════════════════════════╗
║  RABIN-KARP ALGORITHM (PATTERN MATCHING VIA ROLLING HASH)          ║
║  Classic Algorithm  |  Difficulty: Hard  |  Topic: String Hashing  ║
║  Link: https://cp-algorithms.com/string/rabin-karp.html            ║
╚════════════════════════════════════════════════════════════════════╝

  NOTE: The curriculum sheet lists this as slot #23 with no
  LeetCode number ("—"). It's the classic Rabin-Karp algorithm —
  a HASHING-based alternative to the KMP (#20) and Z-function
  (#19) pattern-matching techniques already covered.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Given a `text` and a `pattern`, find EVERY starting index in
  `text` where `pattern` occurs as a contiguous substring —
  using a ROLLING HASH to avoid full character comparisons at
  most positions.

  Input : text, pattern = two strings
  Output: list of integers — all starting indices in `text`
          where `pattern` occurs

  Example 1 — basic (multiple occurrences):
    Input : text = "ababcababcabc", pattern = "abc"
    Output: [2, 7, 10]
    Why?  : "abc" appears starting at indices 2, 7, and 10 —
            same scenario as the Z-function problem, now solved
            via hashing instead

  Example 2 — slightly tricky (hash collision risk):
    Input : text = "aaaaa", pattern = "aa"
    Output: [0, 1, 2, 3]
    Why?  : overlapping matches everywhere — every window's hash
            must be verified against the actual pattern to rule
            out FALSE POSITIVES (different substrings that
            happen to hash the same)

  Example 3 — no match at all:
    Input : text = "hello", pattern = "world"
    Output: []
    Why?  : "world" never appears as a substring of "hello" —
            hash comparison quickly rules out every window

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
  │  Output ಏನು ಬೇಕು?     →  pattern ಎಲ್ಲಿ ಎಲ್ಲಿ ಸಿಗುತ್ತೋ    │
  │                           ಆ starting indices               │
  │  Constraints ಏನಿದೆ?   →  HASHING ಬಳಸಿ solve ಮಾಡಬೇಕು       │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ಇದನ್ನ previous problems (#19 Z-function, #20 KMP)
           ಜೊತೆ compare ಮಾಡಿ ನೋಡಿ!
  →  ಅಲ್ಲಿ ಎರಡರಲ್ಲೂ character-STRUCTURE (prefix-suffix overlap)
     ಬಳಸಿ ಪ್ರತಿ position ಗೂ match check ಮಾಡಿದ್ವಿ
  →  ಇಲ್ಲಿ ಬೇರೆ ದಾರಿ: ಪ್ರತಿ window ಗೂ ಒಂದು NUMBER (hash) compute
     ಮಾಡಿ, ಆ numbers compare ಮಾಡಿ — characters ಸಮ ಇದ್ರೆ ಮಾತ್ರ
     hash ಸಮ ಇರುತ್ತೆ (ಬಹುತೇಕ ಸಲ)!

  ಹಂತ 3 — Rolling Hash ಅಂದ್ರೆ ಏನು?
  →  ಪ್ರತಿ window ರ hash ಅನ್ನ SCRATCH ಇಂದ compute ಮಾಡೋ ಬದಲು,
     ಹಿಂದಿನ window ರ hash ಇಂದ, LEFTMOST character ಅನ್ನ ತೆಗೆದು
     RIGHTMOST character ಅನ್ನ ಸೇರಿಸಿ, O(1) ನಲ್ಲಿ ಹೊಸ hash
     ಪಡೆಯಬಹುದು (polynomial rolling hash formula ಬಳಸಿ)

  ಹಂತ 4 — Hash ಸಮ ಆದ್ರೆ ಸಾಕಾ? (COLLISION ಸಮಸ್ಯೆ)
  →  "ಇಲ್ಲ!" — ಎರಡು ಬೇರೆ ಬೇರೆ substrings ಕೂಡ ಆಕಸ್ಮಿಕವಾಗಿ
      ಒಂದೇ hash value ಪಡೆಯಬಹುದು (collision)
  →  So hash ಸಮ ಆದಾಗ ಮಾತ್ರ, ACTUAL characters ಅನ್ನ ಒಮ್ಮೆ verify
     ಮಾಡಬೇಕು — ಇದೇ "hash first, verify second" strategy

  ಹಂತ 5 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  Rolling hash update O(1) — ಪ್ರತಿ window ಗೂ ಪೂರ್ತಿ re-hash
     ಮಾಡೋ ಅಗತ್ಯ ಇಲ್ಲ
  →  ಹೆಚ್ಚಿನ ಸಲ hash mismatch ಆಗುತ್ತೆ ಅಂದ್ರೆ, ಆ position ಗಳಿಗೆ
     costly character comparison ಮಾಡೋ ಅಗತ್ಯನೇ ಬರಲ್ಲ — average
     case ನಲ್ಲಿ ಇದು ಬಹಳ ವೇಗ

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು:
  →  "Compute a polynomial rolling hash for the pattern and for
      the first window of text of the same length"
  →  "Slide the window one character at a time, updating the
      hash in O(1) by removing the old leading character's
      contribution and adding the new trailing character's"
  →  "Whenever the window's hash equals the pattern's hash,
      double-check with an actual string comparison — hashes can
      collide, so this verification step is essential for
      correctness"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Rabin-Karp — Polynomial Rolling Hash + verification
  Secondary : Brute-force sliding comparison

  WHY Rolling Hash + Verification?
  → A single integer comparison (the hash) is far cheaper than
    comparing m characters directly, and the hash can be updated
    in O(1) per slide instead of recomputed from scratch. The
    verification step (actual string compare on a hash match)
    guards against the rare but real possibility of hash
    collisions, keeping the algorithm CORRECT while staying fast
    on average.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  The key insight: instead of comparing characters directly, we
  can compare a compact NUMERIC fingerprint of each window
  (its polynomial hash mod a large prime). Two equal substrings
  ALWAYS have equal hashes; two different substrings USUALLY
  have different hashes (with a well-chosen base and modulus,
  collisions are extremely rare). The rolling property — updating
  the hash for a shifted window in O(1) using simple arithmetic —
  is what keeps the whole scan linear.

  The journey from brute to optimal:
    Brute thought   →  For each starting position in text,
                       compare all m characters against pattern
    Problem with it →  O(n*m) worst case — comparing full
                       substrings at every position is wasteful
                       when most windows won't match at all
    Better question →  "Can I quickly rule out non-matching
                       windows with a cheap fingerprint, only
                       paying the full comparison cost when the
                       fingerprint says 'maybe'?"
    Insight         →  Polynomial rolling hash — O(1) hash update
                       per slide, verify only on hash matches
    Optimal         →  O(n + m) average case (verification cost
                       is amortized away when collisions are rare)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE (sliding comparison)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Slide the pattern across every valid starting position in
    the text and directly compare characters, no hashing at all.

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
    → Correct, but every position pays the full O(m) comparison
      cost regardless of how quickly it could be ruled out —
      hashing lets most non-matching windows be rejected in O(1).

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 6 — APPROACH 2 — OPTIMAL (Rabin-Karp Rolling Hash)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Compute the pattern's polynomial hash and the hash of the
    first window of `text` (same length as pattern). Slide the
    window one character right at a time, updating the hash in
    O(1): subtract the outgoing character's weighted
    contribution, multiply by the base, add the incoming
    character. Whenever hashes match, verify with a direct
    string comparison before recording a match (guards against
    hash collisions).

  Key steps:
    1. base, mod = fixed constants (large prime modulus)
    2. pattern_hash = polynomial hash of pattern
    3. window_hash = polynomial hash of text[0:m]
    4. high_order = base^(m-1) mod mod   # for removing leading char
    5. for i in range(n - m + 1):
    6.   if pattern_hash == window_hash and text[i:i+m] == pattern:
    7.     record match at i
    8.   roll window_hash forward by one position (O(1))
    9. return matches

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ:
    → "pattern ಗೆ ಮತ್ತು text ರ ಮೊದಲ window ಗೆ polynomial hash
       compute ಮಾಡು. ಪ್ರತಿ ಸಲ window ಅನ್ನ ಒಂದು position ಮುಂದೆ
       ಸರಿಸುವಾಗ, ಹಳೆಯ hash ಇಂದ leading character ತೆಗೆದು, ಹೊಸ
       trailing character ಸೇರಿಸಿ O(1) ನಲ್ಲಿ ಹೊಸ hash ಪಡೆ.
       hashes ಸಮ ಆದಾಗ ಮಾತ್ರ, actual characters verify ಮಾಡಿ
       match confirm ಮಾಡು!"

  Time  : O(n + m) average  →  Why: O(m) to hash pattern and
                                    first window, O(n) to roll
                                    through remaining windows,
                                    verification is rare with a
                                    good hash function
          O(n*m) worst case →  Why: adversarial inputs causing
                                    many hash collisions would
                                    force full verification often
                                    (extremely unlikely with a
                                    well-chosen large prime modulus)
  Space : O(1)  →  Why: only a few running hash values tracked
                        (excluding the output list)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 7 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: text = "ababcababcabc", pattern = "abc"   (m = 3)

  pattern_hash = hash("abc")
  window_hash (starting at text[0:3] = "aba") — computed once

  Slide through positions 0..10:
    at i=0: window="aba", hash mismatch with "abc" → skip
    at i=1: window="bab", hash mismatch → skip
    at i=2: window="abc", HASH MATCHES pattern_hash →
            verify: text[2:5]=="abc" == pattern → CONFIRMED, record 2
    ... continues rolling ...
    at i=7: window="abc" → hash matches → verify → CONFIRMED, record 7
    at i=10: window="abc" → hash matches → verify → CONFIRMED, record 10

  Output: [2, 7, 10] ✓  (same result as the Z-function approach —
  different mechanism, same correct answer)

  ಇನ್ನೊಂದು example — verifying against false positives:
  Input: text = "aaaaa", pattern = "aa"

  Every window ("aa" at positions 0,1,2,3) hashes identically
  AND the actual characters do match every time (no false
  positive here, since all characters truly are 'a') → all 4
  positions confirmed as real matches

  Output: [0, 1, 2, 3] ✓

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 8 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ No match "hello"/"world"?      →  [] — hashes never align
  ✓ Pattern == text exactly?       →  [0] — single full match
  ✓ Overlapping matches "aaaaa"/"aa"? →  [0,1,2,3] — every window
                                        verified individually
  ✓ Pattern longer than text?      →  [] — guard against this
                                        before hashing anything
  ✓ Potential hash collision
    (different substrings, same
    hash by chance)?                →  ALWAYS verify with a real
                                        string comparison before
                                        trusting a hash match

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 9 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                          Time (avg)  Time (worst)  Space
  Brute (sliding compare) O(n*m)      O(n*m)        O(m)
  Optimal (Rabin-Karp)     O(n+m)      O(n*m)*       O(1)   ← use this ✅

  * Worst case only triggers with pathological hash collisions —
    virtually never happens with a large prime modulus and a
    well-chosen base in practice

  Time yaake O(n+m) average? → O(1) hash roll per position, O(m)
                                verification only on the rare
                                hash matches
  Space yaake O(1)?          → A handful of running hash values,
                                no per-character storage needed

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 10 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Rolling Hash (Rabin-Karp) with collision verification

  Ee pattern yaavaaga use maadabeeku?
  → Pattern matching / substring comparison problems where a
     cheap NUMERIC fingerprint can replace expensive direct
     comparisons — especially useful when comparing MANY
     substrings against each other (not just one pattern)
  → Any "compare windows/substrings for equality fast" scenario
     — duplicate substring detection, string equality checks in
     competitive programming

  Idee pattern beere problemsalli kaanisatte:
  → Z-Function / Pattern Matching (structural approach — same
     goal, no hashing, no collision risk but different mechanism)
  → KMP Algorithm / Pattern Matching #28 (also structural — LPS
     array instead of hashing)
  → Longest Palindromic Subsequence #516 (next/final problem in
     curriculum — completely different technique, DP/LCS based)

  Next time intaha problem bandre naanu modalu idannu think maadtene:
  → "Multiple substrings compare madbekagidre, ondu numeric
     fingerprint (rolling hash) use maadu — O(1) per comparison!
     Adre hash match aadaga khandita verify madu — collision
     possible!"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 11 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "Find every position where pattern occurs in text, using a
      rolling hash to fingerprint each window cheaply instead of
      comparing characters directly at every position."

  2. Brute force:
     "Slide pattern across every position, compare directly.
      O(n*m) worst case — no shortcuts."

  3. Optimize:
     "Compute a polynomial hash for pattern and for text's first
      window. Roll the hash forward in O(1) per position
      (remove leading char's contribution, add trailing char's).
      When hashes match, verify with a real string comparison to
      rule out collisions before confirming a match."

  4. Code:
     "Precompute base^(m-1) mod p for removing the leading
      character's contribution. Standard rolling hash update
      formula each step. Always double-check with a direct
      comparison on hash matches."

  5. Complexity:
     "Time O(n+m) on average — O(1) hash rolls, rare O(m)
      verifications. Worst case O(n*m) under pathological
      collisions, essentially never seen in practice. Space
      O(1) beyond the output."

  Mukhya: numeric fingerprint (hash) = cheap way to compare
          substrings, but NEVER trust a hash match blindly —
          always verify to rule out collisions!
"""


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(n*m) Time | O(m) Space (sliding comparison)
# ═══════════════════════════════════════════════════════════════════
def rabin_karp_search_brute(text, pattern):
    """
    Idu modala aaloochane — text ra prati position inda pattern
    jothe direct compare madu, hashing yaavudu illa
    """
    n, m = len(text), len(pattern)
    results = []

    for i in range(n - m + 1):
        if text[i:i + m] == pattern:
            results.append(i)

    return results


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n + m) Average Time | O(1) Space (Rabin-Karp Rolling Hash)
# ═══════════════════════════════════════════════════════════════════
def rabin_karp_search(text, pattern):
    """
    Idu final answer — pattern mattu first window ge polynomial
    hash compute madi, O(1) alli roll madu, hash match aadre
    matra verify madu
    """
    n, m = len(text), len(pattern)
    if m == 0 or m > n:
        return []

    base = 256
    mod = 10 ** 9 + 7

    pattern_hash = 0
    window_hash = 0
    high_order = 1  # base^(m-1) mod mod, for removing the leading char

    for _ in range(m - 1):
        high_order = (high_order * base) % mod

    for i in range(m):
        pattern_hash = (pattern_hash * base + ord(pattern[i])) % mod
        window_hash = (window_hash * base + ord(text[i])) % mod

    results = []
    for i in range(n - m + 1):
        if pattern_hash == window_hash and text[i:i + m] == pattern:
            results.append(i)

        if i < n - m:
            window_hash = (window_hash - ord(text[i]) * high_order) % mod
            window_hash = (window_hash * base + ord(text[i + m])) % mod
            window_hash %= mod

    return results


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # Test 1 — Basic (multiple occurrences)
    assert rabin_karp_search("ababcababcabc", "abc") == [2, 7, 10]

    # Test 2 — Overlapping matches
    assert rabin_karp_search("aaaaa", "aa") == [0, 1, 2, 3]

    # Test 3 — No match at all
    assert rabin_karp_search("hello", "world") == []

    # Test 4 — Pattern equals text
    assert rabin_karp_search("abc", "abc") == [0]

    # Test 5 — Pattern longer than text
    assert rabin_karp_search("ab", "abc") == []

    # Cross-check: brute force must agree on all of the above
    assert rabin_karp_search_brute("ababcababcabc", "abc") == [2, 7, 10]
    assert rabin_karp_search_brute("aaaaa", "aa") == [0, 1, 2, 3]
    assert rabin_karp_search_brute("hello", "world") == []
    assert rabin_karp_search_brute("abc", "abc") == [0]
    assert rabin_karp_search_brute("ab", "abc") == []

    print("All tests passed!")
