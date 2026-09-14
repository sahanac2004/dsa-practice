"""
╔══════════════════════════════════════════════════════════════════╗
║  FIND PEAK ELEMENT                                               ║
║  LeetCode #162  |  Difficulty: Medium  |  Topic: Binary Search  ║
║  Link: https://leetcode.com/problems/find-peak-element/         ║
╚══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  A peak element is one that is strictly greater than its neighbors.
  Given an integer array nums, find a peak element and return its
  index. If multiple peaks exist, return ANY one of them.
  You must solve in O(log n) time.

  Important: nums[-1] = nums[n] = -infinity (imaginary boundaries)
  So first and last elements can also be peaks if they are greater
  than their one neighbor.

  Input : nums = integer array
  Output: index of any peak element

  Example 1 — basic:
    Input : nums = [1,2,3,1]
    Output: 2
    Why?  : nums[2]=3 is greater than nums[1]=2 and nums[3]=1

  Example 2 — slightly tricky (multiple peaks):
    Input : nums = [1,2,1,3,5,6,4]
    Output: 1 or 5 (both valid)
    Why?  : nums[1]=2 > nums[0]=1 and nums[2]=1 → peak
            nums[5]=6 > nums[4]=5 and nums[6]=4 → peak

  Constraints:
    - 1 <= nums.length <= 1000
    - -2^31 <= nums[i] <= 2^31 - 1
    - nums[i] != nums[i+1] for all valid i
    - Must solve in O(log n) time

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Problem odi aada mele namma brain enu think maadabeeku:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  integer array                │
  │  Output ಏನು ಬೇಕು?     →  peak element ರ index         │
  │                           (any peak valid)              │
  │  Constraints ಏನಿದೆ?   →  O(log n) must,               │
  │                           no two adjacent equal         │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ನನಗೆ ಗೊತ್ತಿರೋ simple way ಏನು?
  →  Linear scan — left to right ಹೋಗಿ nums[i] > nums[i+1]
     ಆದ ತಕ್ಷಣ i return ಮಾಡು → O(n)
  →  ಆದರೆ ಇದು slow ಯಾಕೆ?
     O(log n) beeku anta problem says

  ಹಂತ 3 — Better way ಹೇಗೆ ಯೋಚಿಸುವುದು?
  →  "O(log n) → Binary Search. But array not sorted — how?"
  →  Key insight: nums[i] > nums[i+1] → slope going DOWN
     → peak must be on LEFT side (including i)
     nums[i] < nums[i+1] → slope going UP
     → peak must be on RIGHT side (including i+1)
  →  ಯಾವ direction ಲ್ಲಿ slope going up → that side ಲ್ಲಿ
     peak guarantee ಇರತ್ತೆ! (because boundaries = -infinity)
  →  ಇದರಿಂದ ನಾವು Binary Search on Slope use ಮಾಡಬಹуದು!

  ಹಂತ 4 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  nums[-1] = nums[n] = -∞ guarantee ಇದೆ
  →  So going UP direction ಲ್ಲಿ peak MUST exist
  →  Each step half eliminate → O(log n)

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು:
  →  "Array not sorted, but binary search still works!"
  →  "If nums[mid] < nums[mid+1] → ascending slope → peak in right"
  →  "If nums[mid] > nums[mid+1] → descending slope → peak in left"
  →  "Boundaries are -infinity so peak always guaranteed on upward side"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Binary Search → On Slope Direction
  Secondary : —

  WHY Binary Search on unsorted array?
  → We don't need the array to be sorted
  → We only need a property that lets us eliminate half
  → Slope direction (up/down) gives us that property
  → Moving toward upward slope GUARANTEES finding a peak

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Think of the array as a mountain range. The boundaries are
  at -infinity. A peak MUST exist because we always go up from
  -infinity at start and come back down to -infinity at end.

  At any mid point:
  - If nums[mid] < nums[mid+1] → we are on an UPWARD slope
    → the right side has something higher → peak is to the RIGHT
  - If nums[mid] > nums[mid+1] → we are on a DOWNWARD slope
    → the left side is higher → peak is to the LEFT (or at mid)

  Each step eliminates half → O(log n)!

  The journey from brute to optimal:
    Brute thought   →  Linear scan left to right O(n)
    Problem with it →  O(log n) required
    Better question →  "Can binary search work on unsorted array?"
    Insight         →  Yes! Slope direction tells us where peak is.
                       Moving toward higher neighbor guarantees peak.
    Optimal         →  Binary search on slope → O(log n)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Scan left to right. The first time nums[i] > nums[i+1],
    we found a peak at index i. Handle edge cases for last element.

  Pseudocode:
    step 1: for i in range(n-1):
    step 2:   if nums[i] > nums[i+1]: return i
    step 3: return n-1  (last element is peak)

  Time  : O(n)  →  Why: scan entire array in worst case
  Space : O(1)  →  Why: no extra space

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ?
    → O(n) valid adu, but problem demands O(log n)
    → Binary search possible here!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 6 — APPROACH 2 — OPTIMAL (Binary Search on Slope)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Binary search. At each mid, check the slope direction.
    Move toward the higher neighbor — peak guaranteed there.

  Key steps:
    1. left=0, right=n-1
    2. While left < right:
       a. mid = (left+right)//2
       b. if nums[mid] < nums[mid+1]:
             → ascending slope → peak in RIGHT → left=mid+1
          else:
             → descending slope → peak in LEFT or AT mid → right=mid
    3. return left  (left==right == peak index)

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ:
    → "mid ನೋಡಿ: nums[mid] < nums[mid+1] ಆದ್ರೆ ಮೇಲೆ
       ಹೋಗ್ತಿದ್ದೇವೆ → peak right ಲ್ಲಿ → left=mid+1.
       nums[mid] > nums[mid+1] ಆದ್ರೆ ಕೆಳಗೆ ಹೋಗ್ತಿದ್ದೇವೆ
       → peak left ಲ್ಲಿ ಅಥವಾ mid ನಲ್ಲೇ → right=mid.
       left==right ಆದ್ರೆ that's our peak!"

  Time  : O(log n)  →  Why: half eliminated at each step
  Space : O(1)      →  Why: only left, right, mid variables

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 7 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: nums = [1,2,3,1]
  Index:          0 1 2 3

  left=0, right=3
  mid=1 → nums[1]=2, nums[2]=3 → 2 < 3 → ascending → left=2

  left=2, right=3
  mid=2 → nums[2]=3, nums[3]=1 → 3 > 1 → descending → right=2

  left=2 == right=2 → return 2 ✓ (nums[2]=3 is peak)

  ಇನ್ನೊಂದು example — multiple peaks:
  Input: nums = [1,2,1,3,5,6,4]
  Index:          0 1 2 3 4 5 6

  left=0, right=6
  mid=3 → nums[3]=3, nums[4]=5 → 3 < 5 → ascending → left=4

  left=4, right=6
  mid=5 → nums[5]=6, nums[6]=4 → 6 > 4 → descending → right=5

  left=4, right=5
  mid=4 → nums[4]=5, nums[5]=6 → 5 < 6 → ascending → left=5

  left=5 == right=5 → return 5 ✓ (nums[5]=6 is peak)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 8 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ Single element?          →  [1] → index 0 (only element = peak)
  ✓ Two elements?            →  [1,2] → index 1, [2,1] → index 0
  ✓ Peak at start?           →  [5,3,1] → index 0
  ✓ Peak at end?             →  [1,3,5] → index 2
  ✓ Multiple peaks?          →  Any one valid — return leftmost found
  ✓ Strictly increasing?     →  [1,2,3,4] → last index = peak

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 9 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                Time      Space
  Brute Force   O(n)      O(1)
  Optimal       O(log n)  O(1)   ← use this ✅

  Time yaake O(log n)? → Each step left or right half eliminate
  Space yaake O(1)?    → Only 3 variables: left, right, mid

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 10 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Binary Search on Unsorted Array (Slope Direction)

  Ee pattern yaavaaga use maadabeeku?
  → Array not sorted but a LOCAL property helps eliminate half
  → "Find peak", "find any local maximum/minimum"
  → O(log n) required on non-sorted input

  Idee pattern beere problemsalli kaanisatte:
  → Find Peak Element II #1901 (2D version — next in our list!)
  → Find in Mountain Array #1095
  → Peak Index in Mountain Array #852

  Next time intaha problem bandre naanu modalu idannu think maadtene:
  → "Array sorted alla, but O(log n) beeku → slope direction
     check maadu! Ascending iddre right, descending iddre left.
     left==right aadaga that IS the peak!"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 11 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "Find any peak element — strictly greater than both neighbors.
      Boundaries treated as -infinity. Must be O(log n)."

  2. Brute force:
     "Linear scan — first i where nums[i] > nums[i+1] is a peak.
      O(n) time."

  3. Optimize:
     "Binary search works even on unsorted arrays when a local
      property helps eliminate half. Here: if nums[mid] < nums[mid+1],
      we are on an ascending slope — a peak MUST exist to the right
      because the boundary is -infinity. So left = mid+1.
      Otherwise peak is at mid or left — right = mid."

  4. Code:
     "Standard binary search loop with left < right.
      mid comparison with mid+1 determines direction."

  5. Complexity:
     "Time O(log n) — half eliminated each step.
      Space O(1) — only pointers."

  Mukhya: summane kuutu code bareyabeda!
          "Binary search on unsorted array" — impressive statement!
          Slope direction insight explain maadu clearly!
"""


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(n) Time | O(1) Space
# ═══════════════════════════════════════════════════════════════════
def find_peak_element_brute(nums):
    """Idu modala aaloochane — linear scan O(n)"""
    n = len(nums)
    for i in range(n - 1):
        if nums[i] > nums[i + 1]:
            return i
    return n - 1   # last element is peak (ascending array)


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(log n) Time | O(1) Space
# ═══════════════════════════════════════════════════════════════════
def find_peak_element(nums):
    """
    Idu final answer — binary search on slope direction
    Ascending slope → peak in right → left = mid+1
    Descending slope → peak at mid or left → right = mid
    """
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] < nums[mid + 1]:
            # ascending slope → peak guaranteed in right half
            left = mid + 1
        else:
            # descending slope → peak at mid or in left half
            right = mid

    return left   # left == right == peak index


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # Test 1 — Basic, single peak
    assert find_peak_element([1, 2, 3, 1]) == 2

    # Test 2 — Multiple peaks, return any valid
    result = find_peak_element([1, 2, 1, 3, 5, 6, 4])
    assert result in [1, 5]

    # Test 3 — Single element
    assert find_peak_element([1]) == 0

    # Test 4 — Peak at start
    assert find_peak_element([5, 3, 1]) == 0

    # Test 5 — Peak at end (strictly increasing)
    assert find_peak_element([1, 2, 3]) == 2

    # Test 6 — Two elements
    assert find_peak_element([1, 2]) == 1
    assert find_peak_element([2, 1]) == 0

    print("All tests passed!")

You are out of free messages 
