"""
╔══════════════════════════════════════════════════════════════════╗
║  COUNT OF SMALLER NUMBERS AFTER SELF                             ║
║  LeetCode #315  |  Difficulty: Hard  |  Topic: Arrays / Sorting ║
║  Link: https://leetcode.com/problems/count-of-smaller-numbers-  ║
║        after-self/                                               ║
╚══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Given an integer array nums, for each element nums[i], count
  how many elements to its RIGHT are smaller than it.
  Return these counts as an array.

  Input : nums = array of integers
  Output: counts = array where counts[i] = number of elements
                   to the right of nums[i] that are smaller

  Example 1 — basic:
    Input : nums = [5, 2, 6, 1]
    Output: [2, 1, 1, 0]
    Why?  :
      nums[0] = 5 → [2, 6, 1] → 2 elements smaller (2 and 1)  → 2
      nums[1] = 2 → [6, 1]    → 1 element smaller (1)         → 1
      nums[2] = 6 → [1]       → 1 element smaller (1)         → 1
      nums[3] = 1 → []        → nothing to the right          → 0

  Example 2 — slightly tricky (duplicates):
    Input : nums = [2, 0, 1]
    Output: [2, 0, 0]
    Why?  :
      nums[0] = 2 → [0, 1] → both smaller → 2
      nums[1] = 0 → [1]    → 1 is NOT smaller → 0
      nums[2] = 1 → []     → nothing → 0

  Constraints:
    - 1 <= nums.length <= 10^5
    - -10^4 <= nums[i] <= 10^4

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Problem odi aada mele namma brain enu think maadabeeku:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  ಒಂದು integer array          │
  │  Output ಏನು ಬೇಕು?     →  ಪ್ರತಿ element ಗೆ, ಅದರ       │
  │                           right side ಲ್ಲಿ ಎಷ್ಟು        │
  │                           smaller elements ಇವೆ         │
  │                           ಅಂತ count ಬೇಕು              │
  │  Constraints ಏನಿದೆ?   →  n = 10^5 ತನಕ ಇರಬಹುದು,       │
  │                           negative numbers ಕೂಡ ಇರತ್ತೆ  │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ನನಗೆ ಗೊತ್ತಿರೋ simple way ಏನು?
  →  ಪ್ರತಿ element i ಗೆ, ಅದರ right side ಎಲ್ಲ elements j
     ನೋಡಿ nums[j] < nums[i] ಆದ್ರೆ count++ ಮಾಡೋಣ
  →  ಆದರೆ ಇದು slow ಯಾಕೆ?
     n = 10^5 ಆದ್ರೆ → 10^5 × 10^5 = 10^10 operations → TLE!

  ಹಂತ 3 — Better way ಹೇಗೆ ಯೋಚಿಸುವುದು?
  →  "Right side ಲ್ಲಿ smaller elements count ಮಾಡಬೇಕು..."
  →  "ಇದು inversions count ಮಾಡಿದ ಹಾಗೆ ಅಲ್ಲವಾ?"
  →  Merge Sort ಲ್ಲಿ left half ಮತ್ತು right half merge ಮಾಡುವಾಗ,
     right ಅಲ್ಲಿ ಇರೋ element ಎಷ್ಟು left elements ನ jump ಮಾಡಿ
     ಮೊದಲು place ಆಯಿತು ಅಂತ count ಮಾಡಬಹುದು!
  →  ಇದರಿಂದ ನಾವು Merge Sort — Inversion Count use ಮಾಡಬಹುದು!

  ಹಂತ 4 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  Merge Sort ಲ್ಲಿ merge step ನಲ್ಲಿ, right element ಮೊದಲು
     place ಆದ್ರೆ → ಅದು left ಲ್ಲಿ ಉಳಿದ ಎಲ್ಲ elements ಗಿಂತ smaller
  →  ಆ count ಅನ್ನೇ ನಾವು answer ಆಗಿ use ಮಾಡಬಹుದು
  →  Original index track ಮಾಡಲು (index, value) pairs ಇಟ್ಟುಕೊಳ್ಳಬೇಕು

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು:
  →  "For each element, I need to count smaller elements to its right"
  →  "Brute force is O(n²) — nested loops, TLE for n=10^5"
  →  "This is essentially counting inversions, which Merge Sort
      does naturally during the merge step in O(n log n)"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Merge Sort → Inversion Count
  Secondary : Divide and Conquer

  WHY Merge Sort?
  → Problem asks "how many elements to the RIGHT are SMALLER"
    — this is the classic definition of an inversion
  → During merge step, when a right-half element is picked before
    left-half elements, all remaining left elements are larger
    — that count is exactly what we need
  → Merge Sort naturally processes this in O(n log n)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  A pair (i, j) where i < j and nums[i] > nums[j] is called an
  INVERSION. This problem is asking: for each i, how many inversions
  does it form with elements to its right?

  Merge Sort counts inversions for free during the merge step:
  When merging two sorted halves [left] and [right], if right[j]
  is placed before left[i], then left[i], left[i+1], ..., left[end]
  are ALL greater than right[j] — that is exactly our count.

  The journey from brute to optimal:
    Brute thought   →  For every i, scan all j > i and count smaller
    Problem with it →  O(n²) — n=10^5 gives 10^10 ops, TLE
    Better question →  "Can I count these during a sort?"
    Insight         →  Merge Sort's merge step reveals inversions —
                       when right element jumps over left elements,
                       those left elements are all larger than it
    Optimal         →  Modified Merge Sort tracking (index, value)
                       pairs — O(n log n)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    For every element nums[i], scan everything to its right.
    Count how many of those are strictly less than nums[i].

  Pseudocode:
    step 1: result = [0] * n
    step 2: for i from 0 to n-1:
    step 3:   for j from i+1 to n-1:
    step 4:     if nums[j] < nums[i]: result[i] += 1
    step 5: return result

  Time  : O(n²)  →  Why: two nested loops, each up to n
  Space : O(n)   →  Why: result array of size n

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ?
    → n = 10^5 aadre → 10^10 operations → LeetCode TLE aagatte
    → O(n log n) solution beeku

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 6 — APPROACH 2 — OPTIMAL (Modified Merge Sort)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Use Merge Sort on (index, value) pairs.
    During the merge step, when a right-half element is placed
    before remaining left-half elements, those left elements are
    all greater than this right element.
    So add the count of remaining left elements to each of their
    original positions in the result array.

  Key steps:
    1. Create indexed pairs: [(0,5), (1,2), (2,6), (3,1)]
       so we can track original positions after sorting
    2. Run merge sort on these pairs by value
    3. During merge: when right[j] < left[i], all remaining
       left elements (from i to end of left) are greater than
       right[j] — add that count to result[right[j].index]
    4. The result array collects counts at original indices

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ:
    → "Array ನ (index, value) pairs ಮಾಡಿ Merge Sort ಮಾಡು.
       Merge ಮಾಡುವಾಗ right element ನ left element ಗಿಂತ
       ಮೊದಲು place ಮಾಡಿದ್ರೆ, left ಲ್ಲಿ ಉಳಿದ ಎಲ್ಲ elements
       ಅದಕ್ಕಿಂತ ದೊಡ್ಡವು — ಆ count ಅನ್ನು result[right.index]
       ಗೆ add ಮಾಡು. ಹೀಗೆ O(n log n) ಲ್ಲಿ answer ಸಿಗತ್ತೆ!"

  Time  : O(n log n)  →  Why: Merge Sort divides n into log n
                              levels, each level processes n elements
  Space : O(n)        →  Why: auxiliary array for merge + result array

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 7 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: nums = [5, 2, 6, 1]

  Step 1 — Create indexed pairs:
    [(0,5), (1,2), (2,6), (3,1)]

  Step 2 — Merge Sort recursion:

    Split: [(0,5),(1,2)] and [(2,6),(3,1)]

    LEFT side — sort [(0,5),(1,2)]:
      Split: [(0,5)] and [(1,2)]
      Merge [(0,5)] and [(1,2)]:
        Compare 5 vs 2: 2 < 5 → place (1,2) first
        → left has 1 remaining element (5) that is > 2
        → result[1] += 1  → result = [0,1,0,0]
        → place (0,5) next
        Merged left: [(1,2),(0,5)]

    RIGHT side — sort [(2,6),(3,1)]:
      Split: [(2,6)] and [(3,1)]
      Merge [(2,6)] and [(3,1)]:
        Compare 6 vs 1: 1 < 6 → place (3,1) first
        → left has 1 remaining element (6) that is > 1
        → result[3] += 1  → result = [0,1,0,1]
        → place (2,6) next
        Merged right: [(3,1),(2,6)]

    Final merge [(1,2),(0,5)] and [(3,1),(2,6)]:
      Compare 2 vs 1: 1 < 2 → place (3,1)
        → left has 2 remaining [(1,2),(0,5)] → result[3] += 2
        → result = [0,1,0,3]  ← wait, this is wrong!
        
      Hmm, let me retrace — result[3] should be 0 because
      1 is at index 3 (rightmost), nothing is to its right.
      
      KEY POINT: we add to result[left_element.index] when a
      right element jumps over it, NOT to result[right.index].

    Redo final merge [(1,2),(0,5)] and [(3,1),(2,6)]:
      i=0 (left ptr), j=0 (right ptr)
      
      Compare left[0]=(1,2) vs right[0]=(3,1):
        right value 1 < left value 2 → place right (3,1)
        → count of remaining left elements = 2 (both (1,2) and (0,5))
        → result[1] += 1, result[0] += 1
        → result = [1, 2, 0, 0]
        j++

      Compare left[0]=(1,2) vs right[1]=(2,6):
        left value 2 < right value 6 → place left (1,2)
        i++

      Compare left[1]=(0,5) vs right[1]=(2,6):
        left value 5 < right value 6 → place left (0,5)
        i++

      Right remaining: place (2,6)

    Final sorted: [(3,1),(1,2),(0,5),(2,6)]
    result = [2, 1, 1, 0] ✓

  Output: [2, 1, 1, 0] ✓

  ಇನ್ನೊಂದು example — duplicates:
  Input: nums = [2, 0, 1]
  Pairs: [(0,2),(1,0),(2,1)]

  Sort [(0,2)] and [(1,0),(2,1)]:
    Right sort: [(1,0)] and [(2,1)]
      0 < 1 → place (1,0), result[2] += 1 → result=[0,0,1]... 
      wait result[2] means index 2 (value 1), nothing smaller 
      to its right, so this is wrong direction again.
      
      Right element (1,0) placed before (2,1):
        Remaining left from left half = 0 → nothing added
        Place (1,0), then (2,1)
      Sorted right: [(1,0),(2,1)]

  Merge [(0,2)] with [(1,0),(2,1)]:
    Compare 2 vs 0: 0 < 2 → place (1,0)
      remaining left = 1 element (0,2) → result[0] += 1
      result = [1,0,0]
    Compare 2 vs 1: 1 < 2 → place (2,1)
      remaining left = 1 element (0,2) → result[0] += 1
      result = [2,0,0]
    Place remaining (0,2)

  Output: [2, 0, 0] ✓

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 8 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ Single element?           → [5] → [0] — nothing to the right
  ✓ Already sorted ascending? → [1,2,3,4] → [0,0,0,0]
                                 no inversions at all
  ✓ Sorted descending?        → [4,3,2,1] → [3,2,1,0]
                                 maximum inversions
  ✓ Duplicate elements?       → [2,2,2] → [0,0,0]
                                 strictly smaller, so duplicates
                                 don't count — be careful with
                                 comparison operator (use <, not <=)
  ✓ Negative numbers?         → [-1,-2,0,1] → [1,0,0,0]
                                 works fine, merge sort handles it
  ✓ All same elements?        → [3,3,3] → [0,0,0]
                                 no element is strictly smaller

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 9 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                Time          Space
  Brute Force   O(n²)         O(n)
  Optimal       O(n log n)    O(n)     ← use this ✅

  Time yaake O(n log n)?
    → Merge Sort log n levels ittare, each level n elements
       process maadatte → n × log n = O(n log n)

  Space yaake O(n)?
    → Merge ige auxiliary array O(n) beeku
    → result array O(n)
    → Recursion call stack O(log n) — dominated by O(n)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 10 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Merge Sort — Inversion Count

  Ee pattern yaavaaga use maadabeeku?
  → "Count elements smaller/larger than current to its right/left"
  → "Count inversions in an array"
  → O(n²) brute force ide, O(n log n) beeku antadre

  Idee pattern beere problemsalli kaanisatte:
  → Count of Inversions (classic problem — same exact idea)
  → Reverse Pairs LC #493 (nums[i] > 2 * nums[j], i < j)
  → Create Sorted Array through Instructions LC #1649

  Next time intaha problem bandre naanu modalu idannu think maadtene:
  → "Right side alli smaller count maadabekittu, O(n²) slow aagatte
     → inversions antu gottaaytu → Merge Sort use maadu, merge step
     alli right element jump maadidaaga left count add maadu!"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 11 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  (Interviewer mundhe idannu heege helu — always think out loud)

  1. Understand:
     "The problem asks me to count, for each element, how many
      elements to its right are strictly smaller than it."

  2. Brute force:
     "The naive approach is two nested loops — for each i, scan
      all j > i and count nums[j] < nums[i]. That is O(n²),
      which TLEs for n up to 10^5."

  3. Optimize:
     "I notice this is essentially counting inversions — pairs
      (i,j) where i < j and nums[i] > nums[j]. Merge Sort
      naturally reveals inversions during the merge step: when
      a right-half element is placed before left-half elements,
      all remaining left elements are larger than it. I can
      accumulate those counts at the original indices."

  4. Code:
     "I will use a modified Merge Sort on (index, value) pairs
      so I can track original positions. During merge, when I
      pick from the right half, I add the count of remaining
      left elements to their result positions."

  5. Complexity:
     "Time O(n log n) — standard Merge Sort complexity.
      Space O(n) — auxiliary array for merge step."

  Mukhya: summane kuutu code bareyabeda!
          Interviewer ge ninna thinking process kaanabeku.
          Inversion count connection gottaagidre interviewer
          impressed aagatte!
"""


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(n²) Time | O(n) Space
# ═══════════════════════════════════════════════════════════════════
def count_smaller_brute(nums):
    """
    Idu modala aaloochane — simple but slow O(n²)
    Prathi element ge right side scan maadu
    """
    n = len(nums)
    result = [0] * n

    for i in range(n):
        for j in range(i + 1, n):
            if nums[j] < nums[i]:
                result[i] += 1

    return result


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n log n) Time | O(n) Space
# ═══════════════════════════════════════════════════════════════════
def count_smaller(nums):
    """
    Idu final answer — Modified Merge Sort, inversion count O(n log n)
    (index, value) pairs use maadi original position track maadu
    """
    n = len(nums)
    result = [0] * n

    # Create (original_index, value) pairs
    indexed = list(enumerate(nums))

    def merge_sort(arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        return merge(left, right)

    def merge(left, right):
        sorted_arr = []
        i = 0   # pointer for left half
        j = 0   # pointer for right half

        while i < len(left) and j < len(right):
            if right[j][1] < left[i][1]:
                # right element is smaller than left element
                # ALL remaining left elements are > right[j]
                # so add count of remaining left to each left element
                for k in range(i, len(left)):
                    result[left[k][0]] += 1
                sorted_arr.append(right[j])
                j += 1
            else:
                # left element is smaller or equal — place it
                sorted_arr.append(left[i])
                i += 1

        # add remaining elements
        sorted_arr.extend(left[i:])
        sorted_arr.extend(right[j:])
        return sorted_arr

    merge_sort(indexed)
    return result


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL V2 — cleaner merge with left_count tracking
# ═══════════════════════════════════════════════════════════════════
def count_smaller_v2(nums):
    """
    Cleaner version — track how many right elements were placed
    before current left element using a counter
    """
    n = len(nums)
    result = [0] * n
    indexed = list(enumerate(nums))

    def merge_sort(arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        return merge(left, right)

    def merge(left, right):
        sorted_arr = []
        i = 0
        j = 0
        right_count = 0   # how many right elements placed so far

        while i < len(left) and j < len(right):
            if right[j][1] < left[i][1]:
                # right element placed first — it is smaller than left[i]
                right_count += 1
                sorted_arr.append(right[j])
                j += 1
            else:
                # left element placed — right_count elements from right
                # were already placed before it, all smaller than it
                result[left[i][0]] += right_count
                sorted_arr.append(left[i])
                i += 1

        # remaining left elements — all right elements already counted
        while i < len(left):
            result[left[i][0]] += right_count
            sorted_arr.append(left[i])
            i += 1

        sorted_arr.extend(right[j:])
        return sorted_arr

    merge_sort(indexed)
    return result


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # Test 1 — Basic example
    assert count_smaller_v2([5, 2, 6, 1]) == [2, 1, 1, 0], \
        f"Got {count_smaller_v2([5, 2, 6, 1])}"

    # Test 2 — Duplicates
    assert count_smaller_v2([2, 0, 1]) == [2, 0, 0], \
        f"Got {count_smaller_v2([2, 0, 1])}"

    # Test 3 — Single element
    assert count_smaller_v2([1]) == [0], \
        f"Got {count_smaller_v2([1])}"

    # Test 4 — Already sorted ascending (no inversions)
    assert count_smaller_v2([1, 2, 3, 4]) == [0, 0, 0, 0], \
        f"Got {count_smaller_v2([1, 2, 3, 4])}"

    # Test 5 — Sorted descending (max inversions)
    assert count_smaller_v2([4, 3, 2, 1]) == [3, 2, 1, 0], \
        f"Got {count_smaller_v2([4, 3, 2, 1])}"

    # Test 6 — All same elements (duplicates don't count)
    assert count_smaller_v2([3, 3, 3]) == [0, 0, 0], \
        f"Got {count_smaller_v2([3, 3, 3])}"

    # Test 7 — Negative numbers
    assert count_smaller_v2([-1, -2, 0, 1]) == [1, 0, 0, 0], \
        f"Got {count_smaller_v2([-1, -2, 0, 1])}"

    print("All tests passed!")
