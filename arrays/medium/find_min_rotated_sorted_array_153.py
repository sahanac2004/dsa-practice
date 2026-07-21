"""
╔════════════════════════════════════════════════════════════════════════════╗
║  FIND MINIMUM IN ROTATED SORTED ARRAY                                      ║
║  LeetCode #153  |  Difficulty: Medium  |  Topic: Arrays / Binary Search    ║
║  Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/ ║
╚════════════════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  A sorted array (no duplicates) was rotated at some unknown pivot.
  Find the minimum element — and you must do it in O(log n), not by
  scanning the whole array.

  Input : nums = [3, 4, 5, 1, 2]
  Output: 1

  Example 1 — basic:
    Input : nums = [3, 4, 5, 1, 2]
    Output: 1
    Why?  : original sorted array [1,2,3,4,5] was rotated 3 times,
             so the smallest element 1 sits right after the "break point"

  Example 2 — slightly tricky (already sorted, no rotation):
    Input : nums = [11, 13, 15, 17]
    Output: 11
    Why?  : rotating 0 times still counts as a valid rotation — the
             array is technically "rotated by n", so the min is just nums[0]

  Constraints:
    - 1 <= nums.length <= 5000
    - -5000 <= nums[i] <= 5000
    - All integers are UNIQUE (no duplicates)
    - nums is sorted and rotated between 1 and n times

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ಮೊದಲು problem odidaga ನಮ್ಮ brain ಏನು think ಮಾಡಬೇಕು:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ (What are they asking?)
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  sorted array ಇದ್ದು, ಎಲ್ಲೋ ಒಂದು    │
  │                          point ಇಂದ rotate ಮಾಡಿದೆ           │
  │  Output ಏನು ಬೇಕು?     →  ಆ array ನ minimum element        │
  │  Constraints ಏನಿದೆ?   →  n=5000, duplicates ಇಲ್ಲ, O(log n) │
  │                          expect ಮಾಡ್ತಾರೆ (binary search hint)│
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ನನಗೆ ಗೊತ್ತಿರೋ simple way ಏನು? (Brute force thought)
  →  ಪೂರ್ತಿ array ಅನ್ನ scan ಮಾಡಿ min track ಮಾಡೋದು — ಸುಲಭ.
  →  ಆದರೆ ಇದು slow ಯಾಕೆ? → O(n), ಆದ್ರೆ array ಸ್ವತಃ sorted (rotated
     ಆಗಿದ್ರೂ) ಅನ್ನೋ property ಅನ್ನ ಬಳಸ್ದೇ ಹೋಗ್ತಿದ್ದೀವಿ — ಈ info
     use ಮಾಡಿದ್ರೆ log n ಗೆ ಇಳಿಸ್ಬೋದು.

  ಹಂತ 3 — Better way ಹೇಗೆ ಯೋಚಿಸುವುದು? (Optimization thought)
  →  "Array rotated ಆಗಿದ್ರೂ, ಪ್ರತಿ half ನೋಡಿದ್ರೆ ಒಂದು half ಖಂಡಿತ
     sorted ಆಗಿರುತ್ತೆ — ಇನ್ನೊಂದು half ಮಾತ್ರ rotation point ಇರೋ half."
  →  ಅಹಾ moment: mid element ಅನ್ನ nums[right] ಜೊತೆ compare ಮಾಡಿದ್ರೆ,
     mid > right ಆದ್ರೆ minimum right half ನಲ್ಲಿ ಇದೆ ಅಂತ ಗ್ಯಾರಂಟಿ
     (ಯಾಕಂದ್ರೆ rotation point right side ನಲ್ಲಿ ಇರ್ಬೇಕು). mid <= right
     ಆದ್ರೆ mid ಸಹ minimum ಆಗ್ಬೋದು, ಆದ್ರೆ minimum mid ಗಿಂತ left
     side ನಲ್ಲಿ ಇರ್ಲಿಕ್ಕಿಲ್ಲ, so right = mid ಮಾಡಿ half discard ಮಾಡ್ಬೋದು.
  →  ಇದರಿಂದ ನಾವು Binary Search → Answer on Rotated Array use ಮಾಡಬಹುದು!

  ಹಂತ 4 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  Array ಇನ್ನೂ "partially sorted" ಆಗಿರೋದ್ರಿಂದ, ಪ್ರತಿ step ನಲ್ಲಿ
     ಅರ್ಧ ಭಾಗ ಖಂಡಿತ discard ಮಾಡ್ಬಹುದು — ಇದೇ binary search ನ core idea.
  →  O(log n) expect ಮಾಡ್ತಾ ಇರೋ constraint ಸ್ವತಃ binary search signal.
  →  Duplicates ಇಲ್ಲ ಅನ್ನೋ constraint, mid vs right compare clean
     ಆಗಿ ಕೆಲಸ ಮಾಡುತ್ತೆ ಅಂತ ಖಾತ್ರಿ ಕೊಡುತ್ತೆ (duplicates ಇದ್ರೆ ambiguous
     ಆಗ್ತಿತ್ತು).

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು (Think out loud):
  →  "So I'm seeing that even though the array is rotated, at every
      midpoint, at least one half is still fully sorted."
  →  "The brute force would be a linear scan — O(n), but the sorted
      structure hints at O(log n) binary search."
  →  "I compare nums[mid] with nums[right]: if nums[mid] > nums[right],
      the minimum must be in the right half, so I move left = mid + 1;
      otherwise the minimum is at mid or to its left, so right = mid."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Binary Search → Modified (Rotated Array)
  Secondary : None

  WHY this technique?
  → Array is sorted-then-rotated — at every split, one half is always
    still cleanly sorted, letting us eliminate half the search space
  → O(log n) is explicitly achievable and expected (n up to 5000)
  → Comparing nums[mid] to nums[right] (not nums[0]) correctly narrows
    down which half contains the rotation point / minimum

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION (How to think — English)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Key observation: the minimum element is the only element in the
  array that is smaller than its previous neighbor (the "rotation
  break point"). Comparing nums[mid] against nums[right] tells us
  which side of that break point mid is on.

  The journey from brute to optimal:
    Brute thought   →  scan every element, track running minimum
    Problem with it →  O(n), ignores that array is still half-sorted
    Better question →  "which half is guaranteed sorted at each mid?"
    Insight         →  nums[mid] > nums[right] means break point is
                        in the right half; otherwise it's at/left of mid
    Optimal         →  binary search shrinking to the half containing
                        the break point, until left == right

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Scan through the whole array once, keeping track of the smallest
    value seen so far.

  Pseudocode:
    step 1: best = nums[0]
    step 2: for each num in nums: best = min(best, num)
    step 3: return best

  Time  : O(n)  →  Why: visits every element once
  Space : O(1)  →  Why: only one running variable

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ? (Why is this not enough?)
    → Problem explicitly ಕೇಳ್ತಾ ಇದೆ O(log n) algorithm ಬರಿ ಅಂತ —
      sorted structure ಇದ್ದೂ linear scan ಮಾಡೋದು ಆ information waste
      ಮಾಡಿದ ಹಾಗೆ.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚶 SECTION 6 — APPROACH 2 — BETTER (skip — brute jumps straight to optimal)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ಇಲ್ಲಿ intermediate approach ಇಲ್ಲ — binary search insight ಸಿಕ್ಕ
  ತಕ್ಷಣ ನೇರವಾಗಿ optimal ಗೆ ಹೋಗಬಹುದು.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 7 — APPROACH 3 — OPTIMAL   (Binary Search on Rotated Array)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Keep left=0, right=n-1. At each step compute mid. If nums[mid] >
    nums[right], the rotation break point (and thus the minimum) must
    be strictly to the right of mid, so left = mid + 1. Otherwise the
    minimum is at mid or somewhere to its left, so right = mid (never
    right = mid - 1, since mid itself could BE the minimum). Loop
    until left == right — that index holds the minimum.

  Key steps:
    1. left, right = 0, n - 1
    2. while left < right:
         mid = (left + right) // 2
         if nums[mid] > nums[right]: left = mid + 1
         else: right = mid
    3. Return nums[left] (== nums[right])

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ (Say it once in Kanglish so it sticks):
    → "left=0, right=n-1 ಇಟ್ಕೊಂಡು mid ಲೆಕ್ಕ ಹಾಕು. nums[mid] >
        nums[right] ಆದ್ರೆ minimum right side ನಲ್ಲಿದೆ ಅಂತ, left=mid+1
        ಮಾಡು. ಇಲ್ಲಾಂದ್ರೆ minimum mid ಅಥವಾ ಅದರ left ನಲ್ಲಿ ಇದೆ ಅಂತ,
        right=mid ಮಾಡು (mid ಅನ್ನ discard ಮಾಡ್ಬೇಡ). left==right
        ಆಗೋವರೆಗೂ ಇದೇ repeat ಮಾಡು, ಆ index ಆನ್ಸರ್!"

  Time  : O(log n)  →  Why: search space halves every iteration
  Space : O(1)      →  Why: only left, right, mid pointers

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 8 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: nums = [3, 4, 5, 1, 2]

  left=0, right=4
  mid=2 (nums[mid]=5)  → nums[mid]=5 > nums[right]=2 → break point is
                          right of mid → left = mid+1 = 3
  left=3, right=4
  mid=3 (nums[mid]=1)  → nums[mid]=1 <= nums[right]=2 → min is at mid
                          or left of it → right = mid = 3
  left=3, right=3      → loop ends (left == right)

  Output: nums[3] = 1  ✅ matches expected

  ಇನ್ನೊಂದು example — tricky case (no rotation):
  Input: nums = [11, 13, 15, 17]

  left=0, right=3
  mid=1 (nums[mid]=13)  → 13 <= nums[right]=17 → right = mid = 1
  left=0, right=1
  mid=0 (nums[mid]=11)  → 11 <= nums[right]=13 → right = mid = 0
  left=0, right=0        → loop ends

  Output: nums[0] = 11  ✅ matches expected (already sorted array)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 9 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ Single element?          →  left == right from the start, loop
                                 never runs, returns nums[0] directly
  ✓ Two elements?             →  mid = left, one comparison decides it
  ✓ No rotation (fully sorted)? →  nums[mid] never > nums[right], right
                                 keeps shrinking down to index 0
  ✓ Rotation at the very last index? →  minimum ends up as nums[n-1],
                                 handled naturally by the same logic
  ✓ Negative numbers?         →  comparisons work identically, no
                                 special casing needed

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 10 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                Time       Space
  Brute Force   O(n)       O(1)
  Optimal       O(log n)   O(1)    ← use this ✅

  Time ಯಾಕೆ ಅಷ್ಟು?  → ಪ್ರತಿ iteration ನಲ್ಲಿ search space ಅರ್ಧ ಆಗುತ್ತೆ
                        — binary search ನ classic O(log n).
  Space ಯಾಕೆ ಅಷ್ಟು? → left, right, mid ಬಿಟ್ಟು ಬೇರೆ extra structure ಬೇಡ.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 11 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Binary Search on a "Rotated but Half-Sorted" Array

  ಈ pattern ಯಾವಾಗ use ಮಾಡಬೇಕು?
  → Array sorted ಆಗಿತ್ತು ಆದ್ರೆ rotate ಮಾಡಿದ್ದಾರೆ ಅಂತ ಗೊತ್ತಾದಾಗ
  → O(log n) ಕೇಳ್ತಾ ಇದ್ದಾಗ, ಆದ್ರೆ array ಪೂರ್ತಿ sorted ಅಲ್ಲ ಅಂತ ಇದ್ದಾಗ
  → mid ಅನ್ನ ends (left/right) ಜೊತೆ compare ಮಾಡಿ "ಯಾವ half sorted"
    ಅಂತ ನಿರ್ಧಾರ ಮಾಡ್ಬಹುದು ಅಂತ ಗೊತ್ತಾದಾಗ

  ಇದೇ pattern ಬೇರೆ problems ನಲ್ಲಿ ಕಾಣಿಸುತ್ತೆ:
  → Search in Rotated Sorted Array (#33) — same rotated-array binary search family
  → Find Minimum in Rotated Sorted Array II (#154) — duplicates version
  → Search in Rotated Sorted Array II (#81) — duplicates version

  Next time ಇಂತಹ problem ಬಂದ್ರೆ ನಾನು ಮೊದಲು ಇದನ್ನ think ಮಾಡ್ತೇನೆ:
  → "Rotated sorted array ಅಂತ ಕೇಳಿದ ತಕ್ಷಣ, mid ಅನ್ನ right (ಅಥವಾ left)
      ಜೊತೆ compare ಮಾಡಿ ಯಾವ half clean sorted ಅಂತ ಮೊದಲು ಕಂಡುಹಿಡಿ."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 12 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "So the problem is asking me to find the minimum in a sorted
      array that's been rotated some unknown number of times, in
      O(log n) time."

  2. Brute force:
     "The naive approach would be a linear scan tracking the running
      minimum — giving O(n), but that ignores the sorted structure."

  3. Optimize:
     "I notice that no matter where I split the array, at least one
      half is still fully sorted — so I can use binary search,
      comparing nums[mid] to nums[right] to decide which half to keep."

  4. Code:
     "I will use binary search because each comparison lets me safely
      discard half the array while still keeping the half that
      contains the rotation break point (and the minimum)."

  5. Complexity:
     "Time O(log n) because the search space halves every step. Space
      O(1) because I only track two or three pointers."

  ಮುಖ್ಯ: ಸುಮ್ಮನೆ ಕೂತು code ಬರೆಯಬೇಡ!
         Interviewer ಗೆ ನಿನ್ನ thinking process ಕಾಣಬೇಕು.
"""


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(n) Time | O(1) Space
# ═══════════════════════════════════════════════════════════════════
def find_min_brute(nums):
    """ಇದು ಮೊದಲ ಆಲೋಚನೆ — ಪೂರ್ತಿ array scan ಮಾಡಿ min track ಮಾಡೋದು"""
    best = nums[0]
    for num in nums:
        best = min(best, num)
    return best


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(log n) Time | O(1) Space  (Binary Search on Rotated Array)
# ═══════════════════════════════════════════════════════════════════
def find_min(nums):
    """ಇದು final answer — mid ಅನ್ನ right ಜೊತೆ compare ಮಾಡಿ half discard ಮಾಡ್ತಾ ಹೋಗು"""
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    return nums[left]


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")   # Windows cp1252 can't print emoji otherwise

    # Test 1 — Basic example
    assert find_min([3, 4, 5, 1, 2]) == 1

    # Test 2 — Edge case: single element
    assert find_min([5]) == 5

    # Test 3 — Edge case: already sorted, no rotation
    assert find_min([11, 13, 15, 17]) == 11

    # Test 4 — Tricky: rotation right at the last index
    assert find_min([2, 1]) == 1

    print("All tests passed! ✅")
