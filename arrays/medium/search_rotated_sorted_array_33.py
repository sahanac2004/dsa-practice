"""
╔════════════════════════════════════════════════════════════════════════╗
║  SEARCH IN ROTATED SORTED ARRAY                                        ║
║  LeetCode #33  |  Difficulty: Medium  |  Topic: Arrays / Binary Search ║
║  Link: https://leetcode.com/problems/search-in-rotated-sorted-array/   ║
╚════════════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  A sorted array (unique elements) was rotated at some pivot. Given a
  target value, find its index in O(log n) time, or return -1 if it's
  not present.

  Input : nums = [4, 5, 6, 7, 0, 1, 2], target = 0
  Output: 4

  Example 1 — basic:
    Input : nums = [4, 5, 6, 7, 0, 1, 2], target = 0
    Output: 4
    Why?  : target 0 sits at index 4 in this rotated array

  Example 2 — slightly tricky (target not present):
    Input : nums = [4, 5, 6, 7, 0, 1, 2], target = 3
    Output: -1
    Why?  : 3 does not exist anywhere in the array, so must correctly
             report -1 instead of returning a wrong index

  Constraints:
    - 1 <= nums.length <= 5000
    - -10^4 <= nums[i] <= 10^4
    - All values of nums are UNIQUE
    - nums is sorted and rotated between 0 and n-1 times
    - Must run in O(log n) time

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ಮೊದಲು problem odidaga ನಮ್ಮ brain ಏನು think ಮಾಡಬೇಕು:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ (What are they asking?)
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  rotated sorted array + target    │
  │  Output ಏನು ಬೇಕು?     →  target ನ index (ಇಲ್ಲಾಂದ್ರೆ -1)   │
  │  Constraints ಏನಿದೆ?   →  O(log n) expect, unique elements  │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ನನಗೆ ಗೊತ್ತಿರೋ simple way ಏನು? (Brute force thought)
  →  Linear scan ಮಾಡಿ target ಸಿಗುತ್ತಾ ಅಂತ ನೋಡೋದು.
  →  ಆದರೆ ಇದು slow ಯಾಕೆ? → O(n), ಆದ್ರೆ array partially sorted ಆಗಿರೋ
     info ಬಳಸ್ದೆ ಇರ್ತೀವಿ — O(log n) ಗೆ ಇಳಿಸ್ಬೋದು.

  ಹಂತ 3 — Better way ಹೇಗೆ ಯೋಚಿಸುವುದು? (Optimization thought)
  →  "Find Min in Rotated Sorted Array (#153) ನಲ್ಲಿ ಕಲ್ತ ಹಾಗೆ, mid ನ
     ಒಂದು side ಖಂಡಿತ sorted ಆಗಿರುತ್ತೆ. ಆ sorted side ಗೊತ್ತಾದ ಮೇಲೆ,
     target ಆ range ನಲ್ಲಿ ಬರುತ್ತಾ ಅಂತ ಸುಲಭ ಆಗಿ check ಮಾಡ್ಬೋದಲ್ವಾ?"
  →  ಅಹಾ moment: mid ಗೂ left ಗೂ compare ಮಾಡಿ ಯಾವ side sorted ಅಂತ
     ಗೊತ್ತಾದ ಮೇಲೆ, sorted side ನ range (start, end) ಒಳಗೆ target
     ಇದ್ಯಾ ಅಂತ ನೋಡಿ — ಇದ್ರೆ ಆ side ನಲ್ಲೇ search continue ಮಾಡು,
     ಇಲ್ಲಾಂದ್ರೆ ಇನ್ನೊಂದು side ಗೆ ಹೋಗು.
  →  ಇದರಿಂದ ನಾವು Binary Search → Modified (Rotated Array) use ಮಾಡಬಹುದು!

  ಹಂತ 4 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  ಪ್ರತಿ mid ಗೂ, left-half ಅಥವಾ right-half ಒಂದು ಖಂಡಿತ ಸರಿಯಾಗಿ sorted
     ಆಗಿರುತ್ತೆ — ಇದೇ decision ಗೆ ಆಧಾರ.
  →  Sorted half ಸಿಕ್ಕ ಮೇಲೆ, "target ಆ range ಒಳಗೆ ಬರುತ್ತಾ" ಅಂತ ಒಂದೇ
     comparison ನಲ್ಲಿ ಗೊತ್ತಾಗುತ್ತೆ (normal binary search check ಹಾಗೆ).
  →  O(log n) explicitly ಕೇಳ್ತಾ ಇರೋದ್ರಿಂದ binary search ಸ್ಪಷ್ಟ signal.

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು (Think out loud):
  →  "So I'm seeing that even though the whole array isn't sorted,
      one half around any mid always is."
  →  "The brute force would be a linear scan — O(n), but that throws
      away the sorted structure completely."
  →  "I notice that if I figure out which half is sorted, I can check
      whether target falls in that half's range, and binary-search
      into the correct side each time."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Binary Search → Modified (Rotated Array)
  Secondary : None

  WHY this technique?
  → At every mid, one half of the array is guaranteed fully sorted
  → Once we know the sorted half, a simple range check tells us
    whether target lies there — decides which half to keep
  → O(log n) explicitly required, and n up to 5000 fits perfectly

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION (How to think — English)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Key observation: comparing nums[left] with nums[mid] tells us which
  half is sorted. Once we know that, a normal sorted-range check
  (nums[left] <= target < nums[mid], for example) tells us whether
  target is in that sorted half or must be in the other one.

  The journey from brute to optimal:
    Brute thought   →  scan every element until target found
    Problem with it →  O(n), ignores the half-sorted structure
    Better question →  "which half is sorted, and does target fall
                        in its range?"
    Insight         →  compare nums[left] to nums[mid] to identify the
                        sorted half, then range-check target against it
    Optimal         →  binary search, picking the correct half each
                        iteration based on that range check

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Scan through the array left to right, return the index the moment
    target is found; return -1 if the loop finishes without a match.

  Pseudocode:
    step 1: for i in range(n):
    step 2:   if nums[i] == target: return i
    step 3: return -1

  Time  : O(n)  →  Why: may need to check every element
  Space : O(1)  →  Why: no extra structures

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ? (Why is this not enough?)
    → Problem ಸ್ಪಷ್ಟವಾಗಿ O(log n) ಕೇಳ್ತಾ ಇದೆ — sorted structure ಇದ್ದೂ
      linear scan ಮಾಡೋದು ಆ hint waste ಮಾಡಿದ ಹಾಗೆ.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚶 SECTION 6 — APPROACH 2 — BETTER (skip — brute jumps straight to optimal)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ಇಲ್ಲಿ intermediate approach ಇಲ್ಲ — sorted-half insight ಸಿಕ್ಕ ತಕ್ಷಣ
  ನೇರವಾಗಿ optimal ಗೆ ಹೋಗಬಹುದು.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 7 — APPROACH 3 — OPTIMAL   (Binary Search — Identify Sorted Half)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Standard binary search, but at each mid, first figure out which
    half (left..mid or mid..right) is sorted by comparing nums[left]
    with nums[mid]. Then check if target lies within that sorted
    half's value range. If yes, search there; if no, search the
    other half.

  Key steps:
    1. left, right = 0, n - 1
    2. while left <= right:
         mid = (left + right) // 2
         if nums[mid] == target: return mid
         if nums[left] <= nums[mid]:        # left half is sorted
             if nums[left] <= target < nums[mid]: right = mid - 1
             else: left = mid + 1
         else:                               # right half is sorted
             if nums[mid] < target <= nums[right]: left = mid + 1
             else: right = mid - 1
    3. Return -1 if never found

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ (Say it once in Kanglish so it sticks):
    → "mid ಸಿಕ್ಕ target ಆದ್ರೆ ರಿಟರ್ನ್ ಮಾಡು. nums[left] <= nums[mid]
        ಆದ್ರೆ left half sorted — target ಆ range ಒಳಗೆ ಇದ್ರೆ right=mid-1,
        ಇಲ್ಲಾಂದ್ರೆ left=mid+1. ಇಲ್ಲಾಂದ್ರೆ right half sorted — target ಆ
        range ಒಳಗೆ ಇದ್ರೆ left=mid+1, ಇಲ್ಲಾಂದ್ರೆ right=mid-1!"

  Time  : O(log n)  →  Why: search space halves every iteration
  Space : O(1)      →  Why: only left, right, mid pointers

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 8 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 0

  left=0, right=6
  mid=3 (nums[mid]=7)   → nums[mid] != target
                          nums[left]=4 <= nums[mid]=7 → left half sorted
                          target=0 in [4,7)? No → left = mid+1 = 4
  left=4, right=6
  mid=5 (nums[mid]=1)   → nums[mid] != target
                          nums[left]=0 <= nums[mid]=1 → left half sorted
                          target=0 in [0,1)? Yes → right = mid-1 = 4
  left=4, right=4
  mid=4 (nums[mid]=0)   → nums[mid] == target → return 4

  Output: 4  ✅ matches expected

  ಇನ್ನೊಂದು example — tricky case (target not present):
  Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 3

  left=0, right=6
  mid=3 (nums[mid]=7)   → left half sorted (4<=7); target=3 in [4,7)? No
                          → left = mid+1 = 4
  left=4, right=6
  mid=5 (nums[mid]=1)   → left half sorted (0<=1); target=3 in [0,1)? No
                          → left = mid+1 = 6
  left=6, right=6
  mid=6 (nums[mid]=2)   → not target; left half sorted (2<=2);
                          target=3 in [2,2)? No → left = mid+1 = 7
  left=7 > right=6      → loop ends

  Output: -1  ✅ matches expected

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 9 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ Single element?          →  left==right==0, one comparison decides
  ✓ No rotation (fully sorted)? →  always falls into "left half sorted"
                                 branch, behaves like plain binary search
  ✓ Target at the rotation pivot? →  range checks correctly isolate it
                                 (e.g. index 4 in the dry run above)
  ✓ Target not present?       →  loop exits with left > right, return -1
  ✓ Negative target values?   →  range comparisons work identically

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 10 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                Time       Space
  Brute Force   O(n)       O(1)
  Optimal       O(log n)   O(1)    ← use this ✅

  Time ಯಾಕೆ ಅಷ್ಟು?  → ಪ್ರತಿ iteration ನಲ್ಲಿ search space ಅರ್ಧ ಆಗುತ್ತೆ.
  Space ಯಾಕೆ ಅಷ್ಟು? → left, right, mid ಬಿಟ್ಟು ಬೇರೆ extra structure ಬೇಡ.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 11 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Binary Search — Identify the Sorted Half First

  ಈ pattern ಯಾವಾಗ use ಮಾಡಬೇಕು?
  → Array rotated ಆಗಿದ್ದು, ಒಂದು specific target search ಮಾಡ್ಬೇಕು ಅಂತ
    ಇದ್ದಾಗ
  → mid ನ ಎರಡು sides ನಲ್ಲಿ ಒಂದು ಖಂಡಿತ sorted ಇರುತ್ತೆ ಅಂತ ಗುರುತಿಸಿದಾಗ
  → target ಆ sorted range ಒಳಗೆ ಬರುತ್ತಾ ಅಂತ ಸುಲಭ compare ಮಾಡ್ಬಹುದು
    ಅಂತ ಗೊತ್ತಾದಾಗ

  ಇದೇ pattern ಬೇರೆ problems ನಲ್ಲಿ ಕಾಣಿಸುತ್ತೆ:
  → Find Minimum in Rotated Sorted Array (#153) — same rotated-array family
  → Search in Rotated Sorted Array II (#81) — duplicates version
  → Find Peak Element — binary search using structural comparisons

  Next time ಇಂತಹ problem ಬಂದ್ರೆ ನಾನು ಮೊದಲು ಇದನ್ನ think ಮಾಡ್ತೇನೆ:
  → "Rotated array ಒಳಗೆ target search ಅಂತ ಕೇಳಿದ ತಕ್ಷಣ, ಮೊದಲು ಯಾವ
      half sorted ಅಂತ ಕಂಡುಹಿಡಿ, ಆಮೇಲೆ target ಆ range ಒಳಗೆ ಬರುತ್ತಾ
      ಅಂತ ಚೆಕ್ ಮಾಡು."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 12 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "So the problem is asking me to find the index of a target value
      in a rotated sorted array, in O(log n) time, or return -1."

  2. Brute force:
     "The naive approach would be a linear scan checking every
      element — O(n), but that wastes the sorted structure."

  3. Optimize:
     "I notice that at any mid, one half of the array is always
      cleanly sorted — comparing nums[left] to nums[mid] tells me
      which one. Then I just check if target falls in that sorted
      half's range."

  4. Code:
     "I will use a modified binary search because each iteration lets
      me confidently discard the half that can't contain the target,
      based on the sorted-half range check."

  5. Complexity:
     "Time O(log n) because the search space halves every step. Space
      O(1) because I only track left, right, and mid pointers."

  ಮುಖ್ಯ: ಸುಮ್ಮನೆ ಕೂತು code ಬರೆಯಬೇಡ!
         Interviewer ಗೆ ನಿನ್ನ thinking process ಕಾಣಬೇಕು.
"""


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(n) Time | O(1) Space
# ═══════════════════════════════════════════════════════════════════
def search_brute(nums, target):
    """ಇದು ಮೊದಲ ಆಲೋಚನೆ — ಪೂರ್ತಿ array linear scan ಮಾಡಿ target ಹುಡುಕೋದು"""
    for i, num in enumerate(nums):
        if num == target:
            return i
    return -1


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(log n) Time | O(1) Space  (Binary Search — Identify Sorted Half)
# ═══════════════════════════════════════════════════════════════════
def search(nums, target):
    """ಇದು final answer — ಯಾವ half sorted ಅಂತ ಕಂಡುಹಿಡಿದು ಆ range ಒಳಗೆ target ಇದ್ಯಾ ಚೆಕ್ ಮಾಡು"""
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid

        if nums[left] <= nums[mid]:            # left half is sorted
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:                                   # right half is sorted
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")   # Windows cp1252 can't print emoji otherwise

    # Test 1 — Basic example
    assert search([4, 5, 6, 7, 0, 1, 2], 0) == 4

    # Test 2 — Edge case: single element, found
    assert search([5], 5) == 0

    # Test 3 — Edge case: single element, not found
    assert search([5], 3) == -1

    # Test 4 — Tricky: target not present at all
    assert search([4, 5, 6, 7, 0, 1, 2], 3) == -1

    print("All tests passed! ✅")
