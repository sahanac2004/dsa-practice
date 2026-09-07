"""
╔════════════════════════════════════════════════════════════════════╗
║  BINARY SUBARRAYS WITH SUM                                         ║
║  LeetCode #930  |  Difficulty: Medium  |  Topic: Sliding Window    ║
║  Link: https://leetcode.com/problems/binary-subarrays-with-sum/    ║
╚════════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Given a BINARY array `nums` (only 0s and 1s) and an integer
  `goal`, return the NUMBER of non-empty subarrays whose sum
  equals exactly `goal`.

  Input : nums = array of 0s and 1s, goal = target sum
  Output: integer — count of subarrays summing to exactly goal

  Example 1 — basic:
    Input : nums = [1,0,1,0,1], goal = 2
    Output: 4
    Why?  : subarrays (0..2), (0..3), (1..4), (2..4) each sum
            to exactly 2 — four qualifying subarrays

  Example 2 — slightly tricky (goal = 0, all zeros):
    Input : nums = [0,0,0,0,0], goal = 0
    Output: 15
    Why?  : every one of the 5*6/2 = 15 possible subarrays sums
            to 0, since the array is all zeros

  Example 3 — no qualifying subarrays:
    Input : nums = [0,0,0], goal = 1
    Output: 0
    Why?  : with no 1s anywhere, no subarray can ever sum to 1

  Constraints:
    - 1 <= nums.length <= 3 * 10^4
    - nums[i] is either 0 or 1
    - 0 <= goal <= nums.length

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Problem odi aada mele namma brain enu think maadabeeku:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  binary array, target sum goal    │
  │  Output ಏನು ಬೇಕು?     →  sum == goal ಆಗಿರೋ ಎಷ್ಟು          │
  │                           contiguous subarrays ಇವೆ ಅಂತ    │
  │  Constraints ಏನಿದೆ?   →  values ಬರೀ 0/1 — sum ಎಂದಿಗೂ      │
  │                           negative ಆಗಲ್ಲ                  │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ಇದನ್ನ previous sliding window problems (#1004, #904)
           ಜೊತೆ compare ಮಾಡಿ ನೋಡಿ — ಯಾಕೆ ಇದು ಬೇರೆ?
  →  ಅಲ್ಲಿ "AT MOST k" condition ಇತ್ತು — ಸಹಜ ಆಗಿ MONOTONIC
     (window shrink ಮಾಡಿದಾಗ condition ಎಂದಿಗೂ ಜಾಸ್ತಿ ಆಗಲ್ಲ)
  →  ಇಲ್ಲಿ "EXACTLY == goal" ಬೇಕು — ಇದು ಸಹಜ ಆಗಿ monotonic
     ಅಲ್ಲ! (sum ಸಮ ಆದ ಮೇಲೂ ಮತ್ತೆ ಜಾಸ್ತಿ ಆಗಬಹುದು, ಆಮೇಲೆ ಕಡಿಮೆ
     ಆಗಬಹುದು — direct sliding window apply ಮಾಡಕ್ಕಾಗಲ್ಲ)

  ಹಂತ 3 — Classic trick ಏನಿದೆ? "atMost(k) - atMost(k-1)"
  →  "exactly == goal" ಅನ್ನ "atMost(goal) - atMost(goal-1)"
      ಅಂತ ಪುನಃ ಬರೆಯಿರಿ!
  →  atMost(k) = "sum ≤ k ಇರೋ subarrays ಎಷ್ಟು" — ಇದು MONOTONIC
     (values ಎಲ್ಲಾ non-negative ಆಗಿರೋದ್ರಿಂದ, window grow
     ಮಾಡಿದ್ರೆ sum ಎಂದಿಗೂ ಕಡಿಮೆ ಆಗಲ್ಲ) — so ಇದಕ್ಕೆ sliding
     window apply ಮಾಡಬಹುದು!
  →  "sum ≤ goal" ಇಂದ "sum ≤ goal-1" ಕಳೆದ್ರೆ, "sum == goal"
     exactly ಆಗಿರೋ subarrays ಮಾತ್ರ ಉಳಿಯುತ್ತೆ

  ಹಂತ 4 — atMost(k) ಅನ್ನ sliding window ಇಂದ ಹೇಗೆ ಎಣಿಸೋದು?
  →  ಪ್ರತಿ right ಗೆ, window [left,right] valid (sum≤k) ಆಗೋವರೆಗೆ
     left ಅನ್ನ ಸರಿಸು
  →  ಆ position ನಲ್ಲಿ, [left,right] ಒಳಗಡೆ right ಅನ್ನ END ಆಗಿ
     ಇಟ್ಟುಕೊಂಡು ಎಷ್ಟು subarrays ಸಾಧ್ಯ ಅಂದ್ರೆ (right-left+1) —
     ಇದನ್ನ total count ಗೆ ಸೇರಿಸು

  ಹಂತ 5 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  Values non-negative ಆಗಿರೋದ್ರಿಂದ (0/1 ಮಾತ್ರ), atMost(k)
     ಗೆ classic monotonic sliding window ಸರಿಯಾಗಿ apply
     ಆಗುತ್ತೆ — "exactly" problem ಅನ್ನ ಎರಡು "at most" problems
     ಆಗಿ ಒಡೆದ್ರೆ, ಎರಡೂ ಸರಳ ಆಗಿ solve ಮಾಡಬಹುದು

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು:
  →  "'Exactly equal to goal' isn't directly sliding-window
      friendly — but 'at most k' IS, since the array is
      non-negative"
  →  "So I compute atMost(goal) - atMost(goal-1) — subarrays
      with sum ≤ goal, minus subarrays with sum ≤ goal-1, leaves
      exactly the ones summing to goal"
  →  "atMost(k) itself is a standard sliding window: for each
      right, shrink left until sum ≤ k, then add (right-left+1)
      valid subarrays ending at right"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Sliding Window — atMost(k) - atMost(k-1) trick
  Secondary : Brute-force all-subarrays sum check

  WHY atMost(k) - atMost(k-1)?
  → "Exactly k" is not monotonic and doesn't fit a single sliding
    window directly. But since all values are non-negative,
    "sum ≤ k" IS monotonic — a classic sliding window counts it
    cleanly. Subtracting two "at most" counts isolates exactly
    the subarrays with the target sum, without ever leaving the
    monotonic-window world.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  The key insight: counting "subarrays with sum EXACTLY k" is
  hard to do with a single window because the count of valid
  endings for a fixed right doesn't grow or shrink cleanly as
  right increases. But "subarrays with sum AT MOST k" behaves
  perfectly — since 0s and 1s never make the sum decrease as the
  window grows, shrinking is always well-defined. The trick:
  {sum ≤ goal} minus {sum ≤ goal-1} leaves exactly {sum == goal},
  turning one hard counting problem into two easy ones.

  The journey from brute to optimal:
    Brute thought   →  Check every subarray's sum directly,
                       count the ones equal to goal
    Problem with it →  O(n^2) — computing/comparing every
                       subarray's sum from scratch
    Better question →  "Is there a MONOTONIC version of this
                       condition I can slide a window over?"
    Insight         →  "sum ≤ k" is monotonic since values are
                       non-negative; exactly(k) = atMost(k) -
                       atMost(k-1)
    Optimal         →  Two O(n) sliding-window passes (atMost
                       called twice), O(n) total

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE (check every subarray)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    For every starting index, extend the subarray rightward,
    keeping a running sum. Count every subarray whose sum equals
    goal exactly.

  Pseudocode:
    step 1: count = 0
    step 2: for i in range(n):
    step 3:   s = 0
    step 4:   for j in range(i, n):
    step 5:     s += nums[j]
    step 6:     if s == goal: count += 1
    step 7: return count

  Time  : O(n^2)  →  Why: O(n^2) (i,j) pairs, each O(1) running
                          sum update
  Space : O(1)     →  Why: just a running sum and counter

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ?
    → Correct, but quadratic — for n = 3*10^4 this is far too
      slow. The atMost(k) trick brings it down to linear.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 6 — APPROACH 2 — OPTIMAL (atMost(k) sliding window trick)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Define `at_most(k)`: the count of subarrays with sum ≤ k,
    computed via a standard monotonic sliding window (shrink
    left whenever the window sum exceeds k; add right-left+1 for
    every valid right). The answer is `at_most(goal) -
    at_most(goal - 1)` (guarding goal-1 < 0 → returns 0).

  Key steps:
    1. def at_most(k):
    2.   if k < 0: return 0
    3.   left, total, count = 0, 0, 0
    4.   for right in range(n):
    5.     total += nums[right]
    6.     while total > k: total -= nums[left]; left += 1
    7.     count += right - left + 1
    8.   return count
    9. return at_most(goal) - at_most(goal - 1)

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ:
    → "at_most(k) helper: window sum k ಮೀರಿದ್ರೆ left ಅನ್ನ
       ಸರಿಸಿ shrink ಮಾಡು. ಪ್ರತಿ right ಗೂ, (right-left+1) subarrays
       ಸೇರಿಸು — ಇವೆಲ್ಲಾ right ಅನ್ನ end ಆಗಿ ಇಟ್ಟುಕೊಂಡು sum≤k
       ಇರೋ subarrays. ಕೊನೆಗೆ at_most(goal) - at_most(goal-1)
       ಮಾಡಿದ್ರೆ exactly goal ಇರೋ ಕೌಂಟ್ ಸಿಗುತ್ತೆ!"

  Time  : O(n)  →  Why: at_most() itself is O(n) (sliding
                        window), called exactly twice
  Space : O(1)  →  Why: just a few running counters/pointers

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 7 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: nums = [1,0,1,0,1], goal = 2

  at_most(2):
    right=0(1): total=1, count+=1(=1)          [window: 0..0]
    right=1(0): total=1, count+=2(=3)          [window: 0..1]
    right=2(1): total=2, count+=3(=6)          [window: 0..2]
    right=3(0): total=2, count+=4(=10)         [window: 0..3]
    right=4(1): total=3>2 → shrink: left=0
                total-=1(=2), left=1
                count+=(4-1+1)=4(=14)          [window: 1..4]
    at_most(2) = 14

  at_most(1):
    right=0(1): total=1, count+=1(=1)
    right=1(0): total=1, count+=2(=3)
    right=2(1): total=2>1 → shrink: left=0,
                total-=1(=1), left=1
                count+=(2-1+1)=2(=5)
    right=3(0): total=1, count+=(3-1+1)=3(=8)
    right=4(1): total=2>1 → shrink: left=1,
                total-=0(=2), left=2
                total still 2>1 → shrink: left=2,
                total-=1(=1), left=3
                count+=(4-3+1)=2(=10)
    at_most(1) = 10

  Answer: at_most(2) - at_most(1) = 14 - 10 = 4

  Output: 4 ✓

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 8 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ goal = 0, all zeros [0,0,0,0,0]? →  15 — every subarray
                                         qualifies
  ✓ goal larger than possible sum?   →  0 — no subarray can
                                         reach it
  ✓ No 1s at all, goal=1?            →  0 — impossible to hit
  ✓ Single element [1], goal=1?      →  1 — just itself
  ✓ goal = 0 with some 1s present?   →  counts only the runs of
                                         consecutive 0s correctly

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
  Pattern Name: atMost(K) - atMost(K-1) — Exact-Match Sliding Window

  Ee pattern yaavaaga use maadabeeku?
  → "EXACTLY equal to target" subarray-counting problems where
     values are non-negative — the condition itself isn't
     monotonic, but wrapping it as a DIFFERENCE of two "at most"
     counts restores monotonicity
  → Any "count subarrays/substrings with condition == K"
     problem, when "condition ≤ K" is easy to slide a window over

  Idee pattern beere problemsalli kaanisatte:
  → Count Number of Nice Subarrays #1248 (next problem — SAME
     atMost(k)-atMost(k-1) trick, counting odd numbers instead
     of the raw sum)
  → Subarrays with K Different Integers #992 (also uses this
     exact atMost(K)-atMost(K-1) trick, with distinct-count
     instead of sum)
  → Max Consecutive Ones III #1004 (contrast — that one's
     condition, "at most k zeros," was ALREADY monotonic, no
     subtraction trick needed)

  Next time intaha problem bandre naanu modalu idannu think maadtene:
  → "'Exactly K' subarray count kelidre, condition monotonic
     illa antadre → atMost(K) - atMost(K-1) try maadu! Values
     non-negative aadre, atMost() ge classic sliding window
     apply aaguttade."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 11 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "Count non-empty subarrays of a binary array whose sum
      equals goal exactly."

  2. Brute force:
     "Check every subarray's running sum directly, count matches
      to goal. O(n^2)."

  3. Optimize:
     "'Exactly goal' isn't directly sliding-window friendly, but
      'sum ≤ k' is, since values are non-negative. So compute
      at_most(goal) - at_most(goal-1) — a standard monotonic
      sliding window run twice."

  4. Code:
     "at_most(k) helper: shrink left while sum > k, add
      right-left+1 valid endings per right. Guard k<0 → 0.
      Return at_most(goal) - at_most(goal-1)."

  5. Complexity:
     "Time O(n) — two linear sliding-window passes. Space O(1)
      — just counters and pointers."

  Mukhya: 'exactly K' subarray counts often aren't directly
          slidable — but atMost(K) - atMost(K-1) turns them into
          two easy monotonic sliding windows!
"""


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(n^2) Time | O(1) Space (check every subarray)
# ═══════════════════════════════════════════════════════════════════
def num_subarrays_with_sum_brute(nums, goal):
    """
    Idu modala aaloochane — prati subarray ge running sum lekka
    hakidhu, sum == goal sikkidkoodle count madu
    """
    n = len(nums)
    count = 0

    for i in range(n):
        s = 0
        for j in range(i, n):
            s += nums[j]
            if s == goal:
                count += 1

    return count


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n) Time | O(1) Space (atMost(k) - atMost(k-1) trick)
# ═══════════════════════════════════════════════════════════════════
def num_subarrays_with_sum(nums, goal):
    """
    Idu final answer — at_most(k) sliding window helper use madi,
    at_most(goal) - at_most(goal-1) return madu
    """
    def at_most(k):
        if k < 0:
            return 0

        left = 0
        total = 0
        count = 0

        for right in range(len(nums)):
            total += nums[right]

            while total > k:
                total -= nums[left]
                left += 1

            count += right - left + 1

        return count

    return at_most(goal) - at_most(goal - 1)


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # Test 1 — Basic
    assert num_subarrays_with_sum([1, 0, 1, 0, 1], 2) == 4

    # Test 2 — goal = 0, all zeros
    assert num_subarrays_with_sum([0, 0, 0, 0, 0], 0) == 15

    # Test 3 — No qualifying subarrays
    assert num_subarrays_with_sum([0, 0, 0], 1) == 0

    # Test 4 — Single element
    assert num_subarrays_with_sum([1], 1) == 1

    # Test 5 — goal larger than achievable sum
    assert num_subarrays_with_sum([1, 0, 1], 5) == 0

    # Cross-check: brute force must agree on all of the above
    assert num_subarrays_with_sum_brute([1, 0, 1, 0, 1], 2) == 4
    assert num_subarrays_with_sum_brute([0, 0, 0, 0, 0], 0) == 15
    assert num_subarrays_with_sum_brute([0, 0, 0], 1) == 0
    assert num_subarrays_with_sum_brute([1], 1) == 1
    assert num_subarrays_with_sum_brute([1, 0, 1], 5) == 0

    print("All tests passed!")
