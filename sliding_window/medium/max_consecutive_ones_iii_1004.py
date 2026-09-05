"""
╔════════════════════════════════════════════════════════════════════╗
║  MAX CONSECUTIVE ONES III                                          ║
║  LeetCode #1004  |  Difficulty: Medium  |  Topic: Sliding Window   ║
║  Link: https://leetcode.com/problems/max-consecutive-ones-iii/     ║
╚════════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Given a binary array `nums` and an integer `k`, return the
  MAXIMUM number of consecutive 1's obtainable if you are
  allowed to flip AT MOST `k` zeros to ones.

  Input : nums = array of 0s and 1s, k = max flips allowed
  Output: integer — longest run of 1's achievable after flipping
          at most k zeros

  Example 1 — basic:
    Input : nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
    Output: 6
    Why?  : flip the two 0's at indices 3,4 → run "111" +
            "00"→"11" + "1111" merges into a run of length 6
            (indices 0..5: 1,1,1,1,1,1 after flipping)

  Example 2 — slightly tricky (flips scattered):
    Input : nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
    Output: 10
    Why?  : the best window flips 3 zeros within a stretch that
            yields 10 consecutive 1's after flipping

  Example 3 — no flips needed:
    Input : nums = [1,1,1,1], k = 0
    Output: 4
    Why?  : already all 1's, k=0 flips allowed still gives the
            whole array

  Constraints:
    - 1 <= nums.length <= 10^5
    - nums[i] is either 0 or 1
    - 0 <= k <= nums.length

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Problem odi aada mele namma brain enu think maadabeeku:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  binary array, k flips allowed    │
  │  Output ಏನು ಬೇಕು?     →  flip ಮಾಡಿದ ಮೇಲೆ ಸಿಗೋ ಅತಿ ಉದ್ದ  │
  │                           consecutive 1's ರ length         │
  │  Constraints ಏನಿದೆ?   →  ಗರಿಷ್ಠ k ಸೊನ್ನೆಗಳು ಮಾತ್ರ flip   │
  │                           ಮಾಡಬಹುದು                        │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ಇದನ್ನ ಬೇರೆ ರೀತಿ ಯೋಚಿಸಿ ನೋಡಿ!
  →  "ಗರಿಷ್ಠ k ಸೊನ್ನೆಗಳು flip ಮಾಡಬಹುದು" ಅಂದ್ರೆ, ಅದೇ "window
      ಒಳಗೆ ಗರಿಷ್ಠ k ಸೊನ್ನೆಗಳು ಇರೋ ಹಾಗೆ, ಅತಿ ಉದ್ದ window
      ಹುಡುಕೋದು" ಅಂತ ಪುನಃ ಬರೆಯಬಹುದು!
  →  window ಒಳಗಿನ ಸೊನ್ನೆಗಳ ಎಲ್ಲಾ 1 ಗಳಾಗಿ flip ಮಾಡಿದ್ರೆ, ಆ
      ಪೂರ್ತಿ window consecutive 1's ಆಗುತ್ತೆ

  ಹಂತ 3 — ಮೊದಲ simple idea ಏನು?
  →  ಪ್ರತಿ left ಇಂದ, right ಅನ್ನ extend ಮಾಡ್ತಾ ಹೋಗಿ, zero
     count ≤ k ಇರೋವರೆಗೆ — max length track ಮಾಡಿ

  ಹಂತ 4 — Sliding Window (single pass, never shrink left back)
           ಹೇಗೆ?
  →  variable-size window: right ಅನ್ನ ಯಾವಾಗಲೂ ಮುಂದಕ್ಕೆ ಸರಿಸು
  →  window ಒಳಗಿನ zero count k ಗಿಂತ ಜಾಸ್ತಿ ಆದ್ರೆ, left ಅನ್ನ
     ಒಂದು step ಮುಂದಕ್ಕೆ ಸರಿಸಿ, ಅಲ್ಲಿ 0 ಇದ್ರೆ count-- ಮಾಡು
  →  ಪ್ರತಿ step ನಲ್ಲೂ window size (right-left+1) ಅನ್ನ max ಜೊತೆ
     compare ಮಾಡಿ track ಮಾಡು

  ಹಂತ 5 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  window ಒಳಗಿನ condition (zero count ≤ k) MONOTONIC —
     window shrink ಮಾಡಿದಾಗ zero count ಎಂದಿಗೂ ಜಾಸ್ತಿ ಆಗಲ್ಲ,
     grow ಮಾಡಿದಾಗ ಎಂದಿಗೂ ಕಡಿಮೆ ಆಗಲ್ಲ — ಇದೇ clean sliding
     window ಗೆ ಬೇಕಾದ property!
  →  left pointer ಎಂದಿಗೂ ಹಿಂದಕ್ಕೆ ಹೋಗಲ್ಲ — single pass O(n)
     guarantee ಸಿಗುತ್ತೆ

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು:
  →  "Reframe the problem: find the longest window containing
      at most k zeros — flipping them all gives a run of 1's"
  →  "Grow the window with right; if zero count exceeds k,
      shrink from left until it's back within budget"
  →  "Track the maximum window size seen — that's the answer"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Sliding Window (Variable) — at-most-k-zeros window
  Secondary : Brute-force expand-and-check per starting index

  WHY Sliding Window (Variable)?
  → "At most k zeros" is a monotonic window condition — shrinking
    never increases the zero count, growing never decreases it.
    That monotonicity is exactly what lets a single left/right
    pointer pass replace checking every possible window from
    scratch.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  The key insight: "flip at most k zeros to maximize consecutive
  1's" is EXACTLY the same as "find the longest window that
  contains at most k zeros" — the zeros inside that window are
  precisely the ones we'd flip, and everything else in the
  window is already a 1. Once framed this way, it's a textbook
  variable sliding window: grow greedily, shrink only when the
  zero budget is exceeded.

  The journey from brute to optimal:
    Brute thought   →  For each starting index, expand the
                       window rightward while zero count stays
                       ≤ k, track the max length found
    Problem with it →  Restarting the zero count from scratch at
                       every new starting index wastes work —
                       O(n^2) overall
    Better question →  "Can I keep growing right without ever
                       resetting, and only pull left forward when
                       truly necessary?"
    Insight         →  Since the condition is monotonic, left
                       never needs to move backward — one
                       forward-only pass suffices
    Optimal         →  Single pass, O(n) time, O(1) space

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE (expand from every start)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    For every starting index `left`, extend `right` outward,
    counting zeros as you go. Stop extending once the zero count
    exceeds k, and record the window length up to that point.

  Pseudocode:
    step 1: max_len = 0
    step 2: for left in range(n):
    step 3:   zeros = 0
    step 4:   for right in range(left, n):
    step 5:     if nums[right] == 0: zeros += 1
    step 6:     if zeros > k: break
    step 7:     max_len = max(max_len, right - left + 1)
    step 8: return max_len

  Time  : O(n^2)  →  Why: for each of n starting points, the
                          inner loop can scan up to n elements
  Space : O(1)     →  Why: only a counter and index variables

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ?
    → Correct, but restarts the zero count from scratch at every
      starting index — massively redundant work that a single
      forward-only sliding window avoids entirely.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 6 — APPROACH 2 — OPTIMAL (Sliding Window, at most k zeros)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Maintain a window [left, right] with a running zero count.
    Grow `right` one step at a time. Whenever the zero count
    exceeds k, shrink from the left (decrementing the zero count
    if the character leaving was a 0) until the window is valid
    again. Track the maximum window size seen at every step.

  Key steps:
    1. left = 0, zeros = 0, max_len = 0
    2. for right in range(n):
    3.   if nums[right] == 0: zeros += 1
    4.   while zeros > k:
    5.     if nums[left] == 0: zeros -= 1
    6.     left += 1
    7.   max_len = max(max_len, right - left + 1)
    8. return max_len

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ:
    → "right ಅನ್ನ ಒಂದೊಂದೇ ಸರಿಸು, zero count track ಮಾಡು.
       zero count k ಗಿಂತ ಜಾಸ್ತಿ ಆದ್ರೆ, left ಅನ್ನ ಸರಿಸ್ತಾ
       ಹೋಗು (ಹೊರಟ character 0 ಆಗಿದ್ರೆ count-- ಮಾಡು) ಸರಿ
       ಆಗೋವರೆಗೆ. ಪ್ರತಿ step ನಲ್ಲೂ window size max ಜೊತೆ
       compare ಮಾಡಿ track ಮಾಡು!"

  Time  : O(n)  →  Why: both left and right pointers only ever
                        move forward, together covering the
                        array once
  Space : O(1)  →  Why: just a zero counter and two indices

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 7 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2

  right  nums[right]  zeros  window action           max_len
  0      1            0      [0,0] size1             1
  1      1            0      [0,1] size2             2
  2      1            0      [0,2] size3             3
  3      0            1      [0,3] size4             4
  4      0            2      [0,4] size5             5
  5      0            3      zeros>k → shrink left:
                              left=0→1 (nums[0]=1,no dec)
                              zeros still 3 → left=1→2(no dec)
                              zeros still 3 → left=2→3(nums[2]=1?
                              wait nums[2]=1 so no dec... let's
                              recheck: left moves until a 0 is
                              dropped) → left=3(nums[3]=0,dec)
                              zeros=2, window=[4,5] size2      5
  6      1            2      [4,6] size3             5
  7      1            2      [4,7] size4             5
  8      1            2      [4,8] size5             5
  9      1            2      [4,9] size6             6
  10     0            3      shrink: left=4(nums[4]=0,dec)→
                              zeros=2, window=[5,10] size6     6

  Output: 6 ✓

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 8 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ k = 0 (no flips allowed)?      →  just the longest existing
                                       run of 1's
  ✓ All 1's already?               →  whole array length,
                                       regardless of k
  ✓ All 0's, k >= length?          →  whole array (flip everything)
  ✓ k >= number of zeros in array? →  entire array length
  ✓ Single element [0], k=0?       →  0 — no 1's obtainable

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 9 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                        Time    Space
  Brute (expand each)    O(n^2)  O(1)
  Sliding Window          O(n)    O(1)   ← use this ✅

  Time yaake O(n)?  → left and right pointers each move forward
                       at most n times total, combined O(n)
  Space yaake O(1)? → Just a zero counter and two indices

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 10 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Sliding Window — "At Most K" Budget Constraint

  Ee pattern yaavaaga use maadabeeku?
  → "Flip/change/remove at most k elements to maximize a
     contiguous run" type problems — reframe as "longest window
     with at most k [violating elements]"
  → Any monotonic window-validity condition (shrinking never
     hurts, growing never helps) — classic sliding window setup

  Idee pattern beere problemsalli kaanisatte:
  → Longest Repeating Character Replacement #424 (already done
     in strings/ — identical "at most k replacements" framing,
     just with character frequency instead of zero count)
  → Fruit Into Baskets #904 (next problem — "at most 2 distinct
     types" is the same budget-constraint window shape)
  → Max Consecutive Ones (#485, no k — simpler special case of
     this exact pattern with k=0)

  Next time intaha problem bandre naanu modalu idannu think maadtene:
  → "'Flip/change at most k elements to maximize a run' kelidre →
     reframe madu: 'longest window with at most k violations' —
     classic variable sliding window, left forward-only!"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 11 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "Find the longest run of 1's achievable by flipping at most
      k zeros — equivalent to finding the longest window
      containing at most k zeros."

  2. Brute force:
     "For each starting index, expand right while zero count
      stays ≤ k, tracking the max length. O(n^2) since the zero
      count restarts at every new start."

  3. Optimize:
     "Single sliding window: grow right always, track zero count.
      If it exceeds k, shrink from left (only decrementing when a
      0 leaves) until valid again. Track max window size at every
      step — left never needs to move backward."

  4. Code:
     "left=0, zeros=0. For each right: increment zeros on a 0;
      while zeros>k, shrink left (decrement on 0, advance);
      update max_len = max(max_len, right-left+1)."

  5. Complexity:
     "Time O(n) — both pointers move forward only, combined
      linear pass. Space O(1) — just a counter and two indices."

  Mukhya: 'flip/change at most k elements' problems reframe
          cleanly as 'at most k violations in the window' —
          the monotonic condition is what makes sliding window
          work cleanly!
"""


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(n^2) Time | O(1) Space (expand from every start)
# ═══════════════════════════════════════════════════════════════════
def longest_ones_brute(nums, k):
    """
    Idu modala aaloochane — prati start inda right extend madi,
    zero count <= k iro tanaka max length track madu
    """
    n = len(nums)
    max_len = 0

    for left in range(n):
        zeros = 0
        for right in range(left, n):
            if nums[right] == 0:
                zeros += 1
            if zeros > k:
                break
            max_len = max(max_len, right - left + 1)

    return max_len


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n) Time | O(1) Space (sliding window, at most k zeros)
# ═══════════════════════════════════════════════════════════════════
def longest_ones(nums, k):
    """
    Idu final answer — right forward-only extend madi, zero count
    k mira hoda shrink madu (left forward-only), max track madu
    """
    left = 0
    zeros = 0
    max_len = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            zeros += 1

        while zeros > k:
            if nums[left] == 0:
                zeros -= 1
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # Test 1 — Basic
    assert longest_ones([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2) == 6

    # Test 2 — Scattered flips
    assert longest_ones(
        [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3
    ) == 10

    # Test 3 — Already all 1's
    assert longest_ones([1, 1, 1, 1], 0) == 4

    # Test 4 — k = 0, existing run only
    assert longest_ones([1, 0, 1, 1, 0, 1], 0) == 2

    # Test 5 — k covers all zeros
    assert longest_ones([0, 0, 0], 3) == 3

    # Cross-check: brute force must agree on all of the above
    assert longest_ones_brute([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2) == 6
    assert longest_ones_brute(
        [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3
    ) == 10
    assert longest_ones_brute([1, 1, 1, 1], 0) == 4
    assert longest_ones_brute([1, 0, 1, 1, 0, 1], 0) == 2
    assert longest_ones_brute([0, 0, 0], 3) == 3

    print("All tests passed!")
