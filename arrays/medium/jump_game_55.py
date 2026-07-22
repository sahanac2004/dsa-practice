"""
╔═══════════════════════════════════════════════════════════════════╗
║  JUMP GAME                                                        ║
║  LeetCode #55  |  Difficulty: Medium  |  Topic: Arrays / Greedy   ║
║  Link: https://leetcode.com/problems/jump-game/                   ║
╚═══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Each element nums[i] is the maximum jump length FROM that index.
  Starting at index 0, determine if you can reach the last index.

  Input : nums = [2, 3, 1, 1, 4]
  Output: true

  Example 1 — basic:
    Input : nums = [2, 3, 1, 1, 4]
    Output: true
    Why?  : jump 1 step from index 0 to index 1 (value 3), then jump
             3 steps to the last index (4) — reachable

  Example 2 — slightly tricky (a zero blocks the path):
    Input : nums = [3, 2, 1, 0, 4]
    Output: false
    Why?  : no matter how you jump, you always land on index 3
             (value 0), which can't jump anywhere — index 4 is
             unreachable despite that 4 sitting right there

  Constraints:
    - 1 <= nums.length <= 10^4
    - 0 <= nums[i] <= 10^5

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ಮೊದಲು problem odidaga ನಮ್ಮ brain ಏನು think ಮಾಡಬೇಕು:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ (What are they asking?)
  ┌──────────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  ಪ್ರತಿ index ಗೂ max jump length       │
  │  Output ಏನು ಬೇಕು?     →  last index reach ಮಾಡ್ಬಹುದಾ ಅಂತ  │
  │                          true/false                          │
  │  Constraints ಏನಿದೆ?   →  n<=10^4, jump length 0 ಸಹ ಆಗ್ಬೋದು │
  │                          (block ಆಗ್ಬೋದು)                    │
  └──────────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ನನಗೆ ಗೊತ್ತಿರೋ simple way ಏನು? (Brute force thought)
  →  Recursion/DP — ಪ್ರತಿ index i ಇಂದ, 1 ಇಂದ nums[i] ತನಕ ಎಲ್ಲಾ possible
     jumps try ಮಾಡಿ, ಯಾವ್ದಾದ್ರೂ ಒಂದು path last index reach ಮಾಡುತ್ತಾ
     ಅಂತ ನೋಡೋದು.
  →  ಆದರೆ ಇದು slow ಯಾಕೆ? → Exponential branching (each index has up
     to nums[i] choices) — O(2^n) worst case, n=10^4 ಗೆ ಖಂಡಿತ TLE.

  ಹಂತ 3 — Better way ಹೇಗೆ ಯೋಚಿಸುವುದು? (Optimization thought)
  →  "ನಾವು exact path track ಮಾಡ್ಬೇಕಾ, ಅಥವಾ ಬರೀ 'ಎಷ್ಟು far reach
     ಮಾಡ್ಬಹುದು' ಅಂತ ಗೊತ್ತಿದ್ರೆ ಸಾಕಾ?"
  →  ಅಹಾ moment: ಪ್ರತಿ index i ಗೂ, ಆ index reach ಆಗಿದ್ರೆ (i <= farthest
     ಇಲ್ಲಿ ತನಕ reach ಆಗಿರೋದು), ಅಲ್ಲಿಂದ i + nums[i] ತನಕ reach ಮಾಡ್ಬಹುದು.
     ಆದ್ದರಿಂದ ಪ್ರತಿ index ಗೂ "farthest" ಅನ್ನ update ಮಾಡ್ತಾ ಹೋದ್ರೆ ಸಾಕು —
     exact path ಬೇಡ, ಬರೀ "how far can I go" greedy ಆಗಿ track ಮಾಡ್ಬಹುದು!
     ಯಾವಾಗ್ಲಾದ್ರೂ farthest < current index ಆದ್ರೆ, ಆ point stuck ಆಗಿದೆ
     ಅಂತ — false.
  →  ಇದರಿಂದ ನಾವು Greedy → Track Farthest Reachable Index use ಮಾಡಬಹುದು!

  ಹಂತ 4 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  Exact jump sequence ಬೇಡ, ಬರೀ reachability ಬೇಕು — ಇದ್ಕೆ "farthest
     reachable so far" ಅನ್ನೋ single running value ಸಾಕು.
  →  ಪ್ರತಿ index i ಗೆ, ಅದು already reachable ಆಗಿದ್ರೆ ಮಾತ್ರ ಅದರ jump
     value ಪರಿಗಣಿಸ್ಬೇಕು — reach ಆಗ್ದೇ ಇರೋ index ನ jump value irrelevant.
  →  Single left-to-right pass ಸಾಕು, ಯಾಕಂದ್ರೆ farthest ಎಂದೂ ಕಡಿಮೆ
     ಆಗಲ್ಲ (monotonic non-decreasing) — greedy correct ಆಗುತ್ತೆ.

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು (Think out loud):
  →  "A brute-force recursive approach tries every possible jump
      length at every index — exponential, way too slow for n=10^4."
  →  "I realize I don't need the exact path — I just need to know the
      farthest index reachable so far, updated greedily as I scan."
  →  "If at any index i, the farthest reachable point so far is
      already less than i, I'm stuck and can never reach the end."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Greedy → Track Farthest Reachable Index
  Secondary : None

  WHY this technique?
  → We only care about reachability, not the exact jump sequence —
    collapses the problem to tracking one running maximum
  → The farthest-reachable value only ever grows (or stays put) as we
    scan left to right, making a single greedy pass sufficient
  → Any index beyond the current farthest reach can never be visited,
    so we can bail out early (return false) the moment we're stuck

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION (How to think — English)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Key observation: reachability is transitive and monotonic — if
  index i is reachable, then everything up to i + nums[i] becomes
  reachable too. So walking left to right and maintaining
  "farthest = max(farthest, i + nums[i])" for every reachable i
  captures the full reachable frontier without ever needing to
  enumerate actual jump sequences.

  The journey from brute to optimal:
    Brute thought   →  recursively try every jump length from every index
    Problem with it →  exponential blowup, far too slow for n=10^4
    Better question →  "do I need the actual path, or just whether
                        the end is reachable?"
    Insight         →  track only the farthest index reachable so far;
                        that single number is all the state needed
    Optimal         →  one greedy left-to-right pass, O(n) time, O(1) space

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE (Recursive Backtracking)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    From index i, try every possible jump length from 1 to nums[i],
    recursively checking if any of them eventually reach the last
    index.

  Pseudocode:
    step 1: def can_reach(i):
    step 2:   if i >= n-1: return True
    step 3:   for step in range(1, nums[i]+1):
    step 4:     if can_reach(i + step): return True
    step 5:   return False
    step 6: return can_reach(0)

  Time  : O(2^n)  →  Why: each index branches into up to nums[i]
                    recursive calls, worst case exponential
  Space : O(n)    →  Why: recursion depth up to n

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ? (Why is this not enough?)
    → n=10^4 ಗೆ exponential branching ಖಂಡಿತ TLE ಆಗುತ್ತೆ. Greedy
      farthest-reach tracking ಇಂದ O(n) ಗೆ ಇಳಿಸ್ಬೋದು.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚶 SECTION 6 — APPROACH 2 — BETTER (skip — brute jumps straight to optimal)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ಇಲ್ಲಿ intermediate approach ಇಲ್ಲ — greedy insight ಸಿಕ್ಕ ತಕ್ಷಣ
  ನೇರವಾಗಿ optimal ಗೆ ಹೋಗಬಹುದು (DP memoization ಸಹ O(n²) ಆಗುತ್ತೆ, greedy
  ಇಂದ ಇನ್ನೂ ಸುಲಭ ಮತ್ತು fast ಆಗುತ್ತೆ).

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 7 — APPROACH 3 — OPTIMAL   (Greedy — Track Farthest Reachable Index)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Walk left to right, maintaining "farthest" — the furthest index
    reachable so far. At each index i, if i > farthest, we're stuck
    (i itself was never reachable), so return False. Otherwise update
    farthest = max(farthest, i + nums[i]). If farthest ever reaches or
    exceeds the last index, return True.

  Key steps:
    1. farthest = 0
    2. for i in range(n):
         if i > farthest: return False
         farthest = max(farthest, i + nums[i])
    3. Return True (loop completed without getting stuck)

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ (Say it once in Kanglish so it sticks):
    → "farthest=0 ಇಂದ start ಮಾಡು. ಪ್ರತಿ index i ಗೂ, i > farthest ಆದ್ರೆ
        stuck ಆಗಿದೀವಿ ಅಂತ False. ಇಲ್ಲಾಂದ್ರೆ farthest =
        max(farthest, i+nums[i]) ಮಾಡ್ತಾ ಹೋಗು. ಪೂರ್ತಿ loop ಮುಗಿದ್ರೆ
        True!"

  Time  : O(n)  →  Why: single left-to-right pass
  Space : O(1)  →  Why: only one running variable, farthest

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 8 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: nums = [2, 3, 1, 1, 4]

  farthest=0
  i=0 (nums[i]=2): 0<=0 → farthest=max(0, 0+2)=2
  i=1 (nums[i]=3): 1<=2 → farthest=max(2, 1+3)=4
  i=2 (nums[i]=1): 2<=4 → farthest=max(4, 2+1)=4
  i=3 (nums[i]=1): 3<=4 → farthest=max(4, 3+1)=4
  i=4 (nums[i]=4): 4<=4 → farthest=max(4, 4+4)=8
  loop ends (i reached n-1=4)

  Output: True   matches expected

  ಇನ್ನೊಂದು example — tricky case (a zero blocks the path):
  Input: nums = [3, 2, 1, 0, 4]

  farthest=0
  i=0 (nums[i]=3): 0<=0 → farthest=max(0, 0+3)=3
  i=1 (nums[i]=2): 1<=3 → farthest=max(3, 1+2)=3
  i=2 (nums[i]=1): 2<=3 → farthest=max(3, 2+1)=3
  i=3 (nums[i]=0): 3<=3 → farthest=max(3, 3+0)=3
  i=4 (nums[i]=4): 4>farthest(3) → STUCK → return False

  Output: False   matches expected

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 9 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ Single element array?      →  already at the last index, trivially
                                   True (loop runs once, i=0<=0=farthest)
  ✓ All zeros except first?    →  farthest never grows past nums[0],
                                   correctly detects being stuck if n>1
  ✓ Zero at index 0, n>1?      →  farthest stays 0, i=1>0 → False
                                   immediately
  ✓ Large jump values (>= n)?  →  farthest just grows huge but max()
                                   still works, no overflow concerns in Python
  ✓ Zero in the middle but still reachable past it? →  handled since
                                   farthest may already exceed that
                                   index from an earlier jump

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 10 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                Time      Space
  Brute Force   O(2^n)    O(n)
  Optimal       O(n)      O(1)    ← use this 

  Time ಯಾಕೆ ಅಷ್ಟು?  → ಒಂದೇ pass ನಲ್ಲಿ ಪ್ರತಿ index ಅನ್ನ ಒಂದೇ ಸಲ visit.
  Space ಯಾಕೆ ಅಷ್ಟು? → farthest ಒಂದೇ variable ಬಿಟ್ಟು ಬೇರೆ extra
                        structure ಬೇಡ.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 11 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Greedy — Track Farthest Reachable Frontier

  ಈ pattern ಯಾವಾಗ use ಮಾಡಬೇಕು?
  → "Can you reach the end" ಅಂತ ಕೇಳಿದಾಗ, exact path ಬೇಡ, ಬರೀ
    reachability ಬೇಕಾದಾಗ
  → ಪ್ರತಿ position ನಿಂದ "how far can I extend" ಅನ್ನೋ information
    ಇದ್ದಾಗ (jump length, interval end, etc.)
  → "Best possible reach" ಎಂದೂ ಕಡಿಮೆ ಆಗಲ್ಲ (monotonic) ಅಂತ ಗೊತ್ತಾದಾಗ,
    greedy correct ಆಗುತ್ತೆ ಅಂತ prove ಮಾಡ್ಬಹುದಾದಾಗ

  ಇದೇ pattern ಬೇರೆ problems ನಲ್ಲಿ ಕಾಣಿಸುತ್ತೆ:
  → Jump Game II (#45) — same farthest-reach idea, now counting minimum jumps
  → Video Stitching / Gas Station — same "extend the frontier greedily" family
  → Merge Intervals (#56) — similar "track current reach/end" greedy scan

  Next time ಇಂತಹ problem ಬಂದ್ರೆ ನಾನು ಮೊದಲು ಇದನ್ನ think ಮಾಡ್ತೇನೆ:
  → "Reachability ಕೇಳಿದ ತಕ್ಷಣ, exact path track ಮಾಡ್ದೇ, ಬರೀ 'farthest
      reachable so far' ಅನ್ನ single variable ಆಗಿ greedy track ಮಾಡು
      ಅಂತ ಮೊದಲು ಯೋಚಿಸು."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 12 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "I need to determine if I can reach the last index, where each
      index tells me the maximum jump length from there."

  2. Brute force:
     "A recursive approach tries every jump length at every index —
      exponential time, way too slow for n up to 10^4."

  3. Optimize:
     "I don't need the actual jump path — I just need to know the
      farthest index reachable so far. That's a single running value
      I can update greedily as I scan left to right."

  4. Code:
     "I will track 'farthest', and at each index check if it's still
      within reach (i <= farthest); if not, I'm stuck and return
      False immediately. Otherwise I extend farthest using i + nums[i]."

  5. Complexity:
     "Time O(n) — single pass. Space O(1) — just one running
      variable."

  ಮುಖ್ಯ: ಸುಮ್ಮನೆ ಕೂತು code ಬರೆಯಬೇಡ!
         Interviewer ಗೆ ನಿನ್ನ thinking process ಕಾಣಬೇಕು.
"""


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(2^n) Time | O(n) Space  (Recursive Backtracking)
# ═══════════════════════════════════════════════════════════════════
def can_jump_brute(nums):
    """ಇದು ಮೊದಲ ಆಲೋಚನೆ — ಪ್ರತಿ jump length ಅನ್ನ recursively try ಮಾಡೋದು"""
    n = len(nums)

    def can_reach(i):
        if i >= n - 1:
            return True
        for step in range(1, nums[i] + 1):
            if can_reach(i + step):
                return True
        return False

    return can_reach(0)


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n) Time | O(1) Space  (Greedy — Track Farthest Reachable Index)
# ═══════════════════════════════════════════════════════════════════
def can_jump(nums):
    """ಇದು final answer — farthest reachable index ಅನ್ನ single pass ನಲ್ಲಿ greedy track ಮಾಡು"""
    farthest = 0

    for i in range(len(nums)):
        if i > farthest:
            return False
        farthest = max(farthest, i + nums[i])

    return True


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")   # Windows cp1252 can't print emoji otherwise

    # Test 1 — Basic example
    assert can_jump([2, 3, 1, 1, 4]) == True

    # Test 2 — Edge case: single element
    assert can_jump([0]) == True

    # Test 3 — Edge case: all same elements (all 1s, minimal steps)
    assert can_jump([1, 1, 1, 1]) == True

    # Test 4 — Tricky: a zero blocks the path
    assert can_jump([3, 2, 1, 0, 4]) == False

    print("All tests passed! ")
