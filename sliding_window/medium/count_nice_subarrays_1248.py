"""
╔════════════════════════════════════════════════════════════════════╗
║  COUNT NUMBER OF NICE SUBARRAYS                                    ║
║  LeetCode #1248  |  Difficulty: Medium  |  Topic: Sliding Window   ║
║  Link: https://leetcode.com/problems/count-number-of-nice-subarrays/║
╚════════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  A contiguous subarray is called "nice" if it contains EXACTLY
  `k` ODD numbers. Given an array `nums` and an integer `k`,
  return the number of nice subarrays.

  Input : nums = array of integers, k = required count of odds
  Output: integer — number of subarrays containing exactly k
          odd numbers

  Example 1 — basic:
    Input : nums = [1,1,2,1,1], k = 3
    Output: 2
    Why?  : [1,1,2,1] (indices 0-3) and [1,2,1,1] (indices 1-4)
            each contain exactly 3 odd numbers

  Example 2 — slightly tricky (no odd numbers at all):
    Input : nums = [2,4,6], k = 1
    Output: 0
    Why?  : there isn't a single odd number in the array, so no
            subarray can ever contain exactly 1 odd number

  Example 3 — larger array, more matches:
    Input : nums = [2,2,2,1,2,2,1,2,2,2], k = 2
    Output: 16
    Why?  : many overlapping windows between the two odd numbers
            (and extending outward on both sides) each contain
            exactly 2 odds

  Constraints:
    - 1 <= nums.length <= 5 * 10^4
    - 1 <= nums[i] <= 10^5
    - 1 <= k <= nums.length

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Problem odi aada mele namma brain enu think maadabeeku:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  integer array, target odd count k│
  │  Output ಏನು ಬೇಕು?     →  EXACTLY k ODD numbers ಇರೋ ಎಷ್ಟು │
  │                           contiguous subarrays ಇವೆ ಅಂತ    │
  │  Constraints ಏನಿದೆ?   →  "exactly k" — direct monotonic   │
  │                           window ಅಲ್ಲ                     │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ಇದನ್ನ previous problem (#930 Binary Subarrays With
           Sum) ಜೊತೆ EXACT ಆಗಿ CONNECT ಮಾಡಿ ನೋಡಿ!
  →  "ಪ್ರತಿ ODD number ಅನ್ನ 1 ಆಗಿ, EVEN number ಅನ್ನ 0 ಆಗಿ
      ಪರಿಗಣಿಸಿದ್ರೆ, 'exactly k odd numbers' ಅಂದ್ರೆ 'ಆ binary
      transformed array ರಲ್ಲಿ sum EXACTLY k' ಅಂತ ಆಗುತ್ತೆ!"
  →  ಇದೇ #930 ಪ್ರಶ್ನೆ, ಬರೀ different framing ಅಷ್ಟೇ! ಅದೇ
     atMost(k) - atMost(k-1) trick apply ಆಗುತ್ತೆ

  ಹಂತ 3 — atMost(k) ಅನ್ನ ಇಲ್ಲಿ ಹೇಗೆ define ಮಾಡೋದು?
  →  atMost(k) = "ಗರಿಷ್ಠ k ODD numbers ಇರೋ subarrays ಎಷ್ಟು"
  →  odd count MONOTONIC ಆಗಿರೋದ್ರಿಂದ (values ಎಲ್ಲಾ positive,
     ಪ್ರತಿ element odd ಆಗಿರಬಹುದು ಅಥವಾ ಇಲ್ಲ — window grow
     ಮಾಡಿದಾಗ odd count ಎಂದಿಗೂ ಕಡಿಮೆ ಆಗಲ್ಲ), classic sliding
     window apply ಮಾಡಬಹುದು

  ಹಂತ 4 — ಮೊದಲ simple idea (brute) ಏನು?
  →  ಪ್ರತಿ starting index ಇಂದ, odd numbers count ಮಾಡ್ತಾ ಹೋಗಿ,
     count == k ಆದಾಗಲೆಲ್ಲಾ answer ಗೆ 1 ಸೇರಿಸಿ

  ಹಂತ 5 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  "exactly k" ಅನ್ನ ನೇರವಾಗಿ slide ಮಾಡಕ್ಕಾಗಲ್ಲ, ಆದ್ರೆ atMost(k)
     - atMost(k-1) ಆಗಿ ಒಡೆದ್ರೆ ಎರಡೂ ಭಾಗಗಳೂ monotonic —
     ಎರಡು ಸಲ O(n) sliding window ಸಾಕು

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು:
  →  "This is exactly the 'Binary Subarrays With Sum' problem —
      treat odd numbers as 1, even as 0, and count subarrays
      summing to k"
  →  "Since 'exactly k odds' isn't directly monotonic, I compute
      atMost(k) - atMost(k-1), each via a standard sliding window
      counting odd numbers in the window"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Sliding Window — atMost(k) - atMost(k-1) trick
  Secondary : Brute-force all-subarrays odd-count check

  WHY atMost(k) - atMost(k-1) (same as #930)?
  → "Exactly k odd numbers" is not itself a monotonic window
    condition, but "at most k odd numbers" is — growing the
    window never DECREASES the odd count. Splitting the exact
    count into a difference of two at-most counts keeps every
    sliding window monotonic and correct.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  The key insight: this problem is a direct RESKIN of Binary
  Subarrays With Sum (#930) — just replace "is this element 1?"
  with "is this element odd?" All the same monotonic reasoning
  applies: the odd-count of a growing window never decreases, so
  atMost(k) can be counted with a clean sliding window, and
  subtracting atMost(k-1) isolates exactly the subarrays with
  precisely k odd numbers.

  The journey from brute to optimal:
    Brute thought   →  For every starting index, count odd
                       numbers as the window grows, incrementing
                       whenever the count hits exactly k
    Problem with it →  O(n^2) — restarts the odd-count tracking
                       from scratch at every starting index
    Better question →  "Isn't 'odd count ≤ k' monotonic, just
                       like the binary-sum version of this
                       problem?"
    Insight         →  atMost(k) via sliding window (shrink when
                       odd count exceeds k); exactly(k) =
                       atMost(k) - atMost(k-1)
    Optimal         →  Two O(n) sliding-window passes, O(n) total

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE (check every subarray)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    For every starting index, extend the subarray rightward,
    tracking a running odd-number count. Whenever that count
    equals exactly k, this subarray is "nice" — count it.

  Pseudocode:
    step 1: count = 0
    step 2: for i in range(n):
    step 3:   odds = 0
    step 4:   for j in range(i, n):
    step 5:     if nums[j] % 2 == 1: odds += 1
    step 6:     if odds == k: count += 1
    step 7: return count

  Time  : O(n^2)  →  Why: O(n^2) (i,j) pairs, each O(1) odd
                          count update
  Space : O(1)     →  Why: just a running counter

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ?
    → Correct, but quadratic — for n = 5*10^4 this is far too
      slow. The atMost(k) trick brings it down to linear, exactly
      as in the binary-sum version of this problem.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 6 — APPROACH 2 — OPTIMAL (atMost(k) sliding window trick)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Define `at_most(k)`: count of subarrays with AT MOST k odd
    numbers, via a standard monotonic sliding window (shrink
    left whenever the window's odd count exceeds k; add
    right-left+1 for every valid right). The answer is
    `at_most(k) - at_most(k - 1)`.

  Key steps:
    1. def at_most(k):
    2.   if k < 0: return 0
    3.   left, odds, count = 0, 0, 0
    4.   for right in range(n):
    5.     if nums[right] % 2 == 1: odds += 1
    6.     while odds > k:
    7.       if nums[left] % 2 == 1: odds -= 1
    8.       left += 1
    9.     count += right - left + 1
    10.  return count
    11. return at_most(k) - at_most(k - 1)

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ:
    → "at_most(k) helper: odd count k ಮೀರಿದ್ರೆ left ಅನ್ನ
       ಸರಿಸಿ shrink ಮಾಡು. ಪ್ರತಿ right ಗೂ (right-left+1)
       subarrays ಸೇರಿಸು. ಕೊನೆಗೆ at_most(k) - at_most(k-1)
       ಮಾಡಿದ್ರೆ EXACTLY k odd numbers ಇರೋ subarrays ಸಿಗುತ್ತೆ!"

  Time  : O(n)  →  Why: at_most() is one linear sliding-window
                        pass, called exactly twice
  Space : O(1)  →  Why: just a few running counters/pointers

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 7 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: nums = [1,1,2,1,1], k = 3

  at_most(3):
    right=0(1,odd): odds=1, count+=1(=1)
    right=1(1,odd): odds=2, count+=2(=3)
    right=2(2,even): odds=2, count+=3(=6)
    right=3(1,odd): odds=3, count+=4(=10)
    right=4(1,odd): odds=4>3 → shrink: left=0(odd,odds=3),left=1
                    count+=(4-1+1)=4(=14)
    at_most(3) = 14

  at_most(2):
    right=0(1): odds=1, count+=1(=1)
    right=1(1): odds=2, count+=2(=3)
    right=2(2): odds=2, count+=3(=6)
    right=3(1): odds=3>2 → shrink: left=0(odd,odds=2),left=1
                count+=(3-1+1)=3(=9)
    right=4(1): odds=3>2 → shrink: left=1(odd,odds=2),left=2
                count+=(4-2+1)=3(=12)
    at_most(2) = 12

  Answer: at_most(3) - at_most(2) = 14 - 12 = 2

  Output: 2 ✓

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 8 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ No odd numbers at all, k>=1?    →  0 — impossible to hit
  ✓ All odd numbers, k=length?      →  1 — only the full array
                                        qualifies
  ✓ Single element, odd, k=1?       →  1 — just itself
  ✓ Single element, even, k=1?      →  0 — no odd number present
  ✓ k larger than total odd count?  →  0 — never achievable

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 9 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                          Time    Space
  Brute (every subarray)  O(n^2)  O(1)
  Optimal (atMost trick)  O(n)    O(1)   ← use this ✅

  Time yaake O(n)?  → at_most() is one linear sliding-window
                       pass, called exactly twice → still O(n)
  Space yaake O(1)? → Just a few running counters/pointers

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 10 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: atMost(K) - atMost(K-1) — reused on a transformed condition

  Ee pattern yaavaaga use maadabeeku?
  → Any "exactly K [property] elements" subarray-counting
     problem where the property can be turned into a 0/1 flag
     (odd/even, matches-target/doesn't, etc.) — RESKIN it as
     "sum of flags == K" and reuse the atMost(K)-atMost(K-1)
     sliding window trick directly
  → Recognizing problem RESKINS (same structure, different
     surface story) saves having to re-derive a technique

  Idee pattern beere problemsalli kaanisatte:
  → Binary Subarrays With Sum #930 (previous problem — the
     EXACT same trick, this one is a direct reskin of it)
  → Number of Substrings Containing All 3 Chars #1358 (next
     problem — different exact technique, uses "last seen
     position" instead of atMost trick)
  → Subarrays with K Different Integers #992 (also reuses this
     same atMost(K)-atMost(K-1) trick, with distinct-count
     instead of odd-count)

  Next time intaha problem bandre naanu modalu idannu think maadtene:
  → "'Exactly K [property] elements' subarray count kelidre →
     property ge 0/1 flag assign madi, 'Binary Subarrays With
     Sum' reskin antha gurutisu — atMost(K)-atMost(K-1) apply
     madu!"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 11 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "Count subarrays containing exactly k odd numbers."

  2. Brute force:
     "For each start, track a running odd count, count matches
      to k. O(n^2)."

  3. Optimize:
     "Treat odd numbers as 1, even as 0 — this becomes exactly
      'Binary Subarrays With Sum.' Compute at_most(k) -
      at_most(k-1) using a standard monotonic sliding window
      that counts odd numbers in the current window."

  4. Code:
     "at_most(k) helper: shrink left while odd count > k, add
      right-left+1 valid endings per right. Return
      at_most(k) - at_most(k-1)."

  5. Complexity:
     "Time O(n) — two linear sliding-window passes. Space O(1)
      — just counters and pointers."

  Mukhya: recognize problem RESKINS — this is 'Binary Subarrays
          With Sum' wearing an odd/even costume, same trick reused!
"""


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(n^2) Time | O(1) Space (check every subarray)
# ═══════════════════════════════════════════════════════════════════
def number_of_subarrays_brute(nums, k):
    """
    Idu modala aaloochane — prati start inda odd count track
    madi, count == k sikkidkoodle answer ge sersu
    """
    n = len(nums)
    count = 0

    for i in range(n):
        odds = 0
        for j in range(i, n):
            if nums[j] % 2 == 1:
                odds += 1
            if odds == k:
                count += 1

    return count


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n) Time | O(1) Space (atMost(k) - atMost(k-1) trick)
# ═══════════════════════════════════════════════════════════════════
def number_of_subarrays(nums, k):
    """
    Idu final answer — at_most(k) sliding window helper use madi
    (odd count track madi), at_most(k) - at_most(k-1) return madu
    """
    def at_most(limit):
        if limit < 0:
            return 0

        left = 0
        odds = 0
        count = 0

        for right in range(len(nums)):
            if nums[right] % 2 == 1:
                odds += 1

            while odds > limit:
                if nums[left] % 2 == 1:
                    odds -= 1
                left += 1

            count += right - left + 1

        return count

    return at_most(k) - at_most(k - 1)


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # Test 1 — Basic
    assert number_of_subarrays([1, 1, 2, 1, 1], 3) == 2

    # Test 2 — No odd numbers at all
    assert number_of_subarrays([2, 4, 6], 1) == 0

    # Test 3 — Larger array
    assert number_of_subarrays([2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2) == 16

    # Test 4 — Single odd element
    assert number_of_subarrays([1], 1) == 1

    # Test 5 — Single even element, k=1
    assert number_of_subarrays([2], 1) == 0

    # Cross-check: brute force must agree on all of the above
    assert number_of_subarrays_brute([1, 1, 2, 1, 1], 3) == 2
    assert number_of_subarrays_brute([2, 4, 6], 1) == 0
    assert number_of_subarrays_brute([2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2) == 16
    assert number_of_subarrays_brute([1], 1) == 1
    assert number_of_subarrays_brute([2], 1) == 0

    print("All tests passed!")
