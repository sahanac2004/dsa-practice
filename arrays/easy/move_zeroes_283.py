"""
╔══════════════════════════════════════════════════════════════════╗
║  MOVE ZEROES                                                     ║
║  LeetCode #283  |  Difficulty: Easy  |  Topic: Arrays / Two Pointers ║
║  Link: https://leetcode.com/problems/move-zeroes/                ║
╚══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ಮೊದಲು problem odidaga ನಮ್ಮ brain ಏನು think ಮಾಡಬೇಕು:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ (What are they asking?)
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  numbers array (0 ಗಳು ಸಹಿತ)    │
  │  Output ಏನು ಬೇಕು?     →  ಎಲ್ಲಾ 0 ಗಳನ್ನ ಕೊನೆಗೆ push      │
  │                          ಮಾಡಿ, ಉಳಿದ numbers order         │
  │                          ಹಾಗೇ ಇಟ್ಕೊಬೇಕು                  │
  │  Constraints ಏನಿದೆ?   →  IN-PLACE ಮಾಡ್ಬೇಕು, extra        │
  │                          array ಬಳಸೋ ಹಾಗಿಲ್ಲ                │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ನನಗೆ ಗೊತ್ತಿರೋ simple way ಏನು? (Brute force thought)
  →  ಎಲ್ಲಾ non-zero values ಅನ್ನ ಒಂದು ಹೊಸ list ಗೆ ಹಾಕಿ, ಆಮೇಲೆ
     0 ಗಳಿಂದ pad ಮಾಡಿ, ಆ list ಅನ್ನ ಮೂಲ array ಗೆ copy ಮಾಡೋದು.
  →  ಆದರೆ ಇದು ಯಾಕೆ enough ಅಲ್ಲ? → extra O(n) space ಬಳಸ್ತೀವಿ,
     ಆದ್ರೆ problem in-place, O(1) space ಕೇಳ್ತಿದೆ.

  ಹಂತ 3 — Better way ಹೇಗೆ ಯೋಚಿಸುವುದು? (Optimization thought)
  →  "ನಾನು ಒಂದು 'write' pointer ಇಟ್ಕೊಂಡು, next non-zero ಎಲ್ಲಿ
     ಹೋಗಬೇಕು ಅಂತ track ಮಾಡಿದ್ರೆ, ಒಂದೇ pass ಲ್ಲಿ in-place ಮಾಡಕ್ಕಾಗುತ್ತಾ?"
  →  ಅಹಾ moment: read pointer ಯಾವಾಗ non-zero ಕಂಡ್ರೂ, ಅದನ್ನ write
     pointer position ಜೊತೆ swap ಮಾಡಿ write++ ಮಾಡಿದ್ರೆ, zeros
     automatic ಆಗಿ ಬಲಕ್ಕೆ ಹೋಗ್ತಾವೆ.
  →  ಇದರಿಂದ ನಾವು Two Pointers Same-Direction Partition use ಮಾಡಬಹುದು!

  ಹಂತ 4 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  In-place, O(1) space ಬೇಕು ಅನ್ನೋ constraint ಸ್ಟ್ರಾಂಗ್ signal —
     two pointers ಇಲ್ಲಿ classic fit.
  →  Relative order preserve ಮಾಡ್ಬೇಕು ಅಂದ್ರೆ, swap use ಮಾಡಿದ್ರೆ
     order ಕೆಡಲ್ಲ.
  →  write pointer ಯಾವಾಗ್ಲೂ "ಮುಂದಿನ correct position" ಅನ್ನ
     represent ಮಾಡುತ್ತೆ.

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು (Think out loud):
  →  "So I need to push zeros to the end while keeping non-zero
      order, in-place."
  →  "The brute force builds a new array — O(n) extra space."
  →  "I notice I can use a write pointer that only advances on
      non-zero values, swapping as I scan — that's O(1) space."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Two Pointers → Same Direction (Partition Style)
  Secondary : In-place swap

  WHY this technique?
  → Must be done IN-PLACE with no extra array
  → `write` pointer marks where the next non-zero should go,
    `read` pointer scans forward looking for non-zeros
  → Same partition skeleton as Remove Duplicates (#26), Sort Colors

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Given an array nums, move all 0's to the end while maintaining
  the RELATIVE ORDER of the non-zero elements. Must be in-place.

  Input : nums = [0, 1, 0, 3, 12]
  Output: [1, 3, 12, 0, 0]

  Example 1 — basic:
    Input : nums = [0, 1, 0, 3, 12]
    Output: [1, 3, 12, 0, 0]
    Why?  : non-zeros (1, 3, 12) keep their relative order

  Example 2 — slightly tricky:
    Input : nums = [0, 0, 1]
    Output: [1, 0, 0]
    Why?  : the single non-zero moves all the way to the front

  Constraints:
    - Must modify nums in-place (no returning a new array)
    - Relative order of non-zero elements must be preserved

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 INTUITION (How to think)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Can I overwrite the array as I scan, using one pointer to track
  where the NEXT non-zero belongs?

  The journey from brute to optimal:
    Brute thought   →  build a new list of non-zeros, pad with 0s
    Problem with it →  O(n) extra space, violates in-place
    Better question →  "can write and read pointers do this in one pass?"
    Insight         →  swap non-zero into write position, advance write
    Optimal         →  two pointers, same direction, O(1) space

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 APPROACH 1 — BRUTE FORCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Collect non-zeros into a new list, then append zeros.

  Pseudocode:
    step 1: result = [x for x in nums if x != 0]
    step 2: result += [0] * (len(nums) - len(result))
    step 3: nums[:] = result

  Time  : O(n)  →  Why: one pass to filter, one to pad
  Space : O(n)  →  Why: extra array used

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ? (Why is this not enough?)
    → Problem explicitly ಕೇಳ್ತಿದೆ in-place, O(1) extra space.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚶 APPROACH 2 — BETTER (skip — brute jumps straight to optimal)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ಇಲ್ಲಿ intermediate approach ಇಲ್ಲ — write/read pointer insight
  ಸಿಕ್ಕ ತಕ್ಷಣ ನೇರವಾಗಿ in-place optimal ಗೆ ಹೋಗಬಹುದು.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 APPROACH 3 — OPTIMAL  
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Two pointers, same direction, swap non-zeros into place.

  Key steps:
    1. write = 0  (position where next non-zero should land)
    2. For read in range(n):
         if nums[read] != 0:
             swap(nums[read], nums[write])
             write += 1
    3. Array is now correctly partitioned in-place

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ (Say it once in Kanglish so it sticks):
    → "read pointer ಅನ್ನ full array ಮೇಲೆ ಓಡಿಸು. ಎಲ್ಲಿ non-zero
        ಸಿಗುತ್ತೋ ಅಲ್ಲಿ, ಅದನ್ನ write pointer position ಜೊತೆ swap
        ಮಾಡಿ write++ ಮಾಡು. Zero ಗಳು naturally ಬಲಕ್ಕೆ ಸರಿತಾವೆ."

  Time  : O(n)  →  Why: single pass
  Space : O(1)  →  Why: in-place swaps only

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: nums = [0, 1, 0, 3, 12]

  write=0
  read=0  →  nums[0]=0 → skip
  read=1  →  nums[1]=1 → swap(nums[1],nums[0]) → [1,0,0,3,12], write=1
  read=2  →  nums[2]=0 → skip
  read=3  →  nums[3]=3 → swap(nums[3],nums[1]) → [1,3,0,0,12], write=2
  read=4  →  nums[4]=12 → swap(nums[4],nums[2]) → [1,3,12,0,0], write=3

  Output: [1, 3, 12, 0, 0]

  ಇನ್ನೊಂದು example — tricky case:
  Input: nums = [0, 0, 1]
  write=0
  read=0  nums[0]=0 → skip
  read=1  nums[1]=0 → skip
  read=2  nums[2]=1 → swap(nums[2],nums[0]) → [1,0,0], write=1
  Output: [1, 0, 0]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ All zeros?               →  [0,0,0] → [0,0,0] (no change needed)
  ✓ No zeros?                →  [1,2,3] → [1,2,3] (write chases read every step)
  ✓ Single element?          →  [0] → [0]
  ✓ Zeros already at end?    →  [1,2,0,0] → [1,2,0,0] (no-op swaps)
  ✓ Zero only at the start?  →  [0,1,2] → [1,2,0]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                Time      Space
  Brute Force   O(n)      O(n)
  Optimal       O(n)      O(1)    ← use this  

  Time ಯಾಕೆ O(n)?  → Array ಒಮ್ಮೆ ಮಾತ್ರ traverse ಮಾಡ್ತೇವೆ.
  Space ಯಾಕೆ O(1)? → write, read ಎರಡು pointer variables ಸಾಕು.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Two Pointers — Same Direction Write/Read Partition

  ಈ pattern ಯಾವಾಗ use ಮಾಡಬೇಕು?
  → Array ಅನ್ನ IN-PLACE reorder ಮಾಡ್ಬೇಕಾದ್ರೆ (condition ಪ್ರಕಾರ
    ಒಂದನ್ನ ಇಟ್ಕೊಂಡು, ಇನ್ನೊಂದನ್ನ ದೂರ ಮಾಡ್ಬೇಕಾದ್ರೆ)
  → Relative order preserve ಮಾಡ್ಬೇಕಾದಾಗ

  ಇದೇ pattern ಬೇರೆ problems ನಲ್ಲಿ ಕಾಣಿಸುತ್ತೆ:
  → Remove Duplicates from Sorted Array (#26)
  → Remove Element
  → Sort Colors (#75, extended to 3-way partition)

  Next time ಇಂತಹ problem ಬಂದ್ರೆ ನಾನು ಮೊದಲು ಇದನ್ನ think ಮಾಡ್ತೇನೆ:
  → "In-place reorder + preserve order ಕೇಳಿದ್ರೆ, write/read
      pointer partition ಮೊದಲು ಯೋಚಿಸು."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ INTERVIEW ನಲ್ಲಿ ಹೇಗೆ EXPLAIN ಮಾಡಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "So I need to push all zeros to the end, in-place, while
      keeping the relative order of non-zero elements."

  2. Brute force:
     "The naive approach builds a new array of non-zeros then
      pads with zeros — O(n) extra space, but the problem wants
      in-place."

  3. Optimize:
     "I can use a write pointer for where the next non-zero
      should go, and a read pointer that scans the whole array,
      swapping non-zeros into place."

  4. Code:
     "Whenever nums[read] != 0, I swap it with nums[write] and
      advance write."

  5. Complexity:
     "Time O(n) — one pass. Space O(1) — in-place swaps only."

  ಮುಖ್ಯ: ಸುಮ್ಮನೆ ಕೂತು code ಬರೆಯಬೇಡ!
         Interviewer ಗೆ ನಿನ್ನ thinking process ಕಾಣಬೇಕು.
"""


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(n) Time | O(n) Space
# ═══════════════════════════════════════════════════════════════════
def move_zeroes_brute(nums):
    """ಇದು ಮೊದಲ ಆಲೋಚನೆ — new list build ಮಾಡಿ copy back, extra space"""
    non_zeros = [x for x in nums if x != 0]
    non_zeros += [0] * (len(nums) - len(non_zeros))
    nums[:] = non_zeros
    return nums


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n) Time | O(1) Space
# ═══════════════════════════════════════════════════════════════════
def move_zeroes(nums):
    """ಇದು final answer — write/read pointer in-place swap"""
    write = 0
    for read in range(len(nums)):
        if nums[read] != 0:
            nums[read], nums[write] = nums[write], nums[read]
            write += 1
    return nums


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")   # Windows cp1252 can't print   otherwise

    # Test 1 — Basic example
    assert move_zeroes([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]

    # Test 2 — Edge case: all zeros
    assert move_zeroes([0, 0, 0]) == [0, 0, 0]

    # Test 3 — Edge case: no zeros
    assert move_zeroes([1, 2, 3]) == [1, 2, 3]

    # Test 4 — Tricky: zero only at start
    assert move_zeroes([0, 1, 2]) == [1, 2, 0]

    print("All tests passed!  ")
