"""
╔═══════════════════════════════════════════════════════════════════════╗
║  CONTAINS DUPLICATE                                                   ║
║  LeetCode #217  |  Difficulty: Easy  |  Topic: Arrays / Hashing       ║
║  Link: https://leetcode.com/problems/contains-duplicate/              ║
╚═══════════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : HashSet → Seen-Before Lookup
  Secondary : Sorting (alternative, no extra space for hashing)

  WHY HashSet?
  → The question is purely "does ANY value repeat?" — no indices,
    no pairing, just existence.
  → A HashSet gives O(1) average "have I seen this before?" checks,
    so a single pass answers the question in O(n).
  → Classic "seen-before" pattern — simpler cousin of the
    complement-lookup pattern used in Two Sum.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Given an integer array nums, return True if any value appears
  at least twice, and False if every element is distinct.

  Input : nums = [1, 2, 3, 1]
  Output: True
  Why?  : 1 appears at index 0 AND index 3

  Input : nums = [1, 2, 3, 4]
  Output: False
  Why?  : all elements are distinct

  Constraints:
    - 1 <= nums.length <= 10⁵
    - Values can repeat any number of times, order doesn't matter

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 HOW TO THINK (Intuition)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Brute force asks: "for every pair (i, j), are they equal?" → O(n²).

  Key question to move brute → optimal:
  "Do I actually need to compare every PAIR, or can I just remember
   what I've already visited and check membership as I go?"

  → Two ways to detect a repeat without pairwise comparison:
      1. Sort first → duplicates become ADJACENT → O(n log n)
      2. HashSet → O(1) avg membership check → O(n), trades space

  HashSet is preferred here since n is up to 10⁵ and O(n) beats
  O(n log n) — space is cheap, time matters more for large inputs.

  Even shorter Pythonic check: if len(set(nums)) < len(nums) → True.
  (A set auto-drops duplicates, so a size mismatch means duplicates
  existed.) This is the same idea, just written in one line.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 APPROACH 1 — BRUTE FORCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea: Compare every pair (i, j) where i ≠ j

  Pseudocode:
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] == nums[j] → return True
    return False

  Time  : O(n²)  — nested loops
  Space : O(1)   — no extra space

  Why not enough?
    → For n = 10⁵, that's ~10¹⁰ comparisons → TLE

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 APPROACH 2 — BETTER (Sort First)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea: Sort the array — duplicates land next to each other,
        then scan once checking nums[i] == nums[i-1]

  Time  : O(n log n)  — sorting dominates
  Space : O(1) extra  — if in-place sort allowed (O(n) if not)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 APPROACH 3 — OPTIMAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea: Single pass with a HashSet of values seen so far

  Key steps:
    1. seen = empty set
    2. For each num in nums:
         a. If num already in seen → return True (duplicate found)
         b. Otherwise, add num to seen
    3. If loop finishes with no match → return False

  Time  : O(n)  — single pass, O(1) avg set operations
  Space : O(n)  — set can hold up to n elements

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: nums = [1, 2, 3, 1]

  num=1   seen={}         1 not in seen → seen={1}
  num=2   seen={1}        2 not in seen → seen={1,2}
  num=3   seen={1,2}      3 not in seen → seen={1,2,3}
  num=1   seen={1,2,3}    1 IS in seen! → return True ✓

  Input: nums = [1, 2, 3, 4]

  num=1   seen={}         → seen={1}
  num=2   seen={1}        → seen={1,2}
  num=3   seen={1,2}      → seen={1,2,3}
  num=4   seen={1,2,3}    → seen={1,2,3,4}
  Loop ends, no match → return False ✓

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 EDGE CASES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ Single element: [1] → False (nothing to duplicate against)
  ✓ All same value: [5,5,5,5] → True
  ✓ Negative numbers: [-1,-2,-1] → True
  ✓ Duplicate at the very end: [1,2,3,4,4] → True
  ✓ Large distinct array → False, must scan fully (worst case for HashSet approach)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                Time        Space
  Brute Force   O(n²)       O(1)
  Sort First    O(n log n)  O(1)/O(n)
  Optimal       O(n)        O(n)    ← use this

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 PATTERN LEARNED
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  HashSet "Seen-Before" Lookup:
  → Whenever the question is pure EXISTENCE ("has this happened
    before?"), not pairing or counting, reach for a HashSet first —
    it's the simplest form of the HashMap complement-lookup pattern
    from Two Sum, minus the value you'd otherwise store.
  → This same "seen" pattern generalizes to: Longest Consecutive
    Sequence (#128), Happy Number, and cycle detection in graphs.
"""


# ─── BRUTE FORCE  O(n²) ───────────────────────────────────────────
def contains_duplicate_brute(nums):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] == nums[j]:
                return True
    return False


# ─── OPTIMAL  O(n) ────────────────────────────────────────────────
def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


# ─── TEST ─────────────────────────────────────────────────────────
if __name__ == "__main__":
    # Basic — duplicate exists
    print(contains_duplicate([1, 2, 3, 1]))        # True
    # No duplicates
    print(contains_duplicate([1, 2, 3, 4]))        # False
    # All same value
    print(contains_duplicate([5, 5, 5, 5]))        # True
    # Single element
    print(contains_duplicate([1]))                 # False
    # Negative numbers
    print(contains_duplicate([-1, -2, -1]))        # True
