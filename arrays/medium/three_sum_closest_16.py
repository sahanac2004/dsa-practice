"""
╔══════════════════════════════════════════════════════════════════╗
║  3SUM CLOSEST                                                    ║
║  LeetCode #16  |  Difficulty: Medium  |  Topic: Arrays / Two Ptr  ║
║  Link: https://leetcode.com/problems/3sum-closest/                ║
╚══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Given an integer array and a target, find the sum of three
  numbers that is CLOSEST to target (not necessarily equal to it).
  Return that sum. Assume exactly one closest answer exists.

  Input : nums = [-1, 2, 1, -4], target = 1
  Output: 2

  Example 1 — basic:
    Input : nums = [-1, 2, 1, -4], target = 1
    Output: 2
    Why?  : (-1) + 2 + 1 = 2, which is closest to target=1

  Example 2 — slightly tricky (exact match possible):
    Input : nums = [0, 0, 0], target = 1
    Output: 0
    Why?  : Only possible triplet sum is 0+0+0=0 — no other option,
             so 0 is "closest" even though it's not equal to target

  Constraints:
    - 3 <= nums.length <= 500
    - -1000 <= nums[i] <= 1000, -1000 <= target <= 1000
    - Exactly one closest sum is expected (no tie-breaking needed)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ಮೊದಲು problem odidaga ನಮ್ಮ brain ಏನು think ಮಾಡಬೇಕು:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ (What are they asking?)
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  array + target number           │
  │  Output ಏನು ಬೇಕು?     →  target ಗೆ ಹತ್ತಿರ ಇರೋ 3-sum      │
  │  Constraints ಏನಿದೆ?   →  exact match ಇಲ್ಲದೇ ಇರ್ಬೋದು,     │
  │                          closest ಒಂದೇ ಗ್ಯಾರಂಟಿ ಇರುತ್ತೆ    │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ನನಗೆ ಗೊತ್ತಿರೋ simple way ಏನು? (Brute force thought)
  →  ಮೂರು nested loops ಹಾಕಿ, ಪ್ರತಿ triplet sum ಮಾಡಿ, |sum-target|
     ಅನ್ನ track ಮಾಡ್ತಾ, ಚಿಕ್ಕ difference ಇರೋ sum ಅನ್ನ ಇಟ್ಟುಕೊಳ್ಳೋದು.
  →  ಆದರೆ ಇದು slow ಯಾಕೆ? → O(n³), n=500 ಗೆ ಇನ್ನೂ ok ಆಗಿದ್ರೂ,
     3Sum problem ಇಂದ ಗೊತ್ತಾಗಿರೋ better idea ಇಲ್ಲಿ ಸಹ ಕೆಲಸ ಮಾಡುತ್ತೆ.

  ಹಂತ 3 — Better way ಹೇಗೆ ಯೋಚಿಸುವುದು? (Optimization thought)
  →  "3Sum (#15) ನಲ್ಲಿ sort + two-pointer use ಮಾಡಿದ್ವಿ, ಇಲ್ಲೂ ಅದೇ
     idea use ಮಾಡ್ಬೋದಾ? ಆದ್ರೆ ಇಲ್ಲಿ '==0' ಬದ್ಲು 'closest to target'
     ಬೇಕು."
  →  ಅಹಾ moment: Array sort ಮಾಡಿ, i fix ಮಾಡಿ, L/R two pointer ಇಂದ
     current sum ಅನ್ನ target ಜೊತೆ compare ಮಾಡಿ, ಪ್ರತಿ step ನಲ್ಲೂ
     best (closest) sum ಅನ್ನ update ಮಾಡ್ತಾ ಹೋಗೋದು — no need for
     exact-zero check, ಬರೀ diff track ಮಾಡಿದ್ರೆ ಸಾಕು.
  →  ಇದರಿಂದ ನಾವು Sort + Fix-One + Two-Pointer (running best) use
     ಮಾಡಬಹುದು!

  ಹಂತ 4 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  "3 numbers ಇಂದ target ಹತ್ತಿರ sum" ಅಂದ್ರೆ 3Sum ನ variant —
     fix-one + 2-pointer reduction ಇಲ್ಲಿ ಸಹ apply ಆಗುತ್ತೆ.
  →  Sorted array ಆದ್ರೆ, sum < target ಆದ್ರೆ L++ (sum ಜಾಸ್ತಿ ಮಾಡೋಕೆ),
     sum > target ಆದ್ರೆ R-- (sum ಕಡಿಮೆ ಮಾಡೋಕೆ) — monotonic ಆಗಿ
     move ಮಾಡ್ಬೋದು, ಪ್ರತಿ possible closer sum ಅನ್ನ miss ಮಾಡಲ್ಲ.
  →  Exact match ಸಿಕ್ಕ ತಕ್ಷಣ (diff==0) early-exit ಮಾಡ್ಬೋದು —
     ಅದಕ್ಕಿಂತ ಹತ್ತಿರ ಇರೋ ಸಂಖ್ಯೆ ಇರಲ್ಲ.

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು (Think out loud):
  →  "This looks like 3Sum, but instead of checking for an exact
      zero, I need to track the sum closest to target."
  →  "The brute force is three nested loops tracking the minimum
      absolute difference — O(n³), fine for n=500 but not ideal."
  →  "If I sort and fix one element, I can use two pointers on the
      rest just like 3Sum, updating a running 'closest sum so far'
      instead of looking for an exact zero — that's O(n²)."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Two Pointers → Opposite Ends (on sorted array)
  Secondary : Sort + Fix-One-Element reduction, running best-diff tracker

  WHY this technique?
  → Same "fix one, 2-sum the rest" shape as 3Sum, just optimizing a
    distance instead of matching a fixed value
  → Sorted array lets the two pointers move monotonically toward
    the target sum, no need to re-scan
  → Early exit the moment diff == 0 — sum can't get any closer

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION (How to think)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Key observation: this is 3Sum with the equality check replaced by
  a "track the minimum |sum - target|" check. Everything else about
  the sort + fix-one + two-pointer machinery carries over unchanged.

  The journey from brute to optimal:
    Brute thought   →  three nested loops, track best |sum-target|
    Problem with it →  O(n³) — unnecessary given the 3Sum insight
    Better question →  "can I reuse the 3Sum two-pointer reduction?"
    Insight         →  yes — swap the "==0" check for a running best
    Optimal         →  sort, fix i, two-pointer L/R updating best sum

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Try every triplet (i, j, k), compute its sum, and keep the sum
    whose absolute difference from target is smallest.

  Pseudocode:
    step 1: best = nums[0]+nums[1]+nums[2]
    step 2: for i,j,k in all combinations (i<j<k):
    step 3:   if |sum-target| < |best-target|: best = sum
    step 4: return best

  Time  : O(n³)  →  Why: three nested loops over all index combinations
  Space : O(1)   →  Why: only a running best value is tracked

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ? (Why is this not enough?)
    → n=500 ಗೆ n³ ≈ 1.25×10^8 — ಇದು ಇನ್ನೂ pass ಆಗ್ಬೋದು, ಆದ್ರೆ
      3Sum ಇಂದ ಗೊತ್ತಾಗಿರೋ two-pointer trick ಬಳಸಿ O(n²) ಗೆ ಇಳಿಸ್ಬೋದು.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚶 SECTION 6 — APPROACH 2 — BETTER (skip — brute jumps straight to optimal)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ಇಲ್ಲಿ intermediate approach ಇಲ್ಲ — 3Sum ಇಂದ ಗೊತ್ತಾಗಿರೋ sort +
  two-pointer insight ಸಿಕ್ಕ ತಕ್ಷಣ ನೇರವಾಗಿ optimal ಗೆ ಹೋಗಬಹುದು.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 7 — APPROACH 3 — OPTIMAL   (Sort + Two Pointers, running best)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Sort nums. For each fixed i, use two pointers L=i+1, R=n-1 over
    the rest. At each step compute the triplet sum: if it equals
    target, that's the exact closest — return immediately. Otherwise
    update the best-so-far if this sum is closer, then move L right
    (sum too small) or R left (sum too big).

  Key steps:
    1. Sort nums ascending.
    2. closest = sum of first three elements (initial guess).
    3. For i from 0 to n-3:
         L, R = i+1, n-1
         While L < R:
           total = nums[i] + nums[L] + nums[R]
           if |total-target| < |closest-target|: closest = total
           if total == target: return total   (can't get closer)
           elif total < target: L += 1
           else: R -= 1
    4. Return closest.

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ (Say it once in Kanglish so it sticks):
    → "Array sort ಮಾಡಿ, i fix ಮಾಡಿ, L=i+1, R=n-1 ಇಟ್ಟು, current sum
        target ಗಿಂತ ಹತ್ತಿರ ಇದ್ರೆ closest update ಮಾಡು. sum < target
        ಆದ್ರೆ L++, sum > target ಆದ್ರೆ R--, sum == target ಆದ್ರೆ ಅದೇ
        final answer — ತಕ್ಷಣ return ಮಾಡು!"

  Time  : O(n²)  →  Why: O(n log n) sort + O(n) outer loop × O(n) two-pointer scan
  Space : O(1) extra →  Why: sort in-place, only a few scalar trackers used

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 8 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: nums = [-1, 2, 1, -4], target = 1
  Sorted: [-4, -1, 1, 2]

  i=0 (nums[i]=-4)  →  L=1,R=3 → total=-4-1+2=-3 → |−3−1|=4 → closest=-3
                       → total<target(-3<1) → L=2
                       → L=2,R=3 → total=-4+1+2=-1 → |−1−1|=2<4 → closest=-1
                       → total<target(-1<1) → L=3, loop ends (L<R fails)
  i=1 (nums[i]=-1)  →  L=2,R=3 → total=-1+1+2=2 → |2-1|=1<2 → closest=2
                       → total>target(2>1) → R=2, loop ends (L<R fails)
  i=2 → n-3 boundary reached, loop ends

  Output: 2  (matches expected: -1+2+1=2)

  ಇನ್ನೊಂದು example — tricky case (exact match found early):
  Input: nums = [1, 1, 1, 0], target = -100
  Sorted: [0, 1, 1, 1]
  i=0 (nums[i]=0) → L=1,R=3 → total=0+1+1=2 → closest=2 → total>target → R=2
                    → L=1,R=2 → total=0+1+1=2 → same → total>target → R=1, loop ends
  i=1 (nums[i]=1) → L=2,R=3 → total=1+1+1=3 → |3-(-100)|=103, worse than |2-(-100)|=102 → closest stays 2
                    → total>target → R=2, loop ends
  Output: 2 (best achievable, far from target but nothing closer exists)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 9 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ Exactly 3 elements?            →  only one triplet possible, returned directly
  ✓ Exact match exists?            →  early-exit the moment total == target
  ✓ All same elements?             →  every triplet sum is identical, closest = that sum
  ✓ Target far outside all sums?   →  closest still finds the nearest achievable sum
  ✓ Negative numbers / negative target? → absolute difference handles sign correctly

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 10 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                Time      Space
  Brute Force   O(n³)     O(1)
  Optimal       O(n²)     O(1) extra    ← use this 

  Time ಯಾಕೆ ಅಷ್ಟು?  → Sort O(n log n), ನಂತರ ಪ್ರತಿ i ಗೂ two-pointer
                        scan O(n) — ಒಟ್ಟು O(n²) dominates.
  Space ಯಾಕೆ ಅಷ್ಟು? → Sort in-place, closest/L/R ಬಿಟ್ಟು ಬೇರೆ extra
                        structure ಬೇಡ.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 11 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Sort + Fix-One + Two-Pointer (running best-diff variant)

  ಈ pattern ಯಾವಾಗ use ಮಾಡಬೇಕು?
  → "k numbers ಇಂದ target ಗೆ EXACT ಅಲ್ಲ, CLOSEST sum ಬೇಕು" ಅಂತ
    ಕೇಳಿದಾಗ
  → 3Sum ನ two-pointer machinery ಗೊತ್ತಿದ್ರೆ, exact-match check ಅನ್ನ
    "update running best" check ಆಗಿ swap ಮಾಡಬಹುದಾ ಅಂತ ಯೋಚಿಸಿ

  ಇದೇ pattern ಬೇರೆ problems ನಲ್ಲಿ ಕಾಣಿಸುತ್ತೆ:
  → 3Sum (#15) — the exact-match sibling of this problem
  → 4Sum (#18) — same reduction, one more fixed element
  → Two Sum Closest variants (not on LeetCode directly, but common
    in interviews as a follow-up to Two Sum)

  Next time ಇಂತಹ problem ಬಂದ್ರೆ ನಾನು ಮೊದಲು ಇದನ್ನ think ಮಾಡ್ತೇನೆ:
  → "'Closest to target' ಕೇಳಿದ ತಕ್ಷಣ, ಇದು ಯಾವುದೋ Sum problem ನ
      variant ಅಂತ ಗೊತ್ತಾಗುತ್ತೆ — ಆ Sum problem ನ exact-match logic
      ಅನ್ನ running-best-diff logic ಆಗಿ swap ಮಾಡಿದ್ರೆ ಸಾಕು."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 12 — INTERVIEW ನಲ್ಲಿ ಹೇಗೆ EXPLAIN ಮಾಡಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "I need the sum of three numbers that gets as close as possible
      to a given target — not necessarily an exact match."

  2. Brute force:
     "Three nested loops checking every triplet and tracking the
      smallest absolute difference from target — O(n³). Workable for
      n=500 but not optimal."

  3. Optimize:
     "This is structurally identical to 3Sum — fixing one element
      turns the rest into a two-pointer search. I just replace the
      '== 0' check with 'track the closest sum so far'."

  4. Code:
     "Sort the array, fix i, and run L/R pointers on the remainder.
      Move L right if the sum is below target, R left if above, and
      return immediately if I hit an exact match since nothing can
      be closer than that."

  5. Complexity:
     "Time O(n²) — sort is O(n log n), dominated by the O(n) outer
      loop times O(n) two-pointer scan. Space O(1) extra."

  ಮುಖ್ಯ: ಸುಮ್ಮನೆ ಕೂತು code ಬರೆಯಬೇಡ!
         Interviewer ಗೆ ನಿನ್ನ thinking process ಕಾಣಬೇಕು.
"""


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(n^3) Time | O(1) Space
# ═══════════════════════════════════════════════════════════════════
def three_sum_closest_brute(nums, target):
    """ಇದು ಮೊದಲ ಆಲೋಚನೆ — three nested loops, track closest sum"""
    n = len(nums)
    closest = nums[0] + nums[1] + nums[2]
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                total = nums[i] + nums[j] + nums[k]
                if abs(total - target) < abs(closest - target):
                    closest = total
    return closest


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n^2) Time | O(1) Extra Space  (Sort + Two Pointers)
# ═══════════════════════════════════════════════════════════════════
def three_sum_closest(nums, target):
    """ಇದು final answer — sort ಮಾಡಿ, i fix ಮಾಡಿ, L/R two-pointer ಇಂದ closest track"""
    nums.sort()
    n = len(nums)
    closest = nums[0] + nums[1] + nums[2]

    for i in range(n - 2):
        left, right = i + 1, n - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if abs(total - target) < abs(closest - target):
                closest = total
            if total == target:
                return total
            elif total < target:
                left += 1
            else:
                right -= 1

    return closest


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")   # Windows cp1252 can't print emoji otherwise

    # Test 1 — Basic example
    assert three_sum_closest([-1, 2, 1, -4], 1) == 2

    # Test 2 — Edge case: exactly 3 elements
    assert three_sum_closest([0, 1, 2], 3) == 3

    # Test 3 — Edge case: all same elements
    assert three_sum_closest([1, 1, 1, 1], 100) == 3

    # Test 4 — Tricky: target far outside all achievable sums
    assert three_sum_closest([1, 1, 1, 0], -100) == 2

    print("All tests passed! ")
