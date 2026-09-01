"""
╔════════════════════════════════════════════════════════════════════╗
║  PERMUTATION IN STRING                                              ║
║  LeetCode #567  |  Difficulty: Medium  |  Topic: Sliding Window    ║
║  Link: https://leetcode.com/problems/permutation-in-string/        ║
╚════════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Given two strings `s1` and `s2`, return True if `s2` contains a
  permutation of `s1` as a CONTIGUOUS substring — i.e. some
  rearrangement of s1's characters appears somewhere in s2.

  Input : s1 = pattern string, s2 = string to search within
  Output: boolean — True if any permutation of s1 is a substring
          of s2

  Example 1 — basic:
    Input : s1 = "ab", s2 = "eidbaooo"
    Output: True
    Why?  : "ba" (a permutation of "ab") appears in s2

  Example 2 — no match:
    Input : s1 = "ab", s2 = "eidboaoo"
    Output: False
    Why?  : no contiguous substring of s2 is a rearrangement of
            "ab" (chars are separated, not adjacent)

  Example 3 — tricky (s1 longer than remaining s2):
    Input : s1 = "adc", s2 = "dcda"
    Output: True
    Why?  : "cda" (positions 1-3) is a permutation of "adc"

  Constraints:
    - 1 <= s1.length, s2.length <= 10^4
    - s1 and s2 consist of lowercase English letters

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  s1 (pattern), s2 (search in)     │
  │  Output ಏನು ಬೇಕು?     →  s2 ಒಳಗೆ s1 ನ ಯಾವುದಾದ್ರೂ         │
  │                           permutation contiguous ಆಗಿ       │
  │                           ಇದ್ಯಾ ಅಂತ boolean               │
  │  Constraints ಏನಿದೆ?   →  permutation ಅಂದ್ರೆ same         │
  │                           character COUNTS, order ಬೇರೆ    │
  │                           ಇರಬಹುದು                          │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — Key observation ಏನಿದೆ?
  →  "s1 ನ permutation" ಅಂದ್ರೆ, ಆ substring ನ character
     frequency count s1 ನ frequency count ಗೆ EXACTLY match
     ಆಗಬೇಕು — order ಮುಖ್ಯ ಇಲ್ಲ!
  →  ಅಂದ್ರೆ s2 ಒಳಗೆ len(s1) size ಇರೋ ಒಂದು FIXED-SIZE window
     ಹುಡುಕಬೇಕು, ಆ window ನ frequency == s1 ನ frequency

  ಹಂತ 3 — Fixed-size sliding window ಹೇಗೆ apply ಮಾಡೋದು?
  →  s2 ಮೇಲೆ len(s1) size ಇರೋ window ಸರಿಸ್ತಾ ಹೋಗು
  →  ಪ್ರತಿ step ಗೂ window ಗೆ ಒಂದು character add, ಒಂದು character
     remove (window size fixed ಇರೋದ್ರಿಂದ)
  →  frequency counts match ಆದ್ರೆ → True return ಮಾಡು

  ಹಂತ 4 — Frequency match ಅನ್ನ efficient ಆಗಿ ಹೇಗೆ track ಮಾಡೋದು?
  →  ಪ್ರತಿ ಸಲ 26-length arrays compare ಮಾಡೋದ್ರ ಬದಲು, ಒಂದು
     "matches" counter ಇಟ್ಕೊಬಹುದು — ಎಷ್ಟು characters ನ count
     EXACTLY match ಆಗಿದೆ ಅಂತ track ಮಾಡಿ, matches == 26 ಆದ್ರೆ
     ಪೂರ್ತಿ match!

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು:
  →  "A permutation match is just a frequency-count match over a
      fixed-size window — order doesn't matter"
  →  "Slide a window of size len(s1) across s2, incrementally
      updating counts (add the new char, remove the char leaving
      the window) instead of recomputing from scratch each time"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Fixed-size Sliding Window + Frequency Count
  Secondary : Brute-force — sort every window and compare to
              sorted(s1)

  WHY Fixed-size Sliding Window?
  → The window size is always exactly len(s1) — this lets us
    slide by adding one character and removing exactly one
    character each step, avoiding a full recount.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  The journey from brute to optimal:
    Brute thought   →  For every window of size len(s1) in s2,
                       sort it and compare to sorted(s1)
    Problem with it →  O(n) windows, O(m log m) sort each →
                       O(n * m log m) total
    Better question →  "Do I need to sort, or can I just compare
                       frequency counts?"
    Insight         →  Two strings are permutations of each other
                       iff their character frequency counts are
                       identical — and as a fixed-size window
                       slides, only ONE character enters and ONE
                       leaves, so counts update in O(1)
    Optimal         →  Single pass, O(n) time, O(26) space

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE (sort every window)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    For every window of size len(s1) in s2, sort it and compare
    to sorted(s1). If any match, return True.

  Pseudocode:
    step 1: target = sorted(s1); m = len(s1); n = len(s2)
    step 2: for i in range(n - m + 1):
    step 3:   if sorted(s2[i:i+m]) == target: return True
    step 4: return False

  Time  : O(n * m log m)  →  Why: O(n) window starts, each sort
                                  costs O(m log m)
  Space : O(m)             →  Why: each window slice + sorted
                                  copy

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ?
    → Sorting every window from scratch is wasteful — the window
      barely changes between consecutive positions (one char in,
      one char out).

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 6 — APPROACH 2 — OPTIMAL (Fixed-size Sliding Window)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Build frequency arrays for s1 and the first window of s2 of
    the same size. Track a `matches` counter — how many of the 26
    letters currently have equal counts in both arrays. Slide the
    window one character at a time: add the incoming char, remove
    the outgoing char, update `matches` incrementally. If
    matches == 26 at any point, a permutation window was found.

  Key steps:
    1. m, n = len(s1), len(s2); if m > n: return False
    2. s1_count, s2_count = [0]*26, [0]*26
    3. for i in range(m): s1_count[s1[i]] += 1; s2_count[s2[i]] += 1
    4. matches = sum(1 for c in range(26) if s1_count[c] == s2_count[c])
    5. if matches == 26: return True
    6. for right in range(m, n):
    7.   add s2[right], remove s2[right - m], update matches for
        both affected letters
    8.   if matches == 26: return True
    9. return False

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ:
    → "s1 ನ frequency ಮತ್ತು s2 ನ ಮೊದಲ window ನ frequency build
       ಮಾಡು. ಎಷ್ಟು letters count match ಆಗಿದೆ ಅಂತ track ಮಾಡು.
       Window ಸರಿಸ್ತಾ ಹೋದಂಗೆ, ಒಂದು character add ಒಂದು remove
       ಮಾಡಿ matches update ಮಾಡ್ತಾ ಹೋಗು — 26 letters ಎಲ್ಲಾ match
       ಆದ್ರೆ permutation ಸಿಕ್ಕಿತು!"

  Time  : O(n)   →  Why: initial window build O(m) + n-m slides,
                         each O(1) amortized (constant work per
                         step, only checking the 2 affected
                         letters)
  Space : O(26)  →  Why: fixed-size frequency arrays for
                         lowercase letters

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 7 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: s1 = "ab", s2 = "eidbaooo"

  s1_count: a=1, b=1
  First window s2[0:2] = "ei" → e=1, i=1 → matches on 24 unset
  letters (both 0) but a,b mismatch → matches = 24, not 26

  Slide right=2 'd': add 'd', remove 'e' (s2[0])
    window s2[1:3] = "id" → no a,b match yet → matches still 24
  Slide right=3 'b': add 'b', remove 'i' (s2[1])
    window s2[2:4] = "db" → b count now matches (1==1),
    d count no longer 0 vs s1's 0... window = "db": counts
    b=1,d=1 vs s1 a=1,b=1 → a mismatch (0 vs 1) → matches=25
  Slide right=4 'a': add 'a', remove 'd' (s2[2])
    window s2[3:5] = "ba" → counts a=1,b=1 == s1_count exactly
    → matches = 26 → return True ✓

  Output: True (found "ba" at index 3)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 8 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ len(s1) > len(s2)?             →  False immediately — no
                                       window of that size exists
  ✓ s1 == s2 exactly?              →  True — s1 is trivially a
                                       permutation of itself
  ✓ Same char repeated "aaa" in
    s1="aa"?                       →  True as long as counts
                                       match — order irrelevant
  ✓ No overlap at all?             →  False — matches never
                                       reaches 26

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 9 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                          Time           Space
  Brute (sort windows)   O(n*m log m)    O(m)
  Optimal (freq window)  O(n)            O(26)  ← use this ✅

  Time yaake O(n)?   → each slide only updates counts for the 2
                        affected letters, O(1) amortized
  Space yaake O(26)? → fixed frequency arrays, independent of
                        input length

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 10 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Fixed-size Sliding Window + Frequency Match

  Ee pattern yaavaaga use maadabeeku?
  → "Anagram/permutation exists as a substring" type problems —
     fixed window size == len(pattern), frequency comparison
     instead of sorting

  Idee pattern beere problemsalli kaanisatte:
  → Find All Anagrams in a String #438 (same idea, collect ALL
     matching start indices instead of a single boolean)
  → Longest Repeating Character Replacement #424 (variable window
     + frequency, different validity condition)
  → Minimum Window Substring #76 (variable window + need/have
     counters, superset match instead of exact match)

  Next time intaha problem bandre naanu modalu idannu think maadtene:
  → "Permutation/anagram substring bekagidre → fixed-size window +
     frequency array, ondu add ondu remove maadi matches counter
     track madu — sort maadoda agatya illa!"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 11 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "Check if s2 contains any contiguous substring that is a
      rearrangement (permutation) of s1."

  2. Brute force:
     "Slide a window of size len(s1), sort it, compare to
      sorted(s1) — O(n * m log m), too slow for n, m up to 10^4."

  3. Optimize:
     "A permutation match is just a frequency-count match. Slide
      a fixed-size window, incrementally add/remove one character
      per step, and track how many of the 26 letters currently
      match counts exactly. All 26 matching means we found a
      permutation."

  4. Code:
     "Two frequency arrays of size 26, a `matches` counter updated
      in O(1) per slide by only checking the two affected
      letters."

  5. Complexity:
     "Time O(n) — O(1) amortized work per slide.
      Space O(26) — fixed alphabet-size arrays."

  Mukhya: permutation == same frequency counts, order matter
          illa — sort maadbeda, frequency compare madidre saaku!
"""


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(n * m log m) Time | O(m) Space
# ═══════════════════════════════════════════════════════════════════
def check_inclusion_brute(s1, s2):
    """
    Idu modala aaloochane — prati window sort madi sorted(s1) ge
    compare madu
    """
    m, n = len(s1), len(s2)
    if m > n:
        return False

    target = sorted(s1)
    for i in range(n - m + 1):
        if sorted(s2[i:i + m]) == target:
            return True

    return False


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n) Time | O(26) Space (fixed-size sliding window)
# ═══════════════════════════════════════════════════════════════════
def check_inclusion(s1, s2):
    """
    Idu final answer — frequency arrays + matches counter use madi,
    ondu add ondu remove maadutta window slide madu
    """
    m, n = len(s1), len(s2)
    if m > n:
        return False

    s1_count = [0] * 26
    s2_count = [0] * 26

    def idx(ch):
        return ord(ch) - ord('a')

    for i in range(m):
        s1_count[idx(s1[i])] += 1
        s2_count[idx(s2[i])] += 1

    matches = sum(1 for c in range(26) if s1_count[c] == s2_count[c])
    if matches == 26:
        return True

    for right in range(m, n):
        add_ch = idx(s2[right])
        remove_ch = idx(s2[right - m])

        # update count for incoming character
        s2_count[add_ch] += 1
        if s2_count[add_ch] == s1_count[add_ch]:
            matches += 1
        elif s2_count[add_ch] == s1_count[add_ch] + 1:
            matches -= 1

        # update count for outgoing character
        s2_count[remove_ch] -= 1
        if s2_count[remove_ch] == s1_count[remove_ch]:
            matches += 1
        elif s2_count[remove_ch] == s1_count[remove_ch] - 1:
            matches -= 1

        if matches == 26:
            return True

    return False


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # Test 1 — Basic (permutation found)
    assert check_inclusion("ab", "eidbaooo") is True

    # Test 2 — No permutation found
    assert check_inclusion("ab", "eidboaoo") is False

    # Test 3 — Permutation at the tail end
    assert check_inclusion("adc", "dcda") is True

    # Test 4 — s1 longer than s2
    assert check_inclusion("abcd", "ab") is False

    # Test 5 — s1 equals s2 exactly
    assert check_inclusion("abc", "abc") is True

    # Cross-check against brute force
    assert check_inclusion_brute("ab", "eidbaooo") is True
    assert check_inclusion_brute("ab", "eidboaoo") is False
    assert check_inclusion_brute("adc", "dcda") is True
    assert check_inclusion_brute("abcd", "ab") is False
    assert check_inclusion_brute("abc", "abc") is True

    print("All tests passed!")
