"""
╔════════════════════════════════════════════════════════════════════╗
║  MINIMUM WINDOW SUBSTRING                                          ║
║  LeetCode #76  |  Difficulty: Hard  |  Topic: Sliding Window       ║
║  Link: https://leetcode.com/problems/minimum-window-substring/     ║
╚════════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Given two strings `s` and `t`, return the SHORTEST substring of
  `s` that contains every character of `t` (including duplicates)
  — at least as many times as it appears in `t`. Return "" if no
  such substring exists.

  Input : s = source string, t = target characters (with counts)
  Output: string — smallest window of s covering all of t, or ""

  Example 1 — basic:
    Input : s = "ADOBECODEBANC", t = "ABC"
    Output: "BANC"
    Why?  : "BANC" contains 'A', 'B', 'C' — and it's the shortest
            such window in s

  Example 2 — t longer than the match, single char:
    Input : s = "a", t = "a"
    Output: "a"
    Why?  : the whole (and only) string already covers t

  Example 3 — tricky (no valid window exists):
    Input : s = "a", t = "aa"
    Output: ""
    Why?  : s only has one 'a', but t needs two — impossible

  Constraints:
    - 1 <= s.length, t.length <= 10^5
    - s and t consist of English letters (upper/lowercase)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  s (source), t (must-cover chars) │
  │  Output ಏನು ಬೇಕು?     →  t ನ ಎಲ್ಲಾ characters (counts     │
  │                           ಸಮೇತ) cover ಮಾಡೋ s ನ SHORTEST   │
  │                           window                            │
  │  Constraints ಏನಿದೆ?   →  duplicate characters ಇದ್ರೆ,      │
  │                           EXACT count cover ಆಗಬೇಕು        │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — Key observation ಏನಿದೆ?
  →  "cover" ಅಂದ್ರೆ window ಒಳಗಿನ ಪ್ರತಿ required character ನ
     count >= t ಒಳಗಿನ ಆ character ನ count ಆಗಿರಬೇಕು
  →  ಇದು classic "variable-size window expand-then-shrink"
     pattern — right ಇಂದ grow ಮಾಡು, valid ಆದ ತಕ್ಷಣ left ಇಂದ
     shrink ಮಾಡಿ tightest window ಹುಡುಕು

  ಹಂತ 3 — Expand & shrink ಹೇಗೆ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  right ಅನ್ನ ಮುಂದಕ್ಕೆ ಸರಿಸ್ತಾ ಇರು, window ಗೆ characters add
     ಮಾಡ್ತಾ ಹೋಗು
  →  window valid ಆದ ಕೂಡ್ಲೆ (ಎಲ್ಲಾ required chars ಸಿಕ್ಕಿದೆ) —
     left ಅನ್ನ ಎಷ್ಟು ಸಾಧ್ಯವೋ ಅಷ್ಟು ಒಳಗೆ ತಂದು, window valid
     ಆಗಿರೋ ತನಕ shrink ಮಾಡ್ತಾ ಹೋಗು, ಪ್ರತಿ valid window ಗೂ
     length track ಮಾಡು
  →  invalid ಆದ ತಕ್ಷಣ shrink ನಿಲ್ಲಿಸಿ, right ಅನ್ನ ಮತ್ತೆ ಮುಂದಕ್ಕೆ
     ಸರಿಸು

  ಹಂತ 4 — "valid" ಅನ್ನ efficient ಆಗಿ ಹೇಗೆ track ಮಾಡೋದು?
  →  "have" counter (ಎಷ್ಟು DISTINCT required characters ನ count
     ಈಗ satisfy ಆಗಿದೆ) ಮತ್ತು "need" (t ಒಳಗಿನ TOTAL distinct
     required characters) — have == need ಆದ್ರೆ window valid!

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು:
  →  "This is a classic expand-shrink sliding window — grow right
      until the window covers t, then greedily shrink from the
      left while it's still valid, recording the smallest valid
      window seen"
  →  "Track need/have counters over distinct characters so
      validity can be checked in O(1) instead of comparing full
      frequency maps each time"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Sliding Window (variable size, expand + shrink) +
              Frequency Count (need/have counters)
  Secondary : Brute-force check every substring against t's
              frequency requirement

  WHY Expand-Shrink Sliding Window?
  → Once a window covers t, everything useful about making it
    SMALLER lies at its edges — shrinking from the left as far as
    validity allows finds the tightest window ending at the
    current right pointer, without ever re-scanning the interior.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  The journey from brute to optimal:
    Brute thought   →  For every (i, j) pair, build a frequency
                       map of s[i:j+1] and check it covers t
    Problem with it →  O(n^2) substrings, O(n) frequency check
                       each → O(n^3) total
    Better question →  "Once a window covers t, can I shrink it
                       from the left without re-scanning
                       everything, and know exactly when it stops
                       being valid?"
    Insight         →  Track need (distinct chars required) and
                       have (distinct chars currently satisfied)
                       — a single O(1) comparison tells validity;
                       expand right to find validity, shrink left
                       to minimize it
    Optimal         →  Each pointer moves forward only, O(n) time,
                       O(k) space for k distinct chars in t

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE (check every substring)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    For every substring s[i:j+1], build its frequency map and
    check every required character in t is covered with enough
    count. Track the shortest valid one.

  Pseudocode:
    step 1: t_count = frequency map of t; best = None
    step 2: for i in range(n):
    step 3:   for j in range(i, n):
    step 4:     window_count = frequency map of s[i:j+1]
    step 5:     if window_count covers t_count:
    step 6:       update best if shorter; break inner loop
    step 7: return best or ""

  Time  : O(n^3)  →  Why: O(n^2) substrings, each covering-check
                          costs O(|t|) to O(n)
  Space : O(k)     →  Why: frequency maps bounded by distinct
                          characters involved

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ?
    → Rebuilds a frequency map for every substring from scratch —
      massively redundant when consecutive windows overlap almost
      entirely.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 6 — APPROACH 2 — OPTIMAL (Expand-Shrink Sliding Window)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Maintain a window [left, right] and a frequency count of
    characters inside it. `need` = number of distinct characters
    in t; `have` = number of distinct required characters whose
    in-window count has reached their required count. Expand
    `right` until have == need (window valid), then shrink `left`
    while still valid, recording the smallest window at each valid
    point.

  Key steps:
    1. if not t: return ""
    2. t_count = frequency map of t; need = len(t_count)
    3. window_count = {}; have = 0; left = 0
    4. best_len, best_left = infinity, 0
    5. for right, ch in enumerate(s):
    6.   window_count[ch] += 1
    7.   if ch in t_count and window_count[ch] == t_count[ch]:
    8.     have += 1
    9.   while have == need:
    10.    if (right - left + 1) < best_len: update best
    11.    window_count[s[left]] -= 1
    12.    if s[left] in t_count and window_count[s[left]] < t_count[s[left]]:
    13.      have -= 1
    14.    left += 1
    15. return s[best_left:best_left+best_len] or ""

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ:
    → "right ಅನ್ನ ಮುಂದಕ್ಕೆ ಸರಿಸ್ತಾ window ಗೆ characters add ಮಾಡು.
       ಎಲ್ಲಾ required characters ಸಿಕ್ಕ ತಕ್ಷಣ (have == need), left
       ಅನ್ನ ಎಷ್ಟು ಸಾಧ್ಯವೋ ಅಷ್ಟು shrink ಮಾಡು, ಪ್ರತಿ valid window
       ಗೂ length track ಮಾಡು. Invalid ಆದ ತಕ್ಷಣ shrink ನಿಲ್ಲಿಸಿ
       right ಅನ್ನ ಮತ್ತೆ ಮುಂದಕ್ಕೆ ಸರಿಸು!"

  Time  : O(n + m)  →  Why: `right` visits each of n chars once;
                            `left` moves forward at most n times
                            total across the whole run; building
                            t_count costs O(m)
  Space : O(k)       →  Why: frequency maps bounded by the number
                            of distinct characters in t (and s)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 7 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: s = "ADOBECODEBANC", t = "ABC"

  t_count = {A:1, B:1, C:1}, need = 3

  right expands until window "ADOBEC" (indices 0-5) covers
  A,B,C → have=3=need → shrink:
    left=0 'A' removed → window_count[A]=0 < 1 → have=2, stop
    shrink (window before removal "ADOBEC" len=6 recorded as
    best so far)

  right continues expanding... eventually window "CODEBA" then
  "CODEBANC" (indices 5-12) becomes valid again (have=3) →
    shrink from left: removes C,O,D,E one by one while still
    valid ("BANC" all present after trimming CODE) → shrinks to
    "BANC" (indices 9-12, length 4) — have drops below 3 only
    after trying to remove 'B' → stop, "BANC" recorded, shorter
    than 6

  Output: "BANC" ✓ (length 4, shortest valid window)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 8 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ No valid window exists "a"/"aa"? →  "" — t needs more copies
                                          of a char than s has
  ✓ s itself equals t?               →  s — the whole string is
                                          the tightest window
  ✓ t longer than s?                 →  "" — impossible to cover
  ✓ Duplicate chars in t "AABC"?     →  window must satisfy the
                                          EXACT required count per
                                          character, not just
                                          "contains the letter"
  ✓ Multiple valid windows, tie?     →  keep the FIRST shortest
                                          found (leftmost) — any
                                          correct-length answer is
                                          accepted by LeetCode

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 9 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                            Time      Space
  Brute (all substrings)    O(n^3)    O(k)
  Optimal (expand-shrink)   O(n+m)    O(k)   ← use this ✅

  Time yaake O(n+m)?  → `right` and `left` each traverse s at
                         most once (amortized), t_count built once
                         from t
  Space yaake O(k)?   → frequency maps bounded by distinct
                         characters in t (and matched chars in s)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 10 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Sliding Window (expand-shrink) with need/have
                counters

  Ee pattern yaavaaga use maadabeeku?
  → "Smallest/shortest window that SATISFIES a covering condition"
     — expand to find validity, shrink to minimize it
  → Whenever a window's validity can be tracked with an O(1)
     counter update instead of a full recheck

  Idee pattern beere problemsalli kaanisatte:
  → Permutation in String #567 (fixed-size window + exact
     frequency match, simpler validity check)
  → Longest Repeating Character Replacement #424 (variable window,
     but a MAXIMIZING condition instead of minimizing)
  → Longest Substring Without Repeating Characters #3 (variable
     window, uniqueness instead of a covering condition)

  Next time intaha problem bandre naanu modalu idannu think maadtene:
  → "Shortest window covering a set bekagidre → expand-shrink
     sliding window, need/have counters track madi have==need
     aadaga shrink start madu!"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 11 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "Find the shortest substring of s that contains every
      character of t, with at least t's required counts."

  2. Brute force:
     "Check every substring's frequency map against t's — O(n^3),
      far too slow for n up to 10^5."

  3. Optimize:
     "Expand a window with `right` until it covers t (tracked via
      need/have counters over distinct characters), then greedily
      shrink from `left` while still valid, recording the smallest
      window at each valid point. Continue expanding after
      shrinking stalls."

  4. Code:
     "A frequency map for t, a running window frequency map, and
      need/have counters — O(1) validity check per step instead
      of comparing full maps."

  5. Complexity:
     "Time O(n + m) — each pointer moves forward only.
      Space O(k) — bounded by distinct characters involved."

  Mukhya: expand PARDI valid madu, shrink PARDI minimize madu —
          eradu goals na eradu different pointers ge split madu!
"""


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(n^3) Time | O(k) Space
# ═══════════════════════════════════════════════════════════════════
def min_window_brute(s, t):
    """
    Idu modala aaloochane — prati substring na t_count ge covers
    aaguthaa antha check madi shortest track madu
    """
    if not s or not t:
        return ""

    t_count = {}
    for ch in t:
        t_count[ch] = t_count.get(ch, 0) + 1

    def covers(window_count):
        for ch, cnt in t_count.items():
            if window_count.get(ch, 0) < cnt:
                return False
        return True

    best = ""
    n_s = len(s)
    for i in range(n_s):
        window_count = {}
        for j in range(i, n_s):
            window_count[s[j]] = window_count.get(s[j], 0) + 1
            if covers(window_count):
                if best == "" or (j - i + 1) < len(best):
                    best = s[i:j + 1]
                break

    return best


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n + m) Time | O(k) Space (expand-shrink sliding window)
# ═══════════════════════════════════════════════════════════════════
def min_window(s, t):
    """
    Idu final answer — need/have counters track madi, right inda
    expand, valid aadaga left inda shrink madi tightest window hudku
    """
    if not s or not t:
        return ""

    t_count = {}
    for ch in t:
        t_count[ch] = t_count.get(ch, 0) + 1
    need = len(t_count)

    window_count = {}
    have = 0
    left = 0
    best_len = float("inf")
    best_left = 0

    for right, ch in enumerate(s):
        window_count[ch] = window_count.get(ch, 0) + 1
        if ch in t_count and window_count[ch] == t_count[ch]:
            have += 1

        while have == need:
            if (right - left + 1) < best_len:
                best_len = right - left + 1
                best_left = left

            left_ch = s[left]
            window_count[left_ch] -= 1
            if left_ch in t_count and window_count[left_ch] < t_count[left_ch]:
                have -= 1
            left += 1

    return "" if best_len == float("inf") else s[best_left:best_left + best_len]


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # Test 1 — Basic
    assert min_window("ADOBECODEBANC", "ABC") == "BANC"

    # Test 2 — Single character match
    assert min_window("a", "a") == "a"

    # Test 3 — No valid window exists
    assert min_window("a", "aa") == ""

    # Test 4 — t longer than s
    assert min_window("ab", "abc") == ""

    # Test 5 — t equals s
    assert min_window("abc", "abc") == "abc"

    # Cross-check against brute force
    assert min_window_brute("ADOBECODEBANC", "ABC") == "BANC"
    assert min_window_brute("a", "a") == "a"
    assert min_window_brute("a", "aa") == ""
    assert min_window_brute("ab", "abc") == ""
    assert min_window_brute("abc", "abc") == "abc"

    print("All tests passed!")
