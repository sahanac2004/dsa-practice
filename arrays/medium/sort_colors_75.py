"""
╔══════════════════════════════════════════════════════════════════╗
║  SORT COLORS                                                      ║
║  LeetCode #75  |  Difficulty: Medium  |  Topic: Arrays / Two Pointers ║
║  Link: https://leetcode.com/problems/sort-colors/                 ║
╚══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Given an array containing only 0s, 1s, and 2s (representing red,
  white, blue), sort it in-place so all 0s come first, then all 1s,
  then all 2s — in a SINGLE pass, without using a library sort.

  Input : nums = [2, 0, 2, 1, 1, 0]
  Output: [0, 0, 1, 1, 2, 2]

  Example 1 — basic:
    Input : nums = [2, 0, 2, 1, 1, 0]
    Output: [0, 0, 1, 1, 2, 2]
    Why?  : two 0s, two 1s, two 2s — grouped in that order

  Example 2 — slightly tricky (already sorted, or one color missing):
    Input : nums = [2, 2, 2]
    Output: [2, 2, 2]
    Why?  : with only one distinct value, sorting is a no-op — the
             algorithm must not break when a color is entirely absent

  Constraints:
    - n == nums.length
    - 1 <= n <= 300
    - nums[i] is 0, 1, or 2
    - Must sort in-place; a one-pass O(n) solution is expected (no
      built-in sort, ideally O(1) extra space)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ಮೊದಲು problem odidaga ನಮ್ಮ brain ಏನು think ಮಾಡಬೇಕು:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ (What are they asking?)
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  ಬರೀ 0, 1, 2 ಇರೋ array            │
  │  Output ಏನು ಬೇಕು?     →  in-place sort — 0s, 1s, 2s order  │
  │  Constraints ಏನಿದೆ?   →  n<=300, single pass expect, library│
  │                          sort ಬಳಸ್ಬಾರ್ದು                   │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ನನಗೆ ಗೊತ್ತಿರೋ simple way ಏನು? (Brute force thought)
  →  Sort ಬಳಸಿ ಬಿಡೋದು (nums.sort()) — ಸುಲಭ.
  →  ಆದರೆ ಇದು slow ಯಾಕೆ? → O(n log n), ಆದ್ರೆ ಕೇವಲ 3 distinct values
     ಇರೋದ್ರಿಂದ, general purpose sort use ಮಾಡೋದು overkill — count
     ಮಾಡಿ ಅಥವಾ ಒಂದೇ pass ನಲ್ಲಿ ಮಾಡ್ಬೋದು.

  ಹಂತ 3 — Better way ಹೇಗೆ ಯೋಚಿಸುವುದು? (Optimization thought)
  →  "ಪ್ರತಿ color ನ count ಎಣಿಸಿ, ಆಮೇಲೆ array ಅನ್ನ ಆ count ಪ್ರಕಾರ
     overwrite ಮಾಡ್ಬೋದು — ಇದು 2-pass. ಆದ್ರೆ single pass ಬೇಕಾದ್ರೆ?"
  →  ಅಹಾ moment: three pointers ಇಟ್ಕೊಂಡು — low (0s ಗೆ boundary),
     mid (current element), high (2s ಗೆ boundary) — mid ಇಂದ traverse
     ಮಾಡ್ತಾ, nums[mid]==0 ಆದ್ರೆ low ಜೊತೆ swap ಮಾಡಿ ಎರಡೂ pointers
     advance, nums[mid]==2 ಆದ್ರೆ high ಜೊತೆ swap ಮಾಡಿ (mid advance
     ಮಾಡ್ಬಾರ್ದು, swapped element ಮತ್ತೆ check ಆಗ್ಬೇಕು), nums[mid]==1
     ಆದ್ರೆ mid ಒಂದೇ advance ಮಾಡು. ಇದೇ Dutch National Flag algorithm!
  →  ಇದರಿಂದ ನಾವು Two Pointers → 3-Way Partition (Dutch National Flag)
     use ಮಾಡಬಹುದು!

  ಹಂತ 4 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  ಕೇವಲ 3 distinct values (0,1,2) ಇರೋದ್ರಿಂದ, three regions
    (low..mid-1 = 0s, mid..high = unprocessed, high+1..end = 2s)
    ಅಂತ ಇಟ್ಕೊಂಡು invariant maintain ಮಾಡ್ಬಹುದು.
  →  Single pass ಮತ್ತು O(1) space explicit ಆಗಿ ಬೇಕಾಗಿದ್ದೂ, in-place
     swap ಇಂದ ಎರಡೂ ಸಾಧ್ಯ ಆಗುತ್ತೆ.
  →  1s ಗೆ swap ಬೇಡ (ಈಗಾಗಲೇ ಸರಿಯಾದ region ನಲ್ಲಿ ಇರುತ್ತೆ) — mid ಅನ್ನ
     ಮಾತ್ರ advance ಮಾಡಿದ್ರೆ ಸಾಕು.

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು (Think out loud):
  →  "Since there are only 3 distinct values, I don't need a general
      sort — I can partition in a single pass."
  →  "The brute force is calling sort() directly — O(n log n), which
      ignores the fact that there are only 3 possible values."
  →  "I'll use the Dutch National Flag approach: three pointers — low,
      mid, high — that maintain three regions as I scan, swapping 0s
      to the front and 2s to the back."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Two Pointers → 3-Way Partition (Dutch National Flag)
  Secondary : None

  WHY this technique?
  → Only 3 distinct values means we can maintain three contiguous
    regions (0s, 1s, 2s) with pointers instead of a comparison sort
  → Single-pass O(n) with O(1) extra space is explicitly achievable
    and expected given n <= 300 and the value constraint
  → In-place swapping naturally grows the "0s region" from the left
    and the "2s region" from the right as mid scans through

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION (How to think — English)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Key observation: maintain three pointers dividing the array into
  four zones: [0..low-1] all 0s, [low..mid-1] all 1s, [mid..high]
  unprocessed, [high+1..end] all 2s. Scanning with mid and swapping
  appropriately shrinks the unprocessed zone by one each step (or, in
  the 2-swap case, doesn't advance mid since the swapped-in value is
  still unchecked).

  The journey from brute to optimal:
    Brute thought   →  just call nums.sort()
    Problem with it →  O(n log n), ignores the "only 3 values" hint
    Better question →  "can I count occurrences and rewrite, or even
                        do it in one pass with pointers?"
    Insight         →  three regions can be maintained with low/mid/
                        high pointers, swapping in place as we scan
    Optimal         →  Dutch National Flag: single pass, O(1) space,
                        swap 0s left, 2s right, leave 1s where mid finds them

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE (Built-in Sort)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Just call a general-purpose sort on the array.

  Pseudocode:
    step 1: nums.sort()
    step 2: return nums

  Time  : O(n log n)  →  Why: comparison-based sort over n elements
  Space : O(1) to O(n)  →  Why: depends on sort implementation

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ? (Why is this not enough?)
    → Problem "single pass" / "constant space" ಗುರಿ ಇಟ್ಕೊಂಡು ಕೇಳ್ತಾ
      ಇದೆ, ಕೇವಲ 3 values ಇರೋದ್ರಿಂದ general sort ಇಂದ log n factor
      unnecessary.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚶 SECTION 6 — APPROACH 2 — BETTER (Counting Sort — 2 pass)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Count occurrences of 0, 1, 2 in one pass. Then overwrite the array
    in a second pass using those counts.

  Time  : O(n)  →  two linear passes
  Space : O(1)  →  just three counters

  ಇನ್ನೂ better ಮಾಡಬಹುದಾ? → ಹೌದು — single pass ನಲ್ಲೇ ಮಾಡ್ಬಹುದು, Dutch
  National Flag 3-pointer technique ಇಂದ, count ಗಳ ಬದಲು direct swap
  ಮಾಡ್ತಾ ಹೋಗಿ.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 7 — APPROACH 3 — OPTIMAL   (Dutch National Flag — 3 Pointers)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    low=0, mid=0, high=n-1. Scan with mid:
      - nums[mid]==0: swap(low, mid), low+=1, mid+=1
      - nums[mid]==1: mid+=1 (already in correct middle region)
      - nums[mid]==2: swap(mid, high), high-=1 (don't advance mid —
        the swapped-in value from high still needs checking)
    Stop when mid > high.

  Key steps:
    1. low, mid, high = 0, 0, len(nums)-1
    2. while mid <= high:
         if nums[mid]==0: swap(low,mid); low+=1; mid+=1
         elif nums[mid]==1: mid+=1
         else: swap(mid,high); high-=1
    3. Array is now sorted in-place

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ (Say it once in Kanglish so it sticks):
    → "low=mid=0, high=n-1 ಇಟ್ಕೊಂಡು mid ಇಂದ scan ಮಾಡು. nums[mid]==0
        ಆದ್ರೆ low ಜೊತೆ swap ಮಾಡಿ ಎರಡೂ +1. nums[mid]==1 ಆದ್ರೆ ಮಿಡ್ ಅನ್ನ
        ಮಾತ್ರ +1. nums[mid]==2 ಆದ್ರೆ high ಜೊತೆ swap ಮಾಡಿ high-1
        (mid advance ಮಾಡ್ಬೇಡ)! mid > high ಆಗೋವರೆಗೂ repeat ಮಾಡು!"

  Time  : O(n)  →  Why: mid pointer moves forward every step or high
                    shrinks, single pass through the array
  Space : O(1)  →  Why: only three pointers, in-place swaps

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 8 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: nums = [2, 0, 2, 1, 1, 0]

  low=0, mid=0, high=5
  nums[mid]=2  → swap(mid=0,high=5) → nums=[0,0,2,1,1,2], high=4
  nums[mid]=0  → swap(low=0,mid=0) → nums same, low=1, mid=1
  nums[mid]=0  → swap(low=1,mid=1) → nums same, low=2, mid=2
  nums[mid]=2  → swap(mid=2,high=4) → nums=[0,0,1,1,2,2], high=3
  nums[mid]=1  → mid=3
  nums[mid]=1  → mid=4
  mid=4 > high=3 → loop ends

  Output: [0, 0, 1, 1, 2, 2]   matches expected

  ಇನ್ನೊಂದು example — tricky case (one color missing):
  Input: nums = [2, 2, 2]

  low=0, mid=0, high=2
  nums[mid]=2 → swap(0,2) → nums=[2,2,2] (same values), high=1
  nums[mid]=2 → swap(0,1) → nums=[2,2,2] (same values), high=0
  mid=0, high=0 → nums[mid]=2 → swap(0,0) → high=-1
  mid=0 > high=-1 → loop ends

  Output: [2, 2, 2]   matches expected (no-op result, correct)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 9 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ Single element?            →  low=mid=0, high=0, one iteration
                                   correctly places it
  ✓ All same color?            →  loop just shuffles same-valued
                                   elements, no visible change
  ✓ Already sorted?             →  0s and 1s advance mid/low normally,
                                   2s trigger harmless self-swaps
  ✓ Only two colors present?    →  works — the missing color's branch
                                   simply never triggers
  ✓ All 2s at the front (reverse sorted)? →  each swaps to the back
                                   correctly via the high pointer

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 10 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                Time         Space
  Brute Force   O(n log n)   O(1)/O(n) (sort-dependent)
  Better        O(n)         O(1)  (two-pass counting sort)
  Optimal       O(n)         O(1)    ← use this  (single pass)

  Time ಯಾಕೆ ಅಷ್ಟು?  → mid ಪ್ರತಿ step ಗೂ move ಆಗುತ್ತೆ ಅಥವಾ high shrink
                        ಆಗುತ್ತೆ — single pass ನಲ್ಲಿ ಮುಗಿಯುತ್ತೆ.
  Space ಯಾಕೆ ಅಷ್ಟು? → low, mid, high ಬಿಟ್ಟು ಬೇರೆ extra structure ಬೇಡ,
                        in-place swaps ಮಾತ್ರ.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 11 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Dutch National Flag — 3-Way In-Place Partition

  ಈ pattern ಯಾವಾಗ use ಮಾಡಬೇಕು?
  → Array ನಲ್ಲಿ ಕೇವಲ 3 (ಅಥವಾ ಕೆಲವೇ) distinct values ಇದ್ದು, in-place
    single-pass grouping ಬೇಕಾದಾಗ
  → General sort overkill ಅಂತ ಗೊತ್ತಾದಾಗ (values limited/known ಆಗಿರೋದ್ರಿಂದ)
  → "low/mid/high" three-region invariant maintain ಮಾಡ್ಬಹುದು ಅಂತ
    ಗೊತ್ತಾದಾಗ

  ಇದೇ pattern ಬೇರೆ problems ನಲ್ಲಿ ಕಾಣಿಸುತ್ತೆ:
  → Move Zeroes (#283) — simpler 2-way version of this same idea
  → Partition Array According to Given Pivot — generalized 3-way partition
  → Quicksort's partition step (Lomuto/Hoare) — same swapping philosophy

  Next time ಇಂತಹ problem ಬಂದ್ರೆ ನಾನು ಮೊದಲು ಇದನ್ನ think ಮಾಡ್ತೇನೆ:
  → "ಕೇವಲ 2-3 distinct values ಇರೋ array sort ಮಾಡಬೇಕು ಅಂತ ಕೇಳಿದ
      ತಕ್ಷಣ, general sort ಅಲ್ಲ, low/mid/high three-pointer partition
      ಬಳಸು ಅಂತ ಮೊದಲು ಯೋಚಿಸು."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 12 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "I need to sort an array containing only 0s, 1s, and 2s, in
      place, ideally in a single pass."

  2. Brute force:
     "Just calling sort() gives O(n log n), but with only 3 distinct
      values that's wasteful."

  3. Optimize:
     "I can count occurrences of each value and rewrite the array in
      two passes — O(n). But I can do even better with the Dutch
      National Flag technique: three pointers maintaining three
      regions in a single pass."

  4. Code:
     "I will use low/mid/high pointers, swapping 0s to the front,
      leaving 1s in place (just advancing mid), and swapping 2s to
      the back — being careful not to advance mid after a swap with
      high, since that value is still unchecked."

  5. Complexity:
     "Time O(n) — single pass, mid always moves or high shrinks.
      Space O(1) — only three pointers and in-place swaps."

  ಮುಖ್ಯ: ಸುಮ್ಮನೆ ಕೂತು code ಬರೆಯಬೇಡ!
         Interviewer ಗೆ ನಿನ್ನ thinking process ಕಾಣಬೇಕು.
"""


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(n log n) Time | O(1)/O(n) Space  (Built-in Sort)
# ═══════════════════════════════════════════════════════════════════
def sort_colors_brute(nums):
    """ಇದು ಮೊದಲ ಆಲೋಚನೆ — ಬರೀ built-in sort ಬಳಸೋದು"""
    nums.sort()
    return nums


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n) Time | O(1) Space  (Dutch National Flag — 3 Pointers)
# ═══════════════════════════════════════════════════════════════════
def sort_colors(nums):
    """ಇದು final answer — low/mid/high pointers ಇಟ್ಕೊಂಡು single pass ನಲ್ಲಿ 3-way partition"""
    low, mid, high = 0, 0, len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:  # nums[mid] == 2
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

    return nums


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")   # Windows cp1252 can't print emoji otherwise

    # Test 1 — Basic example
    assert sort_colors([2, 0, 2, 1, 1, 0]) == [0, 0, 1, 1, 2, 2]

    # Test 2 — Edge case: single element
    assert sort_colors([1]) == [1]

    # Test 3 — Edge case: all same elements
    assert sort_colors([2, 2, 2]) == [2, 2, 2]

    # Test 4 — Tricky: already sorted, and a color missing
    assert sort_colors([0, 0, 1, 1]) == [0, 0, 1, 1]

    print("All tests passed! ")
