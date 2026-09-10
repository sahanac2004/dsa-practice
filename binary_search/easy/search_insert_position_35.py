"""
╔══════════════════════════════════════════════════════════════════╗
║  SEARCH INSERT POSITION                                           ║
║  LeetCode #35  |  Difficulty: Easy  |  Topic: Binary Search       ║
║  Link: https://leetcode.com/problems/search-insert-position/      ║
╚══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Given a sorted array of DISTINCT integers `nums` and a `target`,
  return the index if target is found. If not, return the index
  where it WOULD be inserted to keep nums sorted.

  Input : nums = [1,3,5,6], target = 5
  Output: 2

  Example 1 — target present:
    Input : nums = [1,3,5,6], target = 5
    Output: 2
    Why?  : 5 is already at index 2

  Example 2 — target absent, fits in middle:
    Input : nums = [1,3,5,6], target = 2
    Output: 1
    Why?  : 2 isn't in the array, but inserting it between 1 and 3
            (index 1) keeps nums sorted

  Example 3 — target bigger than everything:
    Input : nums = [1,3,5,6], target = 7
    Output: 4
    Why?  : 7 belongs at the very end (index 4, one past the last
            element)

  Constraints:
    - 1 <= nums.length <= 10^4
    - nums sorted ascending, all values DISTINCT
    - Must run in O(log n) time

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Problem odi aada mele namma brain enu think maadabeeku:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  SORTED distinct array + target  │
  │  Output ಏನು ಬೇಕು?     →  target ಸಿಕ್ಕ index, ಇಲ್ಲಾಂದ್ರೆ  │
  │                          "ಇಲ್ಲಿ ಇಟ್ಟರೆ sorted ಆಗಿ ಉಳಿಯುತ್ತೆ" │
  │                          ಅನ್ನೋ index                       │
  │  Constraints ಏನಿದೆ?   →  O(log n) → Binary Search hint    │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — Previous problem (#704 Binary Search) ಜೊತೆ ಹೋಲಿಸಿ:
  →  #704 ನಲ್ಲಿ target ಸಿಗದೆ ಹೋದ್ರೆ ಬರೀ -1 return ಮಾಡ್ತಿದ್ವಿ.
  →  ಇಲ್ಲಿ target ಸಿಗದೆ ಹೋದ್ರೆ, "loop ಮುಗಿಯುವ ಹೊತ್ತಿಗೆ `low`
     ಎಲ್ಲಿ ನಿಂತಿದೆಯೋ ಅದೇ insert position!" ಅಂತ ಗಮನಿಸಬೇಕು.

  ಹಂತ 3 — ಯಾಕೆ `low` ಆಗುತ್ತೆ answer?
  →  ಪ್ರತಿ step ನಲ್ಲೂ, target mid ಗಿಂತ ದೊಡ್ಡದಾದ್ರೆ low = mid+1
     (ಅಂದ್ರೆ "target ಇದಕ್ಕಿಂತ ಬಲಗಡೆ ಇರಬೇಕು" ಅಂತ), target mid
     ಗಿಂತ ಚಿಕ್ಕದಾದ್ರೆ high = mid-1 (ಅಂದ್ರೆ "target ಇದಕ್ಕಿಂತ
     ಎಡಗಡೆ ಇರಬೇಕು" ಅಂತ).
  →  loop ಮುಗಿಯುವಾಗ (low > high ಆದಾಗ), `low` ಯಾವಾಗಲೂ "target
     ಗಿಂತ ದೊಡ್ಡದಾದ ಮೊದಲ element" ನ index ಗೆ ಬಂದು ನಿಲ್ಲುತ್ತೆ —
     ಅದೇ correct insert position!

  ಹಂತ 4 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  ಇದು "Lower Bound" concept ನ ಮೊದಲ ಪರಿಚಯ — "target ಗಿಂತ
     ದೊಡ್ಡದಾದ ಅಥವಾ ಸಮ ಇರೋ ಮೊದಲ element ಎಲ್ಲಿ?" ಅನ್ನೋ ಪ್ರಶ್ನೆಗೆ
     ಸಾಮಾನ್ಯ binary search template ಸ್ವಲ್ಪ ಬದಲಾವಣೆ ಜೊತೆ ಉತ್ತರ
     ಕೊಡುತ್ತೆ.

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು (Think out loud):
  →  "This is standard binary search, but instead of returning -1
      on failure, I track where `low` ends up — that's exactly the
      first index where target could be inserted keeping order."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Binary Search — Lower Bound variant
  Secondary : Linear Scan (brute force baseline)

  WHY Binary Search / Lower Bound?
  → Sorted + distinct array + O(log n) requirement
  → The "insert position" IS the lower bound: first index whose
    value is >= target

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION (How to think)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  If target isn't found, where does the search naturally "land"?

  The journey from brute to optimal:
    Brute thought   →  scan left to right, stop at the first
                       element >= target
    Problem with it →  O(n), ignores sortedness
    Better question →  "can binary search narrow down to that
                       same landing spot in O(log n)?"
    Insight         →  the standard binary search loop already
                       converges `low` to the first index >= target
                       when the target is absent
    Optimal         →  run normal binary search; if found return
                       mid, else return `low` when the loop ends

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Scan left to right; the first index whose value is >= target
    is the answer. If nothing qualifies, target belongs at the end.

  Pseudocode:
    step 1: for i in range(n):
    step 2:     if nums[i] >= target → return i
    step 3: return n

  Time  : O(n)  →  Why: may scan the whole array
  Space : O(1)  →  Why: no extra space

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ?
    → Problem demands O(log n); ignores sorted structure.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 6 — APPROACH 2 — OPTIMAL (Binary Search / Lower Bound)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Run the classic binary search. If target is found, return its
    index directly. If the loop ends without finding it, `low` has
    converged exactly to the first index where target could be
    inserted while keeping the array sorted.

  Key steps:
    1. low, high = 0, len(nums) - 1
    2. while low <= high:
    3.     mid = low + (high - low) // 2
    4.     if nums[mid] == target → return mid
    5.     elif nums[mid] < target → low = mid + 1
    6.     else → high = mid - 1
    7. return low   # insert position

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ:
    → "Normal binary search ಮಾಡು. Target ಸಿಕ್ಕಿದ್ರೆ mid return
        ಮಾಡು. ಸಿಗದೆ ಹೋದ್ರೆ, loop ಮುಗಿಯುವಾಗ low ಎಷ್ಟಿದೆಯೋ ಅದೇ
        insert position — ಬೇರೆ ಏನೂ ಬೇಡ."

  Time  : O(log n)  →  Why: search space halves every iteration
  Space : O(1)       →  Why: only a few index variables used

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 7 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: nums = [1,3,5,6], target = 5

  low=0, high=3  →  mid=1 → nums[1]=3 < 5  → low=2
  low=2, high=3  →  mid=2 → nums[2]=5 == 5 → return 2

  Output: 2 ✓

  ಇನ್ನೊಂದು example — target absent, middle:
  Input: nums = [1,3,5,6], target = 2

  low=0, high=3  →  mid=1 → nums[1]=3 > 2  → high=0
  low=0, high=0  →  mid=0 → nums[0]=1 < 2  → low=1
  low=1, high=0  →  loop ends → return low = 1

  Output: 1 ✓

  ಮೂರನೇ example — target bigger than everything:
  Input: nums = [1,3,5,6], target = 7

  low=0, high=3  →  mid=1 → nums[1]=3 < 7 → low=2
  low=2, high=3  →  mid=2 → nums[2]=5 < 7 → low=3
  low=3, high=3  →  mid=3 → nums[3]=6 < 7 → low=4
  low=4, high=3  →  loop ends → return low = 4

  Output: 4 ✓

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 8 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ Target smaller than all?    →  inserted at index 0
  ✓ Target larger than all?     →  inserted at index n (one past
                                     the end, as in Example 3)
  ✓ Target already present?     →  returns its exact index
  ✓ Single element array?       →  [5], target=5 → 0;
                                     [5], target=1 → 0;
                                     [5], target=9 → 1
  ✓ Empty search window at end? →  handled naturally, low simply
                                     equals n when loop finishes

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 9 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                Time        Space
  Brute Force   O(n)        O(1)
  Optimal       O(log n)    O(1)    ← use this ✅

  Time ಯಾಕೆ O(log n)?  → Standard binary search halving.
  Space ಯಾಕೆ O(1)?     → Only low, high, mid tracked.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 10 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Binary Search — Lower Bound (first index >= target)

  ಈ pattern ಯಾವಾಗ use ಮಾಡಬೇಕು?
  → "target ಇಲ್ಲಾಂದ್ರೆ ಎಲ್ಲಿ ಸೇರಿಸಬೇಕು / ಎಲ್ಲಿಂದ ಶುರುವಾಗುತ್ತೆ"
     ಅನ್ನೋ ಪ್ರಶ್ನೆಗಳಿಗೆ — `low` ಯಾವಾಗಲೂ ಆ boundary ಗೆ converge
     ಆಗುತ್ತೆ ಅಂತ ನೆನಪಿಟ್ಟುಕೊಳ್ಳಿ.

  ಇದೇ pattern ಬೇರೆ problems ನಲ್ಲಿ ಕಾಣಿಸುತ್ತೆ (ಈ topic ನ ಮುಂದಿನ
  problems):
  → Find First and Last Position (#34) — lower bound + upper bound
    ಎರಡೂ ಬೇಕಾಗುತ್ತೆ
  → Floor and Ceil in Sorted Array (GFG)
  → Search in Rotated Sorted Array (#33, #81)

  Next time ಇಂತಹ problem ಬಂದ್ರೆ ನಾನು ಮೊದಲು ಇದನ್ನ think ಮಾಡ್ತೇನೆ:
  → "'ಇಲ್ಲಾಂದ್ರೆ ಎಲ್ಲಿ' ಅನ್ನೋ ಪ್ರಶ್ನೆ ಬಂದ್ರೆ, normal binary
      search ಓಡಿಸಿ loop ಮುಗಿಯುವಾಗ `low` ಎಲ್ಲಿ ನಿಂತಿದೆ ಅಂತ ನೋಡು."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 11 — INTERVIEW ನಲ್ಲಿ ಹೇಗೆ EXPLAIN ಮಾಡಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "Find target's index, or the index where it would be inserted
      to keep nums sorted."

  2. Brute force:
     "Scan and return the first index >= target — O(n)."

  3. Optimize:
     "Run standard binary search. If found, return the index. If
      not found, the loop's `low` naturally converges to the first
      index where nums[low] >= target — that's the insert point."

  4. Code:
     "Same low/high/mid loop as classic binary search; just return
      `low` instead of -1 when the loop exits."

  5. Complexity:
     "Time O(log n) — same halving as binary search. Space O(1)."

  ಮುಖ್ಯ: ಈ trick (loop ಮುಗಿಯುವಾಗ low ಎಲ್ಲಿ ನಿಂತಿದೆ ಅಂತ ನೋಡೋದು)
         ಮುಂದೆ ಬರೋ Lower/Upper Bound problems ಗೆ ಬುನಾದಿ — ಚೆನ್ನಾಗಿ
         ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ.
"""


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(n) Time | O(1) Space
# ═══════════════════════════════════════════════════════════════════
def search_insert_brute(nums, target):
    """ಇದು ಮೊದಲ ಆಲೋಚನೆ — linear scan for first element >= target"""
    for i, num in enumerate(nums):
        if num >= target:
            return i
    return len(nums)


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(log n) Time | O(1) Space
# ═══════════════════════════════════════════════════════════════════
def search_insert(nums, target):
    """ಇದು final answer — binary search, low converges to insert index"""
    low, high = 0, len(nums) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return low


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # Test 1 — Target present
    assert search_insert([1, 3, 5, 6], 5) == 2

    # Test 2 — Target absent, fits in middle
    assert search_insert([1, 3, 5, 6], 2) == 1

    # Test 3 — Target bigger than everything
    assert search_insert([1, 3, 5, 6], 7) == 4

    # Test 4 — Target smaller than everything
    assert search_insert([1, 3, 5, 6], 0) == 0

    # Test 5 — Single element, match
    assert search_insert([5], 5) == 0

    # Test 6 — Single element, insert before
    assert search_insert([5], 1) == 0

    # Test 7 — Single element, insert after
    assert search_insert([5], 9) == 1

    # Cross-check: brute force must agree on all of the above
    assert search_insert_brute([1, 3, 5, 6], 5) == 2
    assert search_insert_brute([1, 3, 5, 6], 2) == 1
    assert search_insert_brute([1, 3, 5, 6], 7) == 4
    assert search_insert_brute([1, 3, 5, 6], 0) == 0
    assert search_insert_brute([5], 5) == 0
    assert search_insert_brute([5], 1) == 0
    assert search_insert_brute([5], 9) == 1

    print("All tests passed!")
