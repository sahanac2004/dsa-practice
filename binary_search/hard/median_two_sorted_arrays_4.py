"""
╔══════════════════════════════════════════════════════════════════╗
║  MEDIAN OF TWO SORTED ARRAYS                                     ║
║  LeetCode #4  |  Difficulty: Hard  |  Topic: Binary Search      ║
║  Link: https://leetcode.com/problems/median-of-two-sorted-arrays/║
║  Source: Striver A2Z + NeetCode 150                              ║
╚══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Given two sorted arrays nums1 and nums2 of sizes m and n,
  return the MEDIAN of the two sorted arrays combined.
  Must solve in O(log(m+n)) time.

  Median: middle element of a sorted array.
    - Odd total: single middle element
    - Even total: average of two middle elements

  Input : nums1, nums2 = two sorted integer arrays
  Output: median of merged sorted array (float)

  Example 1 — odd total:
    Input : nums1=[1,3], nums2=[2]
    Output: 2.0
    Why?  : Merged = [1,2,3] → median = 2

  Example 2 — even total:
    Input : nums1=[1,2], nums2=[3,4]
    Output: 2.5
    Why?  : Merged = [1,2,3,4] → median = (2+3)/2 = 2.5

  Constraints:
    - 0 <= m, n <= 1000
    - 1 <= m+n <= 2000
    - -10^6 <= nums1[i], nums2[i] <= 10^6
    - Must be O(log(m+n)) — cannot just merge!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Problem odi aada mele namma brain enu think maadabeeku:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  2 sorted arrays             │
  │  Output ಏನು ಬೇಕು?     →  median of combined array     │
  │  Constraints ಏನಿದೆ?   →  O(log(m+n)) — cannot merge! │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ನನಗೆ ಗೊತ್ತಿರೋ simple way ಏನು?
  →  Merge both arrays, find median → O(m+n)
  →  ಆದರೆ ಇದು slow ಯಾಕೆ?
     O(log(m+n)) beeku — merge allowed alla!

  ಹಂತ 3 — Better way ಹೇಗೆ ಯೋಚಿಸುವುದು?
  →  "Median ಅಂದ್ರೆ: left half ಮತ್ತು right half ನ split point"
  →  Total (m+n) elements, median is at position (m+n)//2
  →  If I binary search on nums1 — "how many elements from
     nums1 go to left half?" — rest come from nums2!
  →  For a valid partition:
     max(left1, left2) <= min(right1, right2)
  →  Binary search on nums1's partition → O(log m)!

  ಹಂತ 4 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  Binary search on smaller array (always nums1)
  →  For each partition of nums1, nums2 partition is determined
  →  Check if partition is valid using 4 boundary values
  →  O(log(min(m,n))) — very efficient!

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು:
  →  "Think of median as a partition — left half and right half"
  →  "Binary search on how many elements from nums1 go to left"
  →  "Valid partition: max_left <= min_right across both arrays"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Binary Search → On Partition Point
  Secondary : —

  WHY Binary Search on partition?
  → Median splits merged array into equal halves
  → Binary search on how many nums1 elements go to left half
  → nums2 partition determined automatically
  → Check validity with 4 boundary values → O(log min(m,n))

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  The KEY insight: median divides merged array into two equal halves.
  Instead of actually merging, binary search for the right PARTITION.

  Say we take i elements from nums1 and j elements from nums2
  for the left half (i + j = half = (m+n+1)//2):

    nums1: [... L1 | R1 ...]   ← i elements on left
    nums2: [... L2 | R2 ...]   ← j elements on left

  Valid partition condition:
    L1 <= R2  AND  L2 <= R1
    (left side max <= right side min across both arrays)

  If L1 > R2 → too many from nums1 → move left (right = i-1)
  If L2 > R1 → too few from nums1 → move right (left = i+1)

  Once valid:
    - Odd total: median = max(L1, L2)
    - Even total: median = (max(L1,L2) + min(R1,R2)) / 2

  The journey from brute to optimal:
    Brute thought   →  Merge + find middle → O(m+n)
    Problem with it →  O(log(m+n)) required
    Better question →  "Can I binary search for the partition?"
    Insight         →  Yes! Median = partition point in merged array
                       Binary search on nums1 → O(log m)
    Optimal         →  Binary search on smaller array → O(log min(m,n))

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Merge both sorted arrays. Find the median directly.

  Pseudocode:
    step 1: merged = sorted(nums1 + nums2)
    step 2: n = len(merged)
    step 3: if n odd: return merged[n//2]
    step 4: else: return (merged[n//2-1] + merged[n//2]) / 2

  Time  : O((m+n) log(m+n))  →  Why: sorting merged array
  Space : O(m+n)             →  Why: merged array

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ?
    → O(log(m+n)) beeku — merge O(m+n) too slow!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚶 SECTION 6 — APPROACH 2 — BETTER (Two Pointer Merge)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Use two pointers to find median without full merge.
    Only traverse until median position.

  Time  : O(m+n)  →  still linear
  Space : O(1)

  ಇನ್ನೂ better ಮಾಡಬಹudaa?
    → YES! Binary search → O(log(m+n))

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 7 — APPROACH 3 — OPTIMAL (Binary Search on Partition)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Binary search on nums1's partition index i (0 to m).
    j is determined: j = half - i where half = (m+n+1)//2.
    Check if partition is valid: L1<=R2 and L2<=R1.
    Adjust i based on which condition fails.

  Key steps:
    1. Ensure nums1 is smaller (swap if needed)
    2. half = (m + n + 1) // 2
    3. left=0, right=m
    4. While left <= right:
       a. i = (left+right)//2        ← partition in nums1
       b. j = half - i               ← partition in nums2
       c. L1 = nums1[i-1] if i>0 else -inf
       d. R1 = nums1[i]   if i<m else +inf
       e. L2 = nums2[j-1] if j>0 else -inf
       f. R2 = nums2[j]   if j<n else +inf
       g. if L1<=R2 and L2<=R1 → VALID partition!
          - if (m+n) odd: return max(L1,L2)
          - else: return (max(L1,L2)+min(R1,R2))/2
       h. elif L1>R2 → too many from nums1 → right=i-1
       i. else → too few from nums1 → left=i+1

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ:
    → "Smaller array ಮೇಲೆ binary search maadu. i = nums1 ಇಂದ
       left half ಗೆ ಹೋಗೋ elements count. j = half - i.
       4 boundary values: L1,R1,L2,R2 calculate maadu.
       L1<=R2 AND L2<=R1 iddre valid partition!
       Odd total: max(L1,L2). Even: (max(L1,L2)+min(R1,R2))/2"

  Time  : O(log(min(m,n)))  →  Binary search on smaller array
  Space : O(1)              →  Only pointers and boundary values

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 8 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: nums1=[1,3], nums2=[2]
  m=2, n=1, half=(2+1+1)//2=2, left=0, right=2

  i=1, j=2-1=1
  L1=nums1[0]=1, R1=nums1[1]=3
  L2=nums2[0]=2, R2=+inf (j=1=n)
  L1<=R2? 1<=inf ✓   L2<=R1? 2<=3 ✓ → VALID!
  total=3 (odd) → return max(L1,L2) = max(1,2) = 2.0 ✓

  Input: nums1=[1,2], nums2=[3,4]
  m=2, n=2, half=(4+1)//2=2, left=0, right=2

  i=1, j=2-1=1
  L1=nums1[0]=1, R1=nums1[1]=2
  L2=nums2[0]=3, R2=nums2[1]=4
  L1<=R2? 1<=4 ✓   L2<=R1? 3<=2 ✗ → L2>R1 → left=2

  i=2, j=2-2=0
  L1=nums1[1]=2, R1=+inf (i=2=m)
  L2=-inf (j=0),  R2=nums2[0]=3
  L1<=R2? 2<=3 ✓   L2<=R1? -inf<=inf ✓ → VALID!
  total=4 (even) → (max(2,-inf) + min(inf,3))/2 = (2+3)/2 = 2.5 ✓

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 9 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ One empty array?       →  nums1=[], nums2=[1,2,3] → works fine
  ✓ Single elements?       →  nums1=[1], nums2=[2] → 1.5
  ✓ All nums1 < all nums2? →  [1,2] and [3,4] → works
  ✓ All nums1 > all nums2? →  [3,4] and [1,2] → works
  ✓ i=0 or j=0?           →  Use -inf for L1 or L2
  ✓ i=m or j=n?           →  Use +inf for R1 or R2

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 10 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                  Time                Space
  Brute (merge)   O((m+n) log(m+n))  O(m+n)
  Two pointer     O(m+n)             O(1)
  Optimal         O(log(min(m,n)))   O(1)   ← use this ✅

  Time yaake O(log min(m,n))?
    → Binary search on smaller array only
  Space yaake O(1)?
    → Only i, j, L1, L2, R1, R2 variables

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 11 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Binary Search on Partition Point

  Ee pattern yaavaaga use maadabeeku?
  → "Find kth element in two sorted arrays"
  → "Find median without merging"
  → Any problem needing O(log n) on combined sorted structure

  Key formulas to remember:
    half = (m + n + 1) // 2
    j = half - i
    L1 = nums1[i-1] if i > 0 else -inf
    R1 = nums1[i]   if i < m else +inf
    L2 = nums2[j-1] if j > 0 else -inf
    R2 = nums2[j]   if j < n else +inf

  Next time intaha problem bandre naanu modalu idannu think maadtene:
  → "Two sorted arrays + O(log n) + median/kth?
     → Binary search on partition! smaller array ಮೇಲೆ binary search.
     L1<=R2 AND L2<=R1 iddre valid! 4 boundary values remember maadu!"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 12 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "Find median of two sorted arrays in O(log(m+n))."

  2. Brute force:
     "Merge arrays, find middle. O(m+n) — not allowed."

  3. Optimize:
     "Key insight: median = partition point of merged array.
      Binary search on how many elements from nums1 go to left half.
      For each i (elements from nums1), j = half-i from nums2.
      Check: L1<=R2 AND L2<=R1 → valid partition.
      L1>R2 → too many from nums1 → go left.
      L2>R1 → too few from nums1 → go right."

  4. Code:
     "Always binary search smaller array. half=(m+n+1)//2.
      For each mid i, compute j=half-i.
      Get 4 boundary values with -inf/+inf guards.
      Valid? Return max(L1,L2) for odd, avg of middle two for even."

  5. Complexity:
     "Time O(log(min(m,n))). Space O(1)."

  Mukhya: summane kuutu code bareyabeda!
          half = (m+n+1)//2 — the +1 handles odd total!
          Always binary search on SMALLER array — mention this!
          4 boundary values with infinity guards — explain clearly!
"""

from math import inf


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O((m+n) log(m+n)) Time | O(m+n) Space
# ═══════════════════════════════════════════════════════════════════
def find_median_sorted_arrays_brute(nums1, nums2):
    """Idu modala aaloochane — merge and find median"""
    merged = sorted(nums1 + nums2)
    n = len(merged)
    if n % 2 == 1:
        return float(merged[n // 2])
    else:
        return (merged[n // 2 - 1] + merged[n // 2]) / 2.0


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(log(min(m,n))) Time | O(1) Space
# ═══════════════════════════════════════════════════════════════════
def find_median_sorted_arrays(nums1, nums2):
    """
    Idu final answer — binary search on partition point
    Always binary search on smaller array for efficiency
    half = (m+n+1)//2 handles both odd and even totals
    """
    # ensure nums1 is always the smaller array
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    m, n = len(nums1), len(nums2)
    half = (m + n + 1) // 2    # size of left half

    left, right = 0, m

    while left <= right:
        i = (left + right) // 2    # elements from nums1 in left half
        j = half - i               # elements from nums2 in left half

        # boundary values with infinity guards
        L1 = nums1[i - 1] if i > 0 else -inf
        R1 = nums1[i]     if i < m else  inf
        L2 = nums2[j - 1] if j > 0 else -inf
        R2 = nums2[j]     if j < n else  inf

        if L1 <= R2 and L2 <= R1:
            # VALID PARTITION FOUND!
            if (m + n) % 2 == 1:
                return float(max(L1, L2))           # odd: left max
            else:
                return (max(L1, L2) + min(R1, R2)) / 2.0  # even: avg middles

        elif L1 > R2:
            right = i - 1   # too many from nums1 → shrink left
        else:
            left = i + 1    # too few from nums1 → expand left


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # Test 1 — Odd total
    assert find_median_sorted_arrays([1, 3], [2]) == 2.0

    # Test 2 — Even total
    assert find_median_sorted_arrays([1, 2], [3, 4]) == 2.5

    # Test 3 — One empty array
    assert find_median_sorted_arrays([], [1]) == 1.0
    assert find_median_sorted_arrays([], [1, 2]) == 1.5

    # Test 4 — All nums1 smaller than nums2
    assert find_median_sorted_arrays([1, 2], [3, 4, 5]) == 3.0

    # Test 5 — All nums1 larger than nums2
    assert find_median_sorted_arrays([4, 5], [1, 2, 3]) == 3.0

    # Test 6 — Single elements
    assert find_median_sorted_arrays([1], [2]) == 1.5

    # Test 7 — Equal elements
    assert find_median_sorted_arrays([1, 1], [1, 1]) == 1.0

    # Test 8 — Negative numbers
    assert find_median_sorted_arrays([-3, -1], [-2, 0]) == -1.5

    print("All tests passed!")

You are out of free messag
