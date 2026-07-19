"""
╔══════════════════════════════════════════════════════════════════╗
║  REMOVE DUPLICATES FROM SORTED ARRAY                             ║
║  LeetCode #26  |  Difficulty: Easy  |  Topic: Arrays / Two Pointers ║
║  Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/ ║
╚══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ಮೊದಲು problem odidaga ನಮ್ಮ brain ಏನು think ಮಾಡಬೇಕು:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ (What are they asking?)
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  SORTED array, duplicates ಇರೋದು │
  │  Output ಏನು ಬೇಕು?     →  unique elements count k, ಮತ್ತು  │
  │                          array ನ ಮೊದಲ k slots ಲ್ಲಿ ಅವೇ    │
  │  Constraints ಏನಿದೆ?   →  IN-PLACE, O(1) extra space      │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ನನಗೆ ಗೊತ್ತಿರೋ simple way ಏನು? (Brute force thought)
  →  ಒಂದು set ಗೆ ಎಲ್ಲಾ unique values ಸೇರಿಸಿ, ಸಾರ್ಟ್ ಮಾಡಿ,
     ಮೂಲ array ಗೆ copy ಮಾಡೋದು.
  →  ಆದರೆ ಇದು ಯಾಕೆ enough ಅಲ್ಲ? → extra space ಬೇಕಾಗುತ್ತೆ, array
     ಈಗಾಗಲೇ sorted ಇರೋ advantage ಬಳಸ್ತಿಲ್ಲ.

  ಹಂತ 3 — Better way ಹೇಗೆ ಯೋಚಿಸುವುದು? (Optimization thought)
  →  "Array ಈಗಾಗಲೇ sorted ಇದೆ ಅಂದ್ರೆ, duplicates ಯಾವಾಗ್ಲೂ
     ADJACENT ಆಗಿ ಇರ್ತಾವಲ್ಲ? ಹಾಗಾದ್ರೆ set ಯಾಕೆ ಬೇಕು?"
  →  ಅಹಾ moment: ಪ್ರತಿ number ಅನ್ನ ಕೊನೆಯ WRITTEN unique value
     ಜೊತೆ ಮಾತ್ರ compare ಮಾಡಿದ್ರೆ ಸಾಕು — ಬೇರೆ ಎಲ್ಲೂ ಹೋಲಿಸೋ
     ಅಗತ್ಯ ಇಲ್ಲ.
  →  ಇದರಿಂದ ನಾವು Two Pointers Same-Direction (compare-to-last-written)
     use ಮಾಡಬಹುದು!

  ಹಂತ 4 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  Array SORTED ಆಗಿರೋದ್ರಿಂದ duplicates adjacent ಆಗಿರ್ತಾವೆ —
     hashset ಬೇಕಿಲ್ಲ.
  →  In-place, O(1) space constraint ಇರೋದ್ರಿಂದ, write/read
     two-pointer skeleton ಮತ್ತೆ perfect fit.
  →  Order preserve ಮಾಡ್ಬೇಕು ಅಂದ್ರೂ ಸಮಸ್ಯೆ ಇಲ್ಲ, sorted array
     ಆಗಿರೋದ್ರಿಂದ order already correct ಇರುತ್ತೆ.

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು (Think out loud):
  →  "Since the array is sorted, duplicates are always adjacent."
  →  "The brute force would use a set — extra space, doesn't
      exploit sortedness."
  →  "I can compare each element to the LAST written unique value
      instead, using a write/read two-pointer pattern."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Two Pointers → Same Direction (Partition Style)
  Secondary : Sorted array property (duplicates are ADJACENT)

  WHY this technique?
  → SORTED array means duplicates sit next to each other — no
    hashset needed to detect repeats
  → `write` pointer for next unique slot, `read` scans forward
  → Same write/read partition skeleton as Move Zeroes (#283)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Given a sorted array nums, remove duplicates IN-PLACE so each
  unique element appears once. Return k = number of unique
  elements; the first k slots must hold them in order.

  Input : nums = [1, 1, 2, 2, 3]
  Output: k = 3, nums[:3] = [1, 2, 3]

  Example 1 — basic:
    Input : nums = [1, 1, 2, 2, 3]
    Output: k=3, nums[:3] = [1, 2, 3]
    Why?  : unique values are 1, 2, 3 — placed at the front

  Example 2 — slightly tricky:
    Input : nums = [1, 1, 1, 1]
    Output: k=1, nums[:1] = [1]
    Why?  : only one unique value exists

  Constraints:
    - nums is already SORTED in non-decreasing order
    - Must modify in-place, O(1) extra space

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 INTUITION (How to think)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Since the array is sorted, can I just compare each element to
  the LAST unique value I wrote, instead of searching a whole set?

  The journey from brute to optimal:
    Brute thought   →  use a set, sort, copy back
    Problem with it →  O(n) extra space, ignores sortedness
    Better question →  "compare to last written, not a whole set?"
    Insight         →  sortedness guarantees duplicates are adjacent
    Optimal         →  write/read two pointers, O(1) space

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 APPROACH 1 — BRUTE FORCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Collect unique values with a set, sort, copy back.

  Pseudocode:
    step 1: unique = sorted(set(nums))
    step 2: for i, v in enumerate(unique): nums[i] = v
    step 3: return len(unique)

  Time  : O(n log n)  →  Why: set + sort
  Space : O(n)  →  Why: extra set/list

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ? (Why is this not enough?)
    → Problem O(1) extra space ಕೇಳ್ತಿದೆ; ಇದು O(n) ಬಳಸುತ್ತೆ.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚶 APPROACH 2 — BETTER (skip — brute jumps straight to optimal)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ಇಲ್ಲಿ intermediate approach ಇಲ್ಲ — sortedness ಬಳಸಿದ ತಕ್ಷಣ
  ನೇರವಾಗಿ O(n) optimal ಗೆ ಹೋಗಬಹುದು.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 APPROACH 3 — OPTIMAL  
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Two pointers, same direction — write only on a new unique value.

  Key steps:
    1. If nums is empty → return 0
    2. write = 0  (index 0 is trivially unique)
    3. For read in range(1, n):
         if nums[read] != nums[write]:
             write += 1
             nums[write] = nums[read]
    4. Return write + 1  (count of unique elements)

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ (Say it once in Kanglish so it sticks):
    → "read pointer ಅನ್ನ ಮುಂದೆ ಓಡಿಸ್ತಾ, ಪ್ರತಿ value ಅನ್ನ write
        pointer ಇರೋ position ಜೊತೆ compare ಮಾಡು. ಬೇರೆ ಇದ್ರೆ, ಅದು
        ಹೊಸ unique value — write++ ಮಾಡಿ ಅಲ್ಲಿ ಇಡು. ಒಂದೇ ಇದ್ರೆ,
        duplicate — skip ಮಾಡು."

  Time  : O(n)  →  Why: single pass
  Space : O(1)  →  Why: in-place, two pointers only

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: nums = [1, 1, 2, 2, 3]

  write=0  (nums[0]=1 is the first unique)

  read=1  →  nums[1]=1 == nums[write]=1  →  duplicate, skip
  read=2  →  nums[2]=2 != nums[write]=1  →  write=1, nums[1]=2 → [1,2,2,2,3]
  read=3  →  nums[3]=2 == nums[write]=2  →  duplicate, skip
  read=4  →  nums[4]=3 != nums[write]=2  →  write=2, nums[2]=3 → [1,2,3,2,3]

  Output: k = write+1 = 3, nums[:3] = [1,2,3]

  ಇನ್ನೊಂದು example — tricky case:
  Input: nums = [1, 1, 1, 1]
  write=0
  read=1,2,3 → all equal nums[write]=1 → always duplicate, skip
  Output: k=1, nums[:1] = [1]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ Empty array?               →  [] → k=0
  ✓ Single element?            →  [5] → k=1, nums=[5]
  ✓ All duplicates?            →  [2,2,2,2] → k=1, nums[:1]=[2]
  ✓ No duplicates?             →  [1,2,3,4] → k=4, nums unchanged
  ✓ Duplicates only at the end?  →  [1,2,3,3,3] → k=3, nums[:3]=[1,2,3]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                Time        Space
  Brute Force   O(n log n)  O(n)
  Optimal       O(n)        O(1)    ← use this  

  Time ಯಾಕೆ O(n)?  → Array ಒಮ್ಮೆ ಮಾತ್ರ traverse ಮಾಡ್ತೇವೆ.
  Space ಯಾಕೆ O(1)? → write, read ಎರಡು pointer variables ಸಾಕು.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Two Pointers — Compare to Last Written

  ಈ pattern ಯಾವಾಗ use ಮಾಡಬೇಕು?
  → Array SORTED ಆಗಿದ್ದು, dedupe/compact in-place ಮಾಡ್ಬೇಕಾದಾಗ
  → Hashset ಬದ್ಲು sortedness (adjacency) ಬಳಸ್ಬಹುದು ಅಂತ ಗೊತ್ತಾದಾಗ

  ಇದೇ pattern ಬೇರೆ problems ನಲ್ಲಿ ಕಾಣಿಸುತ್ತೆ:
  → Remove Duplicates from Sorted Array II (allow up to 2 copies)
  → Move Zeroes (#283) — same write/read skeleton
  → Sort Colors (#75) — 3-way partition extension

  Next time ಇಂತಹ problem ಬಂದ್ರೆ ನಾನು ಮೊದಲು ಇದನ್ನ think ಮಾಡ್ತೇನೆ:
  → "Array sorted ಇದ್ಯಾ? ಇದ್ರೆ, hashset ಬದ್ಲು last-written
      comparison ಸಾಕಾಗುತ್ತಾ ಅಂತ ಮೊದಲು ಯೋಚಿಸು."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ INTERVIEW ನಲ್ಲಿ ಹೇಗೆ EXPLAIN ಮಾಡಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "So I need to dedupe a sorted array in-place and return the
      count of unique elements."

  2. Brute force:
     "I could use a set and sort — O(n log n), O(n) space — but
      that ignores the fact the array is already sorted."

  3. Optimize:
     "Since it's sorted, duplicates are adjacent. I can compare
      each element only to the last WRITTEN unique value."

  4. Code:
     "I'll keep a write pointer for the last unique slot and a
      read pointer scanning forward, advancing write only on a
      new value."

  5. Complexity:
     "Time O(n) — one pass. Space O(1) — in-place, two pointers."

  ಮುಖ್ಯ: ಸುಮ್ಮನೆ ಕೂತು code ಬರೆಯಬೇಡ!
         Interviewer ಗೆ ನಿನ್ನ thinking process ಕಾಣಬೇಕು.
"""


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(n log n) Time | O(n) Space
# ═══════════════════════════════════════════════════════════════════
def remove_duplicates_brute(nums):
    """ಇದು ಮೊದಲ ಆಲೋಚನೆ — set + sort + copy back, extra space"""
    if not nums:
        return 0
    unique = sorted(set(nums))
    for i, v in enumerate(unique):
        nums[i] = v
    return len(unique)


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n) Time | O(1) Space
# ═══════════════════════════════════════════════════════════════════
def remove_duplicates(nums):
    """ಇದು final answer — write/read pointer, compare to last written"""
    if not nums:
        return 0

    write = 0
    for read in range(1, len(nums)):
        if nums[read] != nums[write]:
            write += 1
            nums[write] = nums[read]

    return write + 1


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")   # Windows cp1252 can't print   otherwise

    # Test 1 — Basic example
    nums1 = [1, 1, 2, 2, 3]
    k1 = remove_duplicates(nums1)
    assert (k1, nums1[:k1]) == (3, [1, 2, 3])

    # Test 2 — Edge case: empty array
    assert remove_duplicates([]) == 0

    # Test 3 — Edge case: all duplicates
    nums3 = [2, 2, 2, 2]
    k3 = remove_duplicates(nums3)
    assert (k3, nums3[:k3]) == (1, [2])

    # Test 4 — Tricky: duplicates only at the end
    nums4 = [1, 2, 3, 3, 3]
    k4 = remove_duplicates(nums4)
    assert (k4, nums4[:k4]) == (3, [1, 2, 3])

    print("All tests passed!  ")
