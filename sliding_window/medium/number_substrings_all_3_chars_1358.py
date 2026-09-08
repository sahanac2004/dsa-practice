"""
╔════════════════════════════════════════════════════════════════════╗
║  NUMBER OF SUBSTRINGS CONTAINING ALL THREE CHARACTERS              ║
║  LeetCode #1358  |  Difficulty: Medium  |  Topic: Sliding Window   ║
║  Link: https://leetcode.com/problems/                              ║
║        number-of-substrings-containing-all-three-characters/       ║
╚════════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Given a string `s` consisting only of characters 'a', 'b', and
  'c', return the NUMBER of substrings that contain AT LEAST one
  occurrence of each of the three characters.

  Input : s = a string of only 'a', 'b', 'c'
  Output: integer — count of substrings containing all three

  Example 1 — basic:
    Input : s = "abcabc"
    Output: 10
    Why?  : as we scan left to right, once all three characters
            have appeared, every substring reaching back to the
            start of s (or further, as later occurrences push
            the boundary rightward) also qualifies — they add up
            to 10 total substrings

  Example 2 — slightly tricky (repeats before completion):
    Input : s = "aaacb"
    Output: 3
    Why?  : only once 'b' appears (index 4) do all three exist
            in the string — the substrings "aacb", "acb", "cb"
            wait, actually the 3 valid ones are those ending at
            index 4 with left boundary at index 0, 1, or 2

  Example 3 — smallest valid case:
    Input : s = "abc"
    Output: 1
    Why?  : only the whole string itself contains all three
            characters

  Constraints:
    - 3 <= s.length <= 5 * 10^4
    - s consists only of characters 'a', 'b', 'c'

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Problem odi aada mele namma brain enu think maadabeeku:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  ಬರೀ 'a','b','c' ಇರೋ string      │
  │  Output ಏನು ಬೇಕು?     →  ಮೂರೂ characters (a,b,c) ಗೂ ≥1   │
  │                           ಇರೋ ಎಷ್ಟು substrings ಇವೆ ಅಂತ    │
  │  Constraints ಏನಿದೆ?   →  "ALL THREE ಇರಬೇಕು" — atMost(k)  │
  │                           trick ಬೇಡ, ಬೇರೆ idea ಬೇಕು       │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ಇದನ್ನ previous problems (#930, #1248 — atMost(k)
           trick) ಜೊತೆ contrast ಮಾಡಿ ನೋಡಿ!
  →  ಅಲ್ಲಿ "exactly k" count ಗೆ atMost(k)-atMost(k-1) ಬಳಸಿದ್ವಿ
  →  ಇಲ್ಲಿ "ALL THREE distinct types ≥1 ಇರಬೇಕು" — ಇದು ಬೇರೆ
     RIGID condition, atMost trick ಗೆ ಸರಿಯಾಗಿ ಹೊಂದಲ್ಲ — ಹೊಸ
     idea ಬೇಕು: "LAST SEEN POSITION" trick!

  ಹಂತ 3 — "Last Seen Position" idea ಏನಿದೆ?
  →  ಪ್ರತಿ character (a,b,c) ಗೂ, "ಕೊನೆಯ ಸಲ ಎಲ್ಲಿ ಕಂಡಿತು" ಅಂತ
     track ಮಾಡಿ
  →  ಒಂದು position `right` ಗೆ ಬಂದಾಗ, ಮೂರೂ characters ಗೂ
     last_seen ≥0 ಆಗಿದ್ರೆ (ಅಂದ್ರೆ ಮೂರೂ ಈಗಾಗಲೇ ಕಂಡಿವೆ), ಆ
     `right` ಅನ್ನ END ಆಗಿ ಇಟ್ಟುಕೊಂಡು ಎಷ್ಟು substrings valid
     ಅಂದ್ರೆ: "left" 0 ಇಂದ min(last_a, last_b, last_c) ವರೆಗೆ
     ಎಲ್ಲಿಂದ ಶುರು ಮಾಡಿದ್ರೂ, ಆ ಮೂರೂ characters ಇನ್ನೂ window
     ಒಳಗೆ ಇರುತ್ತೆ!
  →  So valid substrings ending at right = min(last_a, last_b,
     last_c) + 1

  ಹಂತ 4 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  "min(last_a,last_b,last_c)" ಅಂದ್ರೆ, ಎಲ್ಲಿಯವರೆಗೆ back
     ಹೋದ್ರೆ ಮೂರೂ characters ಇನ್ನೂ (ಕನಿಷ್ಠ ಒಮ್ಮೆ) window ಒಳಗೆ
     ಇರುತ್ತೋ ಆ boundary — ಅದಕ್ಕಿಂತ ಎಡಗಡೆ ಎಷ್ಟೇ starting
     points try ಮಾಡಿದ್ರೂ (ಇನ್ನೂ ಹೆಚ್ಚು ಎಡಕ್ಕೆ), still ಎಲ್ಲಾ
     ಮೂರೂ characters ಇರುತ್ತೆ (ಯಾಕಂದ್ರೆ window ದೊಡ್ಡದಾಗಿ ಬೆಳಿತಾ
     ಇರುತ್ತೆ, ಯಾವುದೇ character ಕಳಿಯಲ್ಲ)
  →  ಪ್ರತಿ right ಗೂ ಇದೇ formula apply ಮಾಡಿ ಸೇರಿಸಿದ್ರೆ, ಒಟ್ಟು
     valid substrings ಸಿಗುತ್ತೆ — single O(n) pass!

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು:
  →  "Track the last-seen index of 'a', 'b', and 'c' as I scan"
  →  "Once all three have appeared at least once, every substring
      ending at the current position and starting anywhere from
      0 up to the EARLIEST of those three last-seen indices is
      valid — that's min(last_a, last_b, last_c) + 1 substrings"
  →  "Sum this count at every position — no shrinking or
      complement tricks needed"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Sliding Window — Last Seen Position tracking
  Secondary : Brute-force incremental frequency count per start

  WHY Last Seen Position (not atMost(k))?
  → "All three characters present" isn't naturally an "at most K"
    style condition — it's an "at least 1 each" condition, which
    the atMost(k)-atMost(k-1) subtraction trick doesn't map onto
    cleanly. Tracking each character's most recent index directly
    answers "how far left can I go and still have all three?" —
    exactly what's needed, in a single forward pass.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  The key insight: for a substring ending at index `right` to
  contain all three characters, its LEFT boundary must be at or
  before the EARLIEST of the three characters' most recent
  occurrences up to `right`. Any left boundary from 0 up to that
  earliest last-seen index still captures all three (since
  moving the boundary further left only INCLUDES more
  characters, never drops the ones already guaranteed present).
  So the count of valid substrings ending at `right` is exactly
  that boundary index plus one.

  The journey from brute to optimal:
    Brute thought   →  For each starting index, expand right
                       while maintaining a frequency count of
                       a/b/c, counting every position where all
                       three have appeared at least once
    Problem with it →  O(n^2) — restarts the frequency tracking
                       from scratch at every starting index
    Better question →  "Can I determine, for each right, how
                       FAR LEFT the window could start and still
                       be valid — without rescanning?"
    Insight         →  Track each character's LAST SEEN index;
                       the minimum of the three gives that
                       boundary directly
    Optimal         →  Single O(n) pass, O(1) space (3 tracked
                       indices)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE (incremental frequency per start)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    For every starting index `left`, extend `right` outward,
    maintaining a frequency count of a/b/c within the current
    window. Every time all three counts are positive, this
    (left, right) substring qualifies — count it.

  Pseudocode:
    step 1: count = 0
    step 2: for left in range(n):
    step 3:   freq = {'a':0,'b':0,'c':0}
    step 4:   for right in range(left, n):
    step 5:     freq[s[right]] += 1
    step 6:     if all counts > 0: count += 1
    step 7: return count

  Time  : O(n^2)  →  Why: for each of n starting points, the
                          inner loop can scan up to n characters
  Space : O(1)     →  Why: frequency dict bounded to 3 keys

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ?
    → Correct, but restarts frequency tracking from scratch at
      every starting index — the last-seen-position trick avoids
      this entirely with a single forward pass.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 6 — APPROACH 2 — OPTIMAL (Last Seen Position)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Maintain `last_seen['a']`, `last_seen['b']`, `last_seen['c']`
    (initialized to -1). At each index `i`, update the current
    character's last-seen position. If all three are ≥ 0, add
    `min(last_seen values) + 1` to the running total — that's
    exactly how many valid left boundaries exist for a substring
    ending at `i`.

  Key steps:
    1. last_seen = {'a': -1, 'b': -1, 'c': -1}
    2. total = 0
    3. for i, ch in enumerate(s):
    4.   last_seen[ch] = i
    5.   if all(v != -1 for v in last_seen.values()):
    6.     total += min(last_seen.values()) + 1
    7. return total

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ:
    → "ಪ್ರತಿ character ಗೂ 'ಕೊನೆಯ ಸಲ ಎಲ್ಲಿ ಕಂಡಿತು' track ಮಾಡು.
       ಮೂರೂ ಈಗಾಗಲೇ ಕಂಡಿದ್ರೆ, min(last positions) + 1 ಅನ್ನ
       total ಗೆ ಸೇರಿಸು — ಇದೇ ಈ position ಗೆ ಎಷ್ಟು valid
       substrings ಸಿಗುತ್ತೋ ಅಷ್ಟು!"

  Time  : O(n)  →  Why: single left-to-right pass, O(1) work
                        per character
  Space : O(1)  →  Why: just 3 tracked indices (bounded alphabet)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 7 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: s = "abcabc"

  i  ch  last_seen{a,b,c}   all set?  total += min+1        total
  0  a   {0,-1,-1}          No        —                     0
  1  b   {0,1,-1}           No        —                     0
  2  c   {0,1,2}            Yes       min(0,1,2)+1=1         1
  3  a   {3,1,2}            Yes       min(3,1,2)+1=2         3
  4  b   {3,4,2}            Yes       min(3,4,2)+1=3         6
  5  c   {3,4,5}            Yes       min(3,4,5)+1=4         10

  Output: 10 ✓

  ಇನ್ನೊಂದು example — 'b' arrives late:
  Input: s = "aaacb"

  i=0 a: {0,-1,-1} — not all set
  i=1 a: {1,-1,-1} — not all set
  i=2 a: {2,-1,-1} — not all set
  i=3 c: {2,-1,3} — not all set (b missing)
  i=4 b: {2,4,3} — all set! total += min(2,4,3)+1 = 3

  Output: 3 ✓

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 8 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ Exact minimum "abc"?            →  1 — only the whole string
  ✓ Character missing entirely
    (guaranteed not to happen per
    constraints, but conceptually)?  →  would be 0 — total never
                                        increments if one
                                        last_seen stays -1
  ✓ All three repeated heavily?     →  grows quickly as later
                                        occurrences push the
                                        boundary rightward
  ✓ Third character appears last?  →  handled naturally, count
                                        only starts once all
                                        three seen at least once
  ✓ Minimum length input (n=3)?    →  works correctly as shown
                                        in Example 3

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 9 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                              Time    Space
  Brute (incremental freq)   O(n^2)  O(1)
  Optimal (last seen pos)     O(n)    O(1)   ← use this ✅

  Time yaake O(n)?  → Single left-to-right pass, O(1) work per
                       character (dict update + min of 3 values)
  Space yaake O(1)? → Only 3 tracked "last seen" indices

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 10 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Last Seen Position — "all K types present" counting

  Ee pattern yaavaaga use maadabeeku?
  → "Substring/subarray must contain AT LEAST ONE of EACH of a
     FIXED small set of categories" type counting problems —
     tracking each category's most recent index directly gives
     the valid-starting-boundary without any shrink/expand loop
  → Contrast with atMost(k)-atMost(k-1): that's for "exactly K
     occurrences of ONE property"; this is for "all K DISTINCT
     categories present at least once" — different shape,
     different technique

  Idee pattern beere problemsalli kaanisatte:
  → Binary Subarrays With Sum #930 / Count Number of Nice
     Subarrays #1248 (previous problems — atMost(k) trick,
     contrast with this last-seen-position technique)
  → Subarrays with K Different Integers #992 (next/final problem
     — back to the atMost(k) trick, but for distinct-COUNT
     instead of "all fixed categories present")

  Next time intaha problem bandre naanu modalu idannu think maadtene:
  → "'ALL K categories (fixed, small set) must be present at
     least once' kelidre → atMost(k) trick illa, LAST SEEN
     POSITION track madu! min(last positions)+1 ge valid
     substrings ending here sigatte."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 11 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "Count substrings that contain at least one 'a', one 'b',
      and one 'c' each."

  2. Brute force:
     "For each start, track a/b/c frequency as the window grows,
      counting every valid completion. O(n^2)."

  3. Optimize:
     "Track the last-seen index of each of a/b/c. Once all three
      have appeared, every left boundary from 0 up to the
      minimum of those three indices gives a valid substring
      ending here — add min(last_seen)+1 to the total at each
      position."

  4. Code:
     "Dict last_seen initialized to -1 for a/b/c. Update on each
      character. If none are -1, add min(values)+1 to total."

  5. Complexity:
     "Time O(n) — single pass. Space O(1) — three tracked
      indices."

  Mukhya: 'all K fixed categories present' ≠ 'exactly K count' —
          recognize the difference and reach for last-seen-
          position tracking instead of the atMost(k) trick!
"""


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(n^2) Time | O(1) Space (incremental frequency per start)
# ═══════════════════════════════════════════════════════════════════
def number_of_substrings_brute(s):
    """
    Idu modala aaloochane — prati start inda freq track madi,
    a,b,c ella count>0 aadaga count madu
    """
    n = len(s)
    total = 0

    for left in range(n):
        freq = {'a': 0, 'b': 0, 'c': 0}
        for right in range(left, n):
            freq[s[right]] += 1
            if freq['a'] > 0 and freq['b'] > 0 and freq['c'] > 0:
                total += 1

    return total


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n) Time | O(1) Space (last seen position tracking)
# ═══════════════════════════════════════════════════════════════════
def number_of_substrings(s):
    """
    Idu final answer — prati character ge last seen index track
    madi, ella set aadaga min(last_seen)+1 total ge sersu
    """
    last_seen = {'a': -1, 'b': -1, 'c': -1}
    total = 0

    for i, ch in enumerate(s):
        last_seen[ch] = i

        if last_seen['a'] != -1 and last_seen['b'] != -1 and last_seen['c'] != -1:
            total += min(last_seen.values()) + 1

    return total


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # Test 1 — Basic
    assert number_of_substrings("abcabc") == 10

    # Test 2 — Repeated chars before completion
    assert number_of_substrings("aaacb") == 3

    # Test 3 — Minimum valid length
    assert number_of_substrings("abc") == 1

    # Test 4 — Reordered minimum case
    assert number_of_substrings("cba") == 1

    # Test 5 — Longer stretch with repeats
    assert number_of_substrings("abcabcabc") == 28

    # Cross-check: brute force must agree on all of the above
    assert number_of_substrings_brute("abcabc") == 10
    assert number_of_substrings_brute("aaacb") == 3
    assert number_of_substrings_brute("abc") == 1
    assert number_of_substrings_brute("cba") == 1
    assert number_of_substrings_brute("abcabcabc") == 28

    print("All tests passed!")
