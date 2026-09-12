"""
╔══════════════════════════════════════════════════════════════════╗
║  SEARCH IN ROTATED SORTED ARRAY II                               ║
║  LeetCode #81  |  Difficulty: Medium  |  Topic: Binary Search   ║
║  Link: https://leetcode.com/problems/search-in-rotated-sorted-array-ii/  ║
╚══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Same as LC #33 (Search in Rotated Sorted Array) BUT this time
  the array can have DUPLICATES. Given a rotated sorted array with
  possible duplicates and a target, return True if target exists,
  False otherwise.

  Input : nums = rotated sorted array (with duplicates), target
  Output: True if target exists, False otherwise

  Example 1 — basic:
    Input : nums = [2,5,6,0,0,1,2], target = 0
    Output: True
    Why?  : 0 exists in the array

  Example 2 — slightly tricky (target not present):
    Input : nums = [2,5,6,0,0,1,2], target = 3
    Output: False
    Why?  : 3 does not exist anywhere in array

  Example 3 — tricky duplicate case:
    Input : nums = [1,0,1,1,1], target = 0
    Output: True
    Why?  : duplicates make it hard to determine which half is
            sorted — need special handling

  Constraints:
    - 1 <= nums.length <= 5000
    - -10^4 <= nums[i], target <= 10^4
    - nums is rotated sorted array with possible duplicates

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Problem odi aada mele namma brain enu think maadabeeku:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  rotated sorted array with    │
  │                           duplicates + target           │
  │  Output ಏನು ಬೇಕು?     →  target exists? True/False    │
  │  Constraints ಏನಿದೆ?   →  duplicates allowed —         │
  │                           LC #33 ಗಿಂತ tricky!          │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ನನಗೆ ಗೊತ್ತಿರೋ simple way ಏನು?
  →  Linear scan — O(n) ಲ್ಲಿ find ಮಾಡಬಹುದು
  →  ಆದರೆ ಇದು slow ಯಾಕೆ?
     n=5000 ಆದ್ರೆ 5000 operations — better O(log n) possible

  ಹಂತ 3 — Better way ಹೇಗೆ ಯೋಚಿಸುವುದು?
  →  LC #33 ರಲ್ಲಿ duplicates ಇಲ್ಲದ್ದರಿಂದ left/right half
     sorted ಅಂತ confident ಆಗಿ check ಮಾಡಬಹುದಿತ್ತು
  →  Duplicates ಇದ್ದಾಗ: nums[left] == nums[mid] == nums[right]
     ಆದ್ರೆ which half is sorted ಅಂತ ಗೊತ್ತಾಗಲ್ಲ!
  →  Solution: ಆ case ಲ್ಲಿ left++ ಮತ್ತು right-- ಮಾಡಿ
     duplicates skip ಮಾಡು, rest same as #33!

  ಹಂತ 4 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  nums[left]==nums[mid]==nums[right] → ambiguous case
     → both pointers shrink ಮಾಡಿ disambiguate ಮಾಡು
  →  Otherwise same as #33 — check which half sorted,
     see if target in that half, eliminate other half
  →  Worst case O(n) when all duplicates, avg O(log n)

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು:
  →  "This is LC #33 but with duplicates — one extra case to handle"
  →  "When nums[left]==nums[mid]==nums[right], we can't tell which
      half is sorted — so we shrink both pointers by 1"
  →  "Otherwise same logic as #33 — identify sorted half, binary search"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Binary Search → Rotated Array with Duplicates
  Secondary : —

  WHY modified Binary Search?
  → Array is still mostly sorted — binary search applicable
  → Duplicates create ONE ambiguous case: left==mid==right
  → Handle that case by shrinking both ends, rest = #33 logic
  → Worst case O(n) only when ALL elements are duplicates

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  In LC #33 (no duplicates), we could always tell which half is
  sorted by comparing nums[left] with nums[mid]:
    - nums[left] <= nums[mid] → left half is sorted
    - else → right half is sorted

  With duplicates, nums[left] == nums[mid] creates ambiguity:
    [3,1,2,3,3,3,3] → left=3, mid=3 — can't tell which side!

  Fix: when nums[left] == nums[mid] == nums[right], just do
  left++ and right-- to skip the duplicates. This is the ONLY
  difference from LC #33.

  The journey from brute to optimal:
    Brute thought   →  Linear scan O(n) — find target directly
    Problem with it →  O(n) is valid but binary search possible
    Better question →  "Can I still binary search on rotated array?"
    Insight         →  Yes! Just handle the duplicate ambiguity case
                       by shrinking both pointers
    Optimal         →  Modified binary search O(log n) avg, O(n) worst

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Simply scan every element. If target found, return True.

  Pseudocode:
    step 1: for each num in nums:
    step 2:   if num == target: return True
    step 3: return False

  Time  : O(n)  →  Why: scan entire array once
  Space : O(1)  →  Why: no extra space

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ?
    → Valid adu, but O(log n) average possible with binary search
    → Interviewer always asks for better than linear here

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 6 — APPROACH 2 — OPTIMAL (Modified Binary Search)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Binary search with one extra case for duplicates.
    When nums[left] == nums[mid] == nums[right] → can't determine
    sorted half → shrink both pointers (left++, right--).
    Otherwise use same logic as LC #33.

  Key steps:
    1. left=0, right=n-1
    2. While left <= right:
       a. mid = (left+right)//2
       b. if nums[mid] == target → return True
       c. DUPLICATE CASE: if nums[left]==nums[mid]==nums[right]
          → left++, right-- → continue
       d. LEFT HALF SORTED: if nums[left] <= nums[mid]
          → if target in [nums[left], nums[mid]) → right=mid-1
          → else → left=mid+1
       e. RIGHT HALF SORTED:
          → if target in (nums[mid], nums[right]] → left=mid+1
          → else → right=mid-1
    3. return False

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ:
    → "LC #33 same logic — but ek extra case: left==mid==right
       ಆದ್ರೆ which half sorted ಅಂತ ಗೊತ್ತಾಗಲ್ಲ, so left++
       right-- ಮಾಡಿ skip ಮಾಡು. Rest same as #33!"

  Time  : O(log n) avg, O(n) worst  →  Why: worst case all duplicates
  Space : O(1)                       →  Why: no extra space

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 7 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: nums = [2,5,6,0,0,1,2], target = 0

  left=0 right=6 mid=3 → nums[3]=0 == target → return True ✓

  Input: nums = [2,5,6,0,0,1,2], target = 3

  left=0 right=6 mid=3
    nums[3]=0 ≠ 3
    nums[left]=2, nums[mid]=0, nums[right]=2
    nums[left]==nums[right] but nums[left]≠nums[mid] → not duplicate case
    nums[left]=2 > nums[mid]=0 → RIGHT half sorted
    target=3 in (0,2]? NO → right=mid-1=2

  left=0 right=2 mid=1
    nums[1]=5 ≠ 3
    nums[left]=2 <= nums[mid]=5 → LEFT half sorted
    target=3 in [2,5)? YES → right=mid-1=0

  left=0 right=0 mid=0
    nums[0]=2 ≠ 3
    nums[left]=2 <= nums[mid]=2 → LEFT half sorted
    target=3 in [2,2)? NO → left=mid+1=1

  left=1 > right=0 → exit loop → return False ✓

  ಇನ್ನೊಂದು — duplicate ambiguous case:
  Input: nums=[1,0,1,1,1], target=0

  left=0 right=4 mid=2
    nums[2]=1 ≠ 0
    nums[left]=1 == nums[mid]=1 == nums[right]=1
    → DUPLICATE CASE → left=1, right=3

  left=1 right=3 mid=2
    nums[2]=1 ≠ 0
    nums[left]=0 ≠ nums[mid]=1 (not duplicate case)
    nums[left]=0 <= nums[mid]=1 → LEFT half sorted
    target=0 in [0,1)? YES → right=mid-1=1

  left=1 right=1 mid=1
    nums[1]=0 == target → return True ✓

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 8 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ All same elements?       →  [1,1,1,1], target=0 → False
                                 Every iteration hits duplicate case
                                 left++ right-- until loop ends
  ✓ Single element?          →  [1], target=1 → True
  ✓ Target at boundary?      →  [3,1,1], target=3 → True
  ✓ No rotation?             →  [1,2,3,4,5], target=3 → True
  ✓ All duplicates + target? →  [2,2,2,2,2], target=2 → True

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 9 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                Time              Space
  Brute Force   O(n)              O(1)
  Optimal       O(log n) avg      O(1)   ← use this ✅
                O(n) worst case

  Time yaake O(log n) avg?
    → Binary search half eliminate maadatte each step
    → Only duplicate case both ends shrink → O(n) worst

  Space yaake O(1)?
    → Only left, right, mid variables — no extra space

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 10 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Binary Search on Rotated Array with Duplicates

  Ee pattern yaavaaga use maadabeeku?
  → Rotated sorted array + duplicates + search
  → "Is this an extension of a standard binary search problem?"
  → When ambiguity from duplicates → shrink both pointers

  Idee pattern beere problemsalli kaanisatte:
  → Search in Rotated Sorted Array #33 (same, no duplicates)
  → Find Minimum in Rotated Sorted Array II #154 (duplicates)
  → Count rotations in sorted array

  Next time intaha problem bandre naanu modalu idannu think maadtene:
  → "Rotated array + duplicates? → LC #33 same logic +
     left==mid==right case alli left++, right-- maadu.
     Ek extra case — rest ellaa same!"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 11 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "Search in a rotated sorted array that may contain duplicates.
      Return True if target exists."

  2. Brute force:
     "Linear scan O(n) — works but interviewer wants better."

  3. Optimize:
     "This is LC #33 with one extra case. When nums[left] ==
      nums[mid] == nums[right], we can't determine which half
      is sorted due to duplicates. So we shrink both pointers
      by 1. Otherwise same logic as #33."

  4. Code:
     "Binary search loop. Check mid == target first. Then handle
      duplicate case: left++, right--. Then check which half
      is sorted and eliminate accordingly."

  5. Complexity:
     "Time O(log n) average, O(n) worst case when all duplicates.
      Space O(1)."

  Mukhya: summane kuutu code bareyabeda!
          LC #33 connection mention maadu — shows you see the pattern.
          Duplicate case = only difference — clean explanation!
"""


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(n) Time | O(1) Space
# ═══════════════════════════════════════════════════════════════════
def search_brute(nums, target):
    """Idu modala aaloochane — linear scan O(n)"""
    for num in nums:
        if num == target:
            return True
    return False


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(log n) avg Time | O(1) Space
# ═══════════════════════════════════════════════════════════════════
def search(nums, target):
    """
    Idu final answer — LC #33 same logic +
    duplicate ambiguity case: left++, right--
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        # found target
        if nums[mid] == target:
            return True

        # DUPLICATE CASE — can't determine which half is sorted
        # e.g. [3,1,2,3,3,3,3] → left=3, mid=3, right=3
        if nums[left] == nums[mid] == nums[right]:
            left += 1
            right -= 1

        # LEFT HALF IS SORTED
        elif nums[left] <= nums[mid]:
            # target in left sorted half?
            if nums[left] <= target < nums[mid]:
                right = mid - 1   # search left
            else:
                left = mid + 1    # search right

        # RIGHT HALF IS SORTED
        else:
            # target in right sorted half?
            if nums[mid] < target <= nums[right]:
                left = mid + 1    # search right
            else:
                right = mid - 1   # search left

    return False


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # Test 1 — Basic, target exists
    assert search([2, 5, 6, 0, 0, 1, 2], 0) == True

    # Test 2 — Target not present
    assert search([2, 5, 6, 0, 0, 1, 2], 3) == False

    # Test 3 — Duplicate ambiguous case
    assert search([1, 0, 1, 1, 1], 0) == True

    # Test 4 — All same elements, target absent
    assert search([1, 1, 1, 1], 0) == False

    # Test 5 — All same elements, target present
    assert search([2, 2, 2, 2], 2) == True

    # Test 6 — Single element, found
    assert search([1], 1) == True

    # Test 7 — Single element, not found
    assert search([1], 0) == False

    # Test 8 — No rotation
    assert search([1, 2, 3, 4, 5], 3) == True

    # Test 9 — Target at boundary
    assert search([3, 1, 1], 3) == True

    print("All tests passed!")
