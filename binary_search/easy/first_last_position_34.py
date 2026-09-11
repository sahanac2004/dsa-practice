"""
╔══════════════════════════════════════════════════════════════════════╗
║  FIND FIRST AND LAST POSITION OF ELEMENT IN SORTED ARRAY             ║
║  LeetCode #34  |  Difficulty: Easy  |  Topic: Binary Search          ║
║  Link: https://leetcode.com/problems/                                ║
║        find-first-and-last-position-of-element-in-sorted-array/      ║
╚══════════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Given a sorted array `nums` (values may REPEAT this time) and a
  `target`, return [first_index, last_index] of target's occurrence
  range. If target isn't present, return [-1, -1].

  Input : nums = [5,7,7,8,8,10], target = 8
  Output: [3,4]

  Example 1 — basic:
    Input : nums = [5,7,7,8,8,10], target = 8
    Output: [3,4]
    Why?  : 8 first appears at index 3, last appears at index 4

  Example 2 — target absent:
    Input : nums = [5,7,7,8,8,10], target = 6
    Output: [-1,-1]
    Why?  : 6 doesn't exist anywhere in nums

  Example 3 — single occurrence:
    Input : nums = [1], target = 1
    Output: [0,0]
    Why?  : only one element, and it matches target

  Constraints:
    - 0 <= nums.length <= 10^5
    - nums sorted ascending, values CAN repeat (unlike #704/#35)
    - Must run in O(log n) time

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Problem odi aada mele namma brain enu think maadabeeku:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  SORTED array, DUPLICATES ಇರಬಹುದು│
  │  Output ಏನು ಬೇಕು?     →  target ಮೊದಲ ಮತ್ತು ಕೊನೆಯ index   │
  │  Constraints ಏನಿದೆ?   →  O(log n) → single binary search  │
  │                          ಸಾಲದು, TWO binary searches ಬೇಕು  │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — #704/#35 ಜೊತೆ ಹೋಲಿಸಿ — ಏನು ಬೇರೆ?
  →  ಅಲ್ಲಿ values UNIQUE ಇದ್ವು, ಒಂದೇ match ಸಾಕಿತ್ತು.
  →  ಇಲ್ಲಿ target ಪದೇ ಪದೇ ಬರಬಹುದು — "ಮೊದಲ ಸಲ ಎಲ್ಲಿ ಕಂಡಿತು" ಮತ್ತು
     "ಕೊನೆಯ ಸಲ ಎಲ್ಲಿ ಕಂಡಿತು" ಅಂತ ಎರಡೂ ಬೇಕು.

  ಹಂತ 3 — Better way ಹೇಗೆ ಯೋಚಿಸುವುದು?
  →  "target ಸಿಕ್ಕಿದ ತಕ್ಷಣ return ಮಾಡಿಬಿಟ್ರೆ, ಅದು FIRST occurrence
     ಆ ಅಂತ ಗ್ಯಾರಂಟಿ ಇಲ್ಲ. ಬದಲಿಗೆ, match ಸಿಕ್ಕಾಗ 'ಇನ್ನೂ ಎಡಗಡೆ
     ಇದೇ target ಇದ್ಯಾ' ಅಂತ ಹುಡುಕೋದನ್ನ ಮುಂದುವರೆಸಿದ್ರೆ, ಮೊದಲ
     occurrence ಗೆ converge ಆಗುತ್ತೆ!"
  →  ಅಹಾ moment: ಎರಡು ಬೇರೆ ಬೇರೆ binary searches ಓಡಿಸಿ —
     ಒಂದು "leftmost index of target" ಗೆ, ಇನ್ನೊಂದು "rightmost
     index of target" ಗೆ. ಎರಡೂ O(log n), ಒಟ್ಟು ಇನ್ನೂ O(log n).

  ಹಂತ 4 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  match ಸಿಕ್ಕಾಗ ತಕ್ಷಣ return ಮಾಡದೆ, answer ಅನ್ನ save ಮಾಡಿಟ್ಟು
     ಆ ಬದಿಗೆ (leftmost ಗೆ high=mid-1, rightmost ಗೆ low=mid+1)
     search ಮುಂದುವರೆಸಿದ್ರೆ — ಇನ್ನೂ ಚಿಕ್ಕ/ದೊಡ್ಡ index ಇದ್ಯಾ ಅಂತ
     ಖಚಿತ ಆಗುತ್ತೆ.

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು (Think out loud):
  →  "I'll run two variants of binary search — one biased to find
      the leftmost match, one biased to find the rightmost — each
      still O(log n), so O(log n) total."
  →  "On a match, instead of returning immediately, I record it and
      keep narrowing toward the boundary I want."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Binary Search — Lower Bound + Upper Bound (two passes)
  Secondary : Linear Scan (brute force baseline)

  WHY two biased binary searches?
  → A single "found it, return mid" search gives no guarantee of
    which occurrence it landed on when duplicates exist
  → Biasing the search to keep shrinking even after a match — left
    for first occurrence, right for last — nails both boundaries
    in O(log n) each

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION (How to think)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Finding "a" match isn't enough — I need the FIRST and LAST match.
  Can I bias binary search to keep hunting past a found match?

  The journey from brute to optimal:
    Brute thought   →  scan left to right, note first and last
                       index where nums[i] == target
    Problem with it →  O(n), ignores sortedness entirely
    Better question →  "can I binary search for the boundary
                       itself, instead of just 'a' match?"
    Insight         →  on a match, don't stop — keep shrinking
                       toward the side that finds the extreme
                       occurrence (left: high=mid-1; right:
                       low=mid+1), remembering the best answer seen
    Optimal         →  two O(log n) binary searches, one per bound

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Scan the whole array once, tracking the first and last index
    where nums[i] == target.

  Pseudocode:
    step 1: first, last = -1, -1
    step 2: for i in range(n):
    step 3:     if nums[i] == target:
    step 4:         if first == -1 → first = i
    step 5:         last = i
    step 6: return [first, last]

  Time  : O(n)  →  Why: may scan every element
  Space : O(1)  →  Why: no extra space

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ?
    → Problem demands O(log n); this ignores the sorted structure.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 6 — APPROACH 2 — OPTIMAL (Two Biased Binary Searches)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    find_bound(nums, target, find_first):
      low, high = 0, n-1
      result = -1
      while low <= high:
        mid = low + (high-low)//2
        if nums[mid] == target:
          result = mid                       # record candidate
          if find_first: high = mid - 1      # keep hunting LEFT
          else:          low  = mid + 1      # keep hunting RIGHT
        elif nums[mid] < target: low = mid + 1
        else:                     high = mid - 1
      return result

    Call it once with find_first=True (leftmost), once with
    find_first=False (rightmost).

  Key steps:
    1. first = find_bound(nums, target, True)
    2. if first == -1 → return [-1, -1]   # target absent entirely
    3. last = find_bound(nums, target, False)
    4. return [first, last]

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ:
    → "match ಸಿಕ್ಕಾಗ result ನಲ್ಲಿ save ಮಾಡಿಟ್ಟು, first ಬೇಕಿದ್ರೆ
        high = mid-1 ಮಾಡಿ ಎಡಕ್ಕೆ ಇನ್ನೂ ಹುಡುಕು, last ಬೇಕಿದ್ರೆ
        low = mid+1 ಮಾಡಿ ಬಲಕ್ಕೆ ಇನ್ನೂ ಹುಡುಕು — loop ಮುಗಿಯುವಾಗ
        ಸಿಕ್ಕಿದ್ದೇ extreme occurrence."

  Time  : O(log n)  →  Why: two independent binary searches
  Space : O(1)       →  Why: only a few index variables used

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 7 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: nums = [5,7,7,8,8,10], target = 8

  Finding FIRST (find_first=True):
    low=0,high=5 → mid=2 → nums[2]=7 < 8  → low=3
    low=3,high=5 → mid=4 → nums[4]=8 == 8 → result=4, high=3 (go left)
    low=3,high=3 → mid=3 → nums[3]=8 == 8 → result=3, high=2 (go left)
    low=3,high=2 → loop ends → first = 3

  Finding LAST (find_first=False):
    low=0,high=5 → mid=2 → nums[2]=7 < 8  → low=3
    low=3,high=5 → mid=4 → nums[4]=8 == 8 → result=4, low=5 (go right)
    low=5,high=5 → mid=5 → nums[5]=10 > 8 → high=4
    low=5,high=4 → loop ends → last = 4

  Output: [3, 4] ✓

  ಇನ್ನೊಂದು example — target absent:
  Input: nums = [5,7,7,8,8,10], target = 6

  Finding FIRST: mid comparisons never hit == 6 → result stays -1
  → first == -1, so short-circuit → return [-1, -1] immediately
    (no need to even run the "last" search)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 8 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ Empty array?                →  nums=[] → [-1,-1] (loop never runs)
  ✓ Target absent entirely?     →  [-1,-1]
  ✓ Single element, match?      →  [1], target=1 → [0,0]
  ✓ Single element, no match?   →  [1], target=2 → [-1,-1]
  ✓ ALL elements equal target?  →  [8,8,8], target=8 → [0,2]
  ✓ Target at very start/end?   →  handled naturally by biasing

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 9 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                Time          Space
  Brute Force   O(n)          O(1)
  Optimal       O(log n)      O(1)    ← use this ✅
                (2 searches,
                 still log n)

  Time ಯಾಕೆ O(log n)?  → Two independent binary searches, each
                          O(log n); constants don't matter for
                          Big-O.
  Space ಯಾಕೆ O(1)?     → Only low, high, mid, result tracked.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 10 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Binary Search — Biased Search for First/Last
                (Lower Bound + Upper Bound combined)

  ಈ pattern ಯಾವಾಗ use ಮಾಡಬೇಕು?
  → Sorted array with DUPLICATES, and question asks about the
    BOUNDARY of a value's occurrence range (first/last/count)

  ಇದೇ pattern ಬೇರೆ problems ನಲ್ಲಿ ಕಾಣಿಸುತ್ತೆ (ಈ topic ನ ಮುಂದಿನ
  problems):
  → Count Occurrences in Sorted Array (last - first + 1)
  → Floor and Ceil in Sorted Array
  → Find out how many times array is rotated (min-finding variant)

  Next time ಇಂತಹ problem ಬಂದ್ರೆ ನಾನು ಮೊದಲು ಇದನ್ನ think ಮಾಡ್ತೇನೆ:
  → "Duplicates ಇರೋ sorted array ನಲ್ಲಿ boundary ಕೇಳಿದ್ರೆ, match
      ಸಿಕ್ಕಾಗ ತಕ್ಷಣ return ಮಾಡಬೇಡ — ಸರಿಯಾದ ದಿಕ್ಕಿಗೆ shrink ಮಾಡ್ತಾ
      ಇರು, result ಅನ್ನ save ಮಾಡ್ತಾ ಇರು."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 11 — INTERVIEW ನಲ್ಲಿ ಹೇಗೆ EXPLAIN ಮಾಡಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "Find the first and last index of target in a sorted array
      that may contain duplicates."

  2. Brute force:
     "Scan once, track first and last match — O(n)."

  3. Optimize:
     "Run binary search twice with a small twist: on a match, don't
      stop — keep shrinking toward the left for the first
      occurrence, or toward the right for the last, remembering the
      best index found so far."

  4. Code:
     "One helper function parameterized by direction; call it twice
      and combine the results. Short-circuit to [-1,-1] if the
      first search finds nothing."

  5. Complexity:
     "Time O(log n) — two binary searches, each halving the space.
      Space O(1)."

  ಮುಖ್ಯ: 'find A match' ಮತ್ತು 'find THE first/last match' ಬೇರೆ
         ಬೇರೆ ಪ್ರಶ್ನೆಗಳು — match ಸಿಕ್ಕಾಗ immediately return ಮಾಡೋ
         ಅಭ್ಯಾಸ ಇಲ್ಲಿ ಬಿಡಬೇಕು!
"""


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(n) Time | O(1) Space
# ═══════════════════════════════════════════════════════════════════
def search_range_brute(nums, target):
    """ಇದು ಮೊದಲ ಆಲೋಚನೆ — single scan tracking first & last match"""
    first, last = -1, -1
    for i, num in enumerate(nums):
        if num == target:
            if first == -1:
                first = i
            last = i
    return [first, last]


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(log n) Time | O(1) Space
# ═══════════════════════════════════════════════════════════════════
def _find_bound(nums, target, find_first):
    """ಇದು helper — direction ಗೆ ಅನುಗುಣವಾಗಿ leftmost/rightmost hudukatte"""
    low, high = 0, len(nums) - 1
    result = -1

    while low <= high:
        mid = low + (high - low) // 2

        if nums[mid] == target:
            result = mid
            if find_first:
                high = mid - 1   # keep hunting left for first occurrence
            else:
                low = mid + 1    # keep hunting right for last occurrence
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return result


def search_range(nums, target):
    """ಇದು final answer — two biased binary searches for first & last"""
    first = _find_bound(nums, target, find_first=True)
    if first == -1:
        return [-1, -1]

    last = _find_bound(nums, target, find_first=False)
    return [first, last]


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # Test 1 — Basic example, target repeats
    assert search_range([5, 7, 7, 8, 8, 10], 8) == [3, 4]

    # Test 2 — Target absent
    assert search_range([5, 7, 7, 8, 8, 10], 6) == [-1, -1]

    # Test 3 — Empty array
    assert search_range([], 0) == [-1, -1]

    # Test 4 — Single element, match
    assert search_range([1], 1) == [0, 0]

    # Test 5 — Single element, no match
    assert search_range([1], 2) == [-1, -1]

    # Test 6 — All elements equal target
    assert search_range([8, 8, 8], 8) == [0, 2]

    # Test 7 — Target at very start
    assert search_range([2, 2, 3, 4, 5], 2) == [0, 1]

    # Cross-check: brute force must agree on all of the above
    assert search_range_brute([5, 7, 7, 8, 8, 10], 8) == [3, 4]
    assert search_range_brute([5, 7, 7, 8, 8, 10], 6) == [-1, -1]
    assert search_range_brute([], 0) == [-1, -1]
    assert search_range_brute([1], 1) == [0, 0]
    assert search_range_brute([8, 8, 8], 8) == [0, 2]

    print("All tests passed!")
