"""
╔══════════════════════════════════════════════════════════════════╗
║  MAJORITY ELEMENT                                                ║
║  LeetCode #169  |  Difficulty: Easy  |  Topic: Arrays / Boyer-Moore Voting ║
║  Link: https://leetcode.com/problems/majority-element/           ║
╚══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Given nums of size n, return the MAJORITY element — the one
  appearing MORE THAN ⌊n/2⌋ times. Always assume it exists.

  Input : nums = [2, 2, 1, 1, 1, 2, 2]
  Output: 2

  Example 1 — basic:
    Input : nums = [2, 2, 1, 1, 1, 2, 2]
    Output: 2
    Why?  : 2 appears 4 times, n=7, ⌊7/2⌋=3, and 4 > 3

  Example 2 — slightly tricky:
    Input : nums = [3, 3, 3, 3]
    Output: 3
    Why?  : trivially the majority — every element is the same

  Constraints:
    - Majority element is GUARANTEED to exist
    - n >= 1

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ಮೊದಲು problem odidaga ನಮ್ಮ brain ಏನು think ಮಾಡಬೇಕು:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ (What are they asking?)
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  size n array nums               │
  │  Output ಏನು ಬೇಕು?     →  ⌊n/2⌋ ಗಿಂತ ಜಾಸ್ತಿ ಸಲ ಬಂದ        │
  │                          element (majority)                │
  │  Constraints ಏನಿದೆ?   →  Majority element GUARANTEE ಆಗಿ   │
  │                          ಇರುತ್ತೆ ಅಂತ ಗೊತ್ತು                │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ನನಗೆ ಗೊತ್ತಿರೋ simple way ಏನು? (Brute force thought)
  →  Hashmap ಇಟ್ಕೊಂಡು ಪ್ರತಿ element ನ frequency count ಮಾಡಿ,
     count > n//2 ಇರೋ ಒಂದನ್ನ return ಮಾಡೋದು.
  →  ಆದರೆ ಇದು ಯಾಕೆ enough ಅಲ್ಲ? → O(n) space ಬಳಸುತ್ತೆ, O(1)
     space ಲ್ಲಿ ಮಾಡೋಕ್ಕಾಗುತ್ತಾ ಅಂತ ಯೋಚಿಸ್ಬೇಕು.

  ಹಂತ 3 — Better way ಹೇಗೆ ಯೋಚಿಸುವುದು? (Optimization thought)
  →  "Majority element ⌊n/2⌋ ಗಿಂತ ಜಾಸ್ತಿ ಸಲ ಇದೆ ಅಂದ್ರೆ, ಅದನ್ನ
     ಬೇರೆ ಎಲ್ಲಾ elements ಜೊತೆ 'ಕ್ಯಾನ್ಸಲ್' ಮಾಡ್ತಾ ಹೋದ್ರೂ ಕೊನೆಗೆ
     survive ಆಗಬೇಕಲ್ವಾ?"
  →  ಅಹಾ moment: ಒಂದು candidate + count ಇಟ್ಕೊಂಡು, ಒಂದೇ number
     ಬಂದ್ರೆ count++ (vote FOR), ಬೇರೆ ಬಂದ್ರೆ count-- (vote AGAINST).
     count 0 ಆದ್ರೆ, candidate ಬದಲಾಯಿಸು. Majority element ಗ್ಯಾರಂಟಿ
     ಇರೋದ್ರಿಂದ, ಕೊನೆಗೆ ಅದೇ candidate ಆಗಿ ಉಳೀತದೆ.
  →  ಇದರಿಂದ ನಾವು Boyer-Moore Voting Algorithm use ಮಾಡಬಹುದು!

  ಹಂತ 4 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  Majority element GUARANTEE ಆಗಿ ಇರುತ್ತೆ ಅನ್ನೋ constraint ಇದೇ
     voting ಅನ್ನ safe ಮಾಡುತ್ತೆ — cancel ಆದ್ರೂ ಮತ್ತೆ survive ಆಗುತ್ತೆ.
  →  O(n) time, O(1) space ಬೇಕು ಅಂದಾಗ, hashmap counting (O(n)
     space) ಗಿಂತ ಇದು ಬೆಟರ್.
  →  Sorting (O(n log n)) ಬೇಡ ಅಂತ ಗೊತ್ತಾದಾಗ, voting ಒಂದೇ ಪಾಸ್
     ಲ್ಲಿ ಆಗುತ್ತೆ.

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು (Think out loud):
  →  "So one element is GUARANTEED to appear more than n/2 times."
  →  "A hashmap frequency count works but uses O(n) space."
  →  "I can use Boyer-Moore voting — since the majority outnumbers
      everything else combined, it survives cancellation."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Boyer-Moore Voting Algorithm
  Secondary : Candidate + Counter tracking

  WHY Boyer-Moore?
  → Majority element GUARANTEED to exist — makes voting safe
  → It can survive being "cancelled out" by every other element
  → O(n) time, O(1) space — beats hashmap and sorting both

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 INTUITION (How to think)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Since the majority element appears MORE than half the time, can
  I cancel one occurrence of it against one occurrence of ANY
  different element, and have it still survive at the end?

  The journey from brute to optimal:
    Brute thought   →  hashmap frequency count
    Problem with it →  O(n) space, beatable
    Better question →  "can votes for/against cancel safely?"
    Insight         →  majority outnumbers everything else combined
    Optimal         →  candidate + count, Boyer-Moore voting

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 APPROACH 1 — BRUTE FORCE (HashMap Counting)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Count frequency of every element, return the one > n//2.

  Pseudocode:
    step 1: freq = {}; for num in nums: freq[num] = freq.get(num,0)+1
    step 2: for num, count in freq.items(): if count > n//2: return num

  Time  : O(n)
  Space : O(n)  →  Why: hashmap can store up to n/2 distinct keys

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ? (Why is this not enough?)
    → O(n) extra space ಬಳಸುತ್ತೆ; Boyer-Moore O(1) ಲ್ಲಿ ಮಾಡುತ್ತೆ.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚶 APPROACH 2 — BETTER (skip — brute jumps straight to optimal)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ಇಲ್ಲಿ intermediate approach ಇಲ್ಲ — voting insight ಸಿಕ್ಕ ತಕ್ಷಣ
  ನೇರವಾಗಿ O(1) space optimal ಗೆ ಹೋಗಬಹುದು.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 APPROACH 3 — OPTIMAL   (Boyer-Moore Voting)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Maintain a running candidate + vote count, cancel opposites.

  Key steps:
    1. candidate = None, count = 0
    2. For each num in nums:
         if count == 0: candidate = num
         count += 1 if num == candidate else -1
    3. Return candidate

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ (Say it once in Kanglish so it sticks):
    → "count 0 ಆದಾಗ, current number ಅನ್ನೇ ಹೊಸ candidate ಮಾಡ್ಕೋ.
        Current number candidate ಗೆ match ಆದ್ರೆ count++, ಇಲ್ಲಾಂದ್ರೆ
        count--. Majority element ಗ್ಯಾರಂಟಿ ಇರೋದ್ರಿಂದ, ಕೊನೆ
        candidate ಯಾವಾಗ್ಲೂ ಸರಿಯಾಗಿರುತ್ತೆ."

  Time  : O(n)  →  Why: single pass
  Space : O(1)  →  Why: two variables only

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: nums = [2, 2, 1, 1, 1, 2, 2]

  candidate=None, count=0

  num=2  →  variables: count=0  →  candidate=2, count=1
  num=2  →  variables: count=1  →  match, count=2
  num=1  →  variables: count=2  →  no match, count=1
  num=1  →  variables: count=1  →  no match, count=0
  num=1  →  variables: count=0  →  candidate=1, count=1
  num=2  →  variables: count=1  →  no match, count=0
  num=2  →  variables: count=0  →  candidate=2, count=1

  Output: 2 (2 does appear 4 times, the true majority)

  ಇನ್ನೊಂದು example — tricky case:
  Input: nums = [1, 1, 2, 1, 2]
  candidate=None, count=0
  num=1  count=0 → candidate=1, count=1
  num=1  match → count=2
  num=2  no match → count=1
  num=1  match → count=2
  num=2  no match → count=1
  Output: 1 (n=5, ⌊5/2⌋=2, 1 appears 3 times, 3>2 ✓)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ Single element?      →  [5] → 5 (trivially the majority)
  ✓ All same element?    →  [3,3,3,3] → 3
  ✓ Majority at boundary?  →  [1,1,2,1,2] n=5, ⌊5/2⌋=2, 1 appears 3>2 → 1
  ✓ Two elements?         →  problem guarantees a majority exists,
    so [1,2] (no true majority) won't occur — e.g. [2,2] → 2

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                Time      Space
  Brute Force   O(n)      O(n)
  Optimal       O(n)      O(1)    ← use this  

  Time ಯಾಕೆ O(n)?  → Array ಒಮ್ಮೆ ಮಾತ್ರ traverse ಮಾಡ್ತೇವೆ.
  Space ಯಾಕೆ O(1)? → candidate, count ಎರಡು variables ಸಾಕು.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Boyer-Moore Voting — Cancel Minority Against Majority

  ಈ pattern ಯಾವಾಗ use ಮಾಡಬೇಕು?
  → Problem GUARANTEE ಕೊಡ್ತಿದ್ರೆ ಒಂದು element MORE THAN HALF
    array ಆಕ್ರಮಿಸಿದೆ ಅಂತ
  → Counting ಬೇಡ, candidate cancel ಮಾಡ್ತಾ ಹೋದ್ರೆ ಸಾಕು ಅಂತ
    ಗೊತ್ತಾದಾಗ

  ಇದೇ pattern ಬೇರೆ problems ನಲ್ಲಿ ಕಾಣಿಸುತ್ತೆ:
  → Majority Element II (n/3 times ಗಿಂತ ಜಾಸ್ತಿ ಬಂದ elements —
    ಎರಡು candidates + counts ಒಟ್ಟಿಗೆ track ಮಾಡ್ಬೇಕು)

  Next time ಇಂತಹ problem ಬಂದ್ರೆ ನಾನು ಮೊದಲು ಇದನ್ನ think ಮಾಡ್ತೇನೆ:
  → "'More than half/n-th times' ಗ್ಯಾರಂಟಿ ಕಂಡ ತಕ್ಷಣ, Boyer-Moore
      voting ಮೊದಲು ಯೋಚಿಸು — counting ಬೇಕಿಲ್ಲ."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ INTERVIEW ನಲ್ಲಿ ಹೇಗೆ EXPLAIN ಮಾಡಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "So one element is guaranteed to appear more than n/2 times,
      and I need to find it."

  2. Brute force:
     "A hashmap frequency count works but uses O(n) extra space."

  3. Optimize:
     "Since the majority element outnumbers everything else
      combined, I can use Boyer-Moore voting: cancel one 'vote
      against' per 'vote for', and the majority survives as the
      final candidate."

  4. Code:
     "I'll track a candidate and a count. When count hits 0, I
      pick a new candidate; matching increments, mismatching
      decrements."

  5. Complexity:
     "Time O(n) — one pass. Space O(1) — two variables."

  ಮುಖ್ಯ: ಸುಮ್ಮನೆ ಕೂತು code ಬರೆಯಬೇಡ!
         Interviewer ಗೆ ನಿನ್ನ thinking process ಕಾಣಬೇಕು.
"""


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(n) Time | O(n) Space
# ═══════════════════════════════════════════════════════════════════
def majority_element_brute(nums):
    """ಇದು ಮೊದಲ ಆಲೋಚನೆ — hashmap frequency count, extra space"""
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
    for num, count in freq.items():
        if count > len(nums) // 2:
            return num


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n) Time | O(1) Space  (Boyer-Moore Voting)
# ═══════════════════════════════════════════════════════════════════
def majority_element(nums):
    """ಇದು final answer — Boyer-Moore voting, minority cancels against majority"""
    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1

    return candidate


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")   # Windows cp1252 can't print   otherwise

    # Test 1 — Basic example
    assert majority_element([2, 2, 1, 1, 1, 2, 2]) == 2

    # Test 2 — Edge case: single element
    assert majority_element([5]) == 5

    # Test 3 — Edge case: all same
    assert majority_element([3, 3, 3, 3]) == 3

    # Test 4 — Tricky: majority at the boundary
    assert majority_element([1, 1, 2, 1, 2]) == 1

    print("All tests passed!  ")
