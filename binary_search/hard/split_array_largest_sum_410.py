"""
╔══════════════════════════════════════════════════════════════════╗
║  SPLIT ARRAY LARGEST SUM                                         ║
║  LeetCode #410  |  Difficulty: Hard  |  Topic: Binary Search    ║
║  Link: https://leetcode.com/problems/split-array-largest-sum/   ║
╚══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Given an integer array nums and an integer k, split nums into k
  non-empty subarrays such that the LARGEST SUM among all subarrays
  is MINIMIZED. Return that minimized largest sum.

  Input : nums = integer array, k = number of subarrays
  Output: minimized largest sum across all k subarrays

  Example 1 — basic:
    Input : nums=[7,2,5,10,8], k=2
    Output: 18
    Why?  : Best split: [7,2,5] and [10,8]
            sums = 14 and 18 → largest = 18
            Any other split gives larger "largest sum"
            e.g. [7] and [2,5,10,8]=25 → largest=25 ✗

  Example 2 — slightly tricky:
    Input : nums=[1,2,3,4,5], k=2
    Output: 9
    Why?  : Best split: [1,2,3] and [4,5]
            sums=6 and 9 → largest=9 ✓

  Constraints:
    - 1 <= nums.length <= 1000
    - 0 <= nums[i] <= 10^6
    - 1 <= k <= min(50, nums.length)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Problem odi aada mele namma brain enu think maadabeeku:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  nums array + k splits        │
  │  Output ಏನು ಬೇಕು?     →  minimize the LARGEST subarray │
  │                           sum among k subarrays         │
  │  Constraints ಏನಿದೆ?   →  subarrays contiguous,        │
  │                           order preserved               │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ನನಗೆ ಗೊತ್ತಿರೋ simple way ಏನು?
  →  All possible ways ಲ್ಲಿ k subarrays ಮಾಡಿ minimum of
     maximum ಹುಡುಕೋಣ → O(n^k) → too slow!
  →  DP ಕೂಡ possible → O(n² × k) → valid but binary search faster

  ಹಂತ 3 — Better way ಹೇಗೆ ಯೋಚಿಸುವುದು?
  →  "Capacity to Ship Packages #1011 ಅನ್ನು ನೆನಪಿಸ್ತಿದೆ!"
  →  Answer space: [max(nums), sum(nums)]
     min = max(nums) → each element its own subarray
     max = sum(nums) → entire array one subarray
  →  Monotonic: larger max_sum allowed → fewer subarrays needed
     if capacity C works in k pieces → C+1 also works!
  →  Binary search on capacity, check if k subarrays sufficient!

  ಹಂತ 4 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  EXACT SAME as Capacity to Ship Packages!
     "days" → "k subarrays", "weight" → "subarray sum limit"
  →  Feasibility: greedily split, count pieces needed
  →  Same template, different variable names!

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು:
  →  "This is identical to Capacity to Ship Packages!"
  →  "Binary search on answer [max(nums), sum(nums)]"
  →  "Feasibility: greedy split, count subarrays needed <= k"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Binary Search → On Answer Space
  Secondary : Greedy (feasibility check — greedy split count)

  WHY Binary Search on Answer Space?
  → "Minimize the largest sum" = find minimum valid capacity
  → Same monotonic property as Ship Packages
  → Feasibility: can we split into <= k pieces with max sum <= mid?

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Reframe: "What is the minimum capacity C such that we can split
  nums into AT MOST k subarrays each with sum <= C?"

  This is EXACTLY the same as: "What is the minimum ship capacity
  to ship packages in at most k days?" — just with "subarrays"
  instead of "days"!

  The journey from brute to optimal:
    Brute thought   →  Try all splits → O(n^k) or DP O(n²k)
    Problem with it →  DP valid but binary search cleaner/faster
    Better question →  "Can I binary search on the answer (capacity)?"
    Insight         →  YES! Same pattern as Ship Packages #1011
                       [max(nums), sum(nums)] range, greedy check
    Optimal         →  O(n log(sum)) — binary search + greedy

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE (DP)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    dp[i][j] = minimum largest sum when splitting nums[0..i]
               into j subarrays
    Transition: try all split points for last subarray

  Time  : O(n² × k)  →  Why: n positions × k splits × n transitions
  Space : O(n × k)   →  Why: DP table

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ?
    → Valid adu, but O(n log sum) binary search faster and simpler!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 6 — APPROACH 2 — OPTIMAL (Binary Search on Answer)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Binary search on the answer (max allowed subarray sum).
    For each mid, check if nums can be split into <= k subarrays
    each with sum <= mid (greedy split).

  Key steps:
    1. left=max(nums), right=sum(nums), ans=right
    2. While left <= right:
       a. mid = (left+right)//2
       b. if can_split(mid, k) → ans=mid, right=mid-1
       c. else → left=mid+1
    3. return ans

  can_split(max_sum, k):
    pieces=1, current=0
    for num in nums:
      if current + num > max_sum:
        pieces += 1       # start new subarray
        current = 0
      current += num
    return pieces <= k

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ:
    → "Answer space [max(nums), sum(nums)] ಮೇಲೆ binary search.
       Mid = max allowed subarray sum.
       Greedy: sum exceed ಆದ್ರೆ new piece start maadu, count maadu.
       Pieces <= k ಆದ್ರೆ → valid! Smaller try. Else larger try.
       Ship Packages EXACT same template!"

  Time  : O(n × log(sum(nums)))  →  Why: log steps × O(n) check
  Space : O(1)                   →  Why: only pointers

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 7 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: nums=[7,2,5,10,8], k=2
  left=10 (max), right=32 (sum)

  mid=21 → greedy: 7+2+5=14,+10=24>21 → piece2: 10+8=18
           pieces=2 <= k=2 ✓ → ans=21, right=20

  mid=15 → greedy: 7+2+5=14,+10=24>15 → piece2: 10,+8=18>15
           → piece3: 8 → pieces=3 > k=2 ✗ → left=16

  mid=18 → greedy: 7+2+5=14,+10=24>18 → piece2: 10+8=18
           pieces=2 <= k=2 ✓ → ans=18, right=17

  left=16, right=17
  mid=16 → greedy: 7+2+5=14,+10=24>16 → piece2: 10,+8=18>16
           → piece3: 8 → pieces=3 > k=2 ✗ → left=17

  mid=17 → greedy: 7+2+5=14,+10=24>17 → piece2: 10,+8=18>17
           → piece3: 8 → pieces=3 > k=2 ✗ → left=18

  left=18 > right=17 → return ans=18 ✓

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 8 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ k == n?         →  Each element own subarray → max(nums)
  ✓ k == 1?         →  One subarray = entire array → sum(nums)
  ✓ Single element? →  [5], k=1 → 5
  ✓ Zeros in array? →  Works fine, greedy handles naturally
  ✓ k > n?          →  Constrained: k <= n, so won't happen

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 9 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                Time               Space
  DP            O(n² × k)          O(n × k)
  Optimal       O(n × log(sum))    O(1)     ← use this ✅

  Time yaake O(n log sum)?
    → log(sum) binary search steps on answer range
    → Each step O(n) greedy feasibility check
  Space yaake O(1)?
    → Only left, right, mid, ans, current, pieces

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 10 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Binary Search on Answer Space (5th in series)

  Complete series so far:
  ┌──────────────┬─────────────────────┬───────────────────────┐
  │ Problem      │ Answer Range        │ Feasibility           │
  ├──────────────┼─────────────────────┼───────────────────────┤
  │ Koko   #875  │ [1, max(piles)]     │ sum(ceil(p/k)) <= h   │
  │ Bouq  #1482  │ [1, max(bloom)]     │ bouquets(day) >= m    │
  │ Div   #1283  │ [1, max(nums)]      │ sum(ceil(n/d))<=thresh│
  │ Ship  #1011  │ [max(w), sum(w)]    │ days_needed(c) <= d   │
  │ Split  #410  │ [max(n), sum(n)]    │ pieces(cap) <= k      │
  └──────────────┴─────────────────────┴───────────────────────┘

  Ship #1011 ಮತ್ತು Split #410 IDENTICAL template!
  Only difference: "days" → "k subarrays"

  Next time intaha problem bandre naanu modalu idannu think maadtene:
  → "Minimize maximum subarray sum beeka?
     → Binary Search on Answer! [max, sum] range.
     Greedy: exceed iddre new piece, count pieces <= k?"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 11 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "Split array into k subarrays minimizing the largest sum."

  2. Brute force:
     "DP — O(n²k). Valid but binary search is cleaner."

  3. Optimize:
     "Reframe: find minimum capacity C such that we can split
      into <= k subarrays each with sum <= C.
      This is IDENTICAL to Ship Packages #1011!
      Binary search on [max(nums), sum(nums)].
      Feasibility: greedy split, count pieces needed <= k."

  4. Code:
     "left=max(nums), right=sum(nums). For each mid, greedy:
      if current+num > mid → new piece, pieces++, current=0.
      If pieces<=k → feasible, save ans, try smaller."

  5. Complexity:
     "Time O(n log sum). Space O(1)."

  Mukhya: summane kuutu code bareyabeda!
          "Identical to Ship Packages" — say this, shows pattern!
          left=max(nums) why? — must fit largest element in one piece!
"""


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE (DP) — O(n²k) Time | O(nk) Space
# ═══════════════════════════════════════════════════════════════════
def split_array_dp(nums, k):
    """Idu DP approach — valid but O(n²k)"""
    n = len(nums)
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + nums[i]

    # dp[i][j] = min largest sum splitting nums[0..i-1] into j parts
    INF = float('inf')
    dp = [[INF] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 0

    for i in range(1, n + 1):
        for j in range(1, k + 1):
            for p in range(j - 1, i):
                # last subarray is nums[p..i-1]
                last_sum = prefix[i] - prefix[p]
                dp[i][j] = min(dp[i][j], max(dp[p][j-1], last_sum))

    return dp[n][k]


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n log(sum)) Time | O(1) Space
# ═══════════════════════════════════════════════════════════════════
def split_array(nums, k):
    """
    Idu final answer — binary search on answer space
    IDENTICAL to Ship Packages #1011 — same template!
    left=max(nums): must fit largest element
    right=sum(nums): worst case one subarray
    """
    def can_split(max_sum):
        """Greedy: can we split into <= k pieces with each sum <= max_sum?"""
        pieces = 1
        current = 0
        for num in nums:
            if current + num > max_sum:
                pieces += 1       # start new subarray
                current = 0
            current += num
        return pieces <= k

    left  = max(nums)      # min possible — must fit largest element
    right = sum(nums)      # max possible — whole array as one piece
    ans   = right

    while left <= right:
        mid = (left + right) // 2

        if can_split(mid):
            ans = mid             # valid! try smaller max sum
            right = mid - 1
        else:
            left = mid + 1       # too small, need bigger capacity

    return ans


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # Test 1 — Basic
    assert split_array([7, 2, 5, 10, 8], 2) == 18

    # Test 2 — Second example
    assert split_array([1, 2, 3, 4, 5], 2) == 9

    # Test 3 — k == n (each element own subarray)
    assert split_array([7, 2, 5, 10, 8], 5) == 10

    # Test 4 — k == 1 (entire array one subarray)
    assert split_array([7, 2, 5, 10, 8], 1) == 32

    # Test 5 — Single element
    assert split_array([5], 1) == 5

    # Test 6 — All same elements
    assert split_array([5, 5, 5, 5], 2) == 10

    # Test 7 — Verify DP matches binary search
    assert split_array_dp([7, 2, 5, 10, 8], 2) == 18
    assert split_array_dp([1, 2, 3, 4, 5], 2) == 9

    print("All tests passed!")
