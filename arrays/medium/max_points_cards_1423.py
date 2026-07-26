"""
╔══════════════════════════════════════════════════════════════════╗
║  MAXIMUM POINTS YOU CAN OBTAIN FROM CARDS                         ║
║  LeetCode #1423  |  Difficulty: Medium  |  Topic: Arrays / Sliding Window ║
║  Link: https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/ ║
╚══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Cards are arranged in a row, each with a point value. In each of k
  moves, you can take ONE card from either the very beginning or the
  very end of the row (not the middle). Maximize the total points of
  the k cards you take.

  Input : cardPoints = [1, 2, 3, 4, 5, 6, 1], k = 3
  Output: 12

  Example 1 — basic:
    Input : cardPoints = [1, 2, 3, 4, 5, 6, 1], k = 3
    Output: 12
    Why?  : take the last 3 cards (6, 1, and wrapping to the last-1st
             from front)... actually taking last 2 [1,6]=7 plus first
             1 [1]=1 gives 8; the best is actually taking last three
             [5,6,1]=12 — always taking from the end here wins

  Example 2 — slightly tricky (k equals the array length):
    Input : cardPoints = [9, 7, 7, 9, 7, 7, 9], k = 7
    Output: 55
    Why?  : k == n means you're forced to take every card — there's
             no choice at all, just sum everything

  Constraints:
    - 1 <= cardPoints.length <= 10^5
    - 1 <= cardPoints[i] <= 10^4
    - 1 <= k <= cardPoints.length

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ಮೊದಲು problem odidaga ನಮ್ಮ brain ಏನು think ಮಾಡಬೇಕು:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ (What are they asking?)
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  cards row + k moves               │
  │  Output ಏನು ಬೇಕು?     →  front/back ಇಂದ ಮಾತ್ರ k cards       │
  │                          ತಗೊಂಡು max total points            │
  │  Constraints ಏನಿದೆ?   →  n<=10^5, k<=n, middle ಇಂದ ತಗೊಳ್ಳೋಕೆ │
  │                          ಆಗಲ್ಲ                              │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ನನಗೆ ಗೊತ್ತಿರೋ simple way ಏನು? (Brute force thought)
  →  ಎಲ್ಲಾ possible combinations try ಮಾಡೋದು — i cards front ಇಂದ,
     (k-i) cards back ಇಂದ, i=0 ಇಂದ k ತನಕ, ಪ್ರತಿ combination ನ sum
     ಲೆಕ್ಕ ಹಾಕಿ max ತಗೊಳ್ಳೋದು.
  →  ಆದರೆ ಇದು slow ಯಾಕೆ? → ಪ್ರತಿ combination ಗೂ sum ಮತ್ತೆ ಮತ್ತೆ ಲೆಕ್ಕ
     ಹಾಕಿದ್ರೆ O(k²) — recompute ತಪ್ಪಿಸ್ಬೋದು.

  ಹಂತ 3 — Better way ಹೇಗೆ ಯೋಚಿಸುವುದು? (Optimization thought)
  →  "k cards front/back ಇಂದ ತಗೊಳ್ಳೋದು ಅಂದ್ರೆ, actually middle ನಲ್ಲಿ
     (n-k) cards ಬಿಟ್ಟು ಬಿಡ್ತೀವಿ ಅಂತ ಆಗುತ್ತೆ! ಆದ್ದರಿಂದ 'max sum of k
     cards from ends' = 'total sum - min sum of (n-k) contiguous
     cards from the middle'."
  →  ಅಹಾ moment: (n-k) size ನ sliding window ಅನ್ನ array ಮೂಲಕ ಸ್ಲೈಡ್
     ಮಾಡಿ, ಆ window ನ MINIMUM sum ಕಂಡುಹಿಡಿದ್ರೆ, total_sum - min_window_sum
     ಯೇ answer! ಇದನ್ನ fixed-size sliding window ಇಂದ O(n) ನಲ್ಲಿ
     ಮಾಡ್ಬಹುದು.
  →  ಇದರಿಂದ ನಾವು Sliding Window → Fixed Size (Complement Trick — Minimize
     the Middle) use ಮಾಡಬಹುದು!

  ಹಂತ 4 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  "Take k from ends" ಅನ್ನ "leave (n-k) contiguous in the middle"
     ಅಂತ reframe ಮಾಡಿದ್ರೆ, ಇದು ಒಂದು fixed-size window problem
     ಆಗುತ್ತೆ — sliding window ideal fit.
  →  Total sum fixed ಆಗಿರೋದ್ರಿಂದ, middle window minimize ಮಾಡಿದ್ರೆ,
     automatic ಆಗಿ taken cards ನ sum maximize ಆಗುತ್ತೆ.
  →  Window ಅನ್ನ ಒಂದೇ pass ನಲ್ಲಿ slide ಮಾಡಿ (add new element, remove
     old element) O(n) time ಸಿಗುತ್ತೆ, brute force ನ recompute ಬೇಡ.

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು (Think out loud):
  →  "The naive way tries every split of i cards from front and k-i
      from back — O(k²) if I recompute sums each time."
  →  "I notice that taking k cards from the ends is equivalent to
      leaving behind a contiguous block of n-k cards in the middle —
      so I want to MINIMIZE that middle block's sum."
  →  "That's now a classic fixed-size sliding window problem: slide a
      window of size n-k across the array, track its minimum sum, and
      subtract that from the total."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Sliding Window → Fixed Size (Complement Trick)
  Secondary : None

  WHY this technique?
  → "Take k from both ends" reframes cleanly as "leave a contiguous
    (n-k)-sized block in the middle untaken" — a fixed window
  → Total array sum is constant, so minimizing the untaken window's
    sum directly maximizes the taken cards' sum
  → A fixed-size window can be slid in O(n) using add-new/remove-old,
    avoiding the O(k²) brute-force recomputation

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION (How to think — English)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Key observation: since you always take from the ends, whatever
  remains untaken must be exactly one contiguous block of size n-k
  somewhere in the array (it can't be split into two separate untaken
  chunks, since taking is always from an end). So the problem becomes
  "find the minimum-sum contiguous block of size n-k" — a plain fixed
  window minimum, then subtract from the total sum.

  The journey from brute to optimal:
    Brute thought   →  try every split (i from front, k-i from back),
                        recomputing sums each time
    Problem with it →  O(k²) from repeated summation
    Better question →  "what does the UNTAKEN portion look like, and
                        can I optimize that instead?"
    Insight         →  untaken cards always form one contiguous block
                        of size n-k; minimizing it maximizes the answer
    Optimal         →  fixed-size sliding window over that block,
                        O(n) time, O(1) space

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE (Try Every Front/Back Split)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    For each possible split — i cards from the front, k-i from the
    back (i ranging 0 to k) — compute the sum directly and track the
    maximum.

  Pseudocode:
    step 1: best = 0
    step 2: for i in range(k+1):
    step 3:   front_sum = sum(cardPoints[:i])
    step 4:   back_sum = sum(cardPoints[n-(k-i):]) if k-i > 0 else 0
    step 5:   best = max(best, front_sum + back_sum)
    step 6: return best

  Time  : O(k²)  →  Why: for each of k+1 splits, summing slices costs O(k)
  Space : O(1)   →  Why: no extra structures beyond running sums

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ? (Why is this not enough?)
    → k ಬಹಳ ದೊಡ್ಡ ಆಗ್ಬೋದು (up to n=10^5) — O(k²) ಆಗ್ಲೇ 10^10
      ಆಗ್ಬೋದು, TLE. Complement sliding window ಇಂದ O(n) ಗೆ ಇಳಿಸ್ಬೋದು.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚶 SECTION 6 — APPROACH 2 — BETTER (Prefix/Suffix Sum Arrays)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Precompute prefix sums and suffix sums once, then for each split
    i, look up front_sum and back_sum in O(1) instead of recomputing.

  Time  : O(k)  →  one pass to build prefix/suffix, one pass over splits
  Space : O(n)  →  prefix and suffix sum arrays

  ಇನ್ನೂ better ಮಾಡಬಹುದಾ? → ಹೌದು — complement/sliding-window trick
  ಇಂದ, ಪ್ರತ್ಯೇಕ prefix/suffix arrays ಬೇಡ, single fixed window slide
  ಇಂದ O(n) time, O(1) space ಸಾಧ್ಯ.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 7 — APPROACH 3 — OPTIMAL   (Sliding Window — Minimize the Middle)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Compute total_sum of all cards. The untaken portion is always a
    contiguous block of size (n - k). Slide a fixed window of that
    size across the array, tracking its minimum sum. The answer is
    total_sum minus that minimum window sum.

  Key steps:
    1. total_sum = sum(cardPoints); window_size = n - k
    2. if window_size == 0: return total_sum   # k == n, take everything
    3. window_sum = sum(cardPoints[:window_size]); min_window = window_sum
    4. for i in range(window_size, n):
         window_sum += cardPoints[i] - cardPoints[i - window_size]
         min_window = min(min_window, window_sum)
    5. return total_sum - min_window

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ (Say it once in Kanglish so it sticks):
    → "total_sum ಲೆಕ್ಕ ಹಾಕು. window_size = n-k ಇಟ್ಕೊಂಡು, ಮೊದಲ window
        ನ sum ಲೆಕ್ಕ ಹಾಕಿ min_window ಆಗಿ ಇಡು. ಆಮೇಲೆ window ಅನ್ನ ಒಂದೊಂದೇ
        step slide ಮಾಡ್ತಾ (new element add, old element remove),
        min_window update ಮಾಡ್ತಾ ಹೋಗು. ಕೊನೆಗೆ total_sum - min_window
        ಯೇ answer!"

  Time  : O(n)  →  Why: single pass to build total sum + single pass
                    to slide the window
  Space : O(1)  →  Why: only running sums and pointers tracked

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 8 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: cardPoints = [1, 2, 3, 4, 5, 6, 1], k = 3  (n=7)

  total_sum = 1+2+3+4+5+6+1 = 22
  window_size = n-k = 4

  Initial window (indices 0-3): [1,2,3,4] → window_sum=10, min_window=10

  i=4 (cardPoints[4]=5): window_sum += 5 - cardPoints[0]=1 → 10+5-1=14
                          min_window=min(10,14)=10
  i=5 (cardPoints[5]=6): window_sum += 6 - cardPoints[1]=2 → 14+6-2=18
                          min_window=min(10,18)=10
  i=6 (cardPoints[6]=1): window_sum += 1 - cardPoints[2]=3 → 18+1-3=16
                          min_window=min(10,16)=10

  Output: total_sum - min_window = 22 - 10 = 12   matches expected

  ಇನ್ನೊಂದು example — tricky case (k equals array length):
  Input: cardPoints = [9, 7, 7, 9, 7, 7, 9], k = 7  (n=7)

  total_sum = 9+7+7+9+7+7+9 = 55
  window_size = n-k = 0 → special case, no cards left untaken

  Output: total_sum - 0 = 55   matches expected

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 9 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ k == n (take everything)?  →  window_size = 0, no middle left,
                                   answer is just total_sum
  ✓ k == 1 (take just one card)? →  window_size = n-1, minimum
                                   (n-1)-sized window found, effectively
                                   picks the single best end card
  ✓ Single card, k=1?           →  window_size=0, trivially returns
                                   that one card's value
  ✓ All same point values?      →  every window sums the same, any
                                   split gives the same total
  ✓ Best cards all at one end?  →  sliding window naturally finds the
                                   minimum block regardless of which
                                   side is "better"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 10 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                Time      Space
  Brute Force   O(k²)     O(1)
  Better        O(k)      O(n)  (prefix/suffix arrays)
  Optimal       O(n)      O(1)    ← use this 

  Time ಯಾಕೆ ಅಷ್ಟು?  → total sum ಗೆ O(n), window slide ಗೆ O(n) —
                        ಎರಡೂ ಸೇರಿ O(n).
  Space ಯಾಕೆ ಅಷ್ಟು? → running sums (total_sum, window_sum, min_window)
                        ಬಿಟ್ಟು ಬೇರೆ extra structure ಬೇಡ.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 11 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Sliding Window — Complement Trick (Minimize What's Left Out)

  ಈ pattern ಯಾವಾಗ use ಮಾಡಬೇಕು?
  → "Take k elements from the ends" ಥರ problem ಕೇಳಿದಾಗ — ends ಇಂದ
    ಮಾತ್ರ take ಮಾಡೋದ್ರಿಂದ ಬಿಟ್ಟಿರೋದು ಯಾವಾಗ್ಲೂ ಒಂದೇ contiguous block
    ಆಗುತ್ತೆ ಅಂತ ಗುರುತಿಸಿದಾಗ
  → "Maximize the taken" ಅನ್ನ "minimize the left-out" ಗೆ ಪರಿವರ್ತಿಸಿದ್ರೆ
    ಸುಲಭ ಆಗುತ್ತೆ ಅಂತ ಗೊತ್ತಾದಾಗ (total ಇಂದ subtract ಮಾಡಿ)
  → Fixed window size ಗೊತ್ತಿದ್ದಾಗ (ಇಲ್ಲಿ n-k), sliding window direct
    fit ಆಗುತ್ತೆ

  ಇದೇ pattern ಬೇರೆ problems ನಲ್ಲಿ ಕಾಣಿಸುತ್ತೆ:
  → Maximum Sum of Distinct Subarrays With Length K — same fixed window family
  → Grumpy Bookstore Owner — same "minimize/maximize with a fixed window" complement trick
  → Minimum Size Subarray Sum — different (variable window), but same sliding-window family

  Next time ಇಂತಹ problem ಬಂದ್ರೆ ನಾನು ಮೊದಲು ಇದನ್ನ think ಮಾಡ್ತೇನೆ:
  → "'Only from ends' ಅಂತ ಕೇಳಿದ ತಕ್ಷಣ, ಬಿಟ್ಟಿರೋ middle portion ಯಾವಾಗ್ಲೂ
      ಒಂದೇ contiguous block ಅಂತ ಗುರುತಿಸಿ, total - min(fixed window)
      ಅಂತ reframe ಮಾಡು ಅಂತ ಮೊದಲು ಯೋಚಿಸು."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 12 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "I can only take cards from the front or back of the row, k
      cards total, and I want to maximize their sum."

  2. Brute force:
     "Try every split — i cards from the front, k-i from the back —
      and recompute each sum directly. That's O(k²), too slow when k
      can be up to 10^5."

  3. Optimize:
     "Since I only ever take from the ends, whatever is LEFT OVER is
      always one contiguous block of size n-k. So maximizing what I
      take is the same as minimizing that leftover block — which is
      just a fixed-size sliding window minimum."

  4. Code:
     "I will compute the total sum, then slide a window of size n-k
      across the array — adding the new element and removing the
      outgoing one each step — tracking the minimum window sum, and
      subtract that from the total."

  5. Complexity:
     "Time O(n) — one pass for the total, one pass for the sliding
      window. Space O(1) — just a few running sums."

  ಮುಖ್ಯ: ಸುಮ್ಮನೆ ಕೂತು code ಬರೆಯಬೇಡ!
         Interviewer ಗೆ ನಿನ್ನ thinking process ಕಾಣಬೇಕು.
"""


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(k^2) Time | O(1) Space  (Try Every Front/Back Split)
# ═══════════════════════════════════════════════════════════════════
def max_score_brute(cardPoints, k):
    """ಇದು ಮೊದಲ ಆಲೋಚನೆ — ಪ್ರತಿ front/back split ಗೂ sum ಮತ್ತೆ ಲೆಕ್ಕ ಹಾಕೋದು"""
    n = len(cardPoints)
    best = 0
    for i in range(k + 1):
        front_sum = sum(cardPoints[:i])
        back_count = k - i
        back_sum = sum(cardPoints[n - back_count:]) if back_count > 0 else 0
        best = max(best, front_sum + back_sum)
    return best


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n) Time | O(1) Space  (Sliding Window — Minimize the Middle)
# ═══════════════════════════════════════════════════════════════════
def max_score(cardPoints, k):
    """ಇದು final answer — leftover middle block ಅನ್ನ fixed window ಇಂದ minimize ಮಾಡು"""
    n = len(cardPoints)
    total_sum = sum(cardPoints)
    window_size = n - k

    if window_size == 0:
        return total_sum

    window_sum = sum(cardPoints[:window_size])
    min_window = window_sum

    for i in range(window_size, n):
        window_sum += cardPoints[i] - cardPoints[i - window_size]
        min_window = min(min_window, window_sum)

    return total_sum - min_window


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")   # Windows cp1252 can't print emoji otherwise

    # Test 1 — Basic example
    assert max_score([1, 2, 3, 4, 5, 6, 1], 3) == 12

    # Test 2 — Edge case: single card, k=1
    assert max_score([5], 1) == 5

    # Test 3 — Edge case: all same elements
    assert max_score([4, 4, 4, 4, 4], 2) == 8

    # Test 4 — Tricky: k equals array length, forced to take everything
    assert max_score([9, 7, 7, 9, 7, 7, 9], 7) == 55

    print("All tests passed! ")
