"""
╔════════════════════════════════════════════════════════════════════╗
║  LONGEST REPEATING CHARACTER REPLACEMENT                           ║
║  LeetCode #424  |  Difficulty: Medium  |  Topic: Sliding Window    ║
║  Link: https://leetcode.com/problems/longest-repeating-character-replacement/║
╚════════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Given a string `s` of uppercase letters and an integer `k`, you
  may replace up to `k` characters in the string with any other
  uppercase letter. Return the length of the longest substring
  containing the SAME letter, achievable after such replacements.

  Input : s = a string, k = max replacements allowed
  Output: integer — length of longest same-letter substring
          obtainable

  Example 1 — basic:
    Input : s = "ABAB", k = 2
    Output: 4
    Why?  : replace both 'A's (or both 'B's) → "AAAA" or "BBBB"

  Example 2 — can't replace everything:
    Input : s = "AABABBA", k = 1
    Output: 4
    Why?  : "AABA" → replace the one 'B' → "AAAA" (length 4);
            replacing more than 1 char isn't allowed

  Example 3 — tricky (window doesn't need to shrink on growth):
    Input : s = "ABBB", k = 2
    Output: 4
    Why?  : replace both 'A's worth... actually replace the
            single 'A' and nothing else needed since k=2 >= 1
            mismatch; "ABBB" → "BBBB" possible with 1 replacement

  Constraints:
    - 1 <= s.length <= 10^5
    - s consists of only uppercase English letters
    - 0 <= k <= s.length

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  string s, replacements k        │
  │  Output ಏನು ಬೇಕು?     →  ಒಂದೇ letter ಆಗಬಹುದಾದ max      │
  │                           length window (<=k changes)     │
  │  Constraints ಏನಿದೆ?   →  ಪ್ರತಿ window ಗೂ                │
  │                           (window_size - most_frequent_    │
  │                           char_count) <= k ಆಗಿರಬೇಕು       │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — Key observation ಏನಿದೆ?
  →  ಒಂದು window valid ಆಗಬೇಕಾದ್ರೆ, ಆ window ಒಳಗಿನ MOST
     FREQUENT character ಬಿಟ್ಟು ಉಳಿದಿದ್ದನ್ನೆಲ್ಲ replace
     ಮಾಡಬೇಕಾಗುತ್ತೆ → (window_size - max_freq) replacements ಬೇಕು
  →  ಇದು <= k ಆಗಿದ್ರೆ window valid!

  ಹಂತ 3 — Sliding window ಹೇಗೆ apply ಮಾಡೋದು?
  →  right ಅನ್ನ ಮುಂದಕ್ಕೆ ಸರಿಸ್ತಾ ಇರು, ಪ್ರತಿ character ನ count
     ಹೆಚ್ಚಿಸ್ತಾ ಇರು ಮತ್ತು max_freq update ಮಾಡ್ತಾ ಇರು
  →  window invalid ಆದ್ರೆ (size - max_freq > k), left ಅನ್ನ ಒಂದು
     step ಮುಂದಕ್ಕೆ ಸರಿಸು

  ಹಂತ 4 — Trick ಏನಿದೆ (window never shrinks below best)?
  →  max_freq ಅನ್ನ ಎಂದಿಗೂ decrease ಮಾಡೋ ಅಗತ್ಯ ಇಲ್ಲ! ಯಾಕಂದ್ರೆ
     ನಮಗೆ ಬೇಕಾಗಿರೋದು window SIZE, max_freq ಅಲ್ಲ. ಒಂದು ಸಲ
     ದೊಡ್ಡ window size achieve ಆದ್ರೆ, ಅದಕ್ಕಿಂತ ಕಡಿಮೆ size ನಲ್ಲಿ
     ಆಸಕ್ತಿ ಇಲ್ಲ — window size ಯಾವಾಗಲೂ same ಇರ್ತಾ ಮುಂದಕ್ಕೆ
     ಸರಿಯುತ್ತೆ (shrink ಆಗಲ್ಲ, ಬರೀ slide ಆಗುತ್ತೆ)

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು:
  →  "A window is valid if (window_size - max_char_frequency)
      <= k — that's the number of characters we'd need to
      replace"
  →  "I never need to shrink the window below its best-so-far
      size, so I keep max_freq as a running (possibly stale)
      max and just slide the window when invalid, instead of
      shrinking it"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Sliding Window + Frequency Count
  Secondary : Brute-force check every substring's replacement cost

  WHY Sliding Window?
  → We only care about the maximum achievable window size, never
    a smaller one — so the window can slide (never shrink) once
    it hits its widest valid point, keeping the whole scan O(n).

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  The journey from brute to optimal:
    Brute thought   →  For every substring, count replacements
                       needed (size - most frequent char count)
    Problem with it →  O(n^2) substrings, O(26) or O(n) frequency
                       scan each → too slow
    Better question →  "Can I maintain frequency counts
                       incrementally as a window slides?"
    Insight         →  A window is valid exactly when
                       (size - max_freq) <= k; we never need to
                       shrink below the best window found, only
                       slide forward
    Optimal         →  Single pass, O(n) time, O(26) space

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE (check every substring)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    For every (i, j), count frequency of each letter in s[i:j+1],
    compute (length - max_freq), check it's <= k, track best.

  Pseudocode:
    step 1: best = 0
    step 2: for i in range(n):
    step 3:   freq = {}
    step 4:   for j in range(i, n):
    step 5:     freq[s[j]] += 1
    step 6:     length = j - i + 1
    step 7:     if length - max(freq.values()) <= k:
    step 8:       best = max(best, length)
    step 9: return best

  Time  : O(n^2)  →  Why: O(n^2) windows, max(freq.values()) is
                          O(26) but still nested in O(n^2) loop
  Space : O(26)    →  Why: frequency map bounded by alphabet size

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ?
    → Quadratic — recomputing overlapping windows from scratch
      wastes work sliding windows can reuse.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 6 — APPROACH 2 — OPTIMAL (Sliding Window, non-shrinking)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Grow `right` one step at a time, updating frequency counts and
    a running `max_freq` (may be stale — that's fine, it can only
    undercount, never overcount, so it never falsely validates a
    window). If (window_size - max_freq) > k, slide `left` forward
    by one instead of shrinking the tracked best.

  Key steps:
    1. freq = [0]*26, left = 0, max_freq = 0, best = 0
    2. for right, ch in enumerate(s):
    3.   freq[ch] += 1
    4.   max_freq = max(max_freq, freq[ch])
    5.   window_size = right - left + 1
    6.   if window_size - max_freq > k:
    7.     freq[s[left]] -= 1; left += 1
    8.   best = max(best, right - left + 1)
    9. return best

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ:
    → "right ಅನ್ನ ಒಂದೊಂದೇ ಮುಂದಕ್ಕೆ ಸರಿಸ್ತಾ, frequency ಮತ್ತು
       max_freq update ಮಾಡ್ತಾ ಹೋಗು. Window invalid ಆದ್ರೆ
       (size - max_freq > k) left ಅನ್ನ ಒಂದೇ step ಮುಂದಕ್ಕೆ
       ಸರಿಸು — max_freq ಅನ್ನ ಕಡಿಮೆ ಮಾಡೋ ಅಗತ್ಯ ಇಲ್ಲ!"

  Time  : O(n)   →  Why: `right` visits each index once; `left`
                         moves forward at most n times total
  Space : O(26)  →  Why: fixed-size frequency array for uppercase
                         letters

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 7 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: s = "AABABBA", k = 1

  right=0 'A': freq={A:1}          max_freq=1  size=1  1-1=0<=1  best=1
  right=1 'A': freq={A:2}          max_freq=2  size=2  2-2=0<=1  best=2
  right=2 'B': freq={A:2,B:1}      max_freq=2  size=3  3-2=1<=1  best=3
  right=3 'A': freq={A:3,B:1}      max_freq=3  size=4  4-3=1<=1  best=4
  right=4 'B': freq={A:3,B:2}      max_freq=3  size=5  5-3=2>1 → shrink
               freq[s[0]='A']-=1 → {A:2,B:2}, left=1  size=4 best=4
  right=5 'B': freq={A:2,B:3}      max_freq=3  size=5  5-3=2>1 → shrink
               freq[s[1]='A']-=1 → {A:1,B:3}, left=2  size=4 best=4
  right=6 'A': freq={A:2,B:3}      max_freq=3(stale, real max is 3)
               size=5  5-3=2>1 → shrink
               freq[s[2]='B']-=1 → {A:2,B:2}, left=3  size=4 best=4

  Output: 4 ✓

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 8 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ k = 0?                        →  answer is the longest run of
                                      an already-repeated char
  ✓ k >= len(s)?                  →  entire string can become one
                                      letter → len(s)
  ✓ All same character "AAAA"?    →  4 — no replacements ever
                                      needed
  ✓ Stale max_freq undercount?    →  harmless — it can only make
                                      the window seem MORE invalid
                                      than it is, never falsely
                                      valid, and best is already
                                      locked in before that point

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 9 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                          Time    Space
  Brute (all substrings)  O(n^2)  O(26)
  Optimal (sliding window) O(n)   O(26)  ← use this ✅

  Time yaake O(n)?   → `left` and `right` each move forward at
                        most n times, never backward
  Space yaake O(26)? → fixed frequency array for uppercase
                        English letters

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 10 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Sliding Window + Frequency Count (non-shrinking)

  Ee pattern yaavaaga use maadabeeku?
  → "Longest substring/subarray satisfying a count-based budget
     constraint (at most k replacements/removals/flips)"
  → Window only needs to grow or slide, never shrink below its
     best-so-far size

  Idee pattern beere problemsalli kaanisatte:
  → Longest Substring Without Repeating Characters #3 (window +
     last-seen index instead of frequency)
  → Max Consecutive Ones III (same non-shrinking window idea,
     count of zeros instead of size - max_freq)
  → Permutation in String #567 (fixed-size window + frequency
     match)

  Next time intaha problem bandre naanu modalu idannu think maadtene:
  → "'At most k changes allowed' antha kelidre → sliding window +
     frequency count, valid condition (size - max_freq <= k)
     check madu, window shrink madoda agatya illa!"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 11 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "Find the longest substring that can become all-one-letter
      using at most k character replacements."

  2. Brute force:
     "Check every substring, compute replacements needed as
      length minus the most frequent character's count — O(n^2)."

  3. Optimize:
     "Slide a window, tracking frequency counts and the max
      frequency seen. A window is valid when
      (size - max_freq) <= k. When invalid, slide left forward
      by one — I never need to shrink below the best window
      found, since I'm only interested in the maximum size."

  4. Code:
     "A frequency array of size 26, one pass with `right`,
      conditionally advancing `left`, tracking best window size."

  5. Complexity:
     "Time O(n) — both pointers only move forward.
      Space O(26) — fixed alphabet-sized frequency array."

  Mukhya: max_freq stale aadru problem illa — adu size ne
          overcount madalla, so window kettaddu andre matte
          FALSE andilla!
"""


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(n^2) Time | O(26) Space
# ═══════════════════════════════════════════════════════════════════
def character_replacement_brute(s, k):
    """
    Idu modala aaloochane — prati substring ge frequency count
    madi, replacements needed <= k andre track madu
    """
    n = len(s)
    best = 0

    for i in range(n):
        freq = {}
        for j in range(i, n):
            freq[s[j]] = freq.get(s[j], 0) + 1
            length = j - i + 1
            if length - max(freq.values()) <= k:
                best = max(best, length)

    return best


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n) Time | O(26) Space (sliding window, non-shrinking)
# ═══════════════════════════════════════════════════════════════════
def character_replacement(s, k):
    """
    Idu final answer — running max_freq (stale aadru parwagilla)
    track madi, window invalid aadaga left ne ondu step slide madu
    """
    freq = {}
    left = 0
    max_freq = 0
    best = 0

    for right, ch in enumerate(s):
        freq[ch] = freq.get(ch, 0) + 1
        max_freq = max(max_freq, freq[ch])

        window_size = right - left + 1
        if window_size - max_freq > k:
            freq[s[left]] -= 1
            left += 1

        best = max(best, right - left + 1)

    return best


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # Test 1 — Basic
    assert character_replacement("ABAB", 2) == 4

    # Test 2 — Can't replace everything
    assert character_replacement("AABABBA", 1) == 4

    # Test 3 — k = 0 (no replacements allowed)
    assert character_replacement("ABCDE", 0) == 1

    # Test 4 — k covers whole string
    assert character_replacement("ABCDE", 4) == 5

    # Test 5 — All same character already
    assert character_replacement("AAAA", 2) == 4

    # Cross-check against brute force
    assert character_replacement_brute("ABAB", 2) == 4
    assert character_replacement_brute("AABABBA", 1) == 4
    assert character_replacement_brute("ABCDE", 0) == 1
    assert character_replacement_brute("ABCDE", 4) == 5
    assert character_replacement_brute("AAAA", 2) == 4

    print("All tests passed!")
