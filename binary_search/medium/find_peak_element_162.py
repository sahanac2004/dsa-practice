"""
╔══════════════════════════════════════════════════════════════════╗
║  SINGLE ELEMENT IN A SORTED ARRAY                                ║
║  LeetCode #540  |  Difficulty: Medium  |  Topic: Binary Search  ║
║  Link: https://leetcode.com/problems/single-element-in-a-sorted-array/                                                    ║
╚══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  You are given a sorted array where every element appears exactly
  TWICE except for one element which appears exactly ONCE.
  Find and return the single element.
  Must solve in O(log n) time and O(1) space.

  Input : nums = sorted array, every element twice except one
  Output: the single element that appears only once

  Example 1 — basic:
    Input : nums = [1,1,2,3,3,4,4,8,8]
    Output: 2
    Why?  : 1→twice, 2→once(answer!), 3→twice, 4→twice, 8→twice

  Example 2 — slightly tricky (single at end):
    Input : nums = [3,3,7,7,10,11,11]
    Output: 10
    Why?  : 10 appears only once, at index 4

  Constraints:
    - 1 <= nums.length <= 10^5
    - 0 <= nums[i] <= 10^5
    - Array is sorted
    - Exactly one element appears once, rest appear twice
    - Must be O(log n) time, O(1) space

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Problem odi aada mele namma brain enu think maadabeeku:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  sorted array, every element  │
  │                           twice except one              │
  │  Output ಏನು ಬೇಕು?     →  that one single element      │
  │  Constraints ಏನಿದೆ?   →  O(log n) time must!          │
  │                           O(1) space must!              │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ನನಗೆ ಗೊತ್ತಿರೋ simple way ಏನು?
  →  XOR all elements → duplicate elements cancel out →
     single element ಉಳಿಯತ್ತೆ! O(n) time O(1) space
  →  ಆದರೆ ಇದು slow ಯಾಕೆ?
     O(log n) beeku anta problem says — XOR O(n) aagatte

  ಹಂತ 3 — Better way ಹೇಗೆ ಯೋಚಿಸುವುದು?
  →  "Sorted array + O(log n) → Binary Search!"
  →  Key observation: single element ಮೊದಲು pairs even index
     ಲ್ಲಿ start ಆಗತ್ತೆ, single element ನಂತರ odd index ಲ್ಲಿ!
  →  [1,1,2,3,3] → before single(2): pairs at (0,1)
     after single: pairs at (3,4) → odd index start!
  →  mid even ಆದ್ರೆ: nums[mid]==nums[mid+1] → single is right
     mid even ಆದ್ರೆ: nums[mid]==nums[mid-1] → single is left
  →  ಇದರಿಂದ ನಾವು Binary Search on Index Parity use ಮಾಡಬಹуದು!

  ಹಂತ 4 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  Before single element: every pair starts at even index
  →  After single element: every pair starts at odd index
  →  This parity shift = binary search condition!
  →  mid ಅನ್ನು always even ಮಾಡಿ check maadu — cleaner logic

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು:
  →  "O(log n) required → binary search on sorted array"
  →  "Key insight: before single element, pairs start at even
      indices. After single element, pairs start at odd indices"
  →  "Use this parity to determine which half has the single element"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Binary Search → Index Parity Trick
  Secondary : XOR (brute force O(n))

  WHY Binary Search with parity?
  → Array is sorted → binary search applicable
  → Before single: pairs occupy (0,1),(2,3),(4,5) → even start
  → After single: pairs occupy (odd,even) → odd start
  → mid always even → compare mid with mid+1 → find which side

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Look at the indices carefully:

  [1, 1, 2, 3, 3, 4, 4, 8, 8]
   0  1  2  3  4  5  6  7  8

  Before single(2): pairs are (0,1) — start at EVEN index
  After  single(2): pairs are (3,4),(5,6),(7,8) — start at ODD index

  So if mid is even and nums[mid] == nums[mid+1]:
    → pair starts at even → we are BEFORE the single element
    → single is in RIGHT half → left = mid + 2

  If mid is even and nums[mid] != nums[mid+1]:
    → pair does NOT start here → single element IS at mid or LEFT
    → right = mid

  Always make mid even to keep logic consistent: mid -= (mid % 2)

  The journey from brute to optimal:
    Brute thought   →  XOR all elements → O(n) O(1)
    Problem with it →  Problem demands O(log n)
    Better question →  "What property changes at the single element?"
    Insight         →  Pair index parity flips at the single element!
                       Before: even start, After: odd start
    Optimal         →  Binary search on this parity → O(log n)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE (XOR)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    XOR all elements. Since a^a = 0, all pairs cancel out.
    Only the single element remains.

  Pseudocode:
    step 1: result = 0
    step 2: for num in nums: result ^= num
    step 3: return result

  Time  : O(n)  →  Why: traverse entire array once
  Space : O(1)  →  Why: only one variable

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ?
    → O(n) valid adu, but problem explicitly says O(log n) beeku
    → Sorted array iddare binary search use maadabeeku

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 6 — APPROACH 2 — OPTIMAL (Binary Search + Parity)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Binary search on even indices only.
    If nums[mid] == nums[mid+1] → single is in right half
    If nums[mid] != nums[mid+1] → single is at mid or left half

  Key steps:
    1. left=0, right=n-1
    2. While left < right:
       a. mid = (left+right)//2
       b. Make mid even: if mid%2==1: mid -= 1
       c. if nums[mid] == nums[mid+1]:
             single is RIGHT → left = mid+2
          else:
             single is HERE or LEFT → right = mid
    3. return nums[left]

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ:
    → "mid ಅನ್ನು even ಮಾಡು. nums[mid]==nums[mid+1] ಆದ್ರೆ
       pair even index ಲ್ಲಿ start ಆಗಿದೆ → single RIGHT ಲ್ಲಿ
       → left=mid+2. ಇಲ್ಲದಿದ್ರೆ single LEFT ಲ್ಲಿ ಅಥವಾ mid
       ನಲ್ಲೇ → right=mid. ಕೊನೆಗೆ nums[left] = answer!"

  Time  : O(log n)  →  Why: binary search, half eliminated each step
  Space : O(1)      →  Why: only pointers used

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 7 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: nums = [1,1,2,3,3,4,4,8,8]
  Index:          0 1 2 3 4 5 6 7 8

  left=0, right=8
  mid = 4, mid is even ✓
  nums[4]=3, nums[5]=4 → NOT equal → single at mid or left
  right = 4

  left=0, right=4
  mid = 2, mid is even ✓
  nums[2]=2, nums[3]=3 → NOT equal → single at mid or left
  right = 2

  left=0, right=2
  mid = 1, mid is ODD → mid = 0
  nums[0]=1, nums[1]=1 → EQUAL → single in right half
  left = 0+2 = 2

  left=2, right=2 → exit loop
  return nums[2] = 2 ✓

  ಇನ್ನೊಂದು example — single at end:
  Input: [3,3,7,7,10,11,11]
  Index:   0 1 2 3  4  5  6

  left=0, right=6
  mid=3, odd → mid=2
  nums[2]=7, nums[3]=7 → EQUAL → left=4

  left=4, right=6
  mid=5, odd → mid=4
  nums[4]=10, nums[5]=11 → NOT equal → right=4

  left=4, right=4 → exit
  return nums[4] = 10 ✓

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 8 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ Single element at start?  →  [1,2,2,3,3] → 1
  ✓ Single element at end?    →  [1,1,2,2,3] → 3
  ✓ Single element at middle? →  [1,1,2,3,3] → 2
  ✓ Only one element?         →  [1] → 1
  ✓ Three elements?           →  [1,2,2] → 1 or [1,1,2] → 2

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 9 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                Time      Space
  Brute (XOR)   O(n)      O(1)
  Optimal       O(log n)  O(1)   ← use this ✅

  Time yaake O(log n)? → Binary search, each step half eliminate
  Space yaake O(1)?    → Only left, right, mid variables

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 10 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Binary Search on Index Parity

  Ee pattern yaavaaga use maadabeeku?
  → Sorted array, find anomaly in O(log n)
  → Some property flips/changes at the answer point
  → That property can be used as binary search condition

  Idee pattern beere problemsalli kaanisatte:
  → Find Peak Element #162 (next problem — similar binary search!)
  → Missing Number in sorted array
  → Find rotation count in sorted array

  Next time intaha problem bandre naanu modalu idannu think maadtene:
  → "Sorted array + O(log n) → Binary Search!
     Before single: pairs even index start.
     After single: pairs odd index start.
     Mid even maadu, mid+1 compare maadu → which side decide!"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 11 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "Find the element that appears once in a sorted array where
      every other element appears twice. O(log n) required."

  2. Brute force:
     "XOR all elements — pairs cancel, single remains. O(n) O(1).
      But problem demands O(log n)."

  3. Optimize:
     "Key insight: before the single element, pairs start at even
      indices. After it, pairs start at odd indices. This parity
      flip is our binary search condition. Always check even mid."

  4. Code:
     "Make mid even. If nums[mid]==nums[mid+1] → single is right,
      left=mid+2. Else → single is mid or left, right=mid."

  5. Complexity:
     "Time O(log n) — binary search. Space O(1)."

  Mukhya: summane kuutu code bareyabeda!
          Index parity insight — very elegant, interviewer loves it!
          XOR approach mention maadu first, then upgrade to O(log n).
"""


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(n) Time | O(1) Space (XOR)
# ═══════════════════════════════════════════════════════════════════
def single_non_duplicate_brute(nums):
    """Idu modala aaloochane — XOR, pairs cancel out O(n)"""
    result = 0
    for num in nums:
        result ^= num
    return result


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(log n) Time | O(1) Space
# ═══════════════════════════════════════════════════════════════════
def single_non_duplicate(nums):
    """
    Idu final answer — binary search on index parity
    Always check even mid: if nums[mid]==nums[mid+1] → right half
    else → left half or mid itself
    """
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        # always make mid even for consistent comparison
        if mid % 2 == 1:
            mid -= 1

        if nums[mid] == nums[mid + 1]:
            # pair starts at even index → single is in RIGHT half
            left = mid + 2
        else:
            # pair does NOT start here → single is at mid or LEFT
            right = mid

    return nums[left]


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # Test 1 — Single in middle
    assert single_non_duplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]) == 2

    # Test 2 — Single near end
    assert single_non_duplicate([3, 3, 7, 7, 10, 11, 11]) == 10

    # Test 3 — Single at start
    assert single_non_duplicate([1, 2, 2, 3, 3]) == 1

    # Test 4 — Single at end
    assert single_non_duplicate([1, 1, 2, 2, 3]) == 3

    # Test 5 — Only one element
    assert single_non_duplicate([1]) == 1

    # Test 6 — Three elements, single at start
    assert single_non_duplicate([1, 2, 2]) == 1

    # Test 7 — Three elements, single at end
    assert single_non_duplicate([1, 1, 2]) == 2

    print("All tests passed!")
