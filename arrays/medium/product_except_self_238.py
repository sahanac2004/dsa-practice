"""
╔══════════════════════════════════════════════════════════════════╗
║  PRODUCT OF ARRAY EXCEPT SELF                                    ║
║  LeetCode #238  |  Difficulty: Medium  |  Topic: Arrays / Prefix  ║
║  Link: https://leetcode.com/problems/product-of-array-except-self/║
╚══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Given an array, return a new array where each index holds the
  product of ALL other elements (not itself). Division is NOT
  allowed, and the solution must run in O(n) time.

  Input : nums = [1, 2, 3, 4]
  Output: [24, 12, 8, 6]

  Example 1 — basic:
    Input : nums = [1, 2, 3, 4]
    Output: [24, 12, 8, 6]
    Why?  : result[0] = 2*3*4 = 24, result[1] = 1*3*4 = 12, etc.

  Example 2 — slightly tricky (contains a zero):
    Input : nums = [-1, 1, 0, -3, 3]
    Output: [0, 0, 9, 0, 0]
    Why?  : Every index except the zero's own index multiplies by
             that 0, wiping the product to 0. Only index 2 (the
             zero itself) skips multiplying by 0, giving (-1*1*-3*3)=9

  Constraints:
    - 2 <= nums.length <= 10^5
    - Product of any prefix/suffix fits in a 32-bit integer
    - Must solve without division, ideally O(n) time and O(1) extra space (excluding output)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ಮೊದಲು problem odidaga ನಮ್ಮ brain ಏನು think ಮಾಡಬೇಕು:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ (What are they asking?)
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  ಒಂದು integer array              │
  │  Output ಏನು ಬೇಕು?     →  ಪ್ರತಿ index ಗೆ, ಆ element      │
  │                          ಬಿಟ್ಟು ಬೇರೆ ಎಲ್ಲಾ ಗುಣಿಸಿದ product │
  │  Constraints ಏನಿದೆ?   →  DIVISION use ಮಾಡ್ಬಾರ್ದು, O(n)  │
  │                          time ಬೇಕು                        │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ನನಗೆ ಗೊತ್ತಿರೋ simple way ಏನು? (Brute force thought)
  →  ಪ್ರತಿ i ಗೂ, ಒಂದು inner loop ಹಾಕಿ ಉಳಿದ ಎಲ್ಲಾ elements ಗುಣಿಸೋದು.
  →  ಆದರೆ ಇದು slow ಯಾಕೆ? → O(n²) — n=10^5 ಗೆ 10^10 operations,
     TLE ಗ್ಯಾರಂಟಿ.

  ಹಂತ 3 — Better way ಹೇಗೆ ಯೋಚಿಸುವುದು? (Optimization thought)
  →  "Division allowed ಆಗಿದ್ರೆ, total product / nums[i] ಮಾಡ್ಬೋದಿತ್ತು.
     ಆದ್ರೆ division ಬೇಡ, ಮತ್ತೆ zero ಇದ್ರೆ divide ಮಾಡೋಕೆ ಆಗಲ್ಲ."
  →  ಅಹಾ moment: "result[i] = (i ಗಿಂತ ಮೊದಲಿನ ಎಲ್ಲಾ elements ನ
     product) × (i ಗಿಂತ ನಂತರದ ಎಲ್ಲಾ elements ನ product)" ಅಂತ
     ಬರೀಬಹುದಲ್ವಾ? ಇದೇ prefix product × suffix product!
  →  ಇದರಿಂದ ನಾವು Prefix Product + Suffix Product use ಮಾಡಬಹುದು!

  ಹಂತ 4 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  "except self" ಅಂದ್ರೆ ಎಡಗಡೆ ಎಲ್ಲಾ × ಬಲಗಡೆ ಎಲ್ಲಾ — ಇದನ್ನ
     ಎರಡು ಸಲ pass ಮಾಡಿ (left to right, right to left) ಬರೀಬಹುದು.
  →  Division ಬೇಡ ಅಂದಾಗ, running product accumulate ಮಾಡ್ತಾ
     ಹೋಗೋದೇ natural fit — prefix/suffix ಪ್ಯಾಟರ್ನ್ ಇದೇ ಕೆಲಸ.
  →  Output array ಅನ್ನೇ ಮೊದಲು prefix products store ಮಾಡೋಕೆ use
     ಮಾಡಿ, ನಂತರ suffix product ಅನ್ನ ಒಂದು single variable ಆಗಿ
     ಇಟ್ಟುಕೊಂಡ್ರೆ extra array ಬೇಡ — O(1) extra space (output ಬಿಟ್ಟು).

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು (Think out loud):
  →  "If division were allowed I'd just divide the total product by
      nums[i], but zeros make that break, and division is disallowed."
  →  "The brute force checks every pair, giving O(n²) — too slow for n=10^5."
  →  "I notice result[i] is just (product of everything left of i)
      times (product of everything right of i) — that's a prefix
      product pass and a suffix product pass, O(n) total."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Prefix Product + Suffix Product
  Secondary : Reuse output array to avoid extra O(n) space

  WHY this technique?
  → "Product except self" = left-product × right-product for each index
  → Division is banned, so running products (not total/x) is the way
  → Two linear passes (left→right, right→left) naturally build these

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION (How to think)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Key observation: result[i] = prefix[i-1] * suffix[i+1], where
  prefix[i] is the product of nums[0..i] and suffix[i] is the
  product of nums[i..n-1]. Both can be built with a single running
  variable in one pass each, instead of storing full prefix/suffix
  arrays.

  The journey from brute to optimal:
    Brute thought   →  for each i, multiply all other elements — O(n²)
    Problem with it →  too slow for n=10^5, and repeats work
    Better question →  "can I precompute what's needed instead of
                        recomputing it every time?"
    Insight         →  result[i] only needs everything-left × everything-right
    Optimal         →  one pass builds prefix products into result,
                        second pass multiplies in suffix products on the fly

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    For each index i, loop over the whole array again and multiply
    every element except nums[i].

  Pseudocode:
    step 1: for i in range(n):
    step 2:   product = 1
    step 3:   for j in range(n): if j != i: product *= nums[j]
    step 4:   result[i] = product

  Time  : O(n²)  →  Why: inner loop over n elements, for each of n outer indices
  Space : O(n)   →  Why: output array only (excluding it, O(1) extra)

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ? (Why is this not enough?)
    → n=10^5 ಆದ್ರೆ n² = 10^10 operations — TLE ಗ್ಯಾರಂಟಿ. ಪ್ರತಿ i ಗೂ
      ಪೂರ್ತಿ array ಮತ್ತೆ ಮತ್ತೆ scan ಮಾಡೋದು wasteful.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚶 SECTION 6 — APPROACH 2 — BETTER (prefix + suffix arrays)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Build a prefix[] array where prefix[i] = product of nums[0..i-1],
    and a suffix[] array where suffix[i] = product of nums[i+1..n-1].
    Then result[i] = prefix[i] * suffix[i].

  Time  : O(n)
  Space : O(n) for prefix[] + O(n) for suffix[] (plus output)

  ಇನ್ನೂ better ಮಾಡಬಹುದಾ? → ಹೌದು — suffix array ಬೇಡ, right-to-left
    pass ಮಾಡುವಾಗ ಒಂದೇ running variable ಇಟ್ಟುಕೊಂಡು ನೇರವಾಗಿ result[]
    (ಈಗಾಗಲೇ prefix products ಇಟ್ಟುಕೊಂಡಿರೋ) ಗೆ multiply ಮಾಡಿದ್ರೆ ಸಾಕು.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 7 — APPROACH 3 — OPTIMAL   (Prefix in result[] + running suffix)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    First pass (left to right): result[i] = product of everything
    strictly before i (result[0] = 1, since nothing is to its left).
    Second pass (right to left): keep a running suffix product,
    multiply it into result[i], then update the running product to
    include nums[i].

  Key steps:
    1. result[0] = 1; for i in 1..n-1: result[i] = result[i-1] * nums[i-1]
       (result[] now holds prefix products)
    2. suffix = 1
    3. for i from n-1 down to 0: result[i] *= suffix; suffix *= nums[i]

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ (Say it once in Kanglish so it sticks):
    → "ಎಡಗಡೆಯಿಂದ ಬಲಗಡೆಗೆ ಹೋಗ್ತಾ, result[i] ನಲ್ಲಿ ಎಡಗಡೆ product
        store ಮಾಡು. ನಂತರ ಬಲಗಡೆಯಿಂದ ಎಡಗಡೆಗೆ ಹೋಗ್ತಾ, ಒಂದು suffix
        variable ಇಟ್ಟುಕೊಂಡು, result[i] ಗೆ ಆ suffix ಗುಣಿಸಿ, ಆಮೇಲೆ
        suffix ಗೆ nums[i] ಸೇರಿಸು (ಗುಣಿಸು)!"

  Time  : O(n)  →  Why: exactly two linear passes over the array
  Space : O(1) extra →  Why: only the output array (required) and one running suffix variable

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 8 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: nums = [1, 2, 3, 4]

  Pass 1 (prefix, left to right):
  i=0  →  result[0] = 1 (nothing to the left)
  i=1  →  result[1] = result[0] * nums[0] = 1 * 1 = 1
  i=2  →  result[2] = result[1] * nums[1] = 1 * 2 = 2
  i=3  →  result[3] = result[2] * nums[2] = 2 * 3 = 6
  result after pass 1 = [1, 1, 2, 6]

  Pass 2 (suffix, right to left), suffix starts at 1:
  i=3  →  result[3] = 6 * suffix(1) = 6  →  suffix = 1 * nums[3](4) = 4
  i=2  →  result[2] = 2 * suffix(4) = 8  →  suffix = 4 * nums[2](3) = 12
  i=1  →  result[1] = 1 * suffix(12) = 12  →  suffix = 12 * nums[1](2) = 24
  i=0  →  result[0] = 1 * suffix(24) = 24  →  suffix = 24 * nums[0](1) = 24

  Output: [24, 12, 8, 6]

  ಇನ್ನೊಂದು example — tricky case (contains a zero):
  Input: nums = [-1, 1, 0, -3, 3]
  Pass 1 (prefix): result = [1, -1, -1, 0, 0]
  Pass 2 (suffix, from right), suffix=1:
    i=4: result[4]=0*1=0, suffix=1*3=3
    i=3: result[3]=0*3=0, suffix=3*-3=-9
    i=2: result[2]=-1*-9=9, suffix=-9*0=0
    i=1: result[1]=-1*0=0, suffix=0*1=0
    i=0: result[0]=1*0=0, suffix=0*-1=0
  Output: [0, 0, 9, 0, 0]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 9 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ Exactly 2 elements?           →  result[0]=nums[1], result[1]=nums[0], falls out naturally
  ✓ Single zero in array?         →  every OTHER index becomes 0; the zero's own index gets the real product
  ✓ Two or more zeros?            →  every index becomes 0 (no index can exclude both zeros)
  ✓ Negative numbers?             →  products just carry sign correctly through both passes
  ✓ All ones?                     →  every result is 1 (product of the rest is trivially 1)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 10 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                Time      Space
  Brute Force   O(n²)     O(1) extra (excluding output)
  Better        O(n)      O(n) extra (separate prefix[] + suffix[] arrays)
  Optimal       O(n)      O(1) extra    ← use this ✅

  Time ಯಾಕೆ ಅಷ್ಟು?  → ಎರಡು ಸಲ ಮಾತ್ರ array ಪೂರ್ತಿ scan ಮಾಡ್ತೀವಿ —
                        ಒಟ್ಟು 2n ≈ O(n).
  Space ಯಾಕೆ ಅಷ್ಟು? → prefix products ಅನ್ನೇ output array ನಲ್ಲಿ store
                        ಮಾಡಿ, suffix ಅನ್ನ ಒಂದೇ scalar variable ಆಗಿ
                        ಇಟ್ಟುಕೊಂಡಿದ್ರಿಂದ ಬೇರೆ extra array ಬೇಡ.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 11 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Prefix/Suffix Aggregate (product variant)

  ಈ pattern ಯಾವಾಗ use ಮಾಡಬೇಕು?
  → "ಪ್ರತಿ index ಗೂ, ಎಡಗಡೆ + ಬಲಗಡೆ ಇಂದ ಏನೋ combine ಮಾಡಿ answer
    ಬೇಕು" ಅಂತ ಕೇಳಿದಾಗ (sum, product, max, min ಯಾವುದೇ ಆಗಿರ್ಬೋದು)
  → Division ಅಥವಾ ಒಂದೇ pass ನಲ್ಲಿ ಸಾಧ್ಯ ಆಗದ operation ಬೇಡ ಅಂತ
    constraint ಇದ್ದಾಗ

  ಇದೇ pattern ಬೇರೆ problems ನಲ್ಲಿ ಕಾಣಿಸುತ್ತೆ:
  → Trapping Rain Water (#42) — prefix max / suffix max per index
  → Maximum Product Subarray (#152) — running prefix product with sign flips
  → Subarray Sum Equals K (#560) — prefix SUM instead of product

  Next time ಇಂತಹ problem ಬಂದ್ರೆ ನಾನು ಮೊದಲು ಇದನ್ನ think ಮಾಡ್ತೇನೆ:
  → "'Except self' ಅಥವಾ 'ಎಡ+ಬಲ combine' ಕೇಳಿದ ತಕ್ಷಣ, prefix pass
      ಮತ್ತು suffix pass ಬೇರೆ ಬೇರೆ ಮಾಡ್ಬೋದಾ ಅಂತ ಮೊದಲು ಯೋಚಿಸು.
      Output array ಅನ್ನೇ ಒಂದು pass ಗೆ reuse ಮಾಡಿ space ಉಳಿಸ್ಬಹುದು."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 12 — INTERVIEW ನಲ್ಲಿ ಹೇಗೆ EXPLAIN ಮಾಡಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "For each index, I need the product of every other element,
      without using division, in O(n) time."

  2. Brute force:
     "The naive approach recomputes the product of all other
      elements for every index — O(n²), too slow for n=10^5."

  3. Optimize:
     "result[i] is just the product of everything to its left times
      everything to its right. I can compute left-products in one
      pass and right-products in another, without ever dividing."

  4. Code:
     "First pass left-to-right fills result[i] with the prefix
      product (everything before i). Second pass right-to-left keeps
      a running suffix product, multiplies it into result[i], then
      extends it to include nums[i]."

  5. Complexity:
     "Time O(n) — two linear passes. Space O(1) extra, since the
      output array itself holds the prefix products and I only need
      one extra scalar for the running suffix product."

  ಮುಖ್ಯ: ಸುಮ್ಮನೆ ಕೂತು code ಬರೆಯಬೇಡ!
         Interviewer ಗೆ ನಿನ್ನ thinking process ಕಾಣಬೇಕು.
"""


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(n^2) Time | O(1) Extra Space
# ═══════════════════════════════════════════════════════════════════
def product_except_self_brute(nums):
    """ಇದು ಮೊದಲ ಆಲೋಚನೆ — ಪ್ರತಿ i ಗೂ ಉಳಿದ ಎಲ್ಲಾ elements ಗುಣಿಸೋದು"""
    n = len(nums)
    result = []
    for i in range(n):
        product = 1
        for j in range(n):
            if j != i:
                product *= nums[j]
        result.append(product)
    return result


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n) Time | O(1) Extra Space  (Prefix + Running Suffix)
# ═══════════════════════════════════════════════════════════════════
def product_except_self(nums):
    """ಇದು final answer — prefix products result[] ನಲ್ಲಿ, ನಂತರ running suffix ಗುಣಿಸೋದು"""
    n = len(nums)
    result = [1] * n

    for i in range(1, n):
        result[i] = result[i - 1] * nums[i - 1]

    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]

    return result


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")   # Windows cp1252 can't print emoji otherwise

    # Test 1 — Basic example
    assert product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]

    # Test 2 — Edge case: exactly 2 elements
    assert product_except_self([3, 5]) == [5, 3]

    # Test 3 — Edge case: all same elements (ones)
    assert product_except_self([1, 1, 1, 1]) == [1, 1, 1, 1]

    # Test 4 — Tricky: contains a zero and negative numbers
    assert product_except_self([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]

    print("All tests passed! ✅")
