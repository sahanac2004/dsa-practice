"""
╔═══════════════════════════════════════════════════════════════════════╗
║  4SUM                                                                 ║
║  LeetCode #18  |  Difficulty: Medium  |  Topic: Arrays / Two Pointers ║
║  Link: https://leetcode.com/problems/4sum/                            ║
╚═══════════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Given an array of n integers and a target, return all UNIQUE
  quadruplets [nums[a], nums[b], nums[c], nums[d]] (a, b, c, d are
  distinct indices) such that they sum to target. The result must not
  contain duplicate quadruplets (order within a quadruplet doesn't
  matter, but no repeated value-combinations in the output).

  Input : nums = [1, 0, -1, 0, -2, 2], target = 0
  Output: [[-2,-1,1,2], [-2,0,0,2], [-1,0,0,1]]

  Example 1 — basic:
    Input : nums = [1, 0, -1, 0, -2, 2], target = 0
    Output: [[-2,-1,1,2], [-2,0,0,2], [-1,0,0,1]]
    Why?  : these are the only 3 distinct value combinations that add to 0

  Example 2 — slightly tricky (all same elements):
    Input : nums = [2, 2, 2, 2, 2], target = 8
    Output: [[2,2,2,2]]
    Why?  : only one distinct combination exists even though there are
             many ways to pick 4 indices — duplicates must be collapsed

  Constraints:
    - 1 <= nums.length <= 200
    - -10^9 <= nums[i] <= 10^9
    - -10^9 <= target <= 10^9

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ಮೊದಲು problem odidaga ನಮ್ಮ brain ಏನು think ಮಾಡಬೇಕು:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ (What are they asking?)
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  array + target sum             │
  │  Output ಏನು ಬೇಕು?     →  ಎಲ್ಲಾ unique 4-element groups   │
  │                          which sum to target              │
  │  Constraints ಏನಿದೆ?   →  n<=200, duplicates skip ಮಾಡಬೇಕು,│
  │                          sums overflow ಆಗ್ಬೋದು (use int64) │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ನನಗೆ ಗೊತ್ತಿರೋ simple way ಏನು? (Brute force thought)
  →  4 nested loops ಇಂದ ಎಲ್ಲಾ (a,b,c,d) combinations try ಮಾಡಿ, sum
     ಚೆಕ್ ಮಾಡಿ, ಸಿಕ್ಕಿದ್ರೆ set ನಲ್ಲಿ (duplicates avoid ಮಾಡೋಕೆ) ಸೇರಿಸೋದು.
  →  ಆದರೆ ಇದು slow ಯಾಕೆ? → O(n⁴) — n=200 ಆದ್ರೆ 200⁴ ≈ 1.6 billion,
     ಬಹಳ slow.

  ಹಂತ 3 — Better way ಹೇಗೆ ಯೋಚಿಸುವುದು? (Optimization thought)
  →  3Sum ನಲ್ಲಿ ನಾವು "array sort ಮಾಡಿ, ಒಂದು number fix ಮಾಡಿ, ಉಳಿದ
     ಎರಡಕ್ಕೆ two-pointer use ಮಾಡಿದ್ವಿ" ಅಂತ ನೆನಪಿಸ್ಕೊಂಡ್ರೆ — ಇಲ್ಲಿ ಇನ್ನೊಂದು
     number ಕೂಡ fix ಮಾಡಿದ್ರೆ ಸಾಕು! ಅಂದ್ರೆ 2 nested loops ಇಂದ ಮೊದಲ ಎರಡು
     numbers fix ಮಾಡಿ, ಉಳಿದೆರಡಕ್ಕೆ (sorted array ನಲ್ಲಿ) two-pointer.
  →  ಅಹಾ moment: ಪ್ರತಿ level ನಲ್ಲೂ duplicates ಅನ್ನ "ಹಿಂದಿನ value ಜೊತೆ
     ಸೇಮ್ ಆದ್ರೆ skip ಮಾಡು" ಅಂತ handle ಮಾಡಿದ್ರೆ, unique quadruplets
     ಮಾತ್ರ ಸಿಗುತ್ತೆ — extra set structure ಬೇಡ.
  →  ಇದರಿಂದ ನಾವು Sort + Two Fixed Pointers + Two-Pointer (3Sum
     generalized to k=4) use ಮಾಡಬಹುದು!

  ಹಂತ 4 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  Array sorted ಆದ ಮೇಲೆ, duplicates adjacent ಆಗಿ ಬರುತ್ತೆ — ಅವನ್ನ
    skip ಮಾಡೋದು ಸುಲಭ ಆಗುತ್ತೆ.
  →  Two numbers fix ಮಾಡಿದ ಮೇಲೆ, remaining problem "2Sum on a sorted
    subarray" ಆಗುತ್ತೆ — ಅದಕ್ಕೆ two-pointer perfect fit (L++/R--).
  →  Sorted array ಆಗಿರೋದ್ರಿಂದ, sum ಜಾಸ್ತಿ ಆದ್ರೆ R--, ಕಡಿಮೆ ಆದ್ರೆ L++
    ಅಂತ direction ಗೊತ್ತಾಗುತ್ತೆ — no need for extra hashing.

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು (Think out loud):
  →  "The naive way is 4 nested loops checking every combination —
      O(n⁴), and I'd need a set to dedupe, which adds overhead too."
  →  "I recall that 3Sum fixes one number and two-pointers the rest —
      here I can fix two numbers and two-pointer the remaining pair,
      generalizing the same idea."
  →  "Sorting first lets me skip duplicates cleanly at every fixed
      position, so the output naturally has no duplicate quadruplets
      without needing a set."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Sort + Two Fixed Loops + Two-Pointer (3Sum generalized)
  Secondary : Duplicate-skipping via sorted adjacency

  WHY this technique?
  → Fixing two numbers reduces the problem to "2Sum on a sorted
    subarray," which two-pointer solves in O(n) instead of nested loops
  → Sorting makes duplicate values adjacent, so skipping them at each
    fixed index (and inside the two-pointer loop) is a simple check
  → Avoids the need for a hash set to dedupe results, since sorted
    order + skip logic guarantees each unique quadruplet only once

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION (How to think — English)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Key observation: 4Sum is just 3Sum with one more number fixed, and
  3Sum is just 2Sum with one number fixed. This recursive reduction
  means: sort the array, fix the first two numbers with nested loops,
  then two-pointer the remaining two — the classic "reduce k-Sum to
  two-pointer" pattern.

  The journey from brute to optimal:
    Brute thought   →  4 nested loops trying every quadruplet
    Problem with it →  O(n⁴), way too slow for n=200
    Better question →  "how did 3Sum reduce the problem — can I do
                        that one level deeper?"
    Insight         →  fix two numbers, two-pointer the rest on the
                        sorted remainder
    Optimal         →  sort + 2 nested loops + two-pointer = O(n³)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE (4 Nested Loops + Set)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Try every combination of 4 distinct indices, check if they sum to
    target, and collect sorted tuples in a set to avoid duplicates.

  Pseudocode:
    step 1: result = set()
    step 2: for a in range(n):
    step 3:   for b in range(a+1, n):
    step 4:     for c in range(b+1, n):
    step 5:       for d in range(c+1, n):
    step 6:         if nums[a]+nums[b]+nums[c]+nums[d] == target:
    step 7:           result.add(tuple(sorted([nums[a],nums[b],nums[c],nums[d]])))
    step 8: return list(result)

  Time  : O(n⁴)  →  Why: four nested loops over n elements
  Space : O(n) extra (beyond output) →  Why: set to dedupe quadruplets

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ? (Why is this not enough?)
    → n=200 ಆದ್ರೆ 200⁴ ≈ 1.6 billion iterations — TLE ಆಗತ್ತೆ.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚶 SECTION 6 — APPROACH 2 — BETTER (Fix 2, Hash the 3rd)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Fix the first two numbers with nested loops (O(n²)), then use a
    hash set to find pairs among the rest that complete the target
    sum — similar to the hashmap variant of 2Sum.

  Time  : O(n³)  →  O(n²) for the two fixed loops, O(n) hashing per pair
  Space : O(n)   →  hash set per inner search, plus dedup logic needed

  ಇನ್ನೂ better ಮಾಡಬಹುದಾ? → ಹೌದು — sort ಮಾಡಿ two-pointer use ಮಾಡಿದ್ರೆ,
  hash set ಬೇಡ ಆಗುತ್ತೆ, duplicates naturally skip ಆಗುತ್ತೆ, ಮತ್ತು same
  O(n³) time ಆದ್ರೂ cleaner, less extra space.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 7 — APPROACH 3 — OPTIMAL   (Sort + 2 Fixed Loops + Two-Pointer)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Sort nums. Fix index i (0..n-4) and j (i+1..n-3), skipping
    duplicate values at each level. For the remaining subarray
    (j+1..n-1), use two pointers L=j+1, R=n-1: if the four-sum is too
    small, L++; too big, R--; if it matches, record it and skip past
    duplicates on both sides before continuing.

  Key steps:
    1. sort nums
    2. for i in range(n-3): skip if nums[i] == nums[i-1] (i>0)
    3.   for j in range(i+1, n-2): skip if nums[j] == nums[j-1] (j>i+1)
    4.     L, R = j+1, n-1
    5.     while L < R:
    6.       s = nums[i]+nums[j]+nums[L]+nums[R]
    7.       if s == target: record; L++; R--; skip duplicates at L, R
    8.       elif s < target: L += 1
    9.       else: R -= 1

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ (Say it once in Kanglish so it sticks):
    → "Array sort ಮಾಡಿ, i ಮತ್ತು j ಅನ್ನ ಎರಡು numbers ಆಗಿ fix ಮಾಡ್ತಾ
        ಹೋಗು (duplicates skip ಮಾಡ್ತಾ), ಉಳಿದ ಭಾಗಕ್ಕೆ L,R two-pointer
        ಇಟ್ಟು sum < target ಆದ್ರೆ L++, sum > target ಆದ್ರೆ R--, equal
        ಆದ್ರೆ ಸೇರಿಸಿ ಇಬ್ಬರನ್ನೂ move ಮಾಡ್ತಾ duplicates skip ಮಾಡು!"

  Time  : O(n³)  →  Why: two nested loops O(n²), two-pointer scan O(n) each
  Space : O(1) extra (excluding output/sort)  →  Why: only pointers, no hashing

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 8 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: nums = [1, 0, -1, 0, -2, 2], target = 0
  Sorted: [-2, -1, 0, 0, 1, 2]  (n=6)

  i=0 (nums[i]=-2):
    j=1 (nums[j]=-1): L=2,R=5 → sum=-2-1+0+2=-1 <0 → L++
                      L=3,R=5 → sum=-2-1+0+2=-1 <0 → L++
                      L=4,R=5 → sum=-2-1+1+2=0  == target → record [-2,-1,1,2]
                      L++,R-- → L=5,R=4 → loop ends
    j=2 (nums[j]=0):  L=3,R=5 → sum=-2+0+0+2=0 == target → record [-2,0,0,2]
                      L++,R-- → L=4,R=4 → loop ends (L<R false)
    j=3 (nums[j]=0):  duplicate of j=2's value → skip
  i=1 (nums[i]=-1):
    j=2 (nums[j]=0):  L=3,R=5 → sum=-1+0+0+2=1 >0 → R--
                      L=3,R=4 → sum=-1+0+0+1=0 == target → record [-1,0,0,1]
                      L++,R-- → L=4,R=3 → loop ends
    j=3 (nums[j]=0):  duplicate of j=2's value → skip
  i=2 (nums[i]=0): remaining elements too few / sums won't hit 0 with
                    two positives left → no more matches

  Output: [[-2,-1,1,2], [-2,0,0,2], [-1,0,0,1]]   matches expected

  ಇನ್ನೊಂದು example — tricky case (all same elements):
  Input: nums = [2, 2, 2, 2, 2], target = 8  → sorted: [2,2,2,2,2]

  i=0, j=1: L=2,R=4 → sum=2+2+2+2=8 == target → record [2,2,2,2]
            L++,R-- → L=3,R=3 → loop ends
  i=0, j=2..: nums[j]==nums[j-1] for all further j → all skipped
  i=1,2,..: nums[i]==nums[i-1] for all further i → all skipped

  Output: [[2,2,2,2]]   matches expected — only one unique quadruplet

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 9 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ n < 4?                       →  loop ranges become empty, return []
  ✓ All same elements?           →  duplicate-skip logic collapses to
                                     at most one quadruplet
  ✓ Negative numbers + target?   →  works unchanged, sorting handles sign
  ✓ Sum overflow (very large     →  use int64/Python's arbitrary
    values × 4)?                    precision ints; no wraparound risk
                                     in Python but matters in C++/Java
  ✓ Multiple valid quadruplets    →  duplicate-skip after a match (both
    sharing same L/R value?          L++ and R--) prevents re-recording

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 10 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                Time      Space
  Brute Force   O(n⁴)     O(n)   (dedup set)
  Better        O(n³)     O(n)   (hash-based 2Sum inner loop)
  Optimal       O(n³)     O(1)    ← use this (excluding sort/output)

  Time ಯಾಕೆ ಅಷ್ಟು?  → 2 nested loops O(n²) ಗೆ, ಪ್ರತಿ pair ಗೂ two-pointer
                        scan O(n) — total O(n³).
  Space ಯಾಕೆ ಅಷ್ಟು? → sort ಬಿಟ್ಟು, ಬರೀ pointers (i,j,L,R) ಮಾತ್ರ —
                        no hashing, no extra structures.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 11 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: k-Sum Reduction (Fix k-2, Two-Pointer the Rest)

  ಈ pattern ಯಾವಾಗ use ಮಾಡಬೇಕು?
  → "Find all unique groups of k numbers summing to target" ಥರ
    problem ಕೇಳಿದಾಗ (2Sum, 3Sum, 4Sum, kSum ಎಲ್ಲಾ ಇದೇ family)
  → Duplicates avoid ಮಾಡಬೇಕಾದಾಗ, sort ಮಾಡಿ adjacent skip logic
    use ಮಾಡಬಹುದು ಅಂತ ಗೊತ್ತಾದಾಗ
  → Nested-loop depth = k-2, ಕೊನೆಯ 2 numbers ಗೆ two-pointer ಅಂತ
    pattern ಗುರುತಿಸಿದಾಗ

  ಇದೇ pattern ಬೇರೆ problems ನಲ್ಲಿ ಕಾಣಿಸುತ್ತೆ:
  → 3Sum (LC 15) — same pattern one level shallower
  → 3Sum Closest (LC 16) — same two-pointer core, different objective
  → kSum (generalized, often solved recursively reducing to 2Sum base case)

  Next time ಇಂತಹ problem ಬಂದ್ರೆ ನಾನು ಮೊದಲು ಇದನ್ನ think ಮಾಡ್ತೇನೆ:
  → "kSum ಅಂದ್ರೆ, sort ಮಾಡಿ (k-2) numbers fix ಮಾಡಿ, ಕೊನೆಗೆ 2Sum ಗೆ
      two-pointer reduce ಮಾಡು ಅಂತ ಮೊದಲು ಯೋಚಿಸು."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 12 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "I need all unique quadruplets from the array that sum exactly to
      target, with no duplicate combinations in the output."

  2. Brute force:
     "Four nested loops checking every combination, deduped via a set
      — O(n⁴), too slow for n up to 200."

  3. Optimize:
     "This is the same reduction as 3Sum, one level deeper: sort the
      array, fix two numbers with nested loops, and two-pointer the
      remaining pair — turning the inner search into O(n) instead of
      nested loops or hashing."

  4. Code:
     "Sort nums. For each pair (i, j) with i<j, skipping duplicate
      values at each level, run a two-pointer scan L=j+1, R=n-1 over
      the sorted remainder, adjusting based on whether the four-sum is
      below or above target, and skipping duplicates after each match."

  5. Complexity:
     "Time O(n³) — two nested loops times a linear two-pointer scan.
      Space O(1) extra beyond the output and the sort."

  ಮುಖ್ಯ: ಸುಮ್ಮನೆ ಕೂತು code ಬರೆಯಬೇಡ!
         Interviewer ಗೆ ನಿನ್ನ thinking process ಕಾಣಬೇಕು.
"""


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(n^4) Time | O(n) Space  (4 Nested Loops + Set)
# ═══════════════════════════════════════════════════════════════════
def four_sum_brute(nums, target):
    """ಇದು ಮೊದಲ ಆಲೋಚನೆ — ಎಲ್ಲಾ combinations try ಮಾಡಿ set ಇಂದ dedupe ಮಾಡೋದು"""
    n = len(nums)
    seen = set()
    for a in range(n):
        for b in range(a + 1, n):
            for c in range(b + 1, n):
                for d in range(c + 1, n):
                    if nums[a] + nums[b] + nums[c] + nums[d] == target:
                        seen.add(tuple(sorted([nums[a], nums[b], nums[c], nums[d]])))
    return [list(t) for t in seen]


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n^3) Time | O(1) Extra Space  (Sort + Two Fixed Loops + Two-Pointer)
# ═══════════════════════════════════════════════════════════════════
def four_sum(nums, target):
    """ಇದು final answer — sort ಮಾಡಿ 2 numbers fix ಮಾಡಿ, ಉಳಿದೆರಡಕ್ಕೆ two-pointer"""
    n = len(nums)
    nums = sorted(nums)
    result = []

    for i in range(n - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, n - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue

            L, R = j + 1, n - 1
            while L < R:
                total = nums[i] + nums[j] + nums[L] + nums[R]
                if total == target:
                    result.append([nums[i], nums[j], nums[L], nums[R]])
                    L += 1
                    R -= 1
                    while L < R and nums[L] == nums[L - 1]:
                        L += 1
                    while L < R and nums[R] == nums[R + 1]:
                        R -= 1
                elif total < target:
                    L += 1
                else:
                    R -= 1

    return result


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")   # Windows cp1252 can't print emoji otherwise

    # Test 1 — Basic example
    assert sorted(four_sum([1, 0, -1, 0, -2, 2], 0)) == sorted(
        [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
    )

    # Test 2 — Edge case: fewer than 4 elements
    assert four_sum([1, 2, 3], 6) == []

    # Test 3 — Edge case: all same elements
    assert four_sum([2, 2, 2, 2, 2], 8) == [[2, 2, 2, 2]]

    # Test 4 — Tricky: negative numbers, no valid quadruplet
    assert four_sum([-3, -2, -1, 0, 0, 1, 2, 3], 100) == []

    print("All tests passed! ")
