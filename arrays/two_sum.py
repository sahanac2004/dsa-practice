"""
╔══════════════════════════════════════════════════════════════════╗
║  TWO SUM                                                         ║
║  LeetCode #1  |  Difficulty: Easy  |  Topic: Arrays / Hashing    ║
║  Link: https://leetcode.com/problems/two-sum/                    ║
╚══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : HashMap → Complement Lookup
  Secondary : —

  WHY HashMap?
  → For every number x, I need to find (target - x)
  → Instead of scanning the whole array again (O(n)),
    I can store what I've already seen in O(1) lookup
  → Trade space for time — classic HashMap pattern

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Given an array nums and a target, return indices of two numbers
  that add up to target. Exactly one solution exists.

  Input : nums = [2, 7, 11, 15], target = 9
  Output: [0, 1]
  Why?  : nums[0] + nums[1] = 2 + 7 = 9 ✓

  Constraints:
    - Exactly one valid answer always exists
    - Cannot use the same element twice (different indices)
    - 2 <= nums.length <= 10⁴

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 HOW TO THINK (Intuition)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  For every number x, the number I need is (target - x).
  
  Can I check every pair?         YES → O(n²) brute force
  Can I remember what I've seen?  YES → O(n) with HashMap

  Key insight:
  Instead of looking forward for the complement,
  look backward using a HashMap of what you've already visited.
  When you see a number, check if its complement already exists.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 APPROACH 1 — BRUTE FORCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea: Check every pair (i, j) where i ≠ j

  Pseudocode:
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] + nums[j] == target → return [i, j]

  Time  : O(n²)  — nested loops
  Space : O(1)   — no extra space

  Why not good enough?
    → For n = 10⁴, that's 10⁸ operations → TLE

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 APPROACH 2 — OPTIMAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea: HashMap {value: index} — single pass

  Key steps:
    1. For each number, compute complement = target - num
    2. Check if complement already in HashMap → found!
    3. If not, store current number in HashMap and move on

  Time  : O(n)  — single pass
  Space : O(n)  — HashMap stores up to n elements

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: nums = [2, 7, 11, 15], target = 9

  i=0  num=2   comp=7   seen={}          7 not in seen → seen={2:0}
  i=1  num=7   comp=2   seen={2:0}       2 IN seen! → return [0, 1] ✓

  Another: nums = [3, 2, 4], target = 6

  i=0  num=3   comp=3   seen={}          3 not in seen → seen={3:0}
  i=1  num=2   comp=4   seen={3:0}       4 not in seen → seen={3:0, 2:1}
  i=2  num=4   comp=2   seen={3:0,2:1}   2 IN seen! → return [1, 2] ✓

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 EDGE CASES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ Same value, different indices: [3,3], target=6 → [0,1] ✓
  ✓ Negative numbers: [-1,-2,-3,-4,-5], target=-8 → works fine
  ✓ Only 2 elements: [1,9], target=10 → [0,1]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                Time      Space
  Brute Force   O(n²)     O(1)
  Optimal       O(n)      O(n)    ← use this

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 PATTERN LEARNED
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  HashMap Complement Lookup:
  → Whenever you need to find a PAIR that satisfies a condition,
    think HashMap. Store what you've seen, look up its complement.
  → This same pattern appears in: 4Sum, subarray sum equals k, etc.
"""


# ─── BRUTE FORCE  O(n²) ───────────────────────────────────────────
def two_sum_brute(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]


# ─── OPTIMAL  O(n) ────────────────────────────────────────────────
def two_sum(nums, target):
    seen = {}   # {value: index}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i


# ─── TEST ─────────────────────────────────────────────────────────
if __name__ == "__main__":
    # Basic
    print(two_sum([2, 7, 11, 15], 9))   # [0, 1]
    # Different indices
    print(two_sum([3, 2, 4], 6))         # [1, 2]
    # Same value
    print(two_sum([3, 3], 6))            # [0, 1]
    # Negatives
    print(two_sum([-1, -2, -3, -4], -7)) # [2, 3]
