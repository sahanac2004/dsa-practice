"""
╔══════════════════════════════════════════════════════════════════╗
║  KTH MISSING POSITIVE NUMBER                                     ║
║  LeetCode #1539  |  Difficulty: Easy  |  Topic: Binary Search   ║
║  Link: https://leetcode.com/problems/kth-missing-positive-number/║
╚══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Given a sorted array of distinct positive integers and an integer
  k, return the kth missing positive integer.

  Input : arr = sorted distinct positive integers, k = integer
  Output: kth missing positive number

  Example 1 — basic:
    Input : arr = [2,3,4,7,11], k = 5
    Output: 9
    Why?  : Missing positives in order: 1,5,6,8,9,10...
            1st=1, 2nd=5, 3rd=6, 4th=8, 5th=9 → answer is 9

  Example 2 — slightly tricky (k missing before first element):
    Input : arr = [1,2,3,4], k = 2
    Output: 6
    Why?  : Missing: 5,6,7... → 2nd missing = 6

  Constraints:
    - 1 <= arr.length <= 1000
    - 1 <= arr[i] <= 1000
    - 1 <= k <= 1000
    - arr is sorted and all distinct

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Problem odi aada mele namma brain enu think maadabeeku:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  sorted distinct array + k   │
  │  Output ಏನು ಬೇಕು?     →  kth missing positive number  │
  │  Constraints ಏನಿದೆ?   →  array sorted, distinct,      │
  │                           all positive                  │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ನನಗೆ ಗೊತ್ತಿರೋ simple way ಏನು?
  →  1 ಇಂದ start ಮಾಡಿ missing numbers count ಮಾಡ್ತಾ ಹೋಗೋಣ
     kth missing ಸಿಕ್ಕಿದ್ದಕ್ಕೆ return ಮಾಡೋಣ → O(n+k)
  →  ಆದರೆ ಇದು slow ಯಾಕೆ?
     O(n) valid adu, but O(log n) possible with binary search!

  ಹಂತ 3 — Better way ಹೇಗೆ ಯೋಚಿಸುವುದು?
  →  Key insight: arr[i] ಇದ್ದ index ಲ್ಲಿ expected value i+1
     → missing count at index i = arr[i] - (i+1)
     → arr[i] - i - 1 missing numbers before arr[i]!
  →  [2,3,4,7,11]:
     i=0: arr[0]=2, expected=1, missing=2-0-1=1
     i=3: arr[3]=7, expected=4, missing=7-3-1=3
     i=4: arr[4]=11, expected=5, missing=11-4-1=6
  →  Binary search: find first index where missing_count >= k!

  ಹಂತ 4 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  missing_count = arr[i] - i - 1 is monotonically increasing
  →  Binary search for first index where arr[i]-i-1 >= k
  →  Answer = left + k (elegant formula!)

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು:
  →  "At index i, missing count = arr[i] - (i+1) = arr[i]-i-1"
  →  "This is monotonically increasing → binary search!"
  →  "Find first index where missing >= k, answer = left + k"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Binary Search → On Array (missing count property)
  Secondary : Linear scan (brute force, O(n+k))

  WHY Binary Search here?
  → missing_count at index i = arr[i] - i - 1
  → This is monotonically non-decreasing
  → Binary search to find first position where missing >= k
  → Answer = left + k (elegant!)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  If the array had NO missing numbers, arr[i] would equal i+1.
  The difference arr[i] - (i+1) = arr[i] - i - 1 tells us exactly
  how many numbers are missing BEFORE arr[i].

  arr = [2, 3, 4, 7, 11]
  idx =  0  1  2  3   4
  miss=  1  1  1  3   6   ← arr[i] - i - 1

  We want to find the kth missing number.
  Binary search for first index where missing_count >= k.
  If left = that index, answer = left + k.

  Why left + k?
  → At index left, there are missing_count < k numbers before arr[left-1]
  → So we need (k - missing_count_before_left) more numbers after arr[left-1]
  → Which simplifies to: left + k

  The journey from brute to optimal:
    Brute thought   →  Count missing linearly → O(n+k)
    Problem with it →  O(log n) possible
    Better question →  "Can I binary search on missing count?"
    Insight         →  arr[i]-i-1 = missing count up to index i
                       This is monotonic → binary search!
    Optimal         →  O(log n) with elegant answer formula

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Use a set of array elements. Scan from 1 upward.
    Count missing numbers until we hit the kth one.

  Pseudocode:
    step 1: arr_set = set(arr)
    step 2: missing = 0
    step 3: num = 0
    step 4: while missing < k:
    step 5:   num += 1
    step 6:   if num not in arr_set: missing += 1
    step 7: return num

  Time  : O(n + k)  →  Why: build set O(n), scan up to arr[-1]+k
  Space : O(n)      →  Why: set of all elements

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ?
    → O(n) valid adu, but O(log n) possible!
    → Sorted array iddare binary search think maadu

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 6 — APPROACH 2 — OPTIMAL (Binary Search)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Binary search for the first index where missing_count >= k.
    missing_count at index i = arr[i] - i - 1
    Answer = left + k

  Key steps:
    1. left=0, right=len(arr)
    2. While left < right:
       a. mid = (left+right)//2
       b. missing = arr[mid] - mid - 1
       c. if missing >= k → right=mid  (search left half)
       d. else → left=mid+1           (search right half)
    3. return left + k

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ:
    → "arr[i]-i-1 = i ತನಕ missing count ಎಷ್ಟು ಅಂತ ಹೇಳತ್ತೆ.
       ಇದು monotonic increase aagatte. Binary search maadu —
       first index ಹುಡುಕು where arr[i]-i-1 >= k.
       Answer = left + k — elegant formula!"

  Time  : O(log n)  →  Why: binary search on array indices
  Space : O(1)      →  Why: only pointers

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 7 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: arr=[2,3,4,7,11], k=5

  Missing counts: [2-0-1, 3-1-1, 4-2-1, 7-3-1, 11-4-1]
                = [1,      1,     1,     3,      6    ]

  left=0, right=5
  mid=2 → missing=arr[2]-2-1=4-3=1 < 5 → left=3

  left=3, right=5
  mid=4 → missing=arr[4]-4-1=11-5=6 >= 5 → right=4

  left=3, right=4
  mid=3 → missing=arr[3]-3-1=7-4=3 < 5 → left=4

  left=4 == right=4 → exit
  return left+k = 4+5 = 9 ✓

  ಇನ್ನೊಂದು — all array elements present, missing after:
  Input: arr=[1,2,3,4], k=2

  Missing counts: [0, 0, 0, 0]
  All < k=2, so left goes to right=4
  return 4+2 = 6 ✓ (missing: 5,6 → 2nd is 6)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 8 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ k missing before arr[0]?   →  arr=[5,6,7], k=3 → 3
                                    missing=[4,4,4], all >= k=3
                                    left=0, return 0+3=3 ✓
  ✓ k missing after arr[-1]?   →  arr=[1,2,3], k=5 → 8
                                    left=3, return 3+5=8 ✓
  ✓ Single element?            →  arr=[1], k=1 → 2
  ✓ No missing before arr?     →  arr=[1,2,3,4], k=2 → 6

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 9 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                Time      Space
  Brute Force   O(n+k)    O(n)
  Optimal       O(log n)  O(1)   ← use this ✅

  Time yaake O(log n)? → Binary search on n indices
  Space yaake O(1)?    → Only left, right, mid

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 10 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Binary Search on Array — Missing Count Property

  Ee pattern yaavaaga use maadabeeku?
  → Sorted array with "how many missing" questions
  → Property arr[i]-i-1 gives count of missing numbers before i
  → Binary search on this monotonic property

  Idee pattern beere problemsalli kaanisatte:
  → Find Missing Number #268 (simpler version)
  → Missing Ranges #163
  → Count Negative Numbers in Sorted Matrix

  Next time intaha problem bandre naanu modalu idannu think maadtene:
  → "Sorted array, kth missing? → arr[i]-i-1 = missing count!
     Binary search for first index where count >= k.
     Answer = left + k — remember this formula!"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 11 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "Find the kth missing positive integer from a sorted array."

  2. Brute force:
     "Use a set, scan from 1 upward counting missing. O(n+k)."

  3. Optimize:
     "Key insight: at index i, arr[i]-(i+1) = arr[i]-i-1 tells us
      exactly how many positives are missing before arr[i].
      This count is monotonically non-decreasing — binary search!
      Find first index where missing_count >= k. Answer = left+k."

  4. Code:
     "left=0, right=n. Binary search. missing=arr[mid]-mid-1.
      If missing>=k → right=mid. Else left=mid+1. Return left+k."

  5. Complexity:
     "Time O(log n). Space O(1)."

  Mukhya: summane kuutu code bareyabeda!
          arr[i]-i-1 insight — elegant and surprising!
          Answer = left+k formula — derive it once for interviewer!
"""


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(n+k) Time | O(n) Space
# ═══════════════════════════════════════════════════════════════════
def find_kth_missing_brute(arr, k):
    """Idu modala aaloochane — scan from 1, count missing"""
    arr_set = set(arr)
    missing = 0
    num = 0
    while missing < k:
        num += 1
        if num not in arr_set:
            missing += 1
    return num


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(log n) Time | O(1) Space
# ═══════════════════════════════════════════════════════════════════
def find_kth_missing(arr, k):
    """
    Idu final answer — binary search on missing count property
    arr[i]-i-1 = number of positives missing before arr[i]
    Find first index where this count >= k → answer = left+k
    """
    left, right = 0, len(arr)

    while left < right:
        mid = (left + right) // 2
        missing = arr[mid] - mid - 1   # how many missing before arr[mid]

        if missing >= k:
            right = mid     # might be answer, search left
        else:
            left = mid + 1  # not enough missing yet, search right

    # left = first index where missing_count >= k
    # answer = left + k
    return left + k


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # Test 1 — Basic
    assert find_kth_missing([2, 3, 4, 7, 11], 5) == 9

    # Test 2 — Missing after array
    assert find_kth_missing([1, 2, 3, 4], 2) == 6

    # Test 3 — Missing before first element
    assert find_kth_missing([5, 6, 7], 3) == 3

    # Test 4 — Single element
    assert find_kth_missing([1], 1) == 2
    assert find_kth_missing([2], 1) == 1

    # Test 5 — Large k, missing after array
    assert find_kth_missing([1, 2, 3], 5) == 8

    # Test 6 — k=1
    assert find_kth_missing([2, 3, 4, 7, 11], 1) == 1

    print("All tests passed!")
