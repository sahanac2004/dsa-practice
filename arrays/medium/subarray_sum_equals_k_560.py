"""
╔══════════════════════════════════════════════════════════════════════╗
║  SUBARRAY SUM EQUALS K                                               ║
║  LeetCode #560  |  Difficulty: Medium  |  Topic: Arrays / Prefix Sum ║
║  Link: https://leetcode.com/problems/subarray-sum-equals-k/          ║
╚══════════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Given an integer array and a target k, count how many CONTIGUOUS
  subarrays sum exactly to k. Array can contain negatives, so a
  sliding window won't directly work.

  Input : nums = [1, 1, 1], k = 2
  Output: 2

  Example 1 — basic:
    Input : nums = [1, 1, 1], k = 2
    Output: 2
    Why?  : subarrays [1,1] (index 0-1) and [1,1] (index 1-2) both sum to 2

  Example 2 — slightly tricky (negatives present):
    Input : nums = [1, -1, 0], k = 0
    Output: 3
    Why?  : [1,-1] sums to 0, [-1,0] sums to 0, and [0] alone sums to
             0 — negatives make multiple overlapping subarrays valid

  Constraints:
    - 1 <= nums.length <= 2 * 10^4
    - -1000 <= nums[i] <= 1000
    - -10^7 <= k <= 10^7
    - nums can contain negative numbers, zero, and positive numbers

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ಮೊದಲು problem odidaga ನಮ್ಮ brain ಏನು think ಮಾಡಬೇಕು:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ (What are they asking?)
  ┌────────────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  integer array (negatives ಸಹ) + k     │
  │  Output ಏನು ಬೇಕು?     →  sum == k ಆಗಿರೋ contiguous          │
  │                          subarrays ಎಷ್ಟು ಇವೆ ಅಂತ count        │
  │  Constraints ಏನಿದೆ?   →  n=2*10^4, negatives ಇವೆ (sliding      │
  │                          window ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡಲ್ಲ)             │
  └────────────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ನನಗೆ ಗೊತ್ತಿರೋ simple way ಏನು? (Brute force thought)
  →  ಪ್ರತಿ (i,j) pair ಗೂ subarray sum ಲೆಕ್ಕ ಹಾಕಿ k ಜೊತೆ compare ಮಾಡೋದು.
  →  ಆದರೆ ಇದು slow ಯಾಕೆ? → O(n²) ಅಥವಾ O(n³), n=2*10^4 ಗೆ 4*10^8+
     operations — TLE ಆಗುತ್ತೆ.

  ಹಂತ 3 — Better way ಹೇಗೆ ಯೋಚಿಸುವುದು? (Optimization thought)
  →  "Product of Array Except Self ನಲ್ಲಿ prefix concept use ಮಾಡಿದ್ವಿ.
     ಇಲ್ಲಿ ಸಹ, prefixSum[j] - prefixSum[i-1] = k ಅಂದ್ರೆ subarray
     (i,j) sum = k ಅಂತ. ಇದನ್ನ rearrange ಮಾಡಿದ್ರೆ prefixSum[i-1] =
     prefixSum[j] - k."
  →  ಅಹಾ moment: ಪ್ರತಿ index j ಗೂ, "ನಾನು ಇಲ್ಲಿ ತನಕ ಎಷ್ಟು ಸಲ
     (prefixSum[j] - k) ಅನ್ನೋ prefix sum ಈಗಾಗಲೇ ಬಂದಿದೆ" ಅಂತ ಗೊತ್ತಿದ್ರೆ,
     ಆ ಎಷ್ಟು ಸಲ ಇದೆಯೋ ಅಷ್ಟು subarrays sum=k ಆಗಿರುತ್ತೆ! ಇದನ್ನ HashMap
     ನಲ್ಲಿ prefix sum ಗಳ frequency track ಮಾಡಿ ಒಂದೇ pass ನಲ್ಲಿ ಮಾಡ್ಬೋದು.
  →  ಇದರಿಂದ ನಾವು Prefix Sum + HashMap (running frequency) use ಮಾಡಬಹುದು!

  ಹಂತ 4 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  Negatives ಇರೋದ್ರಿಂದ sliding window (monotonic sum growth
     assumption) ಕೆಲಸ ಮಾಡಲ್ಲ — sum ಯಾವಾಗ್ಬೇಕಾದ್ರೂ ಕಡಿಮೆ ಆಗ್ಬೋದು.
  →  Prefix sum ಇಂದ, ಯಾವುದೇ subarray sum ಅನ್ನ two prefix sums ನ
     difference ಆಗಿ express ಮಾಡ್ಬಹುದು — ಇದೇ two-sum-style lookup ಗೆ
     ಪರಿವರ್ತಿಸುತ್ತೆ.
  →  "Count எத்தனை times seen" ಅಂತ ಕೇಳ್ತಾ ಇರೋದ್ರಿಂದ HashMap frequency
     count ideal fit.

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು (Think out loud):
  →  "Since negatives are allowed, a sliding window won't work here
      because the running sum isn't monotonic."
  →  "The brute force checks every subarray sum directly — O(n²),
      too slow for n up to 2*10^4."
  →  "I notice that subarray sum from i to j equals prefixSum[j] minus
      prefixSum[i-1] — so for each j, I just need to know how many
      earlier prefix sums equal prefixSum[j] - k, which a hashmap
      gives me in O(1)."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Prefix Sum → HashMap (running frequency)
  Secondary : None

  WHY this technique?
  → Negative numbers break sliding window's monotonic-sum assumption
  → Any subarray sum = difference of two prefix sums — reduces the
    problem to a two-sum-style lookup
  → We need a COUNT of matches, so a frequency hashmap (not a set)
    fits perfectly, built incrementally in one pass

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION (How to think — English)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Key observation: sum(i..j) = prefixSum[j] - prefixSum[i-1]. So
  sum(i..j) == k means prefixSum[i-1] == prefixSum[j] - k. As we scan
  left to right building the running prefix sum, at each j we just
  look up how many times (prefixSum[j] - k) has already occurred.

  The journey from brute to optimal:
    Brute thought   →  compute every subarray's sum directly, O(n²)
    Problem with it →  too slow for n = 2*10^4, and repeats work
    Better question →  "can I express subarray sum via two prefix
                        sums and turn this into a lookup?"
    Insight         →  sum(i..j)=k  <=>  prefixSum[i-1] = prefixSum[j]-k
    Optimal         →  single pass, hashmap of prefix-sum frequencies
                        seen so far, add matches as we go

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    For every starting index i, extend the subarray one element at a
    time, keeping a running sum, and count whenever that sum equals k.

  Pseudocode:
    step 1: count = 0
    step 2: for i in range(n):
    step 3:   running_sum = 0
    step 4:   for j in range(i, n): running_sum += nums[j]; if running_sum == k: count += 1
    step 5: return count

  Time  : O(n²)  →  Why: for each start i, extend through the rest of the array
  Space : O(1)   →  Why: only a running sum and counter tracked

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ? (Why is this not enough?)
    → n=2*10^4 ಗೆ n² = 4*10^8 — ಇದು TLE ಆಗುತ್ತೆ. Prefix sum + hashmap
      ಇಂದ O(n) ಗೆ ಇಳಿಸ್ಬೋದು.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚶 SECTION 6 — APPROACH 2 — BETTER (skip — brute jumps straight to optimal)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ಇಲ್ಲಿ intermediate approach ಇಲ್ಲ — prefix sum + hashmap insight
  ಸಿಕ್ಕ ತಕ್ಷಣ ನೇರವಾಗಿ optimal ಗೆ ಹೋಗಬಹುದು.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 7 — APPROACH 3 — OPTIMAL   (Prefix Sum + HashMap)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Walk through the array once, maintaining a running prefix sum and
    a hashmap of {prefix_sum: how many times seen so far}. Initialize
    the map with {0: 1} to handle subarrays that start at index 0. At
    each element, update the running sum, then add
    map.get(running_sum - k, 0) to the answer, then increment
    map[running_sum].

  Key steps:
    1. prefix_count = {0: 1}, running_sum = 0, count = 0
    2. for num in nums:
         running_sum += num
         count += prefix_count.get(running_sum - k, 0)
         prefix_count[running_sum] = prefix_count.get(running_sum, 0) + 1
    3. Return count

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ (Say it once in Kanglish so it sticks):
    → "prefix_count = {0:1} ಇಂದ start ಮಾಡು. ಪ್ರತಿ number ಗೂ
        running_sum ಗೆ add ಮಾಡು. ಆಮೇಲೆ (running_sum - k) ಎಷ್ಟು ಸಲ
        map ನಲ್ಲಿ ಇದೆಯೋ ಅಷ್ಟು count ಗೆ add ಮಾಡು. ಕೊನೆಗೆ running_sum
        ಅನ್ನ map ನಲ್ಲಿ increment ಮಾಡು!"

  Time  : O(n)  →  Why: single pass, O(1) average hashmap lookups
  Space : O(n)  →  Why: prefix sum frequency map can hold up to n entries

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 8 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: nums = [1, 1, 1], k = 2

  Init: prefix_count={0:1}, running_sum=0, count=0

  num=1  → running_sum=1
           count += prefix_count.get(1-2=-1, 0) = 0 → count=0
           prefix_count={0:1, 1:1}
  num=1  → running_sum=2
           count += prefix_count.get(2-2=0, 0) = 1 → count=1
           prefix_count={0:1, 1:1, 2:1}
  num=1  → running_sum=3
           count += prefix_count.get(3-2=1, 0) = 1 → count=2
           prefix_count={0:1, 1:1, 2:1, 3:1}

  Output: 2    matches expected

  ಇನ್ನೊಂದು example — tricky case (negatives, k=0):
  Input: nums = [1, -1, 0], k = 0
  Init: prefix_count={0:1}, running_sum=0, count=0

  num=1   → running_sum=1
            count += prefix_count.get(1-0=1, 0) = 0 → count=0
            prefix_count={0:1, 1:1}
  num=-1  → running_sum=0
            count += prefix_count.get(0-0=0, 0) = 1 → count=1
            prefix_count={0:2, 1:1}
  num=0   → running_sum=0
            count += prefix_count.get(0-0=0, 0) = 2 → count=3
            prefix_count={0:3, 1:1}

  Output: 3    matches expected ([1,-1], [-1,0], [0])

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 9 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ Single element?           →  works — checks if that element == k
  ✓ Whole array sums to k?    →  {0:1} initial entry catches this
                                  subarray starting at index 0
  ✓ Negative numbers present? →  prefix sums can repeat/decrease,
                                  hashmap counts handle it correctly
  ✓ Multiple zeros in a row?  →  each zero can extend a valid k=0
                                  window, frequency counting captures all
  ✓ k not achievable at all?  →  count simply stays 0, returned as-is

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 10 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                Time      Space
  Brute Force   O(n²)     O(1)
  Optimal       O(n)      O(n)    ← use this  

  Time ಯಾಕೆ ಅಷ್ಟು?  → ಒಂದೇ pass ನಲ್ಲಿ ಪ್ರತಿ element ಅನ್ನ ಒಂದೇ ಸಲ
                        visit ಮಾಡ್ತೀವಿ, hashmap lookup average O(1).
  Space ಯಾಕೆ ಅಷ್ಟು? → prefix sum frequencies ಇಡೋಕೆ hashmap — worst
                        case ಎಲ್ಲಾ prefix sums unique ಆಗಿದ್ರೆ n entries.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 11 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Prefix Sum + HashMap Frequency (Subarray Sum Lookup)

  ಈ pattern ಯಾವಾಗ use ಮಾಡಬೇಕು?
  → Contiguous subarray sum == target ಕೇಳಿದಾಗ, ಆದ್ರೆ negatives ಇರೋದ್ರಿಂದ
    sliding window ಕೆಲಸ ಮಾಡ್ದೇ ಇದ್ದಾಗ
  → "Count how many" ಅಂತ ಕೇಳಿದಾಗ (existence ಅಲ್ಲ, count ಬೇಕಾದಾಗ)
  → sum(i,j) ಅನ್ನ two prefix sums ನ difference ಆಗಿ express ಮಾಡ್ಬಹುದು
    ಅಂತ ಗೊತ್ತಾದಾಗ

  ಇದೇ pattern ಬೇರೆ problems ನಲ್ಲಿ ಕಾಣಿಸುತ್ತೆ:
  → Two Sum (#1) — same complement-lookup idea, just on raw values not prefix sums
  → Continuous Subarray Sum (#523) — prefix sum modulo k variant
  → Contiguous Array (#525) — prefix sum with 0/1 balance trick

  Next time ಇಂತಹ problem ಬಂದ್ರೆ ನಾನು ಮೊದಲು ಇದನ್ನ think ಮಾಡ್ತೇನೆ:
  → "Subarray sum == target, negatives ಇವೆ ಅಂತ ಕೇಳಿದ ತಕ್ಷಣ, sliding
      window ಅಲ್ಲ, prefix sum + hashmap complement lookup ಬಳಸು."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 12 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "I need to count how many contiguous subarrays sum exactly to
      k. The array can contain negatives, so sums aren't monotonic."

  2. Brute force:
     "Try every (i,j) subarray and sum it directly — O(n²), too slow
      for n up to 2*10^4."

  3. Optimize:
     "Since negatives break sliding window, I use prefix sums instead:
      sum(i,j) = prefixSum[j] - prefixSum[i-1]. So for each j, I just
      need to know how many earlier prefix sums equal
      prefixSum[j] - k."

  4. Code:
     "I will use a hashmap tracking prefix sum frequencies, seeded
      with {0: 1} for subarrays starting at index 0, updating the
      count and the map in a single pass."

  5. Complexity:
     "Time O(n) — one pass with O(1) average hashmap lookups. Space
      O(n) — the prefix sum frequency map can grow up to n entries."

  ಮುಖ್ಯ: ಸುಮ್ಮನೆ ಕೂತು code ಬರೆಯಬೇಡ!
         Interviewer ಗೆ ನಿನ್ನ thinking process ಕಾಣಬೇಕು.
"""


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(n^2) Time | O(1) Space
# ═══════════════════════════════════════════════════════════════════
def subarray_sum_brute(nums, k):
    """ಇದು ಮೊದಲ ಆಲೋಚನೆ — ಪ್ರತಿ start index ಇಂದ extend ಮಾಡ್ತಾ sum track"""
    n = len(nums)
    count = 0
    for i in range(n):
        running_sum = 0
        for j in range(i, n):
            running_sum += nums[j]
            if running_sum == k:
                count += 1
    return count


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n) Time | O(n) Space  (Prefix Sum + HashMap)
# ═══════════════════════════════════════════════════════════════════
def subarray_sum(nums, k):
    """ಇದು final answer — prefix sum frequency track ಮಾಡಿ complement lookup"""
    prefix_count = {0: 1}
    running_sum = 0
    count = 0

    for num in nums:
        running_sum += num
        count += prefix_count.get(running_sum - k, 0)
        prefix_count[running_sum] = prefix_count.get(running_sum, 0) + 1

    return count


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")   # Windows cp1252 can't print emoji otherwise

    # Test 1 — Basic example
    assert subarray_sum([1, 1, 1], 2) == 2

    # Test 2 — Edge case: single element equal to k
    assert subarray_sum([5], 5) == 1

    # Test 3 — Edge case: all same elements
    assert subarray_sum([1, 1, 1, 1], 2) == 3

    # Test 4 — Tricky: negatives and k = 0
    assert subarray_sum([1, -1, 0], 0) == 3

    print("All tests passed!  ")
