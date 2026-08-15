"""
╔════════════════════════════════════════════════════════════════════╗
║  LONGEST COMMON PREFIX                                             ║
║  LeetCode #14  |  Difficulty: Easy  |  Topic: Strings/Vertical Scan║
║  Link: https://leetcode.com/problems/longest-common-prefix/        ║
╚════════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Given an array of strings `strs`, find the longest string that
  is a PREFIX of every string in the array. If there is no
  common prefix among all of them, return an empty string "".

  Input : strs = list of strings
  Output: string — longest common prefix, or "" if none exists

  Example 1 — basic:
    Input : strs = ["flower", "flow", "flight"]
    Output: "fl"
    Why?  : all three start with "fl", but diverge at the next
            character ('o' vs 'o' vs 'i')

  Example 2 — slightly tricky (no common prefix at all):
    Input : strs = ["dog", "racecar", "car"]
    Output: ""
    Why?  : the very first characters ('d', 'r', 'c') don't even
            match, so no common prefix exists

  Example 3 — longer common prefix:
    Input : strs = ["interspecies", "interstellar", "interstate"]
    Output: "inters"
    Why?  : all three agree through "inters", then diverge
            ('p' vs 't' vs 't'... interstellar/interstate also
            diverge right after, but "inters" is where ALL agree)

  Constraints:
    - 1 <= strs.length <= 200
    - 0 <= strs[i].length <= 200
    - strs[i] consists of only lowercase English letters (if
      non-empty)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Problem odi aada mele namma brain enu think maadabeeku:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  strings ರ list                 │
  │  Output ಏನು ಬೇಕು?     →  ಎಲ್ಲಾ strings ಗೆ common ಆಗಿರೋ  │
  │                           ಅತಿ ದೊಡ್ಡ PREFIX                │
  │  Constraints ಏನಿದೆ?   →  strings ಖಾಲಿ ("") ಕೂಡ ಇರಬಹುದು  │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ಮೊದಲ simple idea ಏನು?
  →  ಮೊದಲ string ಅನ್ನ "candidate prefix" ಅಂತ ತಗೊಳಿ
  →  ಪ್ರತಿ ಮುಂದಿನ string ಜೊತೆ compare ಮಾಡಿ, match ಆಗದೇ
     ಇರೋವರೆಗೆ candidate ಅನ್ನ ಚಿಕ್ಕದು ಮಾಡ್ತಾ ಇರಿ (shrink)
  →  ಇದು horizontal ಆಗಿ ಒಂದೊಂದೇ string ಅನ್ನ ಹೋಲಿಸೋ way

  ಹಂತ 3 — Vertical scanning ಅಂದ್ರೆ ಏನು?
  →  "String by string ಹೋಲಿಸೋ ಬದಲು, COLUMN by COLUMN
      (character index by index) ಹೋಲಿಸಿದ್ರೆ ಹೇಗೆ?"
  →  index 0 ರಲ್ಲಿ ಎಲ್ಲಾ strings ರ character ಒಂದೇ ಇದ್ಯಾ ನೋಡು,
     ಇದ್ರೆ index 1 ಗೆ ಹೋಗು, ಇಲ್ಲಾಂದ್ರೆ ಅಲ್ಲಿಗೆ STOP
  →  ಯಾವ index ನಲ್ಲಿ mismatch ಸಿಗುತ್ತೋ ಅಲ್ಲಿಗೆ answer ready!

  ಹಂತ 4 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  Common prefix ಅಂದ್ರೆ, ಪ್ರತಿ position ನಲ್ಲೂ ಎಲ್ಲಾ strings
     ಒಂದೇ character ಹೊಂದಿರಬೇಕು
  →  Vertical scan ಮಾಡಿದ್ರೆ, ಮೊದಲ mismatch ಸಿಕ್ಕ ತಕ್ಷಣ EARLY
     EXIT ಮಾಡಬಹುದು — ಇಡೀ strings ಪೂರ್ತಿ ಸ್ಕ್ಯಾನ್ ಮಾಡೋ
     ಅಗತ್ಯ ಇಲ್ಲ (e.g., "dog" vs "racecar" ಗೆ index 0 ನಲ್ಲೇ ಗೊತ್ತಾಗುತ್ತೆ!)

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು:
  →  "Use the first string as a reference — walk its characters
      one index at a time"
  →  "At each index, check if every OTHER string has the same
      character at that index"
  →  "Stop the moment there's a mismatch, or we run past the
      end of any string — that index is the prefix length"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Vertical Scanning — column-by-column comparison
  Secondary : Horizontal Scanning — pairwise prefix shrinking

  WHY Vertical Scanning?
  → It compares CHARACTER POSITIONS across all strings at once,
    so it can bail out at the very first mismatched column —
    often much faster in practice than fully processing strings
    one-by-one, especially when an early character already
    breaks the match (like "dog" vs "racecar").

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  The key insight: a common prefix means "at EVERY index up to
  some length, ALL strings agree." Instead of comparing whole
  strings against each other repeatedly, we can walk index by
  index (using any one string, e.g. the first, as the ruler) and
  check that column across every other string. The instant one
  string disagrees (or runs out of characters), we know exactly
  where the common prefix ends.

  The journey from brute to optimal:
    Brute thought   →  Take string 1 as prefix. Compare against
                       string 2, shrink prefix until it matches.
                       Compare that against string 3, shrink
                       again. Repeat for all strings.
    Problem with it →  Works fine (O(S) total), but reprocesses
                       the same prefix characters repeatedly as
                       it shrinks, and doesn't exploit column
                       structure explicitly
    Better question →  "Can I check all strings AT ONCE for each
                       character position, and stop instantly on
                       any disagreement?"
    Insight         →  Iterate character index, compare that
                       column across all strings, stop at first
                       mismatch — no repeated re-shrinking needed
    Optimal         →  Vertical scan, early exit on first
                       mismatched column

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — HORIZONTAL SCANNING (pairwise shrink)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Start with the first string as the current prefix. For every
    other string, shrink the prefix (chop off the last char)
    until it actually IS a prefix of that string. If the prefix
    ever becomes empty, we can stop immediately — no common
    prefix exists.

  Pseudocode:
    step 1: prefix = strs[0]
    step 2: for each s in strs[1:]:
    step 3:   while prefix is not a prefix of s:
    step 4:     prefix = prefix[:-1]      # chop last character
    step 5:     if prefix == "": return ""
    step 6: return prefix

  Time  : O(S)  →  Why: S = sum of all characters; each char
                        participates in a limited number of
                        prefix-shrink comparisons
  Space : O(1)  →  Why: excluding the output, no extra structures

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ?
    → Actually correct and efficient (O(S))! But it repeatedly
      re-checks "is X a prefix of Y" using string slicing/compare
      each shrink step, and processes strings one at a time —
      vertical scanning achieves the same bound with a cleaner
      column-wise early exit.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 6 — APPROACH 2 — OPTIMAL (Vertical Scanning)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Use the first string as the reference. For each character
    index `i` in the first string, check whether every OTHER
    string also has that same character at index `i` (and is
    even long enough to have an index `i`). The moment either
    condition fails, return the prefix built so far.

  Key steps:
    1. if strs is empty → return ""
    2. for i, char in enumerate(strs[0]):
    3.   for other in strs[1:]:
    4.     if i == len(other) or other[i] != char:
    5.       return strs[0][:i]
    6. return strs[0]   # first string itself is the common prefix

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ:
    → "ಮೊದಲ string ಅನ್ನ ruler ಆಗಿ ಬಳಸು. ಪ್ರತಿ index i ಗೆ,
       ಎಲ್ಲಾ ಬೇರೆ strings ನಲ್ಲೂ ಆ index ನಲ್ಲಿ ಅದೇ character
       ಇದ್ಯಾ ನೋಡು. ಎಲ್ಲಾದ್ರೂ mismatch ಅಥವಾ string ಮುಗಿದ್ರೆ,
       ಅಲ್ಲಿಗೆ ಮುಂಚಿನ ಭಾಗ ಅನ್ನೇ ಫೈನಲ್ ಪ್ರಿಫಿಕ್ಸ್ ಆಗಿ return ಮಾಡು."

  Time  : O(S)  →  Why: worst case touches every character once,
                        but usually exits FAR earlier on mismatch
  Space : O(1)  →  Why: excluding the output, only index counters
                        used

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 7 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: strs = ["flower", "flow", "flight"]

  i   char (from strs[0])   check "flow"     check "flight"    action
  0   'f'                   'f' matches      'f' matches       continue
  1   'l'                   'l' matches      'l' matches       continue
  2   'o'                   'o' matches      'i' MISMATCH      stop here

  Return strs[0][:2] = "fl"

  Output: "fl" ✓

  ಇನ್ನೊಂದು example — no common prefix:
  Input: strs = ["dog", "racecar", "car"]

  i=0, char='d' (from strs[0])
  check "racecar": index 0 is 'r' → MISMATCH immediately

  Return strs[0][:0] = ""

  Output: "" ✓

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 8 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ Single string ["abc"]?         →  "abc" — trivially itself
  ✓ One string is empty ["", "a"]? →  "" — index 0 already fails
                                       for the empty string
  ✓ All strings identical?         →  the whole string is returned
  ✓ No overlap at all?             →  "" — mismatch at index 0
  ✓ One string is a prefix of the
    others (e.g. "fl", "flow")?    →  the SHORTEST string wins as
                                       the bound (loop runs out of
                                       characters in strs[0] or
                                       hits len(other) first)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 9 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                      Time    Space
  Horizontal Scan     O(S)    O(1)
  Vertical Scan       O(S)    O(1)   ← use this ✅ (better early exit)

  S = total number of characters across all strings

  Time yaake O(S)?   → Worst case every character gets compared
                        once across the scan
  Space yaake O(1)?  → Only index counters — no extra data
                        structures (output string aside)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 10 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Vertical (Column-wise) Scanning

  Ee pattern yaavaaga use maadabeeku?
  → Multiple strings/arrays ge across COMMON pattern
     (prefix/suffix/matching position) hudukbekagidre
  → Early exit sadhya iddaga — column-by-column check madidre
     pratiyondu string full scan madoda agatya illa

  Idee pattern beere problemsalli kaanisatte:
  → Isomorphic Strings #205 (next problem — character mapping,
     different technique but same "compare across positions" vibe)
  → Word Search / Matrix problems (row/column scanning)
  → Valid Word Abbreviation type problems

  Next time intaha problem bandre naanu modalu idannu think maadtene:
  → "Multiple strings ge common prefix/pattern bekagidre →
     vertical scan try maadu — column by column check madi,
     first mismatch sikkidkoodle immediately stop maadu!"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 11 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "Find the longest prefix shared by ALL strings in the
      array — return empty string if they don't share anything."

  2. Brute force:
     "Horizontal scan: start with the first string as prefix,
      shrink it against each subsequent string until it fits.
      O(S) total, but processes one string fully at a time."

  3. Optimize:
     "Vertical scan: walk character index by index using the
      first string as a ruler, checking that same index across
      every other string. Stop the instant any string disagrees
      or runs out of characters — often exits much earlier."

  4. Code:
     "For each index i in strs[0], loop through the rest of the
      strings checking strs[0][i] against other[i] (guarding
      against short strings). Mismatch → return strs[0][:i]."

  5. Complexity:
     "Time O(S) worst case — S = total characters. Space O(1)
      extra, ignoring the output string."

  Mukhya: vertical scan = column-by-column comparison — powerful
          whenever you need the FIRST point of disagreement across
          multiple sequences!
"""


# ═══════════════════════════════════════════════════════════════════
# APPROACH 1 — Horizontal Scanning — O(S) Time | O(1) Space
# ═══════════════════════════════════════════════════════════════════
def longest_common_prefix_horizontal(strs):
    """
    Idu modala aaloochane — modala string prefix andkondu,
    prati string jothe shrink madtha hogu
    """
    if not strs:
        return ""

    prefix = strs[0]

    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if prefix == "":
                return ""

    return prefix


# ═══════════════════════════════════════════════════════════════════
# APPROACH 2 — OPTIMAL — Vertical Scanning — O(S) Time | O(1) Space
# ═══════════════════════════════════════════════════════════════════
def longest_common_prefix(strs):
    """
    Idu final answer — column by column (index by index)
    ellaa strings holisi, modala mismatch sikkidkoodle stop madu
    """
    if not strs:
        return ""

    for i, char in enumerate(strs[0]):
        for other in strs[1:]:
            if i == len(other) or other[i] != char:
                return strs[0][:i]

    return strs[0]      # first string itself is the common prefix


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # Test 1 — Basic
    assert longest_common_prefix(["flower", "flow", "flight"]) == "fl"

    # Test 2 — No common prefix
    assert longest_common_prefix(["dog", "racecar", "car"]) == ""

    # Test 3 — Longer common prefix
    assert longest_common_prefix(
        ["interspecies", "interstellar", "interstate"]
    ) == "inters"

    # Test 4 — Single string
    assert longest_common_prefix(["abc"]) == "abc"

    # Test 5 — One string is empty
    assert longest_common_prefix(["", "a"]) == ""

    # Test 6 — Shortest string is a prefix of the others
    assert longest_common_prefix(["fl", "flow", "flower"]) == "fl"

    # Cross-check: horizontal approach must agree on all of the above
    assert longest_common_prefix_horizontal(["flower", "flow", "flight"]) == "fl"
    assert longest_common_prefix_horizontal(["dog", "racecar", "car"]) == ""
    assert longest_common_prefix_horizontal(
        ["interspecies", "interstellar", "interstate"]
    ) == "inters"
    assert longest_common_prefix_horizontal(["abc"]) == "abc"
    assert longest_common_prefix_horizontal(["", "a"]) == ""
    assert longest_common_prefix_horizontal(["fl", "flow", "flower"]) == "fl"

    print("All tests passed!")
