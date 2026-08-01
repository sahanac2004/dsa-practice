"""
╔══════════════════════════════════════════════════════════════════╗
║  ROTATE ARRAY                                                       ║
║  LeetCode #189  |  Difficulty: Medium  |  Topic: Arrays             ║
║  Link: https://leetcode.com/problems/rotate-array/                  ║
╚══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Given an array, rotate it to the right by k steps, in-place. Every
  element moves k positions to the right, wrapping around to the
  front when it goes past the end.

  Input : nums = [1,2,3,4,5,6,7], k = 3
  Output: [5,6,7,1,2,3,4]

  Example 1 — basic:
    Input : nums = [1,2,3,4,5,6,7], k = 3
    Output: [5,6,7,1,2,3,4]
    Why?  : the last 3 elements wrap around to the front

  Example 2 — slightly tricky (k larger than array length):
    Input : nums = [1,2], k = 3
    Output: [2,1]
    Why?  : rotating by 3 on a length-2 array is the same as rotating
             by 3 % 2 = 1

  Constraints:
    - 1 <= nums.length <= 10^5
    - -2^31 <= nums[i] <= 2^31 - 1
    - 0 <= k <= 10^5

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ಮೊದಲು problem odidaga ನಮ್ಮ brain ಏನು think ಮಾಡಬೇಕು:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ (What are they asking?)
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  array + k (rotate right count)  │
  │  Output ಏನು ಬೇಕು?     →  in-place ಆಗಿ right ಗೆ k ಸಲ       │
  │                          rotate ಮಾಡಿದ array               │
  │  Constraints ಏನಿದೆ?   →  n<=10^5, k n ಗಿಂತ ಜಾಸ್ತಿ ಆಗ್ಬೋದು │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ನನಗೆ ಗೊತ್ತಿರೋ simple way ಏನು? (Brute force thought)
  →  k ಸಲ, ಪ್ರತಿ ಸಲಾನೂ ಕೊನೆಯ element ಅನ್ನ ತೆಗೆದು ಮುಂದೆ insert
     ಮಾಡೋದು (one step rotation, repeated k times).
  →  ಆದರೆ ಇದು slow ಯಾಕೆ? → ಪ್ರತಿ rotation ಗೂ O(n) shift ಬೇಕು, k
     ಸಲ repeat ಮಾಡಿದ್ರೆ O(n*k) — k ಕೂಡ 10^5 ಆಗ್ಬೋದು, TLE.

  ಹಂತ 3 — Better way ಹೇಗೆ ಯೋಚಿಸುವುದು? (Optimization thought)
  →  Extra array ಇಟ್ಕೊಂಡು, ಪ್ರತಿ element ನ new position ಲೆಕ್ಕ ಹಾಕಿ
     ((i+k) % n) ನೇರ ಆಗಿ place ಮಾಡಿದ್ರೆ O(n) time ಸಿಗುತ್ತೆ, ಆದ್ರೆ
     O(n) extra space ಬೇಕಾಗುತ್ತೆ.
  →  ಅಹಾ moment: ಇನ್ ಪ್ಲೇಸ್ ಆಗಿ ಮಾಡೋಕೆ, "reversal trick" use
     ಮಾಡ್ಬೋದು! ಇಡೀ array ಅನ್ನ reverse ಮಾಡಿ, ಆಮೇಲೆ ಮೊದಲ k elements
     ಅನ್ನ reverse ಮಾಡಿ, ಉಳಿದ (n-k) elements ಅನ್ನ ಪ್ರತ್ಯೇಕ reverse
     ಮಾಡಿದ್ರೆ, exact rotation ಸಿಗುತ್ತೆ — extra array ಬೇಡ!
  →  ಇದರಿಂದ ನಾವು Reversal Trick (Reverse Whole, Then Reverse Parts)
     use ಮಾಡಬಹುದು!

  ಹಂತ 4 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  Whole array ಅನ್ನ reverse ಮಾಡಿದ್ರೆ, elements ಎಲ್ಲಾ ಸರಿಯಾದ
     "relative block" ಗಳಲ್ಲಿ ಇರ್ತಾವೆ ಆದ್ರೆ each block internally
     reversed ಆಗಿರುತ್ತೆ.
  →  ಆ ಎರಡು blocks (first k, ಮತ್ತು remaining n-k) ಅನ್ನ ಪ್ರತ್ಯೇಕ
     reverse ಮಾಡಿದ್ರೆ, ಆ blocks internally correct order ಗೆ ಬರುತ್ತೆ,
     ಆದ್ರೆ overall position ಸರಿಯಾಗೇ ಇರುತ್ತೆ (rotated).
  →  ಮೂರೂ reversals in-place ಆಗಿ O(1) extra space ನಲ್ಲಿ ಆಗುತ್ತೆ.

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು (Think out loud):
  →  "The naive way rotates one step at a time, k times — O(n*k),
      too slow when both n and k can be up to 10^5."
  →  "Using an extra array and placing each element at (i+k)%n gets
      O(n) time but O(n) space, which I can avoid."
  →  "The reversal trick does it in-place: reverse the whole array,
      then reverse the first k and the last n-k elements separately
      — that gives the exact right rotation with zero extra space."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Reversal Trick (Reverse Whole, Then Reverse Parts)
  Secondary : Modulo normalization (k %= n)

  WHY this technique?
  → Reversing the whole array, then reversing each of the two
    resulting blocks, produces exactly the rotated order — a well
    known in-place transformation
  → Avoids the O(n) auxiliary array needed by the direct placement
    approach, meeting the in-place requirement
  → k can exceed n, so normalizing with k %= n first avoids redundant
    full-cycle rotations

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION (How to think — English)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Key observation: rotating right by k is equivalent to swapping the
  positions of two blocks — the last k elements and the first n-k
  elements — while keeping each block's internal order. Reversing the
  whole array swaps the blocks' positions AND reverses each block's
  internal order; reversing each block again undoes just the internal
  reversal, leaving the blocks correctly swapped and internally
  correct — exactly the rotation.

  The journey from brute to optimal:
    Brute thought   →  rotate one step at a time, k times
    Problem with it →  O(n*k), way too slow for large n and k
    Better question →  "can I place every element directly at its
                        final position instead of shifting repeatedly?"
    Insight         →  reversing the whole array then reversing each
                        block undoes exactly the right thing, in-place
    Optimal         →  three reversals: whole, first k, last n-k;
                        O(n) time, O(1) space

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE (Rotate One Step, k Times)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Repeat k times: pop the last element and insert it at the front.

  Pseudocode:
    step 1: for _ in range(k):
    step 2:   last = nums.pop()
    step 3:   nums.insert(0, last)

  Time  : O(n*k)  →  Why: each pop/insert shifts up to n elements, repeated k times
  Space : O(1)    →  Why: no extra structures, just in-place shifts

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ? (Why is this not enough?)
    → n=10^5, k=10^5 ಆದ್ರೆ n*k = 10^10 — ಸಂಪೂರ್ಣ TLE.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚶 SECTION 6 — APPROACH 2 — BETTER (Extra Array, Direct Placement)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Normalize k %= n. Create a new array of size n, and for each
    index i, place nums[i] at position (i + k) % n. Copy the result
    back into nums.

  Time  : O(n)  →  one pass to fill the new array, one pass to copy back
  Space : O(n)  →  the auxiliary array of size n

  ಇನ್ನೂ better ಮಾಡಬಹುದಾ? → ಹೌದು — reversal trick ಇಂದ, extra array
  ಬೇಡ ಆಗುತ್ತೆ, O(1) space ಗೆ ಇಳಿಸ್ಬೋದು.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 7 — APPROACH 3 — OPTIMAL   (Reversal Trick)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Normalize k %= n (handles k >= n and k == 0 cleanly). Reverse the
    entire array. Then reverse the first k elements, and separately
    reverse the remaining n-k elements — all in-place.

  Key steps:
    1. k %= n
    2. reverse(nums, 0, n-1)
    3. reverse(nums, 0, k-1)
    4. reverse(nums, k, n-1)

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ (Say it once in Kanglish so it sticks):
    → "k = k % n ಮಾಡಿ (overflow avoid ಮಾಡೋಕೆ), ಇಡೀ array reverse
        ಮಾಡು, ಆಮೇಲೆ ಮೊದಲ k elements ಅನ್ನ reverse ಮಾಡು, ಕೊನೆಗೆ ಉಳಿದ
        n-k elements ಅನ್ನ reverse ಮಾಡು — rotation ready!"

  Time  : O(n)  →  Why: three reversals, each touching disjoint or full
                    ranges, total work bounded by O(n)
  Space : O(1)  →  Why: reversals done in-place with swaps

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 8 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: nums = [1,2,3,4,5,6,7], k = 3  (n=7)

  k %= n → k = 3 (unchanged, already < n)

  Step 1 — reverse whole array (0 to 6):
    [7,6,5,4,3,2,1]

  Step 2 — reverse first k=3 elements (0 to 2):
    [5,6,7,4,3,2,1]

  Step 3 — reverse remaining n-k=4 elements (3 to 6):
    [5,6,7,1,2,3,4]

  Output: [5,6,7,1,2,3,4]   matches expected

  ಇನ್ನೊಂದು example — tricky case (k larger than n):
  Input: nums = [1,2], k = 3  (n=2)

  k %= n → k = 3 % 2 = 1

  Step 1 — reverse whole array: [2,1]
  Step 2 — reverse first k=1 element: [2,1]  (single element, no change)
  Step 3 — reverse remaining n-k=1 element: [2,1]  (single element, no change)

  Output: [2,1]   matches expected

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 9 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ k == 0?                      →  after k %= n, first reversal
                                     range is empty — array stays
                                     unrotated (as expected)
  ✓ k == n (full cycle)?         →  k %= n makes it 0, no rotation,
                                     array unchanged
  ✓ k > n?                       →  k %= n normalizes it to the
                                     equivalent smaller rotation
  ✓ Single element array?        →  n=1, k %= 1 always 0, no-op
  ✓ n == k after modulo edge?    →  handled since k %= n guarantees
                                     0 <= k < n always

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 10 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                Time      Space
  Brute Force   O(n*k)    O(1)
  Better        O(n)      O(n)   (extra array)
  Optimal       O(n)      O(1)    ← use this

  Time ಯಾಕೆ ಅಷ್ಟು?  → ಮೂರು reversals, ಪ್ರತಿಯೊಂದೂ ಒಟ್ಟು n elements
                        ಗಿಂತ ಜಾಸ್ತಿ touch ಮಾಡಲ್ಲ — total O(n).
  Space ಯಾಕೆ ಅಷ್ಟು? → in-place swaps ಮಾತ್ರ, extra array ಬೇಡ.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 11 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Reversal Trick (Block Swap via Three Reversals)

  ಈ pattern ಯಾವಾಗ use ಮಾಡಬೇಕು?
  → "Rotate array in-place" ಥರ problem ಕೇಳಿದಾಗ
  → Two contiguous blocks ನ position swap ಮಾಡಬೇಕಾದಾಗ, extra space
    ಇಲ್ಲದೆ
  → In-place, O(1) space constraint ಇದ್ದಾಗ

  ಇದೇ pattern ಬೇರೆ problems ನಲ್ಲಿ ಕಾಣಿಸುತ್ತೆ:
  → Reverse Words in a String (LC 151) — same block-reversal idea
    applied to words
  → Left Rotate Array by One/D places — same trick, simpler case
  → Rotate List (Linked List, LC 61) — same rotation goal, different
    data structure (pointer manipulation instead of reversal)

  Next time ಇಂತಹ problem ಬಂದ್ರೆ ನಾನು ಮೊದಲು ಇದನ್ನ think ಮಾಡ್ತೇನೆ:
  → "'Rotate in-place' ಅಂತ ಕಂಡ ತಕ್ಷಣ, whole-reverse + part-reverse
      trick use ಮಾಡ್ಬೋದಾ ಅಂತ ಮೊದಲು ಯೋಚಿಸು, ಮತ್ತು k %= n ಮಾಡೋದನ್ನ
      ಮರೆಯಬೇಡ."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 12 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "I need to rotate the array right by k positions, in-place,
      wrapping elements around."

  2. Brute force:
     "Rotate one step at a time, k times — O(n*k), too slow when both
      n and k can be up to 10^5."

  3. Optimize:
     "Placing each element directly at (i+k)%n in a new array gets
      O(n) time but needs O(n) extra space. The reversal trick avoids
      that: reverse the whole array, then reverse the two resulting
      blocks separately — that's exactly the rotation, in-place."

  4. Code:
     "Normalize k %= n first. Reverse the whole array, then reverse
      the first k elements, then reverse the remaining n-k elements."

  5. Complexity:
     "Time O(n) — three linear reversals. Space O(1) — everything
      happens via in-place swaps."

  ಮುಖ್ಯ: ಸುಮ್ಮನೆ ಕೂತು code ಬರೆಯಬೇಡ — always think out loud!
         Interviewer ಗೆ ನಿನ್ನ thinking process ಕಾಣಬೇಕು.
"""


def _reverse(nums, left, right):
    """ಒಂದು helper — nums[left..right] ಅನ್ನ in-place reverse ಮಾಡುತ್ತೆ"""
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(n*k) Time | O(1) Space  (Rotate One Step, k Times)
# ═══════════════════════════════════════════════════════════════════
def rotate_brute(nums, k):
    """ಇದು ಮೊದಲ ಆಲೋಚನೆ — ಕೊನೆಯ element ಅನ್ನ ಮುಂದೆ ತರೋದು, k ಸಲ repeat"""
    for _ in range(k):
        last = nums.pop()
        nums.insert(0, last)
    return nums


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n) Time | O(1) Space  (Reversal Trick)
# ═══════════════════════════════════════════════════════════════════
def rotate(nums, k):
    """ಇದು final answer — whole array reverse ಮಾಡಿ, ಆಮೇಲೆ ಎರಡು blocks ಪ್ರತ್ಯೇಕ reverse ಮಾಡು"""
    n = len(nums)
    k %= n
    if k == 0:
        return nums

    _reverse(nums, 0, n - 1)
    _reverse(nums, 0, k - 1)
    _reverse(nums, k, n - 1)
    return nums


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")   # Windows cp1252 can't print emoji otherwise

    # Test 1 — Basic example
    assert rotate([1, 2, 3, 4, 5, 6, 7], 3) == [5, 6, 7, 1, 2, 3, 4]

    # Test 2 — Edge case: k larger than array length
    assert rotate([1, 2], 3) == [2, 1]

    # Test 3 — Edge case: k == 0 (no rotation)
    assert rotate([1, 2, 3], 0) == [1, 2, 3]

    # Test 4 — Edge case: k == n (full cycle, unchanged)
    assert rotate([1, 2, 3], 3) == [1, 2, 3]

    # Test 5 — Tricky: single element array
    assert rotate([1], 5) == [1]

    print("All tests passed! ")
