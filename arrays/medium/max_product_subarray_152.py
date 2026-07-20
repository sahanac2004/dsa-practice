"""
╔══════════════════════════════════════════════════════════════════╗
║  MAXIMUM PRODUCT SUBARRAY                                        ║
║  LeetCode #152  |  Difficulty: Medium  |  Topic: Arrays / DP      ║
║  Link: https://leetcode.com/problems/maximum-product-subarray/    ║
╚══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Given an integer array (can include negatives and zeros), find the
  contiguous subarray with the LARGEST product, and return that
  product.

  Input : nums = [2, 3, -2, 4]
  Output: 6

  Example 1 — basic:
    Input : nums = [2, 3, -2, 4]
    Output: 6
    Why?  : subarray [2, 3] has product 6, the largest possible
             (the whole array's product is -48, dragged negative by -2)

  Example 2 — slightly tricky (two negatives flip to a big positive):
    Input : nums = [-2, 3, -4]
    Output: 24
    Why?  : the whole array's product = (-2)*3*(-4) = 24 — the two
             negatives cancel out, so including everything wins here,
             unlike Example 1 where a single negative should be excluded

  Constraints:
    - 1 <= nums.length <= 1000
    - -10 <= nums[i] <= 10
    - Subarray must be contiguous and non-empty
    - Product can flip sign entirely based on how many negatives are included

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ಮೊದಲು problem odidaga ನಮ್ಮ brain ಏನು think ಮಾಡಬೇಕು:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ (What are they asking?)
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  negative/positive/zero ಇರೋ      │
  │                          integer array                     │
  │  Output ಏನು ಬೇಕು?     →  contiguous subarray ನ ಗರಿಷ್ಠ    │
  │                          product                           │
  │  Constraints ಏನಿದೆ?   →  negatives ಇರೋದ್ರಿಂದ sign flip    │
  │                          ಆಗ್ಬೋದು, zero ಸಹ ಇರ್ಬೋದು          │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ನನಗೆ ಗೊತ್ತಿರೋ simple way ಏನು? (Brute force thought)
  →  ಪ್ರತಿ subarray (i,j) ಗೂ product ಲೆಕ್ಕ ಹಾಕಿ max track ಮಾಡೋದು.
  →  ಆದರೆ ಇದು slow ಯಾಕೆ? → O(n²) subarrays, ಪ್ರತಿ product ಕೂಡ
     O(n) ಗೆ ಹೋಗ್ಬೋದು — total O(n³) (ಅಥವಾ prefix products ಬಳಸಿ
     O(n²)) — n=1000 ಗೆ ಇನ್ನೂ ಸಾಕಷ್ಟು slow.

  ಹಂತ 3 — Better way ಹೇಗೆ ಯೋಚಿಸುವುದು? (Optimization thought)
  →  "Maximum Subarray (Kadane's, sum version) ನಲ್ಲಿ, ಪ್ರತಿ i ಗೂ
     'ಇಲ್ಲಿ ತನಕ ಬಂದಿರೋ best sum' track ಮಾಡಿದ್ವಿ. Product ಗೆ ಅದೇ
     idea use ಮಾಡ್ಬೋದಾ?"
  →  ಅಹಾ moment: Sum ಗೆ negative number add ಮಾಡಿದ್ರೆ ಕಡಿಮೆ ಆಗುತ್ತೆ
     ಅಷ್ಟೇ, ಆದ್ರೆ PRODUCT ಗೆ ಒಂದು negative ಗುಣಿಸಿದ್ರೆ SIGN ಫ್ಲಿಪ್
     ಆಗುತ್ತೆ! ಅಂದ್ರೆ ಇಲ್ಲಿ ತನಕ ಇದ್ದ "ಅತ್ಯಂತ ಚಿಕ್ಕ (most negative)"
     product ಸಹ ಒಂದು ಮುಂದಿನ negative ಸಿಕ್ಕಾಗ "ಅತ್ಯಂತ ದೊಡ್ಡ" ಆಗಿ
     ಬದಲಾಗ್ಬೋದು! ಆದ್ದರಿಂದ ಪ್ರತಿ i ಗೂ ಎರಡೂ track ಮಾಡ್ಬೇಕು — max
     AND min ಇಲ್ಲಿ ತನಕದ product.
  →  ಇದರಿಂದ ನಾವು DP → Track Running Min & Max use ಮಾಡಬಹುದು!

  ಹಂತ 4 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  Product ನಲ್ಲಿ negative × negative = positive — sign flip ಆಗೋ
     ಸಾಧ್ಯತೆ ಇರೋದ್ರಿಂದ, only "max so far" track ಮಾಡಿದ್ರೆ ಸಾಲಲ್ಲ.
  →  ಪ್ರತಿ index ಗೂ, current element ಇಂದ (previous max × current)
     ಅಥವಾ (previous min × current) ಅಥವಾ (current ಒಂದೇ) — ಈ ಮೂರರಲ್ಲಿ
     ದೊಡ್ಡ value ಯೇ ಆ index ಗೆ new max ಆಗುತ್ತೆ (ಚಿಕ್ಕದೇ new min).
  →  Zero ಸಿಕ್ಕಾಗ, product reset ಆಗುತ್ತೆ (0 ಗುಣಿಸಿದ್ರೆ ಎಲ್ಲಾ 0) —
     ಆದ್ರೆ current element ಒಂದೇ ಆಗಿ ಮತ್ತೆ start ಮಾಡೋಕೆ ಆಗುತ್ತೆ,
     ಇದನ್ನ max(current, prevMax*current, prevMin*current) formula
     ಸ್ವಾಭಾವಿಕವಾಗಿ handle ಮಾಡುತ್ತೆ.

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು (Think out loud):
  →  "This looks like Kadane's algorithm, but for products instead
      of sums."
  →  "The brute force checks every subarray's product — O(n²) or
      worse, and doesn't scale well."
  →  "The key difference from Kadane's sum version is that a negative
      number can flip the most negative running product into the
      most positive one — so at each step I need to track both a
      running max AND a running min."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Dynamic Programming (1D) → Track Running Min & Max
  Secondary : Kadane's-style single pass

  WHY this technique?
  → Product (unlike sum) can flip sign — a very negative running
    product can become the best positive one after one more negative
  → Tracking only a running max (like sum-Kadane's) would silently
    lose the best answer whenever a negative number shows up
  → Single pass, O(1) extra state (curMax, curMin) — no need to
    revisit earlier elements

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION (How to think)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Key observation: at every index, the best product ending here is
  either the element itself (restart), or the element times the
  best product ending at the previous index — but "best" could mean
  the most positive OR the most negative previous product, because
  a negative current element swaps their roles.

  The journey from brute to optimal:
    Brute thought   →  check every subarray's product, O(n²) or worse
    Problem with it →  too slow, and doesn't reuse any earlier work
    Better question →  "can I extend Kadane's sum trick to products?"
    Insight         →  negatives flip sign, so track BOTH running
                        max and running min ending at each index
    Optimal         →  single pass updating (curMax, curMin) together,
                        recording the global best curMax seen

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    For every starting index i, extend the subarray one element at a
    time, keeping a running product, and update the global best.

  Pseudocode:
    step 1: best = nums[0]
    step 2: for i in range(n):
    step 3:   product = 1
    step 4:   for j in range(i, n): product *= nums[j]; best = max(best, product)
    step 5: return best

  Time  : O(n²)  →  Why: for each start i, extend through the rest of the array
  Space : O(1)   →  Why: only a running product and best value tracked

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ? (Why is this not enough?)
    → n=1000 ಗೆ n² = 10^6 — ಇದು ನಿಜವಾಗ್ಲೂ pass ಆಗ್ಬೋದು, ಆದ್ರೆ
      Kadane's-style single pass ಇಂದ O(n) ಗೆ ಇಳಿಸ್ಬೋದು ಅಂತ ಗೊತ್ತಾದ್ರೆ
      ಯಾಕೆ ಬಿಡೋದು.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚶 SECTION 6 — APPROACH 2 — BETTER (skip — brute jumps straight to optimal)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ಇಲ್ಲಿ intermediate approach ಇಲ್ಲ — running min/max insight ಸಿಕ್ಕ
  ತಕ್ಷಣ ನೇರವಾಗಿ optimal ಗೆ ಹೋಗಬಹುದು.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 7 — APPROACH 3 — OPTIMAL   (Track Running Min & Max)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Keep curMax and curMin — the best and worst product of a
    subarray ENDING at the current index. At each new element, if
    the element itself is negative, swap curMax and curMin first
    (since multiplying by a negative flips which one becomes bigger),
    then update both against "just this element alone" vs "extending
    the previous best/worst". Track the global best curMax seen.

  Key steps:
    1. curMax = curMin = best = nums[0]
    2. For i from 1 to n-1:
         if nums[i] < 0: swap(curMax, curMin)
         curMax = max(nums[i], curMax * nums[i])
         curMin = min(nums[i], curMin * nums[i])
         best = max(best, curMax)
    3. Return best.

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ (Say it once in Kanglish so it sticks):
    → "curMax, curMin, best ಅನ್ನ nums[0] ಇಂದ start ಮಾಡು. ಪ್ರತಿ
        next element negative ಆಗಿದ್ರೆ ಮೊದಲು curMax, curMin swap
        ಮಾಡು. ಆಮೇಲೆ curMax = max(element, curMax*element), curMin
        = min(element, curMin*element), best = max(best, curMax)
        ಅಂತ update ಮಾಡ್ತಾ ಹೋಗು!"

  Time  : O(n)  →  Why: single pass through the array
  Space : O(1)  →  Why: only curMax, curMin, best scalars tracked

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 8 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: nums = [2, 3, -2, 4]

  Init: curMax=2, curMin=2, best=2

  i=1 (nums[i]=3)   → not negative, no swap
                      curMax=max(3, 2*3)=6, curMin=min(3, 2*3)=3
                      best=max(2,6)=6
  i=2 (nums[i]=-2)  → negative! swap curMax,curMin → curMax=3, curMin=6
                      curMax=max(-2, 3*-2)=max(-2,-6)=-2
                      curMin=min(-2, 6*-2)=min(-2,-12)=-12
                      best=max(6,-2)=6
  i=3 (nums[i]=4)   → not negative, no swap
                      curMax=max(4, -2*4)=max(4,-8)=4
                      curMin=min(4, -12*4)=min(4,-48)=-48
                      best=max(6,4)=6

  Output: 6 (matches expected — subarray [2,3])

  ಇನ್ನೊಂದು example — tricky case (two negatives cancel to a big positive):
  Input: nums = [-2, 3, -4]
  Init: curMax=-2, curMin=-2, best=-2

  i=1 (nums[i]=3)   → not negative, no swap
                      curMax=max(3, -2*3)=max(3,-6)=3
                      curMin=min(3, -2*3)=min(3,-6)=-6
                      best=max(-2,3)=3
  i=2 (nums[i]=-4)  → negative! swap curMax,curMin → curMax=-6, curMin=3
                      curMax=max(-4, -6*-4)=max(-4,24)=24
                      curMin=min(-4, 3*-4)=min(-4,-12)=-12
                      best=max(3,24)=24

  Output: 24 (matches expected — the whole array, negatives cancel out)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 9 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ Single element?                →  best = that element itself, loop never runs
  ✓ Contains a zero?                →  curMax/curMin reset to the zero (or restart
                                        fresh at the next element) via the max(element, ...) term
  ✓ All negative numbers?          →  swap logic + the running formulas find the
                                        best even-length product automatically
  ✓ All negative, odd count?       →  best ends up being a single element (least
                                        negative one) since no full-array product works
  ✓ Two negatives with a zero between? → each side of the zero is handled as an
                                        independent restart, no cross-contamination

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 10 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                Time      Space
  Brute Force   O(n²)     O(1)
  Optimal       O(n)      O(1)    ← use this ✅

  Time ಯಾಕೆ ಅಷ್ಟು?  → ಒಂದೇ pass ನಲ್ಲಿ ಪ್ರತಿ element ಅನ್ನ ಒಂದೇ ಸಲ
                        visit ಮಾಡ್ತೀವಿ — O(n).
  Space ಯಾಕೆ ಅಷ್ಟು? → curMax, curMin, best ಬಿಟ್ಟು ಬೇರೆ extra
                        structure ಬೇಡ.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 11 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Kadane's Variant — Track Running Min & Max (sign-flip aware)

  ಈ pattern ಯಾವಾಗ use ಮಾಡಬೇಕು?
  → Contiguous subarray/subsequence ಇಂದ MAX ಬೇಕು, ಆದ್ರೆ operation
    sign-flip ಆಗೋ ಸಾಧ್ಯತೆ ಇರುತ್ತೆ (product with negatives) ಅಂತ
    ಇದ್ದಾಗ
  → ಬರೀ "running max" track ಮಾಡಿದ್ರೆ ಸಾಲಲ್ಲ ಅಂತ ಗೊತ್ತಾದಾಗ — worst
    case ಸಹ future ಗೆ best ಆಗ್ಬಹುದು ಅಂತ ಯೋಚಿಸಿದಾಗ

  ಇದೇ pattern ಬೇರೆ problems ನಲ್ಲಿ ಕಾಣಿಸುತ್ತೆ:
  → Maximum Subarray / Kadane's (#53) — the sum-only sibling (no min needed)
  → Best Time to Buy and Sell Stock III/IV (#123, #188) — state-machine DP,
    tracks multiple running states at once
  → Product of Array Except Self (#238) — different problem, but same
    "track running product both directions" flavor

  Next time ಇಂತಹ problem ಬಂದ್ರೆ ನಾನು ಮೊದಲು ಇದನ್ನ think ಮಾಡ್ತೇನೆ:
  → "Contiguous subarray ಇಂದ product/multiplication based max ಕೇಳಿದ
      ತಕ್ಷಣ, negatives sign flip ಮಾಡ್ತಾವೆ ಅಂತ ನೆನಪಿಟ್ಟುಕೊಂಡು, running
      max ಜೊತೆ running min ಸಹ track ಮಾಡ್ಬೇಕು ಅಂತ ಮೊದಲು ಯೋಚಿಸು."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 12 — INTERVIEW ನಲ್ಲಿ ಹೇಗೆ EXPLAIN ಮಾಡಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "I need the contiguous subarray with the largest product —
      negatives and zeros can appear, so the product's sign can
      swing either way as the subarray grows."

  2. Brute force:
     "Try every subarray and compute its product directly — O(n²).
      Workable for n=1000, but there's a linear-time approach."

  3. Optimize:
     "This is Kadane's algorithm, but for products. The twist is
      that multiplying by a negative number can turn the smallest
      running product into the largest one, so I need to track both
      a running max AND a running min at every index."

  4. Code:
     "At each element, if it's negative, I swap my running max and
      min first. Then I update both as max/min of (the element
      alone) versus (element times the previous running value), and
      record the best max seen."

  5. Complexity:
     "Time O(n) — single pass. Space O(1) — just three running
      scalars: current max, current min, and the global best."

  ಮುಖ್ಯ: ಸುಮ್ಮನೆ ಕೂತು code ಬರೆಯಬೇಡ!
         Interviewer ಗೆ ನಿನ್ನ thinking process ಕಾಣಬೇಕು.
"""


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(n^2) Time | O(1) Space
# ═══════════════════════════════════════════════════════════════════
def max_product_brute(nums):
    """ಇದು ಮೊದಲ ಆಲೋಚನೆ — ಪ್ರತಿ start index ಇಂದ extend ಮಾಡ್ತಾ product track"""
    n = len(nums)
    best = nums[0]
    for i in range(n):
        product = 1
        for j in range(i, n):
            product *= nums[j]
            best = max(best, product)
    return best


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n) Time | O(1) Space  (Track Running Min & Max)
# ═══════════════════════════════════════════════════════════════════
def max_product(nums):
    """ಇದು final answer — negative ಸಿಕ್ಕಾಗ curMax/curMin swap ಮಾಡಿ track"""
    cur_max = cur_min = best = nums[0]

    for num in nums[1:]:
        if num < 0:
            cur_max, cur_min = cur_min, cur_max
        cur_max = max(num, cur_max * num)
        cur_min = min(num, cur_min * num)
        best = max(best, cur_max)

    return best


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")   # Windows cp1252 can't print emoji otherwise

    # Test 1 — Basic example
    assert max_product([2, 3, -2, 4]) == 6

    # Test 2 — Edge case: single element
    assert max_product([-5]) == -5

    # Test 3 — Edge case: contains a zero, splitting the array
    assert max_product([0, 2, -3, 4, 0, -1]) == 4

    # Test 4 — Tricky: two negatives cancel to a big positive
    assert max_product([-2, 3, -4]) == 24

    print("All tests passed! ✅")
