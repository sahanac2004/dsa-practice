"""
╔══════════════════════════════════════════════════════════════════╗
║  BINARY SEARCH                                                    ║
║  LeetCode #704  |  Difficulty: Easy  |  Topic: Binary Search      ║
║  Link: https://leetcode.com/problems/binary-search/               ║
╚══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Given an array of integers `nums` sorted in ascending order, and
  an integer `target`, return the index of target if it exists in
  nums, otherwise return -1.

  Input : nums = [-1,0,3,5,9,12], target = 9
  Output: 4

  Example 1 — basic:
    Input : nums = [-1,0,3,5,9,12], target = 9
    Output: 4
    Why?  : 9 is at index 4

  Example 2 — not found:
    Input : nums = [-1,0,3,5,9,12], target = 2
    Output: -1
    Why?  : 2 is not present anywhere in nums

  Constraints:
    - 1 <= nums.length <= 10^4
    - nums is sorted in ascending order, all values are UNIQUE
    - Must write an algorithm with O(log n) runtime complexity

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Problem odi aada mele namma brain enu think maadabeeku:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  SORTED array + ಒಂದು target      │
  │  Output ಏನು ಬೇಕು?     →  target ಸಿಕ್ಕ index, ಇಲ್ಲಾಂದ್ರೆ -1│
  │  Constraints ಏನಿದೆ?   →  "O(log n)" ಅಂತ ಬರೀ ಬರೀ ಇದೆ —   │
  │                          linear scan ಸಾಕಾಗಲ್ಲ ಅಂತ hint!   │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ನನಗೆ ಗೊತ್ತಿರೋ simple way ಏನು? (Brute force thought)
  →  ಎಡದಿಂದ ಬಲಕ್ಕೆ ಒಂದೊಂದೇ element ನೋಡ್ತಾ target ಇದ್ಯಾ ಅಂತ check
     ಮಾಡೋದು.
  →  ಆದರೆ array SORTED ಆಗಿದೆ ಅನ್ನೋ info ಅನ್ನ ಇದು ಪೂರ್ತಿ waste
     ಮಾಡುತ್ತೆ — O(n) ಆಗುತ್ತೆ, O(log n) ಬೇಕಲ್ವಾ?

  ಹಂತ 3 — Better way ಹೇಗೆ ಯೋಚಿಸುವುದು? (Optimization thought)
  →  "Array sorted ಆಗಿದೆ ಅಂದ್ರೆ, ಮಧ್ಯದ element ನೋಡಿ target ಅದಕ್ಕಿಂತ
     ದೊಡ್ಡದೋ ಚಿಕ್ಕದೋ ಅಂತ ಗೊತ್ತಾದ್ರೆ, ಅರ್ಧ array ಅನ್ನೇ ಬಿಟ್ಟುಬಿಡಬಹುದಲ್ವಾ?"
  →  ಅಹಾ moment: ಪ್ರತಿ step ನಲ್ಲಿ search space ಅನ್ನ ಅರ್ಧಕ್ಕೆ
     ಇಳಿಸ್ತಾ ಹೋದ್ರೆ, log n steps ನಲ್ಲೇ answer ಸಿಗುತ್ತೆ!

  ಹಂತ 4 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  SORTED array ಇದ್ದಾಗ ಮಾತ್ರ "mid ಗಿಂತ target ದೊಡ್ಡದಾ ಚಿಕ್ಕದಾ"
     ಅನ್ನೋ ಪ್ರಶ್ನೆಗೆ ಒಂದೇ ಒಂದು comparison ಸಾಕು, ಇಡೀ ಒಂದು ಬದಿ
     ಅನ್ನ discard ಮಾಡಬಹುದು.
  →  O(log n) ಬೇಕು ಅಂದಾಗ, sorted data ಮೇಲೆ ಮೊದಲು Binary Search
     ಯೋಚಿಸಬೇಕು.

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು (Think out loud):
  →  "The array is sorted, so a linear scan wastes that structure."
  →  "I'll keep two pointers, low and high, and repeatedly check
      the middle element."
  →  "If mid equals target, done. If target is smaller, search the
      left half; if larger, search the right half — this halves
      the search space every step, giving O(log n)."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Binary Search — classic index search
  Secondary : Linear Scan (brute force baseline)

  WHY Binary Search?
  → Array is SORTED — every comparison against mid tells us which
    half can be safely discarded
  → O(log n) requirement in the constraints is a direct signal to
    halve the search space each step

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION (How to think)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Do I need to look at every element, or can sortedness let me
  eliminate half the array with a single comparison?

  The journey from brute to optimal:
    Brute thought   →  scan left to right, compare each element
    Problem with it →  O(n), ignores that nums is sorted
    Better question →  "can I compare against the MIDDLE and
                       discard a whole half?"
    Insight         →  sorted order guarantees everything left of
                       mid is smaller, everything right is larger
    Optimal         →  shrink [low, high] by half each iteration

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Scan every index left to right, return the index the moment
    target is found.

  Pseudocode:
    step 1: for i in range(n):
    step 2:     if nums[i] == target → return i
    step 3: return -1

  Time  : O(n)  →  Why: may need to inspect every element
  Space : O(1)  →  Why: no extra space

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ? (Why is this not enough?)
    → Problem explicitly demands O(log n); linear scan doesn't
      use the sorted structure at all.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 6 — APPROACH 2 — OPTIMAL (Binary Search)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Maintain a search window [low, high]. Repeatedly check the
    middle element:
      - if nums[mid] == target      → found, return mid
      - if nums[mid] < target       → answer must be to the right,
                                       move low = mid + 1
      - if nums[mid] > target       → answer must be to the left,
                                       move high = mid - 1
    Stop when low > high (window empty) → target not present.

  Key steps:
    1. low, high = 0, len(nums) - 1
    2. while low <= high:
    3.     mid = low + (high - low) // 2   # avoids overflow
    4.     if nums[mid] == target → return mid
    5.     elif nums[mid] < target → low = mid + 1
    6.     else → high = mid - 1
    7. return -1

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ (Say it once in Kanglish so it sticks):
    → "low, high ಇಟ್ಕೊಂಡು mid ಲೆಕ್ಕ ಹಾಕಿ, mid ಸಮ ಆದ್ರೆ done,
        target mid ಗಿಂತ ದೊಡ್ಡದಾದ್ರೆ ಬಲಕ್ಕೆ ಹೋಗು, ಚಿಕ್ಕದಾದ್ರೆ
        ಎಡಕ್ಕೆ ಹೋಗು, low > high ಆಗೋವರೆಗೂ ಇದೇ repeat ಮಾಡು."

  Time  : O(log n)  →  Why: search space halves every iteration
  Space : O(1)       →  Why: only a few index variables used

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 7 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: nums = [-1,0,3,5,9,12], target = 9

  low=0, high=5  →  mid=2 → nums[2]=3 < 9  → low=3
  low=3, high=5  →  mid=4 → nums[4]=9 == 9 → return 4

  Output: 4 ✓

  ಇನ್ನೊಂದು example — target not present:
  Input: nums = [-1,0,3,5,9,12], target = 2

  low=0, high=5  →  mid=2 → nums[2]=3 > 2  → high=1
  low=0, high=1  →  mid=0 → nums[0]=-1 < 2 → low=1
  low=1, high=1  →  mid=1 → nums[1]=0 < 2  → low=2
  low=2, high=1  →  loop ends (low > high) → return -1

  Output: -1 ✓

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 8 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ Single element, match?      →  [5], target=5 → 0
  ✓ Single element, no match?   →  [5], target=1 → -1
  ✓ Target smaller than all?    →  low never moves right, ends -1
  ✓ Target larger than all?     →  high never moves left, ends -1
  ✓ Target at first/last index? →  handled naturally by mid math
  ✓ mid overflow (other langs)? →  low + (high-low)//2 avoids it
                                     (not an issue in Python, but
                                     good habit for C++/Java)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 9 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                Time        Space
  Brute Force   O(n)        O(1)
  Optimal       O(log n)    O(1)    ← use this ✅

  Time ಯಾಕೆ O(log n)?  → Search window halves every iteration.
  Space ಯಾಕೆ O(1)?     → Only low, high, mid tracked — no extra
                          structures.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 10 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Binary Search — classic index search

  ಈ pattern ಯಾವಾಗ use ಮಾಡಬೇಕು?
  → Data is SORTED (or can be framed as sorted) AND the question
    is "find exact value / boundary" with an O(log n) expectation

  ಇದೇ pattern ಬೇರೆ problems ನಲ್ಲಿ ಕಾಣಿಸುತ್ತೆ (ಈ topic ನ ಮುಂದಿನ
  problems):
  → Lower Bound / Upper Bound
  → Search Insert Position (#35)
  → Find First and Last Position (#34)
  → Search in Rotated Sorted Array (#33, #81)

  Next time ಇಂತಹ problem ಬಂದ್ರೆ ನಾನು ಮೊದಲು ಇದನ್ನ think ಮಾಡ್ತೇನೆ:
  → "Array sorted ಇದ್ಯಾ? ಇದ್ರೆ, low-high-mid template ಇಟ್ಕೊಂಡು
      ಪ್ರತಿ step ಗೂ search space ಅರ್ಧ ಮಾಡ್ತಾ ಹೋಗು."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 11 — INTERVIEW ನಲ್ಲಿ ಹೇಗೆ EXPLAIN ಮಾಡಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "I need to find target's index in a sorted array, or -1 if
      it's absent — and it must run in O(log n)."

  2. Brute force:
     "A linear scan works but is O(n) — it ignores that the array
      is sorted."

  3. Optimize:
     "Since it's sorted, I can compare target against the middle
      element and eliminate half the array each time — that's
      binary search."

  4. Code:
     "Two pointers low and high bound the search window. I compute
      mid, compare nums[mid] to target, and move low or high
      accordingly until they cross."

  5. Complexity:
     "Time O(log n) — the window halves every step. Space O(1) —
      just a few index variables."

  ಮುಖ್ಯ: ಸುಮ್ಮನೆ ಕೂತು code ಬರೆಯಬೇಡ!
         Interviewer ಗೆ ನಿನ್ನ thinking process ಕಾಣಬೇಕು.
"""


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(n) Time | O(1) Space
# ═══════════════════════════════════════════════════════════════════
def search_brute(nums, target):
    """ಇದು ಮೊದಲ ಆಲೋಚನೆ — linear scan, sorted structure use ಮಾಡಲ್ಲ"""
    for i, num in enumerate(nums):
        if num == target:
            return i
    return -1


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(log n) Time | O(1) Space
# ═══════════════════════════════════════════════════════════════════
def search(nums, target):
    """ಇದು final answer — classic binary search on sorted array"""
    low, high = 0, len(nums) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # Test 1 — Basic example, target present
    assert search([-1, 0, 3, 5, 9, 12], 9) == 4

    # Test 2 — Target absent
    assert search([-1, 0, 3, 5, 9, 12], 2) == -1

    # Test 3 — Edge case: single element, match
    assert search([5], 5) == 0

    # Test 4 — Edge case: single element, no match
    assert search([5], 1) == -1

    # Test 5 — Target at first index
    assert search([-1, 0, 3, 5, 9, 12], -1) == 0

    # Test 6 — Target at last index
    assert search([-1, 0, 3, 5, 9, 12], 12) == 5

    # Cross-check: brute force must agree on all of the above
    assert search_brute([-1, 0, 3, 5, 9, 12], 9) == 4
    assert search_brute([-1, 0, 3, 5, 9, 12], 2) == -1
    assert search_brute([5], 5) == 0
    assert search_brute([5], 1) == -1

    print("All tests passed!")
