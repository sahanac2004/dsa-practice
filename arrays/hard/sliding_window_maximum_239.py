"""
╔══════════════════════════════════════════════════════════════════╗
║  SLIDING WINDOW MAXIMUM                                             ║
║  LeetCode #239  |  Difficulty: Hard  |  Topic: Arrays / Monotonic Deque ║
║  Link: https://leetcode.com/problems/sliding-window-maximum/        ║
╚══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Given an array and a window size k, slide the window of size k from
  left to right across the array, one step at a time, and return the
  maximum value in each window position.

  Input : nums = [1,3,-1,-3,5,3,6,7], k = 3
  Output: [3,3,5,5,6,7]

  Example 1 — basic:
    Input : nums = [1,3,-1,-3,5,3,6,7], k = 3
    Output: [3,3,5,5,6,7]
    Why?  : window [1,3,-1]→3, [3,-1,-3]→3, [-1,-3,5]→5,
             [-3,5,3]→5, [5,3,6]→6, [3,6,7]→7

  Example 2 — slightly tricky (k equals array length):
    Input : nums = [4,2,7], k = 3
    Output: [7]
    Why?  : only one window exists (the whole array), max is 7

  Constraints:
    - 1 <= nums.length <= 10^5
    - -10^4 <= nums[i] <= 10^4
    - 1 <= k <= nums.length

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Problem odi aada mele namma brain enu think maadabeeku:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ (What are they asking?)
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  array + window size k           │
  │  Output ಏನು ಬೇಕು?     →  ಪ್ರತಿ window position ನ max     │
  │  Constraints ಏನಿದೆ?   →  n<=10^5, negative numbers ಸಾಧ್ಯ  │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ನನಗೆ ಗೊತ್ತಿರೋ simple way ಏನು? (Brute force thought)
  →  ಪ್ರತಿ window position ಗೂ, ಆ k elements ನ max ಅನ್ನ ನೇರ ಆಗಿ scan
     ಮಾಡಿ ಹುಡುಕೋದು.
  →  ಆದರೆ ಇದು slow ಯಾಕೆ? → (n-k+1) windows, ಪ್ರತಿಯೊಂದಕ್ಕೂ O(k) scan
     → O(n*k), k ಬಹಳ ದೊಡ್ಡ ಆಗಿದ್ರೆ O(n²) ಹತ್ರ ಹೋಗುತ್ತೆ.

  ಹಂತ 3 — Better way ಹೇಗೆ ಯೋಚಿಸುವುದು? (Optimization thought)
  →  Window ಒಂದು step slide ಆದಾಗ, ಬಹಳಷ್ಟು elements ಸೇಮ್ ಆಗೇ
     ಇರುತ್ತಾವೆ — full rescan ಬೇಡ, ಬರೀ ಹೊಸ element ಸೇರಿಸಿ, ಹಳೇ element
     ತೆಗೆಯೋದು ಸಾಕು. ಆದ್ರೆ "max" ಅನ್ನ efficiently track ಮಾಡೋದು ಹೇಗೆ?
  →  ಅಹಾ moment: ಒಂದು element x ಸೇರಿಸುವಾಗ, ಅದಕ್ಕಿಂತ ಚಿಕ್ಕ ಇರೋ
     elements ಎಡಗಡೆ ಇದ್ರೆ, ಅವು ಎಂದೂ future window ಗಳ max ಆಗೋಕೆ ಆಗಲ್ಲ
     (x ಇನ್ನೂ window ನಲ್ಲಿ ಇರೋ ತನಕ) — ಆದ್ದರಿಂದ ಅವನ್ನ discard ಮಾಡ್ಬೋದು!
     ಇದೇ monotonic decreasing deque idea — front ನಲ್ಲಿ ಯಾವಾಗ್ಲೂ current
     window ನ max ಇರುತ್ತೆ.
  →  ಇದರಿಂದ ನಾವು Monotonic Deque (Decreasing — Sliding Window Max)
     use ಮಾಡಬಹುದು!

  ಹಂತ 4 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  Deque ನಲ್ಲಿ indices store ಮಾಡ್ತೀವಿ (values ಅಲ್ಲ), ಅವುಗಳ values
     decreasing order ನಲ್ಲಿ ಇರುತ್ತೆ — front ಯಾವಾಗ್ಲೂ current window
     ನ max index.
  →  ಹೊಸ element ಸೇರಿಸುವಾಗ, ಅದಕ್ಕಿಂತ ಚಿಕ್ಕ elements back ಇಂದ pop
     ಮಾಡಿ discard ಮಾಡ್ತೀವಿ (ಅವು useless ಆಗಿ ಬಿಡ್ತಾವೆ).
  →  Window ಇಂದ ಹೊರಗೆ ಹೋದ index front ನಲ್ಲಿ ಇದ್ರೆ, ಅದನ್ನ ಕೂಡ pop
     ಮಾಡ್ತೀವಿ — ಪ್ರತಿ index ಒಂದೇ ಸಲ push+pop ಆಗೋದ್ರಿಂದ O(n) total.

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು (Think out loud):
  →  "The naive way rescans each window for its max — O(n*k), too
      slow when both n and k can be up to 10^5."
  →  "I notice that when a new, larger element enters the window,
      every smaller element to its left becomes permanently useless
      — it can never be the max of any future window while the
      larger one is still in range."
  →  "That means I can maintain a monotonic decreasing deque of
      indices: pop smaller elements from the back when a bigger one
      arrives, and pop expired indices from the front — the front
      always holds the current window's max."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Monotonic Deque → Decreasing (Sliding Window Maximum)
  Secondary : Sliding Window → Fixed Size

  WHY this technique?
  → A smaller element to the left of a larger one can never become
    the max of any window that still contains the larger element —
    it's safe to discard permanently
  → Storing indices (not values) lets the deque detect when the
    front index has expired out of the current window
  → Each index enters and leaves the deque at most once, giving O(n)
    total work despite the nested-looking while loops

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION (How to think — English)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Key observation: maintain a deque of indices whose corresponding
  values are strictly decreasing from front to back. When a new
  element arrives, pop all smaller elements from the back (they're
  now dominated and useless), then push the new index. If the front
  index has slid out of the current window, pop it from the front.
  The front of the deque is always the current window's maximum.

  The journey from brute to optimal:
    Brute thought   →  rescan every window from scratch for its max
    Problem with it →  O(n*k), too slow for large n and k
    Better question →  "can I avoid rescanning by keeping only
                        'candidates that could still become the max'?"
    Insight         →  a smaller element left of a larger one is
                        permanently dominated — discard it
    Optimal         →  monotonic decreasing deque of indices, O(n)
                        time, O(k) space

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE (Rescan Every Window)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    For each window start position, scan all k elements in that
    window directly to find the max.

  Pseudocode:
    step 1: result = []
    step 2: for i in range(n - k + 1):
    step 3:   result.append(max(nums[i:i+k]))
    step 4: return result

  Time  : O(n*k)  →  Why: (n-k+1) windows, each requiring an O(k) scan
  Space : O(1) extra (excluding output) →  Why: no extra structures

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ? (Why is this not enough?)
    → n=10^5, k=10^5 ಆದ್ರೆ n*k = 10^10 — TLE ಆಗತ್ತೆ.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚶 SECTION 6 — APPROACH 2 — BETTER (Max-Heap with Lazy Deletion)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Push (value, index) pairs onto a max-heap as the window slides.
    When peeking the max, discard heap-top entries whose index has
    fallen out of the current window (lazy deletion) until a valid
    one is found.

  Time  : O(n log n)  →  each push/pop is O(log n), n elements total
  Space : O(n)         →  heap can grow up to n entries in the worst case

  ಇನ್ನೂ better ಮಾಡಬಹುದಾ? → ಹೌದು — monotonic deque ಇಂದ, O(log n)
  heap operations ಬೇಡ ಆಗುತ್ತೆ, amortized O(1) per element ಸಿಗುತ್ತೆ,
  total O(n).

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 7 — APPROACH 3 — OPTIMAL   (Monotonic Decreasing Deque)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Maintain a deque of indices with strictly decreasing values. For
    each new index i: pop from the back while nums[back] <= nums[i]
    (they're dominated), append i, pop from the front if it's fallen
    out of the window (i - front >= k). Once the window is full
    (i >= k-1), the front holds the current max.

  Key steps:
    1. dq = deque(); result = []
    2. for i in range(n):
         while dq and nums[dq[-1]] <= nums[i]: dq.pop()
         dq.append(i)
         if dq[0] <= i - k: dq.popleft()
         if i >= k - 1: result.append(nums[dq[0]])
    3. return result

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ (Kanglish one-liner so it sticks):
    → "Decreasing values ನ deque (indices) ಇಟ್ಕೊಂಡು, ಹೊಸ element
        ಬಂದಾಗ ಅದಕ್ಕಿಂತ ಚಿಕ್ಕ elements back ಇಂದ pop ಮಾಡಿ ಹೊಸದನ್ನ
        append ಮಾಡು. Front expired ಆಗಿದ್ರೆ popleft ಮಾಡು. Window full
        ಆದ ಮೇಲೆ, front ಯೇ current max!"

  Time  : O(n)  →  Why: each index pushed once and popped at most once
                    across the whole run (amortized O(1) per element)
  Space : O(k)  →  Why: deque holds at most k indices at any time

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 8 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: nums = [1,3,-1,-3,5,3,6,7], k = 3

  i=0 (1): dq empty → append 0 → dq=[0]
  i=1 (3): nums[0]=1<=3 → pop 0 → dq=[]; append 1 → dq=[1]
  i=2 (-1): nums[1]=3 not<=-1 → no pop; append 2 → dq=[1,2]
            i>=k-1(2>=2) → result=[nums[1]]=[3]
  i=3 (-3): nums[2]=-1 not<=-3 → no pop; append 3 → dq=[1,2,3]
            dq[0]=1 <= i-k=0? 1<=0 false → no popleft
            result=[3, nums[1]=3]=[3,3]
  i=4 (5): nums[3]=-3<=5 → pop 3; nums[2]=-1<=5 → pop 2;
           nums[1]=3<=5 → pop 1 → dq=[]; append 4 → dq=[4]
           result=[3,3, nums[4]=5]=[3,3,5]
  i=5 (3): nums[4]=5 not<=3 → no pop; append 5 → dq=[4,5]
           dq[0]=4 <= i-k=2? false → no popleft
           result=[3,3,5, nums[4]=5]=[3,3,5,5]
  i=6 (6): nums[5]=3<=6 → pop 5; nums[4]=5<=6 → pop 4 → dq=[];
           append 6 → dq=[6]
           result=[3,3,5,5, nums[6]=6]=[3,3,5,5,6]
  i=7 (7): nums[6]=6<=7 → pop 6 → dq=[]; append 7 → dq=[7]
           dq[0]=7 <= i-k=4? false → no popleft
           result=[3,3,5,5,6, nums[7]=7]=[3,3,5,5,6,7]

  Output: [3,3,5,5,6,7]   matches expected

  ಇನ್ನೊಂದು example — tricky case (k equals array length):
  Input: nums = [4,2,7], k = 3

  i=0 (4): dq=[0]
  i=1 (2): nums[0]=4 not<=2 → append 1 → dq=[0,1]
  i=2 (7): nums[1]=2<=7 → pop 1; nums[0]=4<=7 → pop 0 → dq=[];
           append 2 → dq=[2]
           i>=k-1(2>=2) → result=[nums[2]]=[7]

  Output: [7]   matches expected

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 9 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ k == 1?                      →  every element is its own window's
                                     max, result == nums unchanged
  ✓ k == n (whole array)?        →  single window, result has just
                                     one element — the global max
  ✓ All same elements?           →  every push pops nothing (equal
                                     values, `<=` still pops correctly
                                     dedupes), each window's max ==
                                     that shared value
  ✓ Negative numbers?            →  works unchanged since deque
                                     comparisons are value-agnostic
  ✓ Strictly decreasing array?   →  deque holds all k elements at
                                     once (nothing ever dominated
                                     immediately), front stays the
                                     leftmost until it expires

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 10 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                Time         Space
  Brute Force   O(n*k)       O(1)
  Better        O(n log n)   O(n)   (max-heap with lazy deletion)
  Optimal       O(n)         O(k)    ← use this

  Time yaake ashtu?  → ಪ್ರತಿ index ಒಂದೇ ಸಲ deque ಗೆ push ಆಗುತ್ತೆ,
                        ಒಂದೇ ಸಲ pop ಆಗುತ್ತೆ — amortized O(1), total O(n).
  Space yaake ashtu? → deque ನಲ್ಲಿ ಗರಿಷ್ಠ k indices ಮಾತ್ರ ಇರ್ತಾವೆ.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 11 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Monotonic Deque (Sliding Window Extremum)

  Ee pattern yaavaaga use maadabeeku?
  → "Sliding window max/min" ಥರ problem ಕೇಳಿದಾಗ
  → An element being dominated (permanently useless once a bigger/
    smaller one arrives within range) ಅಂತ ಗುರುತಿಸಿದಾಗ
  → Fixed-size window + need for O(1) amortized max/min query

  Idee pattern beere problemsalli kaanisatte:
  → Shortest Subarray with Sum at Least K (LC 862) — monotonic deque
    on prefix sums
  → Constrained Subsequence Sum (LC 1425) — sliding window max deque
    inside a DP
  → Largest Rectangle in Histogram — related monotonic stack family
    (already solved in this repo, boundary-finding variant)

  Next time intaha problem bandre naanu modalu idannu think maadtene:
  → "'Sliding window max/min' anta kanda takshana, monotonic deque
      (decreasing for max, increasing for min) track maadi, front
      ondu answer anta modalu yochisu."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 12 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "I need the maximum of every fixed-size k window as it slides
      across the array, one step at a time."

  2. Brute force:
     "Rescan each window directly — O(n*k), too slow. A max-heap with
      lazy deletion gets it to O(n log n) but adds heap overhead."

  3. Optimize:
     "I notice a smaller element to the left of a larger one can
      never be the max of any window that still contains the larger
      one — so I can discard it permanently, keeping only a
      monotonic decreasing sequence of candidates."

  4. Code:
     "Maintain a deque of indices. For each new index, pop smaller
      values from the back, append the new index, pop the front if
      it's expired out of the window, and once the window is full,
      the front is the current max."

  5. Complexity:
     "Time O(n) — each index is pushed and popped at most once.
      Space O(k) — the deque holds at most k indices."

  Mukhya: summane kuutu code bareyabeda! Interviewer ge ninna thinking
          process kaanabeku.
"""

from collections import deque


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(n*k) Time | O(1) Extra Space  (Rescan Every Window)
# ═══════════════════════════════════════════════════════════════════
def sliding_window_max_brute(nums, k):
    """Idu modala aaloochane — prati window ge direct scan maadi max hudukodu"""
    n = len(nums)
    result = []
    for i in range(n - k + 1):
        result.append(max(nums[i:i + k]))
    return result


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n) Time | O(k) Space  (Monotonic Decreasing Deque)
# ═══════════════════════════════════════════════════════════════════
def sliding_window_max(nums, k):
    """Idu final answer — decreasing deque ittukondu front nalli current max track maadu"""
    dq = deque()  # stores indices, values decreasing front to back
    result = []

    for i, num in enumerate(nums):
        while dq and nums[dq[-1]] <= num:
            dq.pop()
        dq.append(i)

        if dq[0] <= i - k:
            dq.popleft()

        if i >= k - 1:
            result.append(nums[dq[0]])

    return result


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")

    # Test 1 — Basic example
    assert sliding_window_max([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]

    # Test 2 — Edge case: k == n (whole array)
    assert sliding_window_max([4, 2, 7], 3) == [7]

    # Test 3 — Edge case: k == 1 (every element its own window)
    assert sliding_window_max([5, 1, 9, 3], 1) == [5, 1, 9, 3]

    # Test 4 — Tricky: all same elements
    assert sliding_window_max([2, 2, 2, 2], 2) == [2, 2, 2]

    # Test 5 — Tricky: strictly decreasing
    assert sliding_window_max([5, 4, 3, 2, 1], 2) == [5, 4, 3, 2]

    print("All tests passed!")
