"""
╔══════════════════════════════════════════════════════════════════╗
║  3SUM                                                            ║
║  LeetCode #15  |  Difficulty: Medium  |  Topic: Arrays / Two Ptr  ║
║  Link: https://leetcode.com/problems/3sum/                       ║
╚══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Given an integer array, find all UNIQUE triplets [a, b, c] such
  that a + b + c == 0. No duplicate triplets in the output, and the
  same triplet in a different order does not count as different.

  Input : nums = [-1, 0, 1, 2, -1, -4]
  Output: [[-1, -1, 2], [-1, 0, 1]]

  Example 1 — basic:
    Input : nums = [-1, 0, 1, 2, -1, -4]
    Output: [[-1, -1, 2], [-1, 0, 1]]
    Why?  : (-1)+(-1)+2=0 and (-1)+0+1=0 are the only zero-sum triplets

  Example 2 — slightly tricky (duplicates + no answer):
    Input : nums = [0, 0, 0]
    Output: [[0, 0, 0]]
    Why?  : 0+0+0=0, but only ONE triplet should be returned even
             though there are 3 zeros to pick from

  Constraints:
    - 3 <= nums.length <= 3000
    - -1e5 <= nums[i] <= 1e5
    - Output triplets must be unique (no duplicate [a,b,c] sets)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ಮೊದಲು problem odidaga ನಮ್ಮ brain ಏನು think ಮಾಡಬೇಕು:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ (What are they asking?)
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  ಒಂದು unsorted integer array     │
  │  Output ಏನು ಬೇಕು?     →  ಎಲ್ಲಾ unique triplets ಯಾವುದು    │
  │                          sum 0 ಆಗುತ್ತೋ ಅವು                │
  │  Constraints ಏನಿದೆ?   →  Duplicate triplets ಬೇಡ, order    │
  │                          matter ಆಗಲ್ಲ, negatives ಇರುತ್ತೆ  │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ನನಗೆ ಗೊತ್ತಿರೋ simple way ಏನು? (Brute force thought)
  →  ಮೂರು nested loops ಹಾಕಿ, ಪ್ರತಿ (i, j, k) triplet ನ sum check
     ಮಾಡಿ, 0 ಆದ್ರೆ result ಗೆ ಸೇರಿಸೋದು.
  →  ಆದರೆ ಇದು slow ಯಾಕೆ? → O(n³) time, ಮತ್ತೆ duplicates ಬರೋದನ್ನ
     ತಡೆಯೋಕೆ set ಬೇರೆ ಬೇಕಾಗುತ್ತೆ — messy ಮತ್ತು slow.

  ಹಂತ 3 — Better way ಹೇಗೆ ಯೋಚಿಸುವುದು? (Optimization thought)
  →  "Two Sum ತರಹ ಪ್ರತಿ pair ಗೆ complement search ಮಾಡ್ಬೋದಾ?
     ಆದ್ರೆ ಇಲ್ಲಿ 3 numbers, so ಒಂದನ್ನ fix ಮಾಡಿ, ಉಳಿದ ಎರಡಕ್ಕೆ
     two-sum ಮಾಡಿದ್ರೆ ಆಗುತ್ತಲ್ವಾ?"
  →  ಅಹಾ moment: Array ಅನ್ನ SORT ಮಾಡಿದ್ರೆ, ಒಂದು number fix ಮಾಡಿ,
     ಉಳಿದ portion ನಲ್ಲಿ L (left) ಮತ್ತು R (right) pointers ಇಟ್ಟು,
     sum ಚೆಕ್ ಮಾಡಿ L++ ಅಥವಾ R-- ಮಾಡ್ಬೋದು — duplicates ಸಹ ಸುಲಭವಾಗಿ
     skip ಮಾಡ್ಬೋದು ಯಾಕಂದ್ರೆ sorted ಆಗಿರೋದ್ರಿಂದ same values
     ಪಕ್ಕ ಪಕ್ಕ ಇರುತ್ತೆ.
  →  ಇದರಿಂದ ನಾವು Sort + Fix-One + Two-Pointer use ಮಾಡಬಹುದು!

  ಹಂತ 4 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  Sorted array ಆದ್ರೆ, two-pointer ಇಂದ target sum ಗೆ O(n) ನಲ್ಲಿ
     search ಮಾಡ್ಬೋದು — Two Sum II (sorted) ನ ಇದೇ idea.
  →  Fix ಮಾಡಿದ i ಗಿಂತ ದೊಡ್ಡ index ಗಳಲ್ಲೇ L, R ಇಟ್ಟುಕೊಂಡ್ರೆ,
     ಪ್ರತಿ triplet ಒಂದೇ ಸಲ ಕಾಣುತ್ತೆ (i < L < R ಯಾವಾಗ್ಲೂ).
  →  Duplicate values sorted ಆಗಿ ಪಕ್ಕದಲ್ಲಿರೋದ್ರಿಂದ, i, L, R
     ಮೂರಕ್ಕೂ "skip same value" logic ಹಾಕಿ duplicate triplets
     ತಪ್ಪಿಸ್ಬೋದು.

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು (Think out loud):
  →  "So I'm seeing that this is Two Sum but with three numbers —
      if I fix one number, the rest becomes a Two Sum problem."
  →  "The brute force would be three nested loops, O(n³), plus
      extra dedup logic — that's messy and slow."
  →  "If I sort the array first, I can fix one element and use two
      pointers on the remaining sorted portion — that gets me to
      O(n²), and sorting also makes duplicate-skipping trivial."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Two Pointers → Opposite Ends (on sorted array)
  Secondary : Sort + Fix-One-Element reduction (3Sum → 2Sum)

  WHY this technique?
  → Need triplets summing to a target (0) — classic fix-one + 2Sum shape
  → Sorting exposes duplicates as adjacent elements, easy to skip
  → Sorted order lets two pointers move monotonically toward the target

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION (How to think)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Key observation: 3Sum(target=0) reduces to, for each i, a
  2Sum(target = -nums[i]) problem on the rest of the (sorted) array.
  Sorting also makes duplicate detection free — equal values sit
  next to each other, so we just skip repeats at each pointer.

  The journey from brute to optimal:
    Brute thought   →  three nested loops + a set to dedupe
    Problem with it →  O(n³) time, awkward duplicate handling
    Better question →  "if I fix one number, is the rest just 2Sum?"
    Insight         →  sorted array + two pointers solves 2Sum in O(n)
    Optimal         →  sort once, fix i, two-pointer (L, R) for the pair

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Try every triplet (i, j, k) with i < j < k, check if the sum is
    zero, and use a set of sorted tuples to avoid duplicate triplets.

  Pseudocode:
    step 1: for i in range(n): for j in range(i+1, n): for k in range(j+1, n):
    step 2:   if nums[i]+nums[j]+nums[k] == 0: add sorted((i,j,k) values) to a set
    step 3: return list of unique triplets from the set

  Time  : O(n³)  →  Why: three nested loops over all index combinations
  Space : O(n) or more →  Why: set of triplets to dedupe, plus result storage

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ? (Why is this not enough?)
    → n=3000 ಆದ್ರೆ, n³ ≈ 2.7×10^10 operations — TLE ಗ್ಯಾರಂಟಿ.
      Duplicate handling ಗೆ set ಬೇರೆ ಬೇಕಾಗಿ, code ಕೂಡ messy ಆಗುತ್ತೆ.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚶 SECTION 6 — APPROACH 2 — BETTER (fix one, hashset for the pair)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Fix nums[i], then do a Two-Sum-with-hashmap on the remaining
    elements (unsorted) to find pairs summing to -nums[i]. Still
    need a set of sorted tuples to dedupe triplets since the array
    isn't sorted.

  Time  : O(n²) average
  Space : O(n) for the hashmap per fixed i, plus dedup set

  ಇನ್ನೂ better ಮಾಡಬಹುದಾ? → ಹೌದು — sorting ಮೊದಲೇ ಮಾಡಿದ್ರೆ, hashmap
    ಕೂಡ ಬೇಡ, duplicate skip ಕೂಡ index-based ಆಗಿ ಸುಲಭ ಆಗುತ್ತೆ.
    Two pointers ಇಂದ extra space ಇಲ್ಲದೇ ಇದೇ O(n²) ಸಿಗುತ್ತೆ.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 7 — APPROACH 3 — OPTIMAL    (Sort + Two Pointers)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Sort nums. For each index i (the fixed element), skip it if it's
    a duplicate of the previous i. Then run two pointers L = i+1,
    R = n-1 over the rest: if the three-sum is too small move L
    right, too big move R left, and if it's exactly zero record the
    triplet and skip past any duplicate values at both L and R
    before continuing.

  Key steps:
    1. Sort nums ascending.
    2. For i from 0 to n-3: skip if nums[i] == nums[i-1] (dup fix).
       If nums[i] > 0, break early — smallest element positive means
       no triplet ahead can sum to 0.
    3. L, R = i+1, n-1. While L < R:
         total = nums[i] + nums[L] + nums[R]
         if total < 0: L += 1
         elif total > 0: R -= 1
         else: record [nums[i], nums[L], nums[R]], then move L and R
               inward while skipping duplicate values at each.

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ (Say it once in Kanglish so it sticks):
    → "Array sort ಮಾಡಿ, i ಅನ್ನ fix ಮಾಡಿ (duplicate i skip ಮಾಡ್ತಾ),
        L = i+1, R = n-1 ಇಟ್ಟು, sum < 0 ಆದ್ರೆ L++ ಮಾಡು, sum > 0
        ಆದ್ರೆ R-- ಮಾಡು, sum == 0 ಆದ್ರೆ answer ಸೇರಿಸಿ L++ R-- ಮಾಡಿ,
        duplicate L/R values ಸಹ skip ಮಾಡ್ತಾ ಹೋಗು!"

  Time  : O(n²)  →  Why: O(n log n) sort + O(n) outer loop × O(n) two-pointer scan
  Space : O(1) extra (excluding output) →  Why: sort in-place, only pointers used

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 8 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: nums = [-1, 0, 1, 2, -1, -4]
  Sorted: [-4, -1, -1, 0, 1, 2]

  i=0 (nums[i]=-4)  →  L=1,R=5 → sum=-4-1+2=-3 <0 → L=2
                       → sum=-4-1+2=-3 <0 → L=3
                       → sum=-4+0+2=-2 <0 → L=4
                       → sum=-4+1+2=-1 <0 → L=5, loop ends (L<R fails)
  i=1 (nums[i]=-1)  →  L=2,R=5 → sum=-1-1+2=0 → record [-1,-1,2]
                       → L=3,R=4 (skip dups: none) → sum=-1+0+1=0 → record [-1,0,1]
                       → L=4,R=3 → loop ends
  i=2 (nums[i]=-1)  →  same as previous i (-1) → SKIP (duplicate fix)
  i=3 (nums[i]=0)   →  L=4,R=5 → sum=0+1+2=3 >0 → R=4, loop ends (L<R fails)
  i=4 → n-3 boundary reached, loop ends

  Output: [[-1, -1, 2], [-1, 0, 1]]

  ಇನ್ನೊಂದು example — tricky case (all zeros):
  Input: nums = [0, 0, 0, 0]
  Sorted: [0, 0, 0, 0]
  i=0 (nums[i]=0) → L=1,R=3 → sum=0 → record [0,0,0]
                    → skip dup L (nums[1]==nums[2]==0) → L=2,R=2 → loop ends
  i=1 (nums[i]=0) → same as previous i (0) → SKIP (duplicate fix)
  Output: [[0, 0, 0]]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 9 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ Fewer than 3 elements?         →  return [] immediately (n < 3)
  ✓ All same elements (all 0)?     →  dedupe via skip-i and skip-L/R gives one triplet
  ✓ No triplet sums to zero?       →  return [] (loop finishes with nothing recorded)
  ✓ All positive / all negative?   →  early break when nums[i] > 0 (can't reach 0)
  ✓ Duplicate values scattered?    →  sorting groups them, skip logic at i, L, R handles it

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 10 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                Time         Space
  Brute Force   O(n³)        O(n) (dedup set)
  Better        O(n²) avg    O(n) (hashmap + dedup set)
  Optimal       O(n²)        O(1) extra    ← use this   

  Time ಯಾಕೆ ಅಷ್ಟು?  → Sort O(n log n), ನಂತರ ಪ್ರತಿ i ಗೂ two-pointer
                        scan O(n) — ಒಟ್ಟು O(n²) dominates.
  Space ಯಾಕೆ ಅಷ್ಟು? → Sort in-place, L/R pointers ಬಿಟ್ಟು ಬೇರೆ extra
                        structure ಬೇಡ (output list ಎಣಿಸಲ್ಲ).

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 11 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Sort + Fix-One + Two-Pointer (kSum reduction)

  ಈ pattern ಯಾವಾಗ use ಮಾಡಬೇಕು?
  → "Find k numbers that sum to target" ಥರದ problem ಬಂದಾಗ
  → Duplicate results ತಪ್ಪಿಸಬೇಕು ಅಂತ ಇದ್ದಾಗ (sorting ಸಹಾಯ ಮಾಡುತ್ತೆ)
  → Brute force O(n^k) ಆಗಿದ್ದು, ಒಂದು dimension reduce ಮಾಡಿ two
    pointer ಗೆ ಇಳಿಸಬಹುದಾ ಅಂತ ಯೋಚಿಸಿದಾಗ

  ಇದೇ pattern ಬೇರೆ problems ನಲ್ಲಿ ಕಾಣಿಸುತ್ತೆ:
  → 3Sum Closest (#16)
  → 4Sum (#18) — fix TWO elements, then two-pointer on the rest
  → Two Sum II — Input Array Is Sorted (#167)

  Next time ಇಂತಹ problem ಬಂದ್ರೆ ನಾನು ಮೊದಲು ಇದನ್ನ think ಮಾಡ್ತೇನೆ:
  → "kSum problem ಬಂತು ಅಂದ್ರೆ, sort ಮಾಡಿ, (k-2) elements fix ಮಾಡಿ,
      ಕೊನೆಯ 2 ಕ್ಕೆ two-pointer ಹಾಕಬಹುದಾ ಅಂತ ಮೊದಲು ಯೋಚಿಸು. Duplicate
      skip ಅನ್ನ every fixed level ನಲ್ಲೂ ಮರೀಬೇಡ."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 12 — INTERVIEW ನಲ್ಲಿ ಹೇಗೆ EXPLAIN ಮಾಡಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "I need all unique triplets in the array that sum to zero,
      with no duplicate triplets in the output."

  2. Brute force:
     "The naive approach is three nested loops checking every
      triplet, giving O(n³), plus extra work to dedupe — that
      would TLE for n up to 3000."

  3. Optimize:
     "I notice fixing one element turns this into a Two Sum
      problem on the rest. If I sort first, Two Sum on a sorted
      array can be done with two pointers in O(n), and sorting
      also makes duplicates trivial to skip."

  4. Code:
     "I'll sort the array, iterate i as the fixed element skipping
      duplicates, and run L/R two pointers on the remainder,
      moving inward based on whether the sum is too small or too
      big, and skipping duplicate values at L and R after a match."

  5. Complexity:
     "Time O(n²) — sort is O(n log n), dominated by the O(n) outer
      loop times O(n) two-pointer scan. Space O(1) extra beyond the
      output, since I sort in place."

  ಮುಖ್ಯ: ಸುಮ್ಮನೆ ಕೂತು code ಬರೆಯಬೇಡ!
         Interviewer ಗೆ ನಿನ್ನ thinking process ಕಾಣಬೇಕು.
"""


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(n^3) Time | O(n) Space
# ═══════════════════════════════════════════════════════════════════
def three_sum_brute(nums):
    """ಇದು ಮೊದಲ ಆಲೋಚನೆ — three nested loops + dedup set"""
    n = len(nums)
    triplets = set()
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    triplets.add(tuple(sorted((nums[i], nums[j], nums[k]))))
    return [list(t) for t in triplets]


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n^2) Time | O(1) Extra Space  (Sort + Two Pointers)
# ═══════════════════════════════════════════════════════════════════
def three_sum(nums):
    """ಇದು final answer — sort ಮಾಡಿ, i fix ಮಾಡಿ, L/R two-pointer scan"""
    nums.sort()
    n = len(nums)
    result = []

    for i in range(n - 2):
        if nums[i] > 0:
            break
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, n - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

    return result


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")   # Windows cp1252 can't print emoji otherwise

    def normalize(triplets):
        return sorted(sorted(t) for t in triplets)

    # Test 1 — Basic example
    assert normalize(three_sum([-1, 0, 1, 2, -1, -4])) == normalize([[-1, -1, 2], [-1, 0, 1]])

    # Test 2 — Edge case: fewer than 3 elements
    assert three_sum([1, 2]) == []

    # Test 3 — Edge case: all same elements
    assert normalize(three_sum([0, 0, 0, 0])) == normalize([[0, 0, 0]])

    # Test 4 — Tricky: no valid triplet (all positive)
    assert three_sum([1, 2, 3, 4]) == []

    print("All tests passed!   ")
