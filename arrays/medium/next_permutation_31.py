"""
╔════════════════════════════════════════════════════════════════════╗
║  NEXT PERMUTATION                                                  ║
║  LeetCode #31  |  Difficulty: Medium  |  Topic: Arrays             ║
║  Link: https://leetcode.com/problems/next-permutation/             ║
╚════════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  A permutation of an array is one of its orderings. "Next
  permutation" means the next ordering in lexicographic (dictionary)
  order — the smallest ordering that is strictly greater than the
  current one. If the current ordering is already the largest
  possible, wrap around to the smallest (fully sorted ascending).
  Must be done in-place with O(1) extra space.

  Input : nums = [1, 2, 3]
  Output: [1, 3, 2]

  Example 1 — basic:
    Input : nums = [1, 2, 3]
    Output: [1, 3, 2]
    Why?  : the very next lexicographic arrangement after 1,2,3

  Example 2 — slightly tricky (already the largest permutation):
    Input : nums = [3, 2, 1]
    Output: [1, 2, 3]
    Why?  : no bigger arrangement exists, so wrap to the smallest one

  Constraints:
    - 1 <= nums.length <= 100
    - 0 <= nums[i] <= 100

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ಮೊದಲು problem odidaga ನಮ್ಮ brain ಏನು think ಮಾಡಬೇಕು:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ (What are they asking?)
  ┌───────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  ಒಂದು array of numbers           │
  │  Output ಏನು ಬೇಕು?     →  next lexicographically greater  │
  │                          arrangement, in-place            │
  │  Constraints ಏನಿದೆ?   →  n<=100, O(1) extra space ಬೇಕು    │
  └───────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ನನಗೆ ಗೊತ್ತಿರೋ simple way ಏನು? (Brute force thought)
  →  ಎಲ್ಲಾ possible permutations generate ಮಾಡಿ, sort ಮಾಡಿ, current
     permutation ಎಲ್ಲಿ ಇದೆ ಅಂತ ಹುಡುಕಿ, ಅದರ ಮುಂದಿನದನ್ನ return ಮಾಡೋದು.
  →  ಆದರೆ ಇದು slow ಯಾಕೆ? → n! permutations generate ಮಾಡೋದೇ
     insane — n=100 ಆದ್ರೆ impossible.

  ಹಂತ 3 — Better way ಹೇಗೆ ಯೋಚಿಸುವುದು? (Optimization thought)
  →  "Next permutation" ಅಂದ್ರೆ, right side ನಿಂದ ಸಾಧ್ಯವಾದಷ್ಟು ಕಡಿಮೆ
     digits change ಮಾಡಿ, ಆದ್ರೆ overall value ಸ್ವಲ್ಪ ಜಾಸ್ತಿ ಆಗಬೇಕು.
  →  ಅಹಾ moment: ಬಲಗಡೆ ಇಂದ ನೋಡ್ತಾ ಹೋದ್ರೆ, ಎಲ್ಲಿ decreasing sequence
     ಮುಗಿತ್ತೋ (ಅಂದ್ರೆ nums[i] < nums[i+1] ಸಿಗುತ್ತೋ), ಅಲ್ಲಿ ಆ pivot ಅನ್ನ
     ಸ್ವಲ್ಪ ಜಾಸ್ತಿ ಇರೋ ಒಂದು number ಜೊತೆ swap ಮಾಡಿ, ಅದರ ಬಲಗಡೆ ಇರೋದನ್ನ
     ascending order ಗೆ reverse ಮಾಡಿದ್ರೆ ಸಾಕು — ಅದೇ next permutation!
  →  ಇದರಿಂದ ನಾವು Two-Pointer + In-place Rearrangement (Pivot-Swap-
     Reverse) use ಮಾಡಬಹುದು!

  ಹಂತ 4 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  ಬಲಗಡೆ ಇಂದ suffix ಯಾವಾಗ decreasing ಆಗಿರುತ್ತೋ, ಅದು ಆಗಲೇ "largest
     arrangement of that suffix" ಆಗಿರುತ್ತೆ — ಅದನ್ನ change ಮಾಡೋಕೆ
     ಆಗಲ್ಲ, ಅದರ ಎಡಗಡೆ ಇರೋ pivot ಅನ್ನೇ ಬದಲಾಯಿಸಬೇಕು.
  →  Pivot ಅನ್ನ, ಅದಕ್ಕಿಂತ ಜಾಸ್ತಿ ಇರೋ suffix ನ smallest number ಜೊತೆ
     swap ಮಾಡಿದ್ರೆ, minimum possible increase ಆಗುತ್ತೆ.
  →  Swap ಆದ ಮೇಲೆ suffix ಇನ್ನೂ decreasing ಆಗಿರುತ್ತೆ (largest), ಅದನ್ನ
     reverse ಮಾಡಿದ್ರೆ ascending (smallest) ಆಗುತ್ತೆ — overall smallest
     possible increase ಸಿಗುತ್ತೆ.

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು (Think out loud):
  →  "The naive way generates all permutations and finds the next one
      in sorted order — factorial time, useless for n up to 100."
  →  "I notice that scanning from the right, the longest suffix that's
      already decreasing can't be rearranged to something bigger — so
      I need to find where that decreasing run breaks."
  →  "Once I find that breakpoint, I swap it with the smallest
      element in the suffix that's still bigger than it, then reverse
      the suffix to make it the smallest possible — giving the
      overall next permutation."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Two-Pointer → Pivot-Swap-Reverse (In-place Rearrangement)
  Secondary : None

  WHY this technique?
  → "Next lexicographic arrangement" always breaks at the rightmost
    point where the sequence stops decreasing — a fixed, findable pivot
  → Swapping the pivot with the smallest larger element in the suffix
    guarantees the minimum possible increase
  → Reversing the suffix afterward converts it from "largest" (still
    descending) to "smallest" (ascending), completing the minimal step

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION (How to think — English)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Key observation: a strictly decreasing suffix is already the LARGEST
  arrangement of those elements — there's no way to rearrange it to
  something bigger. So the "increase" must come from the element just
  before that suffix (the pivot). Swap the pivot with the smallest
  suffix element still bigger than it, then reverse the suffix to make
  it ascending (smallest) — that's the minimal possible bump upward.

  The journey from brute to optimal:
    Brute thought   →  generate all permutations, sort, find next
    Problem with it →  O(n!) time and space, totally infeasible
    Better question →  "where does the array stop being able to grow
                        just by rearranging the tail?"
    Insight         →  find rightmost pivot i where nums[i] < nums[i+1];
                        everything after i is already maximal
    Optimal         →  swap pivot with smallest larger suffix element,
                        reverse the suffix

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE (Generate All Permutations)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Generate every permutation of nums, sort them lexicographically,
    locate the current one, and return the one right after it (or the
    first one if current is last).

  Pseudocode:
    step 1: perms = sorted(all permutations of nums)
    step 2: idx = perms.index(tuple(nums))
    step 3: return perms[(idx + 1) % len(perms)]

  Time  : O(n! * n log n)  →  Why: n! permutations, each compared while sorting
  Space : O(n! * n)        →  Why: storing every permutation

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ? (Why is this not enough?)
    → n=100 ಆದ್ರೆ 100! permutations — universe ನಲ್ಲಿ ಇರೋ atoms ಗಿಂತ
      ಜಾಸ್ತಿ! ಸಂಪೂರ್ಣ infeasible.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚶 SECTION 6 — APPROACH 2 — BETTER (if exists)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    No meaningful middle ground here — the moment you spot the pivot
    insight, you go straight to the O(n) in-place approach. There
    isn't a natural "polynomial but not optimal" middle step like
    prefix/suffix arrays for this problem.

  Time  : —
  Space : —

  ಇನ್ನೂ better ಮಾಡಬಹುದಾ? → ಇದೇ optimal, directly SECTION 7 ಗೆ ಹೋಗೋಣ.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 7 — APPROACH 3 — OPTIMAL   (Pivot — Swap — Reverse)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Scan from the right to find the first index i where
    nums[i] < nums[i+1] (the pivot). If none exists, the whole array
    is descending — reverse it entirely (wrap to smallest). Otherwise,
    scan from the right again to find the smallest element greater
    than nums[i], swap them, then reverse everything after index i.

  Key steps:
    1. i = n - 2; while i >= 0 and nums[i] >= nums[i+1]: i -= 1
    2. if i == -1: reverse(nums, 0, n-1); return  # was fully descending
    3. j = n - 1; while nums[j] <= nums[i]: j -= 1
    4. swap(nums[i], nums[j])
    5. reverse(nums, i+1, n-1)

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ (Say it once in Kanglish so it sticks):
    → "ಬಲಗಡೆ ಇಂದ ಎಡಗಡೆಗೆ ಹೋಗ್ತಾ, ಎಲ್ಲಿ nums[i] < nums[i+1] ಸಿಗುತ್ತೋ
        ಅದೇ pivot i. ಅದು ಸಿಗ್ದೇ ಇದ್ರೆ, whole array reverse ಮಾಡಿ ಬಿಡು.
        ಸಿಕ್ಕಿದ್ರೆ, ಬಲಗಡೆ ಇಂದ nums[i] ಗಿಂತ ಸ್ವಲ್ಪ ಜಾಸ್ತಿ ಇರೋ ಮೊದಲ
        number j ಹುಡುಕಿ swap ಮಾಡು, ಆಮೇಲೆ i+1 ಇಂದ ಕೊನೆ ತನಕ reverse
        ಮಾಡು — next permutation ready!"

  Time  : O(n)  →  Why: two linear scans (find pivot, find swap target) + one reverse
  Space : O(1)  →  Why: in-place swaps and reversal, no extra structures

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 8 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: nums = [1, 2, 3]  (n=3)

  Find pivot: i=1 → nums[1]=2, nums[2]=3, 2<3 → pivot found at i=1
  Find swap target: j=2 → nums[2]=3 > nums[1]=2 → j=2
  Swap nums[1] and nums[2] → [1, 3, 2]
  Reverse suffix from i+1=2 to end (single element, no change) → [1, 3, 2]

  Output: [1, 3, 2]   matches expected

  ಇನ್ನೊಂದು example — tricky case (fully descending):
  Input: nums = [3, 2, 1]

  Find pivot: i=1 → nums[1]=2, nums[2]=1, 2>=1 → i-- → i=0 → nums[0]=3,
              nums[1]=2, 3>=2 → i-- → i=-1 → no pivot found
  Whole array is descending → reverse entirely → [1, 2, 3]

  Output: [1, 2, 3]   matches expected (wrapped to smallest)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 9 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ Single element array?        →  no pivot possible (i starts at -1
                                     range), falls to full reverse (no-op)
  ✓ Already the largest perm?    →  no pivot found → reverse whole
                                     array → wraps to smallest
  ✓ All duplicate elements?      →  pivot search uses >=, so duplicates
                                     never falsely mark a pivot; reverses
                                     correctly to a no-op
  ✓ Two elements?                →  simple swap if ascending, reverse
                                     if descending
  ✓ Only the last two differ?    →  pivot found right at n-2, minimal
                                     swap + reverse handles it directly

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 10 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                Time         Space
  Brute Force   O(n! n log n) O(n! n)
  Optimal       O(n)          O(1)    ← use this

  Time ಯಾಕೆ ಅಷ್ಟು?  → pivot ಹುಡುಕೋಕೆ ಒಂದು pass, swap target ಹುಡುಕೋಕೆ
                        ಒಂದು pass, reverse ಗೆ ಒಂದು pass — all linear.
  Space ಯಾಕೆ ಅಷ್ಟು? → in-place swap ಮತ್ತು reverse ಮಾತ್ರ, extra array ಬೇಡ.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 11 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Pivot-Swap-Reverse (In-place Lexicographic Step)

  ಈ pattern ಯಾವಾಗ use ಮಾಡಬೇಕು?
  → "Next/previous lexicographic permutation" ಥರ problem ಕೇಳಿದಾಗ
  → Decreasing/increasing suffix ಬಗ್ಗೆ ಯೋಚಿಸಬೇಕಾದಾಗ ("this part is
    already maximal/minimal, so it can't help")
  → In-place, O(1) space constraint ಇದ್ದಾಗ

  ಇದೇ pattern ಬೇರೆ problems ನಲ್ಲಿ ಕಾಣಿಸುತ್ತೆ:
  → Previous Permutation (mirror logic, increasing suffix instead)
  → Permutation Sequence (LC 60) — related permutation-ordering family
  → Rearrange array elements by sign — different, but same "in-place
    rearrangement with pointers" family

  Next time ಇಂತಹ problem ಬಂದ್ರೆ ನಾನು ಮೊದಲು ಇದನ್ನ think ಮಾಡ್ತೇನೆ:
  → "ಬಲಗಡೆ ಇಂದ decreasing suffix ಎಲ್ಲಿ ಮುಗಿತ್ತೋ ಅಲ್ಲಿ pivot ಇದೆ ಅಂತ
      ಮೊದಲು ಹುಡುಕು — ಅದೇ key to next permutation."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 12 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "I need to rearrange the array in-place into the next
      lexicographically greater permutation, or wrap to the smallest
      if it's already the largest."

  2. Brute force:
     "Generate all permutations and find the next one — factorial
      time and space, completely infeasible even for n=20."

  3. Optimize:
     "Scanning from the right, a decreasing run is already maximal for
      those positions — I can't get a bigger arrangement there. So I
      look for the pivot just before that run breaks."

  4. Code:
     "Find the rightmost pivot i where nums[i] < nums[i+1]. If none
      exists, reverse the whole array. Otherwise, find the smallest
      element to the right of i that's still bigger than nums[i], swap
      them, then reverse everything after i."

  5. Complexity:
     "Time O(n) — a constant number of linear passes. Space O(1) —
      everything happens in-place with swaps and reversal."

  ಮುಖ್ಯ: ಸುಮ್ಮನೆ ಕೂತು code ಬರೆಯಬೇಡ — always think out loud!
         Interviewer ಗೆ ನಿನ್ನ thinking process ಕಾಣಬೇಕು.
"""


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n) Time | O(1) Space  (Pivot — Swap — Reverse)
# ═══════════════════════════════════════════════════════════════════
def next_permutation(nums):
    """ಇದು final answer — pivot ಹುಡುಕಿ, swap ಮಾಡಿ, suffix reverse ಮಾಡು (in-place)"""
    n = len(nums)

    # Step 1: find the rightmost pivot where the sequence stops decreasing
    i = n - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1

    if i == -1:
        # Fully descending — this was the largest permutation, wrap to smallest
        nums.reverse()
        return nums

    # Step 2: find the smallest element to the right of i that's still > nums[i]
    j = n - 1
    while nums[j] <= nums[i]:
        j -= 1

    # Step 3: swap pivot with that element
    nums[i], nums[j] = nums[j], nums[i]

    # Step 4: reverse the suffix after i to make it the smallest arrangement
    nums[i + 1:] = reversed(nums[i + 1:])
    return nums


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")   # Windows cp1252 can't print emoji otherwise

    # Test 1 — Basic example
    assert next_permutation([1, 2, 3]) == [1, 3, 2]

    # Test 2 — Edge case: single element
    assert next_permutation([1]) == [1]

    # Test 3 — Edge case: already the largest permutation (wrap around)
    assert next_permutation([3, 2, 1]) == [1, 2, 3]

    # Test 4 — Tricky: duplicates present
    assert next_permutation([1, 1, 5]) == [1, 5, 1]

    # Test 5 — Tricky: only last two differ
    assert next_permutation([1, 3, 2]) == [2, 1, 3]

    print("All tests passed! ")
