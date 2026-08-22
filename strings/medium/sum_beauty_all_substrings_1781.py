"""
╔════════════════════════════════════════════════════════════════════╗
║  SUM OF BEAUTY OF ALL SUBSTRINGS                                   ║
║  LeetCode #1781  |  Difficulty: Medium  |  Topic: Strings/HashMap  ║
║  Link: https://leetcode.com/problems/sum-of-beauty-of-all-substrings/║
╚════════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  The BEAUTY of a string is defined as:
    (frequency of its MOST frequent character)
    − (frequency of its LEAST frequent character)

  For example, the beauty of "abaacc" is 3 - 1 = 2 (character
  'a' appears 3 times, 'c' appears 2 times, 'b' appears 1 time
  — most frequent is 3, least frequent is 1).

  Given a string `s`, return the SUM of the beauty of every
  substring of `s`.

  Input : s = a string
  Output: integer — sum of beauty over all substrings

  Example 1 — basic:
    Input : s = "aabcb"
    Output: 5
    Why?  : most substrings have beauty 0 (all characters appear
            equally often, or only one distinct character);
            exactly 5 substrings ("aab","aabc","aabcb","abcb",
            "bcb") have beauty 1 each, summing to 5

  Example 2 — slightly tricky (single character):
    Input : s = "aabcbaa"
    Output: 17
    Why?  : more substrings, more overlap between max/min
            frequencies — beauty accumulates from many
            substrings with differing character distributions

  Example 3 — trivial (all same character, always beauty 0):
    Input : s = "aaaa"
    Output: 0
    Why?  : every substring has only ONE distinct character, so
            max frequency == min frequency always → beauty 0

  Constraints:
    - 1 <= s.length <= 500
    - s consists of only lowercase English letters

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Problem odi aada mele namma brain enu think maadabeeku:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  ಒಂದು string s                   │
  │  Output ಏನು ಬೇಕು?     →  ಪ್ರತಿ substring ರ beauty        │
  │                           (max freq - min freq) sum ಮಾಡಿ  │
  │  Constraints ಏನಿದೆ?   →  n ≤ 500 — O(n^2) ಅಥವಾ O(26n^2)  │
  │                           range ನಲ್ಲಿ solution ಸಾಕಾಗುತ್ತೆ│
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ಮೊದಲ simple idea ಏನು?
  →  ಪ್ರತಿ substring ಅನ್ನ actual ಆಗಿ slice ಮಾಡಿ, ಅದರ characters
     ಎಣಿಸಿ frequency dict build ಮಾಡಿ, max-min ಲೆಕ್ಕ ಹಾಕಿ sum
     ಗೆ ಸೇರಿಸಿ

  ಹಂತ 3 — ಇದು ಯಾಕೆ slow ಆಗುತ್ತೆ ಅಂತ ಗಮನಿಸಿ
  →  ಪ್ರತಿ substring ಗೂ frequency dict ಅನ್ನ SCRATCH ಇಂದ build
     ಮಾಡ್ತಿದ್ದೀವಿ — ಆದ್ರೆ ಪಕ್ಕದ substring (ಒಂದೇ start, j+1)
     ಗೆ almost ಅದೇ frequencies, ಬರೀ ಒಂದು character extra!

  ಹಂತ 4 — Better way ಹೇಗೆ?
  →  "ಪ್ರತಿ start index i ಗೆ, freq array ಒಂದೇ ಸಲ reset ಮಾಡಿ,
      ಆಮೇಲೆ j ಅನ್ನ ಬಲಕ್ಕೆ extend ಮಾಡ್ತಾ ಇರೋ ಹಾಗೆ, ಪ್ರತಿ ಸಲ
      ಒಂದೇ character increment ಮಾಡಿದ್ರೆ ಸಾಕಲ್ವಾ?" ಅಂತ ಯೋಚಿಸಿ
  →  ಪ್ರತಿ character ಗೆ ಗರಿಷ್ಠ 26 (lowercase letters) ಮಾತ್ರ
     ಇರೋದ್ರಿಂದ, max/min compute ಮಾಡೋಕೆ ಪ್ರತಿ ಸಲ O(26) ಸಾಕು —
     ಪೂರ್ತಿ substring ಮತ್ತೆ ಎಣಿಸೋ ಅಗತ್ಯ ಇಲ್ಲ!

  ಹಂತ 5 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  ಫ್ರೀಕ್ವೆನ್ಸಿ array ಅನ್ನ INCREMENTALLY (ಒಂದೊಂದೇ character
     add ಮಾಡ್ತಾ) maintain ಮಾಡಿದ್ರೆ, ಪ್ರತಿ substring ಗೂ O(n)
     re-counting ಬೇಡ — ಇದೇ ಪ್ರಮುಖ optimization!

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು:
  →  "For each starting index, I'll maintain a running frequency
      array of 26 letters, extending it one character at a time
      rather than rebuilding from scratch"
  →  "After each extension, computing max and min frequency
      costs O(26) — a constant — since the alphabet is bounded"
  →  "This turns an O(n^3) re-counting approach into O(26 n^2)"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : HashMap/Array Frequency Counter — incremental extension
  Secondary : Rebuild-from-scratch frequency counting per substring

  WHY incremental frequency tracking?
  → Adjacent substrings sharing the same start index differ by
    exactly ONE character. Rebuilding the entire frequency count
    for each one throws away almost all the previous work —
    incrementally extending it reuses everything and drops an
    O(n) factor from every inner step.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  The key insight: for a fixed starting index `i`, the substring
  s[i:j+1] and s[i:j+2] differ by exactly one new character. So
  instead of recomputing frequencies for s[i:j+2] from scratch,
  we can just increment the count for the one new character in
  an ALREADY-BUILT frequency array. Since the alphabet is only
  26 letters, computing max/min over that array is a cheap O(26)
  constant-time operation at every step.

  The journey from brute to optimal:
    Brute thought   →  For every (i, j) pair, slice out the
                       substring and build its frequency count
                       completely from scratch
    Problem with it →  Building frequencies from scratch costs
                       O(length), and summed across all O(n^2)
                       substrings this becomes O(n^3)
    Better question →  "Can I REUSE the frequency count from the
                       previous substring instead of rebuilding?"
    Insight         →  Fix the start `i`, extend `j` one step at
                       a time, updating one frequency slot only
    Optimal         →  O(n^2) outer iterations × O(26) max/min
                       computation = O(26 n^2) = O(n^2)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE (rebuild frequency each time)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    For every pair of indices (i, j), slice out the substring
    s[i:j+1], build its character frequency dictionary from
    scratch, then compute max(freq) - min(freq) and add it to
    the running total.

  Pseudocode:
    step 1: total = 0
    step 2: for i in range(n):
    step 3:   for j in range(i, n):
    step 4:     freq = count characters in s[i:j+1] from scratch
    step 5:     total += max(freq.values()) - min(freq.values())
    step 6: return total

  Time  : O(n^3)  →  Why: O(n^2) substrings, each frequency
                          build costs O(length of substring),
                          which sums to O(n^3) overall
  Space : O(1)     →  Why: at most 26 distinct characters tracked
                          at once (excluding the substring slice)

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ?
    → Correct, but rebuilding the frequency count from scratch
      for every substring wastes almost all the work done for
      the previous (shorter) substring with the same start.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 6 — APPROACH 2 — OPTIMAL (Incremental Frequency Array)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    For each starting index `i`, reset a 26-slot frequency array
    ONCE. Then extend `j` from `i` to n-1, incrementing only the
    ONE new character's count each step. After each extension,
    compute max and min (over nonzero entries) in O(26) and add
    the difference to the running total.

  Key steps:
    1. total = 0
    2. for i in range(n):
    3.   freq = [0] * 26
    4.   for j in range(i, n):
    5.     freq[s[j] - 'a'] += 1
    6.     max_freq = max(freq)
    7.     min_freq = min(f for f in freq if f > 0)
    8.     total += max_freq - min_freq
    9. return total

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ:
    → "ಪ್ರತಿ start i ಗೆ, 26-slot freq array ಒಂದೇ ಸಲ reset ಮಾಡು.
       j ಅನ್ನ ಬಲಕ್ಕೆ extend ಮಾಡ್ತಾ, ಪ್ರತಿ ಸಲ ಒಂದೇ character
       increment ಮಾಡು. ಆಮೇಲೆ max ಮತ್ತು (nonzero) min ಎಣಿಸಿ,
       ವ್ಯತ್ಯಾಸ ಅನ್ನ total ಗೆ ಸೇರಿಸು — ಇದನ್ನ ಪ್ರತಿ substring
       ಗೂ ಮಾಡು!"

  Time  : O(26 n^2) = O(n^2)  →  Why: n starting points, each
                                     extends up to n steps, each
                                     step's max/min costs O(26)
  Space : O(26) = O(1)         →  Why: one fixed-size frequency
                                     array reused per start index

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 7 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: s = "aabcb"   (indices: a=0 a=1 b=2 c=3 b=4)

  i=0: freq resets to all zero
    j=0 "a":      freq{a:1}          → beauty 1-1=0
    j=1 "aa":     freq{a:2}          → beauty 2-2=0
    j=2 "aab":    freq{a:2,b:1}      → beauty 2-1=1
    j=3 "aabc":   freq{a:2,b:1,c:1}  → beauty 2-1=1
    j=4 "aabcb":  freq{a:2,b:2,c:1}  → beauty 2-1=1
    subtotal: 0+0+1+1+1 = 3

  i=1: freq resets
    j=1 "a":      beauty 0
    j=2 "ab":     freq{a:1,b:1}      → beauty 0
    j=3 "abc":    freq{a:1,b:1,c:1}  → beauty 0
    j=4 "abcb":   freq{a:1,b:2,c:1}  → beauty 2-1=1
    subtotal: 0+0+0+1 = 1

  i=2: freq resets
    j=2 "b": 0     j=3 "bc": freq{b:1,c:1}→0     j=4 "bcb": freq{b:2,c:1}→1
    subtotal: 0+0+1 = 1

  i=3: "c"→0, "cb"→freq{c:1,b:1}→0     subtotal: 0

  i=4: "b"→0     subtotal: 0

  Total: 3 + 1 + 1 + 0 + 0 = 5

  Output: 5 ✓

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 8 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ Single character "a"?          →  0 — only one substring,
                                       max==min always for it
  ✓ All same character "aaaa"?     →  0 — every substring has
                                       exactly one distinct char
  ✓ All distinct characters "abc"? →  every substring where all
                                       chars appear once → beauty
                                       0 for every substring
  ✓ Two characters, unequal counts
    ("aab")?                       →  substrings like "aab" have
                                       beauty 2-1=1
  ✓ Longer mixed string?           →  accumulates many nonzero
                                       beauty contributions

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 9 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                              Time      Space
  Brute (rebuild each time)  O(n^3)    O(1)
  Optimal (incremental freq) O(26n^2)  O(26)   ← use this ✅

  Time yaake O(26n^2)? → n starting points × n extensions ×
                          O(26) max/min computation each step
  Space yaake O(26)?   → One fixed-size (26-slot) frequency
                          array reused per starting index

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 10 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Incremental Frequency Extension (fixed start, growing end)

  Ee pattern yaavaaga use maadabeeku?
  → "All substrings" / "all subarrays" aggregation problems —
     bittu ellaa substring ge frequency FRESH-A build maadoda,
     fixed start ge incrementally extend maadu
  → Alphabet-bounded (≤26) aggregation checks — O(26) per step
     still counts as O(1), giving overall O(n^2) instead of O(n^3)

  Idee pattern beere problemsalli kaanisatte:
  → Sort Characters by Frequency #451 (same frequency-array idea,
     different goal — sorting instead of aggregating)
  → Subarray Sum Equals K family (fixed-start incremental sum,
     same "don't recompute from scratch" principle)
  → Reverse Every Word in a String #557 (next problem in
     curriculum — different technique, two pointers)

  Next time intaha problem bandre naanu modalu idannu think maadtene:
  → "'All substrings/subarrays' over enu aggregate madbekagidre →
     fixed start, incrementally extend end — freq/sum FRESH-A
     rebuild madoda! Alphabet bounded aadre, O(26) per step still
     O(1) ansutte."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 11 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "Beauty of a string = max char frequency minus min char
      frequency. Sum this value over every substring of s."

  2. Brute force:
     "For every substring, rebuild its frequency count from
      scratch and compute max-min. O(n^3) since rebuilding
      costs O(length) per substring."

  3. Optimize:
     "Fix the start index and extend the end one character at a
      time, updating a 26-slot frequency array incrementally
      instead of rebuilding it. Max/min over 26 slots is O(1)."

  4. Code:
     "Outer loop over start i, reset freq array. Inner loop over
      end j, increment freq[s[j]], compute max(freq) and
      min(nonzero freq), add the difference to the total."

  5. Complexity:
     "Time O(26 n^2) = O(n^2) — n^2 (i,j) pairs, O(26) work each.
      Space O(26) = O(1) — one reusable frequency array."

  Mukhish: 'sum over all substrings' problems alli, per-substring
           FRESH rebuild madoda — fixed start inda incrementally
           extend madidre, huge factor of n save aaguttade!
"""


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(n^3) Time | O(1) Space (rebuild frequency each time)
# ═══════════════════════════════════════════════════════════════════
def beauty_sum_brute(s):
    """
    Idu modala aaloochane — prati substring ge frequency dict
    scratch inda build madi, max-min lekka hakodu
    """
    n = len(s)
    total = 0

    for i in range(n):
        for j in range(i, n):
            freq = {}
            for ch in s[i:j + 1]:
                freq[ch] = freq.get(ch, 0) + 1
            total += max(freq.values()) - min(freq.values())

    return total


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(26 n^2) = O(n^2) Time | O(26) Space (incremental frequency)
# ═══════════════════════════════════════════════════════════════════
def beauty_sum(s):
    """
    Idu final answer — prati start i ge freq array onde sala
    reset madi, j extend maadtha incrementally update madu
    """
    n = len(s)
    total = 0

    for i in range(n):
        freq = [0] * 26
        for j in range(i, n):
            freq[ord(s[j]) - ord('a')] += 1
            max_freq = max(freq)
            min_freq = min(f for f in freq if f > 0)
            total += max_freq - min_freq

    return total


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # Test 1 — Basic
    assert beauty_sum("aabcb") == 5

    # Test 2 — Longer mixed string
    assert beauty_sum("aabcbaa") == 17

    # Test 3 — All same character
    assert beauty_sum("aaaa") == 0

    # Test 4 — All distinct characters
    assert beauty_sum("abc") == 0

    # Test 5 — Single character
    assert beauty_sum("a") == 0

    # Cross-check: brute force must agree on all of the above
    assert beauty_sum_brute("aabcb") == 5
    assert beauty_sum_brute("aabcbaa") == 17
    assert beauty_sum_brute("aaaa") == 0
    assert beauty_sum_brute("abc") == 0
    assert beauty_sum_brute("a") == 0

    print("All tests passed!")
