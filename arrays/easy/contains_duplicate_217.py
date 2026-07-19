"""
╔══════════════════════════════════════════════════════════════════╗
║  CONTAINS DUPLICATE                                              ║
║  LeetCode #217  |  Difficulty: Easy  |  Topic: Arrays / Hashing  ║
║  Link: https://leetcode.com/problems/contains-duplicate/         ║
╚══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ಮೊದಲು problem odidaga ನಮ್ಮ brain ಏನು think ಮಾಡಬೇಕು:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ (What are they asking?)
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  integers array nums               │
  │  Output ಏನು ಬೇಕು?     →  ಯಾವುದಾದ್ರೂ value 2 ಸಲ          │
  │                          repeat ಆಗಿದ್ಯಾ ಅಂತ True/False   │
  │  Constraints ಏನಿದೆ?   →  order ಮ್ಯಾಟರ್ ಆಗಲ್ಲ, ಬರೀ          │
  │                          existence ಮಾತ್ರ ಕೇಳ್ತಾರೆ           │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ನನಗೆ ಗೊತ್ತಿರೋ simple way ಏನು? (Brute force thought)
  →  ಪ್ರತಿ pair (i, j) ಗೂ compare ಮಾಡಿ ಒಂದೇ value ಇದ್ಯಾ ಅಂತ
     check ಮಾಡೋದು.
  →  ಆದರೆ ಇದು slow ಯಾಕೆ? → n=10^5 ಆದ್ರೆ n² comparisons, TLE.

  ಹಂತ 3 — Better way ಹೇಗೆ ಯೋಚಿಸುವುದು? (Optimization thought)
  →  "ಪ್ರತಿ number ನೋಡಿದಾಗ, ಇದನ್ನ ಮೊದಲೇ ನಾನು ನೋಡಿದ್ದೀನಾ ಅಂತ
     ಗೊತ್ತಾದ್ರೆ ಸಾಕಲ್ವಾ? ಪೂರ್ತಿ ಪೇರ್ compare ಯಾಕೆ ಬೇಕು?"
  →  ಅಹಾ moment: ಒಂದು HashSet ನಲ್ಲಿ "ಇಷ್ಟರ ವರೆಗೆ ನಾನು ಕಂಡಿದ್ದು"
     ಅನ್ನ store ಮಾಡ್ತಾ ಹೋದ್ರೆ, O(1) ನಲ್ಲಿ "ಇದು ಮೊದಲೇ ಇತ್ತಾ" ಅಂತ
     ಗೊತ್ತಾಗುತ್ತೆ.
  →  ಇದರಿಂದ ನಾವು HashSet Seen-Before Lookup use ಮಾಡಬಹುದು!

  ಹಂತ 4 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  Question ಬರೀ EXISTENCE ("ಇದ್ಯಾ?") ಕೇಳ್ತಿದೆ, pairing ಅಥವಾ
     counting ಬೇಕಿಲ್ಲ — HashSet ಗೆ ಇದು perfect fit.
  →  Order matter ಆಗಲ್ಲ ಅಂದ್ರೆ sorting ಬೇಕಿಲ್ಲ, direct membership
     check ಸಾಕು.
  →  O(n) time ಬೇಕು ಅಂದಾಗ HashSet ಮೊದಲು ಯೋಚಿಸಬೇಕು.

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು (Think out loud):
  →  "So I just need to know if ANY value repeats, not where."
  →  "The brute force checks every pair — O(n²)."
  →  "I notice this is a pure existence check, so a HashSet gives
      me O(1) average membership testing in a single pass."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : HashSet → Seen-Before Lookup
  Secondary : Sorting (alternative, adjacent-duplicate check)

  WHY HashSet?
  → Pure existence question — no indices, no pairing
  → O(1) average "have I seen this before?" checks
  → Simpler cousin of the complement-lookup pattern from Two Sum

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Given an integer array nums, return True if any value appears
  at least twice, and False if every element is distinct.

  Input : nums = [1, 2, 3, 1]
  Output: True

  Example 1 — basic:
    Input : nums = [1, 2, 3, 1]
    Output: True
    Why?  : 1 appears at index 0 AND index 3

  Example 2 — slightly tricky:
    Input : nums = [1, 2, 3, 4]
    Output: False
    Why?  : all elements are distinct

  Constraints:
    - 1 <= nums.length <= 10⁵
    - Values can repeat any number of times, order doesn't matter

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 INTUITION (How to think)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Do I need to compare every PAIR, or can I remember what I've
  already visited and check membership as I go?

  The journey from brute to optimal:
    Brute thought   →  compare every pair (i, j)
    Problem with it →  O(n²), too slow for n=10⁵
    Better question →  "can I just check 'seen before' in O(1)?"
    Insight         →  HashSet membership check is O(1) average
    Optimal         →  single pass, HashSet of seen values

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 APPROACH 1 — BRUTE FORCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Compare every pair (i, j) where i ≠ j.

  Pseudocode:
    step 1: for i in range(n):
    step 2:     for j in range(i+1, n):
    step 3:         if nums[i] == nums[j] → return True

  Time  : O(n²)  →  Why: nested loops over all pairs
  Space : O(1)   →  Why: no extra space

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ? (Why is this not enough?)
    → n = 10⁵ ಆದ್ರೆ ~10¹⁰ comparisons → TLE.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚶 APPROACH 2 — BETTER (Sort First)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Sort the array — duplicates land next to each other, then
    scan once checking nums[i] == nums[i-1].

  Time  : O(n log n)  — sorting dominates
  Space : O(1) extra  — if in-place sort allowed

  ಇನ್ನೂ better ಮಾಡಬಹುದಾ? → ಹೌದು — sorting ಬೇಡ, HashSet ಆದ್ರೆ
  O(n) ಗೆ ಬರುತ್ತೆ.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 APPROACH 3 — OPTIMAL  
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Single pass with a HashSet of values seen so far.

  Key steps:
    1. seen = empty set
    2. For each num in nums:
         a. If num already in seen → return True (duplicate found)
         b. Otherwise, add num to seen
    3. If loop finishes with no match → return False

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ (Say it once in Kanglish so it sticks):
    → "Array ಅನ್ನ ಒಮ್ಮೆ scan ಮಾಡ್ತಾ, ಪ್ರತಿ number ಗೂ ಅದು seen
        set ನಲ್ಲಿ ಇದ್ಯಾ ಅಂತ ಚೆಕ್ ಮಾಡು. ಇದ್ರೆ True return ಮಾಡು,
        ಇಲ್ಲಾಂದ್ರೆ set ಗೆ ಸೇರಿಸಿ ಮುಂದೆ ಹೋಗು."

  Time  : O(n)  →  Why: single pass, O(1) avg set operations
  Space : O(n)  →  Why: set can hold up to n elements

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: nums = [1, 2, 3, 1]

  num=1  →  variables: seen={}         →  1 not in seen → seen={1}
  num=2  →  variables: seen={1}        →  2 not in seen → seen={1,2}
  num=3  →  variables: seen={1,2}      →  3 not in seen → seen={1,2,3}
  num=1  →  variables: seen={1,2,3}    →  1 IS in seen! → return True

  Output: True

  ಇನ್ನೊಂದು example — tricky case:
  Input: nums = [1, 2, 3, 4]
  Every number is new → seen grows to {1,2,3,4}, loop ends, no match.
  Output: False

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ Single element?     →  [1] → False (nothing to duplicate against)
  ✓ All same value?     →  [5,5,5,5] → True
  ✓ Negative numbers?   →  [-1,-2,-1] → True
  ✓ Duplicate at end?   →  [1,2,3,4,4] → True
  ✓ Large distinct array?  →  False, must scan fully (worst case)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                Time        Space
  Brute Force   O(n²)       O(1)
  Sort First    O(n log n)  O(1)/O(n)
  Optimal       O(n)        O(n)    ← use this  

  Time ಯಾಕೆ O(n)?  → Array ಒಮ್ಮೆ ಮಾತ್ರ traverse ಮಾಡ್ತೇವೆ.
  Space ಯಾಕೆ O(n)? → Worst case ಎಲ್ಲ n elements set ನಲ್ಲಿ ಹೋಗ್ತಾವೆ.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: HashSet Seen-Before Lookup

  ಈ pattern ಯಾವಾಗ use ಮಾಡಬೇಕು?
  → Question ಬರೀ "ಇದು ಮೊದಲೇ ಆಗಿತ್ತಾ?" ಅಂತ existence ಕೇಳ್ತಿದ್ರೆ
  → Pairing ಅಥವಾ counting ಬೇಕಿಲ್ಲ, ಬರೀ membership ಸಾಕಾದಾಗ

  ಇದೇ pattern ಬೇರೆ problems ನಲ್ಲಿ ಕಾಣಿಸುತ್ತೆ:
  → Longest Consecutive Sequence (#128)
  → Happy Number
  → Cycle detection in graphs (visited set)

  Next time ಇಂತಹ problem ಬಂದ್ರೆ ನಾನು ಮೊದಲು ಇದನ್ನ think ಮಾಡ್ತೇನೆ:
  → "ಬರೀ 'ಇದ್ಯಾ ಇಲ್ಲವಾ' ಪ್ರಶ್ನೆ ಬಂತು ಅಂದ್ರೆ, HashSet ಮೊದಲು
      ಯೋಚಿಸು — pairing ಗಿಂತ ಸುಲಭ."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ INTERVIEW ನಲ್ಲಿ ಹೇಗೆ EXPLAIN ಮಾಡಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "So I just need to know if ANY value appears twice — order
      and position don't matter."

  2. Brute force:
     "The naive approach compares every pair — O(n²), which
      would TLE for n up to 10⁵."

  3. Optimize:
     "Since it's a pure existence check, I can use a HashSet to
      test membership in O(1) average as I scan once."

  4. Code:
     "I'll keep a set of seen values; if the current number is
      already in it, return True immediately."

  5. Complexity:
     "Time O(n) — one pass. Space O(n) — set can hold up to n items."

  ಮುಖ್ಯ: ಸುಮ್ಮನೆ ಕೂತು code ಬರೆಯಬೇಡ!
         Interviewer ಗೆ ನಿನ್ನ thinking process ಕಾಣಬೇಕು.
"""


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(n²) Time | O(1) Space
# ═══════════════════════════════════════════════════════════════════
def contains_duplicate_brute(nums):
    """ಇದು ಮೊದಲ ಆಲೋಚನೆ — every pair compare, simple but slow"""
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] == nums[j]:
                return True
    return False


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n) Time | O(n) Space
# ═══════════════════════════════════════════════════════════════════
def contains_duplicate(nums):
    """ಇದು final answer — HashSet seen-before lookup, fast and clean"""
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")   # Windows cp1252 can't print   otherwise

    # Test 1 — Basic example
    assert contains_duplicate([1, 2, 3, 1]) is True

    # Test 2 — Edge case: no duplicates
    assert contains_duplicate([1, 2, 3, 4]) is False

    # Test 3 — Edge case: single element
    assert contains_duplicate([1]) is False

    # Test 4 — Tricky: negative numbers
    assert contains_duplicate([-1, -2, -1]) is True

    print("All tests passed!  ")
