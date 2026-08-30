"""
╔════════════════════════════════════════════════════════════════════╗
║  LONGEST SUBSTRING WITHOUT REPEATING CHARACTERS                    ║
║  LeetCode #3  |  Difficulty: Medium  |  Topic: Sliding Window      ║
║  Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/║
╚════════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Given a string `s`, find the LENGTH of the longest substring
  that contains no repeating characters.

  Input : s = a string
  Output: integer — length of the longest substring with all
          unique characters

  Example 1 — basic:
    Input : s = "abcabcbb"
    Output: 3
    Why?  : "abc" is the longest substring with no repeats

  Example 2 — all same character:
    Input : s = "bbbbb"
    Output: 1
    Why?  : only a single character can be kept in the window
            at a time

  Example 3 — tricky (repeat mid-window):
    Input : s = "pwwkew"
    Output: 3
    Why?  : "wke" — note "pwke" is NOT a substring (skips chars),
            answer must be a contiguous substring

  Constraints:
    - 0 <= s.length <= 5 * 10^4
    - s consists of English letters, digits, symbols, spaces

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  ಒಂದು string s                   │
  │  Output ಏನು ಬೇಕು?     →  no-repeat substring ನ max length│
  │  Constraints ಏನಿದೆ?   →  answer CONTIGUOUS substring     │
  │                           ಆಗಿರಬೇಕು, subsequence ಅಲ್ಲ     │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ಮೊದಲ simple idea ಏನು?
  →  ಎಲ್ಲಾ substrings generate ಮಾಡಿ, ಪ್ರತಿಯೊಂದೂ unique
     characters ಆಗಿದ್ಯಾ ಚೆಕ್ ಮಾಡಿ, longest track ಮಾಡಿ

  ಹಂತ 3 — Key observation ಏನಿದೆ?
  →  Window ಒಳಗೆ ಒಂದು duplicate character ಸಿಕ್ಕ ತಕ್ಷಣ, ಆ
     duplicate ನ ಮೊದಲ occurrence ಗಿಂತ MUಂದೆ left ಅನ್ನ
     ಸರಿಸಿಬಿಟ್ಟರೆ ಸಾಕು — window ಇಡೀ reset ಮಾಡೋ ಅಗತ್ಯ ಇಲ್ಲ

  ಹಂತ 4 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  right pointer ಒಂದೊಂದೇ character add ಮಾಡ್ತಾ ಹೋಗುತ್ತೆ
  →  duplicate ಸಿಕ್ಕಾಗ left ಅನ್ನ ಆ duplicate ಗಿಂತ ಒಂದು ಮುಂದೆ
     ಜಂಪ್ ಮಾಡಿಸಿ, window ಯಾವಾಗಲೂ unique characters ಮಾತ್ರ
     ಹೊಂದಿರೋ ಹಾಗೆ ಮಾಡಬಹುದು — ಪ್ರತಿ character ಒಮ್ಮೆ ಮಾತ್ರ
     add ಮತ್ತು ಒಮ್ಮೆ ಮಾತ್ರ remove ಆಗುತ್ತೆ → O(n)

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು:
  →  "Maintain a sliding window of unique characters using a
      HashMap of last-seen index"
  →  "When a repeat is found inside the window, jump `left` to
      just past the previous occurrence — never shrink one at a
      time when we already know exactly where to jump"
  →  "Track the max window size seen throughout"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Sliding Window + HashMap (last-seen index)
  Secondary : Brute-force substring generation + uniqueness check

  WHY Sliding Window?
  → The window only ever needs to GROW (right) or JUMP forward
    (left) — it never needs to shrink one character at a time or
    restart from scratch, since we know exactly where the
    duplicate is and can jump directly past it.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  The journey from brute to optimal:
    Brute thought   →  Check every substring for uniqueness
    Problem with it →  O(n^2) substrings, O(n) uniqueness check
                       each → O(n^3) total
    Better question →  "Do I need to re-check the whole window
                       every time, or can I just track what's
                       already inside it?"
    Insight         →  A HashMap of {char: last_seen_index} lets
                       us detect a repeat in O(1) and jump `left`
                       directly past it instead of shrinking
                       one step at a time
    Optimal         →  Single pass, O(n) time, O(min(n, charset))
                       space

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE (check every substring)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    For every (i, j) pair, check if s[i:j+1] has all unique
    characters using a set; track the max valid length.

  Pseudocode:
    step 1: best = 0
    step 2: for i in range(n):
    step 3:   seen = set()
    step 4:   for j in range(i, n):
    step 5:     if s[j] in seen: break
    step 6:     seen.add(s[j]); best = max(best, j - i + 1)
    step 7: return best

  Time  : O(n^2)  →  Why: O(n^2) start/end pairs in the worst
                          case, inner loop breaks on repeat
  Space : O(min(n, charset))  →  Why: the `seen` set per outer
                          iteration

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ?
    → Still quadratic — re-scans overlapping windows from
      scratch instead of reusing work already done.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 6 — APPROACH 2 — OPTIMAL (Sliding Window + HashMap)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Keep a window [left, right] with all unique characters and a
    HashMap of {char: last_seen_index}. When s[right] was seen
    before AND its last index is >= left, jump left to
    last_seen_index + 1. Track max(right - left + 1).

  Key steps:
    1. last_seen = {}, left = 0, best = 0
    2. for right, ch in enumerate(s):
    3.   if ch in last_seen and last_seen[ch] >= left:
    4.     left = last_seen[ch] + 1
    5.   last_seen[ch] = right
    6.   best = max(best, right - left + 1)
    7. return best

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ:
    → "right ಅನ್ನ ಒಂದೊಂದೇ ಮುಂದಕ್ಕೆ ಸರಿಸ್ತಾ ಹೋಗು. ಆ character
       window ಒಳಗೇ ಮೊದಲೇ ಇದ್ಯಾ ಅಂತ ಚೆಕ್ ಮಾಡು — ಇದ್ರೆ left ಅನ್ನ
       ಆ previous occurrence ಗಿಂತ ಒಂದು ಮುಂದೆ ಜಂಪ್ ಮಾಡಿಸು.
       ಪ್ರತಿ step ಗೂ window size track ಮಾಡ್ತಾ ಹೋಗು!"

  Time  : O(n)  →  Why: each index visited once by `right`;
                        `left` only ever moves forward
  Space : O(min(n, charset))  →  Why: HashMap holds at most one
                        entry per distinct character

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 7 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: s = "abcabcbb"

  right=0 'a': not seen → last_seen={a:0}         window="a"     best=1
  right=1 'b': not seen → last_seen={a:0,b:1}     window="ab"    best=2
  right=2 'c': not seen → last_seen={a:0,b:1,c:2} window="abc"   best=3
  right=3 'a': seen at 0 >= left(0) → left=1      window="bca"   best=3
  right=4 'b': seen at 1 >= left(1) → left=2      window="cab"   best=3
  right=5 'c': seen at 2 >= left(2) → left=3      window="abc"   best=3
  right=6 'b': seen at 4 >= left(3) → left=5      window="cb"    best=3
  right=7 'b': seen at 6 >= left(5) → left=7      window="b"     best=3

  Output: 3 ✓

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 8 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ Empty string ""?               →  0 — no characters at all
  ✓ All same character "bbbbb"?    →  1 — window can never
                                        exceed size 1
  ✓ Stale index in map "pwwkew"?   →  MUST check
                                        last_seen[ch] >= left,
                                        else a stale earlier
                                        index wrongly shrinks left
  ✓ All unique "abcdef"?           →  6 — whole string is the
                                        answer

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 9 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                          Time    Space
  Brute (all substrings)  O(n^2)  O(min(n,charset))
  Optimal (sliding window) O(n)   O(min(n,charset))  ← use this ✅

  Time yaake O(n)?   → `left` and `right` each traverse the
                        string at most once
  Space yaake O(k)?  → HashMap holds at most one entry per
                        distinct character in the charset

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 10 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Sliding Window (variable size) + last-seen HashMap

  Ee pattern yaavaaga use maadabeeku?
  → "Longest/shortest CONTIGUOUS substring/subarray satisfying a
     constraint" ಅಂದ್ರೆ, ಆ constraint window shrink/grow ಮಾಡ್ತಾ
     maintain ಮಾಡಬಹುದಾದ್ರೆ

  Idee pattern beere problemsalli kaanisatte:
  → Longest Repeating Character Replacement #424 (window + max
     frequency count)
  → Permutation in String #567 (fixed-size window + frequency
     match)
  → Minimum Window Substring #76 (variable window + need/have
     counters)

  Next time intaha problem bandre naanu modalu idannu think maadtene:
  → "No-repeat/unique-elements window bekagidre → sliding window +
     last-seen index HashMap, duplicate sikkaaga left ne
     directly jump maadu!"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 11 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "Find the length of the longest contiguous substring with
      all distinct characters."

  2. Brute force:
     "Check every substring for uniqueness with a set — O(n^3)
      total, too slow."

  3. Optimize:
     "Slide a window and track the last-seen index of each
      character. On a repeat inside the window, jump `left`
      straight past the earlier occurrence instead of shrinking
      one step at a time."

  4. Code:
     "A HashMap {char: last_index}, one pass with `right`,
      conditionally moving `left`, tracking the max window size."

  5. Complexity:
     "Time O(n) — single pass, `left` only moves forward.
      Space O(min(n, charset))."

  Mukhya: duplicate sikkaaga window reset maadbeda — ELLI jump
          maadbeku antha gottide, direct aa point ge jump maadu!
"""


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(n^2) Time | O(min(n, charset)) Space
# ═══════════════════════════════════════════════════════════════════
def length_of_longest_substring_brute(s):
    """
    Idu modala aaloochane — prati start index inda seen set
    build madi, duplicate sikka tanaka expand madu
    """
    n = len(s)
    best = 0

    for i in range(n):
        seen = set()
        for j in range(i, n):
            if s[j] in seen:
                break
            seen.add(s[j])
            best = max(best, j - i + 1)

    return best


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n) Time | O(min(n, charset)) Space (sliding window)
# ═══════════════════════════════════════════════════════════════════
def length_of_longest_substring(s):
    """
    Idu final answer — last-seen index HashMap use madi, duplicate
    sikkaaga left ne nera avaru occurrence dati jump madisu
    """
    last_seen = {}
    left = 0
    best = 0

    for right, ch in enumerate(s):
        if ch in last_seen and last_seen[ch] >= left:
            left = last_seen[ch] + 1
        last_seen[ch] = right
        best = max(best, right - left + 1)

    return best


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # Test 1 — Basic
    assert length_of_longest_substring("abcabcbb") == 3

    # Test 2 — All same character
    assert length_of_longest_substring("bbbbb") == 1

    # Test 3 — Repeat mid-window (non-adjacent substring trap)
    assert length_of_longest_substring("pwwkew") == 3

    # Test 4 — Empty string
    assert length_of_longest_substring("") == 0

    # Test 5 — All unique
    assert length_of_longest_substring("abcdef") == 6

    # Cross-check against brute force
    assert length_of_longest_substring_brute("abcabcbb") == 3
    assert length_of_longest_substring_brute("bbbbb") == 1
    assert length_of_longest_substring_brute("pwwkew") == 3
    assert length_of_longest_substring_brute("") == 0
    assert length_of_longest_substring_brute("abcdef") == 6

    print("All tests passed!")
