"""
╔══════════════════════════════════════════════════════════════════╗
║  TOP K FREQUENT ELEMENTS                                         ║
║  LeetCode #347  |  Difficulty: Medium  |  Topic: Arrays/Heap    ║
║  Link: https://leetcode.com/problems/top-k-frequent-elements/   ║
╚══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Given an integer array and a number k, return the k most
  frequent elements. The answer can be in any order.
  It is guaranteed that the answer is unique.

  Input : nums = list of integers, k = integer
  Output: list of k most frequent elements

  Example 1 — basic:
    Input : nums = [1,1,1,2,2,3], k = 2
    Output: [1, 2]
    Why?  : 1 appears 3 times, 2 appears 2 times, 3 appears 1 time
            top 2 frequent = [1, 2]

  Example 2 — slightly tricky (single element):
    Input : nums = [1], k = 1
    Output: [1]
    Why?  : only one element, k=1 so return it

  Constraints:
    - 1 <= nums.length <= 10^5
    - k is always valid (1 <= k <= unique elements count)
    - Answer is unique — no ties for the kth position

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Problem odi aada mele namma brain enu think maadabeeku:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  integers array + k number   │
  │  Output ಏನು ಬೇಕು?     →  k most frequent elements     │
  │  Constraints ಏನಿದೆ?   →  n=10^5, answer unique        │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ನನಗೆ ಗೊತ್ತಿರೋ simple way ಏನು?
  →  HashMap ಲ್ಲಿ frequency count ಮಾಡಿ, sort ಮಾಡಿ
     top k elements return ಮಾಡೋಣ
  →  ಆದರೆ ಇದು slow ಯಾಕೆ?
     Sort = O(n log n) — better O(n) solution ಇದೆ!

  ಹಂತ 3 — Better way ಹೇಗೆ ಯೋಚಿಸುವುದು?
  →  "Sort ಇಲ್ಲದೆ top k find ಮಾಡಬಹುದಾ?"
  →  Approach 1: Min Heap of size k → O(n log k)
  →  Approach 2: Bucket Sort → frequency = index → O(n)!
  →  Bucket Sort most elegant — frequency max = n, so
     buckets[freq] = [elements with that freq]

  ಹಂತ 4 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  Frequency 1 to n taka range iddare — perfect for buckets!
  →  Reverse scan from n → 1, first k elements = answer
  →  O(n) time — better than sort or heap

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು:
  →  "Count frequencies with HashMap first"
  →  "Brute: sort by frequency — O(n log n)"
  →  "Better: min heap size k — O(n log k)"
  →  "Best: bucket sort — frequency is bounded by n → O(n)"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Bucket Sort (O(n) — best approach)
  Secondary : Min Heap of size k (O(n log k) — also acceptable)

  WHY Bucket Sort?
  → Frequency is always between 1 and n — bounded range
  → Bounded range = perfect for bucket sort
  → Avoids sorting cost entirely → O(n)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Key observation: frequency of any element is between 1 and n.
  So we can create n+1 buckets where bucket[i] = all elements
  that appear exactly i times. Then scan from right (highest freq)
  and collect k elements.

  The journey from brute to optimal:
    Brute thought   →  Count freq, sort by freq, take top k
    Problem with it →  O(n log n) — sort is expensive
    Better question →  "Can I avoid sorting entirely?"
    Insight         →  Frequency is bounded by n → use as index!
                       Bucket sort: buckets[freq] = [elements]
    Optimal         →  Bucket sort O(n) — scan from high freq down

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Count frequency of each element using HashMap.
    Sort elements by frequency in descending order.
    Return first k elements.

  Pseudocode:
    step 1: count = Counter(nums)
    step 2: sorted_items = sorted(count, key=lambda x: -count[x])
    step 3: return sorted_items[:k]

  Time  : O(n log n)  →  Why: sorting n unique elements
  Space : O(n)        →  Why: HashMap stores all unique elements

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ?
    → O(n log n) valid aagatte but O(n) possible idde
    → Problem says answer in O(n log n) or better → heap/bucket better

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚶 SECTION 6 — APPROACH 2 — BETTER (Min Heap)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Count frequencies. Maintain a min heap of size k.
    For each element, push to heap. If heap size > k, pop min.
    At end, heap contains k most frequent elements.

  Time  : O(n log k)  →  Why: n elements, heap ops cost log k
  Space : O(n + k)    →  Why: HashMap O(n) + heap O(k)

  ಇನ್ನೂ better ಮಾಡಬಹುದಾ? → YES! Bucket sort = O(n)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 7 — APPROACH 3 — OPTIMAL (Bucket Sort)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Count frequencies. Create buckets where index = frequency.
    buckets[i] = list of elements that appear exactly i times.
    Scan from right (highest freq) and collect until k elements.

  Key steps:
    1. count = Counter(nums) → {element: frequency}
    2. buckets = [[] for _ in range(n+1)]  ← index = frequency
    3. For each (num, freq): buckets[freq].append(num)
    4. Scan buckets from right → collect until len(result) == k

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ:
    → "Frequency count maadu. Frequency = index aagi buckets
       create maadu. buckets[3] = frequency 3 iddooru elements.
       Right inda scan maadi k elements collect maadu — O(n)!"

  Time  : O(n)   →  Why: count O(n) + bucket fill O(n) + scan O(n)
  Space : O(n)   →  Why: buckets array of size n+1

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 8 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: nums = [1,1,1,2,2,3], k = 2

  Step 1 — Count frequencies:
    count = {1:3, 2:2, 3:1}

  Step 2 — Fill buckets (size n+1 = 7):
    buckets[0] = []
    buckets[1] = [3]       ← 3 appears 1 time
    buckets[2] = [2]       ← 2 appears 2 times
    buckets[3] = [1]       ← 1 appears 3 times
    buckets[4] = []
    buckets[5] = []
    buckets[6] = []

  Step 3 — Scan from right, collect k=2 elements:
    i=6 → [] → skip
    i=5 → [] → skip
    i=4 → [] → skip
    i=3 → [1] → result=[1], len=1 < k
    i=2 → [2] → result=[1,2], len=2 == k → stop!

  Output: [1, 2] ✓

  ಇನ್ನೊಂದು example:
  Input: nums = [1], k = 1
  count = {1:1}
  buckets[1] = [1]
  Scan from right → i=1 → [1] → result=[1] → done
  Output: [1] ✓

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 9 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ Single element?          →  [1], k=1 → [1]
  ✓ All same elements?       →  [1,1,1], k=1 → [1]
  ✓ k equals unique count?   →  [1,2,3], k=3 → [1,2,3]
  ✓ All equal frequency?     →  [1,2,3], k=2 → any 2 (answer unique
                                 guaranteed by problem)
  ✓ Negative numbers?        →  [-1,-1,2], k=1 → [-1]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 10 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                Time          Space
  Brute Force   O(n log n)    O(n)
  Min Heap      O(n log k)    O(n + k)
  Bucket Sort   O(n)          O(n)     ← use this ✅

  Time yaake O(n)?  → 3 linear passes — count, fill, scan
  Space yaake O(n)? → buckets array size n+1 + count HashMap

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 11 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Bucket Sort — Frequency as Index

  Ee pattern yaavaaga use maadabeeku?
  → "Top k frequent / least frequent elements"
  → Values or frequencies are bounded by n
  → Need to avoid O(n log n) sort cost

  Idee pattern beere problemsalli kaanisatte:
  → Sort Characters by Frequency #451 (same idea, strings)
  → Top K Frequent Words #692 (same + lexicographic order)
  → Find K Closest Elements #658

  Next time intaha problem bandre naanu modalu idannu think maadtene:
  → "Top k frequent? → HashMap count maadu → frequency bounded
     by n → bucket sort use maadu → O(n) alli solve!"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 12 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "Return the k most frequently occurring elements."

  2. Brute force:
     "Count frequencies, sort by frequency descending, take k.
      That is O(n log n)."

  3. Optimize:
     "I can do better — frequency is bounded between 1 and n.
      Bounded range means bucket sort! Use frequency as index,
      scan from highest frequency down to collect k elements."

  4. Code:
     "Counter for frequencies, buckets list of size n+1,
      fill buckets, scan right to left, collect k elements."

  5. Complexity:
     "Time O(n) — three linear passes.
      Space O(n) — buckets + HashMap."

  Mukhya: summane kuutu code bareyabeda!
          Bucket sort trick — O(n log n) → O(n) improvement
          interviewer ge very impressive aagatte!
"""

import heapq
from collections import Counter


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(n log n) Time | O(n) Space
# ═══════════════════════════════════════════════════════════════════
def top_k_frequent_brute(nums, k):
    """Idu modala aaloochane — count + sort O(n log n)"""
    count = Counter(nums)
    return sorted(count, key=lambda x: -count[x])[:k]


# ═══════════════════════════════════════════════════════════════════
# BETTER — O(n log k) Time | O(n + k) Space (Min Heap)
# ═══════════════════════════════════════════════════════════════════
def top_k_frequent_heap(nums, k):
    """Min heap of size k — O(n log k)"""
    count = Counter(nums)
    # heapq gives min heap — store (freq, num)
    return [num for freq, num in heapq.nlargest(k, count.items(),
                                                 key=lambda x: x[1])]


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n) Time | O(n) Space (Bucket Sort)
# ═══════════════════════════════════════════════════════════════════
def top_k_frequent(nums, k):
    """Idu final answer — bucket sort, frequency as index O(n)"""
    count = Counter(nums)

    # buckets[i] = list of elements with frequency i
    # max possible frequency = len(nums)
    buckets = [[] for _ in range(len(nums) + 1)]

    for num, freq in count.items():
        buckets[freq].append(num)

    # scan from highest frequency to lowest
    result = []
    for i in range(len(buckets) - 1, 0, -1):
        for num in buckets[i]:
            result.append(num)
            if len(result) == k:
                return result

    return result


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # Test 1 — Basic
    assert sorted(top_k_frequent([1,1,1,2,2,3], 2)) == [1, 2]

    # Test 2 — Single element
    assert top_k_frequent([1], 1) == [1]

    # Test 3 — k equals all unique elements
    assert sorted(top_k_frequent([1,2,3], 3)) == [1, 2, 3]

    # Test 4 — Negative numbers
    assert top_k_frequent([-1,-1,2], 1) == [-1]

    # Test 5 — All same
    assert top_k_frequent([1,1,1,1], 1) == [1]

    print("All tests passed!")
