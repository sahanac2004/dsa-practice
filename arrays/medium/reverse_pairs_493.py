"""
╔══════════════════════════════════════════════════════════════════╗
║  REVERSE PAIRS                                                      ║
║  LeetCode #493  |  Difficulty: Hard  |  Topic: Arrays / Merge Sort  ║
║  Link: https://leetcode.com/problems/reverse-pairs/                 ║
╚══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Given an array nums, count the number of "reverse pairs" — index
  pairs (i, j) with i < j such that nums[i] > 2 * nums[j].

  Input : nums = [1, 3, 2, 3, 1]
  Output: 2

  Example 1 — basic:
    Input : nums = [1, 3, 2, 3, 1]
    Output: 2
    Why?  : (1,4) → nums[1]=3 > 2*nums[4]=2  and
             (3,4) → nums[3]=3 > 2*nums[4]=2

  Example 2 — slightly tricky (larger values, negative numbers):
    Input : nums = [2, 4, 3, 5, 1]
    Output: 3
    Why?  : (1,4): 4>2*1=2 ; (2,4): 3>2*1=2 ; (3,4): 5>2*1=2 — three pairs

  Constraints:
    - 1 <= nums.length <= 5 * 10^4
    - -2^31 <= nums[i] <= 2^31 - 1

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ಮೊದಲು problem odidaga ನಮ್ಮ brain ಏನು think ಮಾಡಬೇಕು:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ (What are they asking?)
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  ಒಂದು array of numbers          │
  │  Output ಏನು ಬೇಕು?     →  i<j ಮತ್ತು nums[i] > 2*nums[j]   │
  │                          ಆಗಿರೋ pairs ನ count             │
  │  Constraints ಏನಿದೆ?   →  n<=5*10^4, negative numbers      │
  │                          ಇರೋಕೆ ಸಾಧ್ಯ, overflow ಎಚ್ಚರ      │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ನನಗೆ ಗೊತ್ತಿರೋ simple way ಏನು? (Brute force thought)
  →  ಪ್ರತಿ (i,j) pair ಗೂ (i<j), nums[i] > 2*nums[j] ಚೆಕ್ ಮಾಡಿ count
     ಮಾಡೋದು — nested loops.
  →  ಆದರೆ ಇದು slow ಯಾಕೆ? → O(n²) — n=5*10^4 ಆದ್ರೆ 2.5*10^9,
     ಬಹಳ slow.

  ಹಂತ 3 — Better way ಹೇಗೆ ಯೋಚಿಸುವುದು? (Optimization thought)
  →  Count Inversions problem (i<j, nums[i]>nums[j]) merge sort ಇಂದ
     O(n log n) ಗೆ solve ಆಗುತ್ತೆ ಅಂತ ಗೊತ್ತಿದ್ರೆ — ಇಲ್ಲಿ condition ಸ್ವಲ್ಪ
     ಬೇರೆ (nums[i] > 2*nums[j]) ಆದ್ರೂ, ಸೇಮ್ merge sort structure use
     ಮಾಡ್ಬೋದು.
  →  ಅಹಾ moment: merge sort ನಲ್ಲಿ, left half ಮತ್ತು right half ಎರಡೂ
     ಆಗಲೇ individually sorted ಆಗಿದ್ರೆ, ಪ್ರತಿ left element ಗೂ, ಎಷ್ಟು
     right elements ಅದರ half ಗಿಂತ ಕಡಿಮೆ ಇವೆ ಅಂತ two-pointer ಇಂದ
     linear time ನಲ್ಲಿ ಹುಡುಕ್ಬೋದು — merge step ಗೆ ಮೊದಲೇ, count
     ಮಾಡಿ ಬಿಡ್ಬೇಕು (merge ಆದ ಮೇಲೆ order ಬದಲಾಗುತ್ತೆ, count ತಪ್ಪಾಗುತ್ತೆ).
  →  ಇದರಿಂದ ನಾವು Merge Sort (Modified — Count During Divide &
     Conquer) use ಮಾಡಬಹುದು!

  ಹಂತ 4 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  Merge sort ಆಗಲೇ ಎರಡು halves ಅನ್ನ sort ಮಾಡಿ merge ಮಾಡುತ್ತೆ —
     ಆ sorted property ಅನ್ನ use ಮಾಡಿ, cross-half pairs ಅನ್ನ O(n)
     ನಲ್ಲಿ count ಮಾಡ್ಬಹುದು (two pointers, no need for nested loop).
  →  Divide & conquer ಇಂದ, ಪ್ರತಿ level ನಲ್ಲೂ ಎಲ್ಲಾ cross pairs count
     ಆಗುತ್ತೆ — within-half pairs recursive calls ನಲ್ಲೇ already
     count ಆಗಿರುತ್ತೆ.
  →  Count ಗೆ ಮತ್ತು merge ಗೆ ಬೇರೆ ಬೇರೆ pointers use ಮಾಡಿದ್ರೆ, correctness
     ಗ್ಯಾರಂಟಿ ಆಗುತ್ತೆ (merge sorted order ಬದಲಿಸಿದ ಮೇಲೆ count ಮಾಡಿದ್ರೆ
     ತಪ್ಪಾಗುತ್ತೆ, ಆದ್ದರಿಂದ merge ಗಿಂತ ಮೊದಲೇ count ಮಾಡ್ಬೇಕು).

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು (Think out loud):
  →  "The naive way checks every pair — O(n²), too slow for n up to 5*10^4."
  →  "This resembles Count Inversions, which merge sort solves in
      O(n log n) by counting cross-pairs during the merge step —
      I can adapt the same divide-and-conquer structure here."
  →  "Since both halves are already sorted before merging, I can use
      two pointers to count, for each left element, how many right
      elements satisfy nums[i] > 2*nums[j] in linear time — but I
      must count BEFORE actually merging, since merging changes order."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Merge Sort (Modified — Count Cross Pairs Before Merging)
  Secondary : Two-Pointer (within the count step, over sorted halves)

  WHY this technique?
  → The problem reduces to counting cross-half pairs at every level of
    a divide-and-conquer split — exactly merge sort's structure
  → Sorted halves let a two-pointer scan count qualifying pairs in
    O(n) per level instead of nested loops
  → Counting must happen before the merge overwrites the original
    left/right order, since the condition depends on relative position

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION (How to think — English)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Key observation: every reverse pair (i, j) with i < j either lies
  entirely within the left half, entirely within the right half, or
  crosses between them (i in left, j in right, since the array
  position order is preserved by index, not value). Recursively
  counting within each half and then counting cross pairs at merge
  time (using two pointers since both halves are sorted) covers all
  pairs exactly once, in O(n log n) total.

  The journey from brute to optimal:
    Brute thought   →  check every (i,j) pair directly
    Problem with it →  O(n²), too slow for large n
    Better question →  "does sorting help count pairs faster, like it
                        does for Count Inversions?"
    Insight         →  merge sort's divide step naturally separates
                        pairs into within-half and cross-half; sorted
                        halves let cross-half counting run in O(n)
    Optimal         →  modified merge sort, counting during the
                        divide-and-conquer, O(n log n) time

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE (Check Every Pair)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    For every pair of indices (i, j) with i < j, check if
    nums[i] > 2 * nums[j] and count how many satisfy it.

  Pseudocode:
    step 1: count = 0
    step 2: for i in range(n):
    step 3:   for j in range(i+1, n):
    step 4:     if nums[i] > 2 * nums[j]: count += 1
    step 5: return count

  Time  : O(n²)  →  Why: nested loop over all index pairs
  Space : O(1)   →  Why: only a running counter

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ? (Why is this not enough?)
    → n=5*10^4 ಆದ್ರೆ n² = 2.5*10^9 — TLE ಆಗತ್ತೆ.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚶 SECTION 6 — APPROACH 2 — BETTER (if exists)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    No natural polynomial-but-not-optimal middle ground here (unlike
    problems where a hashmap or prefix array helps) — the moment you
    recognize the Count Inversions parallel, you go straight to the
    modified merge sort. A BIT/Fenwick tree with coordinate
    compression is an alternative O(n log n) approach, but it's not
    simpler than merge sort for this problem.

  Time  : —
  Space : —

  ಇನ್ನೂ better ಮಾಡಬಹುದಾ? → ಇದೇ optimal class (O(n log n)), directly
  SECTION 7 ಗೆ ಹೋಗೋಣ.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 7 — APPROACH 3 — OPTIMAL   (Modified Merge Sort)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Recursively split the array in half, sort-and-count each half,
    then — BEFORE merging — count cross-half pairs using two pointers
    over the two already-sorted halves. Finally merge the halves as
    in standard merge sort.

  Key steps:
    1. if len <= 1: return 0 (base case, no pairs possible)
    2. mid = len // 2; count = mergeSortCount(left) + mergeSortCount(right)
    3. j = 0 (pointer into right half)
    4. for i in range(len(left)):
         while j < len(right) and left[i] > 2 * right[j]: j += 1
         count += j
    5. merge left and right into sorted order (standard merge step)
    6. return count

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ (Say it once in Kanglish so it sticks):
    → "Array ಅನ್ನ ಎರಡು halves ಆಗಿ ಒಡೆದು, ಪ್ರತಿ half ಅನ್ನ recursively
        sort+count ಮಾಡು. ಆಮೇಲೆ, merge ಮಾಡೋ ಮೊದಲೇ, left ನ ಪ್ರತಿ element
        ಗೂ, right ನಲ್ಲಿ ಎಷ್ಟು elements 'left[i] > 2*right[j]' condition
        satisfy ಮಾಡ್ತಾವೆ ಅಂತ two-pointer ಇಂದ ಎಣಿಸು. ಕೊನೆಗೆ normal
        merge ಮಾಡು!"

  Time  : O(n log n)  →  Why: standard merge sort recurrence, with an
                          extra O(n) counting pass per merge level
  Space : O(n)         →  Why: temporary arrays needed for merging

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 8 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: nums = [1, 3, 2, 3, 1]  (n=5)

  Split: left=[1,3,2] (idx 0-2), right=[3,1] (idx 3-4)

  Recurse on left=[1,3,2]:
    Split: [1] and [3,2] → recurse [3,2] → split [3],[2] → count=0
      merge count step: left=[3],right=[2] → 3>2*2=4? No → count+=0
      merged: [2,3]
    Now left=[1] (count 0), right=[2,3] (count 0)
    Count step: left=[1] vs right=[2,3] → 1>2*2? No → count+=0
    merged: [1,2,3], subtotal count = 0

  Recurse on right=[3,1]:
    Split: [3],[1] → count step: 3>2*1=2? Yes → count=1
    merged: [1,3], subtotal count = 1

  Now merge left=[1,2,3] (sorted, count so far 0) with
  right=[1,3] (sorted, count so far 1):
    i=0 (left[0]=1): j moves while 1 > 2*right[j] → right[0]=1,
                     1>2? No → j stays 0 → count += j(0) = 0
    i=1 (left[1]=2): 2>2*1=2? No (not strictly greater) → j stays 0
                     → count += 0
    i=2 (left[2]=3): 3>2*1=2? Yes → j=1; 3>2*right[1]=3? 3>6? No →
                     j stays 1 → count += j(1) = 1

  Total count = 0 (left subtree) + 1 (right subtree) + 0+0+1 (cross) = 2

  Output: 2   matches expected

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 9 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ Single element / empty array? →  base case returns 0 immediately,
                                      no pairs possible
  ✓ Negative numbers?             →  2*nums[j] works fine with
                                      negatives, comparisons unaffected
  ✓ Values causing overflow        →  use Python's arbitrary precision
    (2 * nums[i] near INT_MAX)?      ints; in C++/Java, cast to a
                                      wider type (long) before doubling
  ✓ All elements identical?       →  nums[i] > 2*nums[j] fails for
                                      equal values (2x is strictly
                                      greater needed), count stays 0
                                      unless values are negative
  ✓ Strictly decreasing array?    →  many pairs qualify; algorithm's
                                      two-pointer count naturally
                                      captures all of them

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 10 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                Time         Space
  Brute Force   O(n²)        O(1)
  Optimal       O(n log n)   O(n)    ← use this

  Time ಯಾಕೆ ಅಷ್ಟು?  → merge sort recurrence T(n) = 2T(n/2) + O(n)
                        (count step + merge step, both linear per
                        level) → O(n log n).
  Space ಯಾಕೆ ಅಷ್ಟು? → merge step ಗೆ temporary arrays ಬೇಕು, recursion
                        stack depth O(log n) — dominant term O(n).

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 11 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Modified Merge Sort (Count Cross Pairs Pre-Merge)

  ಈ pattern ಯಾವಾಗ use ಮಾಡಬೇಕು?
  → "Count pairs (i,j) with i<j satisfying some comparison condition"
    ಥರ problem ಕೇಳಿದಾಗ (inversions, reverse pairs, etc.)
  → O(n²) brute force ಇದ್ರೆ, ಮತ್ತು condition sorted order ಇಂದ two-
    pointer ಇಂದ speed ಆಗುತ್ತೆ ಅಂತ ಗುರುತಿಸಿದಾಗ
  → Divide & conquer ಇಂದ "within-half" ಮತ್ತು "cross-half" ಅಂತ
    problem split ಆಗುತ್ತೆ ಅಂತ ಗೊತ್ತಾದಾಗ

  ಇದೇ pattern ಬೇರೆ problems ನಲ್ಲಿ ಕಾಣಿಸುತ್ತೆ:
  → Count Inversions (GfG classic) — same structure, simpler condition
    (nums[i] > nums[j])
  → Count of Smaller Numbers After Self (LC 315) — same merge-sort-
    count family, tracks per-index counts instead of a total
  → Number of Range Sums (LC 327) — similar divide & conquer counting

  Next time ಇಂತಹ problem ಬಂದ್ರೆ ನಾನು ಮೊದಲು ಇದನ್ನ think ಮಾಡ್ತೇನೆ:
  → "'Count pairs with i<j and some comparison' ಅಂತ ಕಂಡ ತಕ್ಷಣ, merge
      sort ಇಂದ within-half + cross-half split ಮಾಡಿ, cross-half ಅನ್ನ
      two-pointer ಇಂದ (merge ಗಿಂತ ಮೊದಲೇ!) count ಮಾಡು ಅಂತ ಮೊದಲು
      ಯೋಚಿಸು."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 12 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "I need to count index pairs (i,j) with i<j where
      nums[i] > 2*nums[j] — similar to counting inversions, but with
      a doubled comparison."

  2. Brute force:
     "Check every pair directly — O(n²), too slow for n up to 5*10^4."

  3. Optimize:
     "This is structurally the same as Count Inversions, which merge
      sort solves in O(n log n). I split the array, recursively solve
      each half, and count cross-half pairs using two pointers over
      the sorted halves before merging them."

  4. Code:
     "In the merge step, before actually merging, walk a pointer j
      through the sorted right half for each left element i, counting
      how many right elements satisfy left[i] > 2*right[j] — since
      both halves are sorted, this pointer only moves forward, giving
      O(n) per level. Then perform the standard merge."

  5. Complexity:
     "Time O(n log n) — merge sort recurrence with linear work per
      level. Space O(n) — temporary arrays for merging."

  ಮುಖ್ಯ: ಸುಮ್ಮನೆ ಕೂತು code ಬರೆಯಬೇಡ!
         Interviewer ಗೆ ನಿನ್ನ thinking process ಕಾಣಬೇಕು.
"""


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(n^2) Time | O(1) Space  (Check Every Pair)
# ═══════════════════════════════════════════════════════════════════
def reverse_pairs_brute(nums):
    """ಇದು ಮೊದಲ ಆಲೋಚನೆ — ಎಲ್ಲಾ (i,j) pairs ಚೆಕ್ ಮಾಡಿ count ಮಾಡೋದು"""
    n = len(nums)
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] > 2 * nums[j]:
                count += 1
    return count


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n log n) Time | O(n) Space  (Modified Merge Sort)
# ═══════════════════════════════════════════════════════════════════
def reverse_pairs(nums):
    """ಇದು final answer — merge sort ಇಂದ, cross-half pairs ಅನ್ನ merge ಗಿಂತ ಮೊದಲೇ count ಮಾಡು"""

    def sort_and_count(arr):
        if len(arr) <= 1:
            return arr, 0

        mid = len(arr) // 2
        left, left_count = sort_and_count(arr[:mid])
        right, right_count = sort_and_count(arr[mid:])

        # Count cross-half pairs BEFORE merging (order still intact)
        cross_count = 0
        j = 0
        for i in range(len(left)):
            while j < len(right) and left[i] > 2 * right[j]:
                j += 1
            cross_count += j

        # Standard merge step
        merged = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        merged.extend(left[i:])
        merged.extend(right[j:])

        return merged, left_count + right_count + cross_count

    _, total = sort_and_count(nums)
    return total


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")   # Windows cp1252 can't print emoji otherwise

    # Test 1 — Basic example
    assert reverse_pairs([1, 3, 2, 3, 1]) == 2

    # Test 2 — Slightly tricky: larger values
    assert reverse_pairs([2, 4, 3, 5, 1]) == 3

    # Test 3 — Edge case: single element / empty
    assert reverse_pairs([1]) == 0
    assert reverse_pairs([]) == 0

    # Test 4 — Edge case: no qualifying pairs
    assert reverse_pairs([1, 2, 3, 4, 5]) == 0

    # Test 5 — Tricky: negative numbers
    assert reverse_pairs([-5, -3, -1]) == 1  # (-5 > 2*-3 = -6)

    print("All tests passed! ")
