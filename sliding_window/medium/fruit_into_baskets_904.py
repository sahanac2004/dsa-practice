"""
╔════════════════════════════════════════════════════════════════════╗
║  FRUIT INTO BASKETS                                                ║
║  LeetCode #904  |  Difficulty: Medium  |  Topic: Sliding Window    ║
║  Link: https://leetcode.com/problems/fruit-into-baskets/           ║
╚════════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  A row of fruit trees is given as `fruits`, where `fruits[i]`
  is the TYPE of fruit tree i produces. You have exactly TWO
  baskets, each holding only ONE fruit type (unlimited quantity
  of that type). Starting from any tree, you must pick exactly
  one fruit from every tree moving RIGHT, stopping the moment a
  third fruit type would be required.

  Return the MAXIMUM number of fruits you can collect this way.

  Input : fruits = array of fruit type integers
  Output: integer — max fruits collectible with only 2 basket types

  Example 1 — basic:
    Input : fruits = [1, 2, 1]
    Output: 3
    Why?  : only two distinct types (1 and 2) appear in the
            entire array — both baskets suffice, collect everything

  Example 2 — slightly tricky (must skip the start):
    Input : fruits = [0, 1, 2, 2]
    Output: 3
    Why?  : starting at index 0 hits three types (0,1,2) too
            soon; starting at index 1 gives [1,2,2] — only 2
            types, length 3, which is the best possible

  Example 3 — longer stretch in the middle:
    Input : fruits = [1, 2, 3, 2, 2]
    Output: 4
    Why?  : the window [2,3,2,2] (indices 1-4) has only types
            {2,3} — length 4, better than any window containing
            the initial "1"

  Constraints:
    - 1 <= fruits.length <= 10^5
    - 0 <= fruits[i] < fruits.length

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Problem odi aada mele namma brain enu think maadabeeku:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  fruit types ಇರೋ array           │
  │  Output ಏನು ಬೇಕು?     →  ಗರಿಷ್ಠ 2 DISTINCT types ಇರೋ     │
  │                           ಅತಿ ಉದ್ದ CONTIGUOUS subarray    │
  │                           ರ length                        │
  │  Constraints ಏನಿದೆ?   →  ಎಲ್ಲಿ ಬೇಕಾದ್ರೂ ಶುರು ಮಾಡಬಹುದು,   │
  │                           ಆದ್ರೆ contiguous ಆಗಿ ಮಾತ್ರ       │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — "2 baskets, ಒಂದೊಂದು type ಗೂ ಒಂದು basket" ಅಂದ್ರೆ
           ಏನಂತ ಪುನಃ ಬರೆಯಿರಿ
  →  ಇದೇ "ಗರಿಷ್ಠ 2 DISTINCT elements ಇರೋ ಅತಿ ಉದ್ದ contiguous
     subarray ಹುಡುಕು" ಅನ್ನೋ classic problem — 'k' ಅನ್ನ 2 ಗೆ
     fix ಮಾಡಿದ ಹಾಗೆ!
  →  ಇದೇ #395 (K Distinct Characters) ಮತ್ತು strings ರ
     Longest Substring with At Most K Distinct Characters
     problems ಗೆ EXACT ಆಗಿ ಹೊಂದುತ್ತೆ, ಬರೀ k=2 fixed

  ಹಂತ 3 — ಮೊದಲ simple idea ಏನು?
  →  ಪ್ರತಿ starting point ಇಂದ, right ಅನ್ನ extend ಮಾಡ್ತಾ ಹೋಗಿ,
     distinct types ≤ 2 ಇರೋವರೆಗೆ — max length track ಮಾಡಿ

  ಹಂತ 4 — Sliding Window (frequency map) ಹೇಗೆ?
  →  freq map ಇಟ್ಟುಕೊಂಡು, right ಅನ್ನ ಒಂದೊಂದೇ ಸರಿಸಿ, ಆ fruit
     type ರ count ++ ಮಾಡು
  →  distinct types (freq map ರ keys count) > 2 ಆದ್ರೆ, left
     ಅನ್ನ ಸರಿಸ್ತಾ ಹೋಗು, ಆ fruit type ರ count -- ಮಾಡಿ, count 0
     ಆದ್ರೆ ಆ key ಅನ್ನ map ಇಂದ ತೆಗೆ
  →  ಪ್ರತಿ step ನಲ್ಲೂ window size ಅನ್ನ max ಜೊತೆ compare ಮಾಡಿ
     track ಮಾಡು

  ಹಂತ 5 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  "distinct types ≤ 2" condition MONOTONIC — window shrink
     ಮಾಡಿದಾಗ distinct count ಎಂದಿಗೂ ಜಾಸ್ತಿ ಆಗಲ್ಲ — ಇದೇ clean
     variable sliding window ಗೆ ಬೇಕಾದ property
  →  left pointer ಎಂದಿಗೂ ಹಿಂದಕ್ಕೆ ಹೋಗಲ್ಲ — single pass O(n)

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು:
  →  "This is 'longest subarray with at most 2 distinct values'
      in disguise — the two baskets map directly to k=2"
  →  "Maintain a frequency map of the window; if distinct count
      exceeds 2, shrink from the left until it's back to 2"
  →  "Track the max window size throughout — that's the answer"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Sliding Window (Variable) — at-most-2-distinct-types
  Secondary : Brute-force expand-and-check per starting index

  WHY Sliding Window (at-most-k, k=2)?
  → "At most 2 distinct fruit types in the window" is a monotonic
    condition — exactly the shape that a growing/shrinking window
    with a frequency map handles cleanly and in one linear pass,
    just like the general "at most K distinct" family.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  The key insight: two baskets, one type each, means the picking
  spree is really just "the longest contiguous stretch containing
  at most 2 distinct fruit types." Once reframed this way, it's
  the exact same problem as "Longest Substring with At Most K
  Distinct Characters" with k hardcoded to 2 — a frequency map
  sliding window tracks how many distinct types are currently in
  play, shrinking only when a third type sneaks in.

  The journey from brute to optimal:
    Brute thought   →  For each starting index, expand right
                       while distinct-type count stays ≤ 2,
                       tracking the max length
    Problem with it →  Restarting the type-tracking from scratch
                       at every new start wastes work — O(n^2)
    Better question →  "Can I keep growing right without ever
                       resetting, pulling left forward only when
                       a third type actually appears?"
    Insight         →  Monotonic condition → single forward-only
                       two-pointer pass suffices
    Optimal         →  O(n) time, O(1) space (map holds at most
                       3 keys before a shrink)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE (expand from every start)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    For every starting index `left`, extend `right` outward,
    tracking the set of distinct types seen. Stop extending once
    a third type appears, recording the window length up to
    that point.

  Pseudocode:
    step 1: max_len = 0
    step 2: for left in range(n):
    step 3:   types = set()
    step 4:   for right in range(left, n):
    step 5:     types.add(fruits[right])
    step 6:     if len(types) > 2: break
    step 7:     max_len = max(max_len, right - left + 1)
    step 8: return max_len

  Time  : O(n^2)  →  Why: for each of n starting points, the
                          inner loop can scan up to n elements
  Space : O(1)     →  Why: the types set holds at most 3 elements

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ?
    → Correct, but recomputes the distinct-type tracking from
      scratch at every starting index — a single forward-only
      sliding window avoids this redundant work entirely.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 6 — APPROACH 2 — OPTIMAL (Sliding Window, at most 2 distinct)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Maintain a frequency map of fruit types currently in the
    window [left, right]. Grow `right` one step at a time,
    incrementing that type's count. Whenever the map has more
    than 2 distinct keys, shrink from the left — decrement the
    leaving type's count, and remove it from the map if it hits
    zero — until only 2 types remain. Track the max window size.

  Key steps:
    1. left = 0, freq = {}, max_len = 0
    2. for right in range(n):
    3.   freq[fruits[right]] = freq.get(fruits[right], 0) + 1
    4.   while len(freq) > 2:
    5.     freq[fruits[left]] -= 1
    6.     if freq[fruits[left]] == 0: del freq[fruits[left]]
    7.     left += 1
    8.   max_len = max(max_len, right - left + 1)
    9. return max_len

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ:
    → "right ಅನ್ನ ಒಂದೊಂದೇ ಸರಿಸಿ, freq map update ಮಾಡು.
       distinct types (map keys) > 2 ಆದ್ರೆ, left ಅನ್ನ ಸರಿಸ್ತಾ
       ಹೋಗು, ಆ type count-- ಮಾಡಿ, 0 ಆದ್ರೆ map ಇಂದ ತೆಗೆ —
       ಸರಿ ಆಗೋವರೆಗೆ. ಪ್ರತಿ step ನಲ್ಲೂ window size max track
       ಮಾಡು!"

  Time  : O(n)  →  Why: both left and right pointers only ever
                        move forward, combined O(n) total
  Space : O(1)  →  Why: freq map holds at most 3 keys at once
                        (bounded constant, not input-size dependent)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 7 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: fruits = [1, 2, 3, 2, 2]

  right  fruit  freq after add        distinct  action        max_len
  0      1      {1:1}                 1         window[0,0]   1
  1      2      {1:1,2:1}             2         window[0,1]   2
  2      3      {1:1,2:1,3:1}         3         shrink: left=0
                                                 (fruit=1,count→0,
                                                 remove) left=1
                                                 freq={2:1,3:1}
                                                 window[1,2]   2
  3      2      {2:2,3:1}             2         window[1,3]   3
  4      2      {2:3,3:1}             2         window[1,4]   4

  Output: 4 ✓

  ಇನ್ನೊಂದು example — must skip the start:
  Input: fruits = [0, 1, 2, 2]

  right0(0): freq{0:1} window[0,0] max1
  right1(1): freq{0:1,1:1} window[0,1] max2
  right2(2): freq{0:1,1:1,2:1} distinct3 → shrink left=0(fruit0,
             remove) left=1, freq{1:1,2:1} window[1,2] max2
  right3(2): freq{1:1,2:2} window[1,3] max3

  Output: 3 ✓

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 8 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ Only 1 or 2 types in whole array? →  entire array length
                                          (e.g. [1,2,1] → 3)
  ✓ Single tree [5]?                  →  1 — trivially itself
  ✓ All same type [3,3,3,3]?          →  4 — only 1 distinct type
                                          throughout
  ✓ Every tree a different type
    [1,2,3,4]?                        →  2 — best possible is
                                          any adjacent pair
  ✓ Best window in the middle?        →  handled naturally, no
                                          special-casing needed

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 9 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                        Time    Space
  Brute (expand each)    O(n^2)  O(1)
  Sliding Window          O(n)    O(1)   ← use this ✅

  Time yaake O(n)?  → left and right pointers each move forward
                       at most n times total, combined O(n)
  Space yaake O(1)? → freq map bounded to at most 3 keys at once

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 10 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Sliding Window — "At Most K Distinct" (k fixed to 2)

  Ee pattern yaavaaga use maadabeeku?
  → "Longest contiguous run with at most K distinct types/values/
     categories" family — the "2 baskets" story is just a
     fixed-K=2 dress-up of this well-known template
  → Whenever a real-world constraint ("N baskets," "N colors
     allowed," etc.) translates directly to "at most N distinct
     values in the window"

  Idee pattern beere problemsalli kaanisatte:
  → Longest Substring with At Most K Distinct Characters (general
     K version of this exact same technique)
  → Max Consecutive Ones III #1004 (previous problem — same
     "at most k violations" sliding window shape, zeros instead
     of a third distinct type)
  → Binary Subarrays With Sum #930 (next problem — different
     exact-match framing, but same sliding-window toolbox)

  Next time intaha problem bandre naanu modalu idannu think maadtene:
  → "'N baskets/colors/types allowed' kelidre → 'at most N
     distinct values in window' antha reframe madu — frequency
     map sliding window, left forward-only!"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 11 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "Two baskets, one fruit type each — find the longest
      contiguous stretch of trees with at most 2 distinct fruit
      types."

  2. Brute force:
     "For each start, expand right tracking distinct types seen,
      stop at a third type. O(n^2) since tracking restarts every
      time."

  3. Optimize:
     "Reframe as 'longest subarray with at most 2 distinct
      values.' Sliding window with a frequency map: grow right,
      shrink left whenever a third type appears, track max size."

  4. Code:
     "freq dict keyed by fruit type. While len(freq) > 2, shrink
      left (decrement count, delete key at zero). Update max
      after every right-pointer step."

  5. Complexity:
     "Time O(n) — both pointers move forward only. Space O(1) —
      map bounded to 3 keys."

  Mukhya: 'N baskets/types allowed' stories are almost always
          'at most N distinct values in a window' in disguise —
          spot the reframe and reuse the classic sliding window!
"""


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(n^2) Time | O(1) Space (expand from every start)
# ═══════════════════════════════════════════════════════════════════
def total_fruit_brute(fruits):
    """
    Idu modala aaloochane — prati start inda right extend madi,
    distinct types <= 2 iro tanaka max length track madu
    """
    n = len(fruits)
    max_len = 0

    for left in range(n):
        types = set()
        for right in range(left, n):
            types.add(fruits[right])
            if len(types) > 2:
                break
            max_len = max(max_len, right - left + 1)

    return max_len


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n) Time | O(1) Space (sliding window, at most 2 distinct)
# ═══════════════════════════════════════════════════════════════════
def total_fruit(fruits):
    """
    Idu final answer — right forward-only extend madi, distinct
    types (freq map keys) > 2 aadre left shrink madu, max track madu
    """
    left = 0
    freq = {}
    max_len = 0

    for right in range(len(fruits)):
        freq[fruits[right]] = freq.get(fruits[right], 0) + 1

        while len(freq) > 2:
            freq[fruits[left]] -= 1
            if freq[fruits[left]] == 0:
                del freq[fruits[left]]
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # Test 1 — Basic (whole array works)
    assert total_fruit([1, 2, 1]) == 3

    # Test 2 — Must skip the start
    assert total_fruit([0, 1, 2, 2]) == 3

    # Test 3 — Best window in the middle
    assert total_fruit([1, 2, 3, 2, 2]) == 4

    # Test 4 — Single tree
    assert total_fruit([5]) == 1

    # Test 5 — Every tree a different type
    assert total_fruit([1, 2, 3, 4]) == 2

    # Cross-check: brute force must agree on all of the above
    assert total_fruit_brute([1, 2, 1]) == 3
    assert total_fruit_brute([0, 1, 2, 2]) == 3
    assert total_fruit_brute([1, 2, 3, 2, 2]) == 4
    assert total_fruit_brute([5]) == 1
    assert total_fruit_brute([1, 2, 3, 4]) == 2

    print("All tests passed!")
